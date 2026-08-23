#!/usr/bin/env python3
"""
Agent triage: model-assigned category, summary, and contradiction flags.

Slots into the monthly refresh between the recall guard and build_site.py.
Reads library/flash_library.json, writes enriched records back to it, and
persists its own output to library/triage.json.

Why triage.json is separate and committed
-----------------------------------------
flash_harvest.py rewrites flash_library.json on every run, so anything written
into that file alone would be destroyed by the next harvest. triage.json is the
durable store, keyed by PMID; this script re-merges it into the library on each
run. A PMID is triaged exactly once, ever, unless SCHEMA_VERSION is bumped.

What this does NOT touch
------------------------
Records routed by publication type -- Reviews & Consensus, Perspectives &
Commentary, Point-Counterpoint, Opinions & Debate -- keep the category
flash_harvest.py gave them. Publication type is metadata, not a judgment call,
and the deterministic router is correct. The agent only categorizes records
sitting in the six content categories or in Uncategorized.

The keyword category is never discarded. It is preserved as
`category_keyword` and any disagreement with the agent is surfaced in the PR
body, so a month of disagreements tells you whether to trust the agent, retune
the keyword model, or fix the category scopes.

Usage:  python3 pipeline/triage_agent.py [--limit N] [--dry-run]
Env:    ANTHROPIC_API_KEY (required), TRIAGE_MODEL (optional)
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LIB = ROOT / "library"
LIBRARY = LIB / "flash_library.json"
TRIAGE = LIB / "triage.json"
CLAIMS = LIB / "claims.yml"
REFRESH = ROOT / ".refresh"

SCHEMA_VERSION = 1
MODEL = os.environ.get("TRIAGE_MODEL", "claude-sonnet-5")
MAX_TOKENS = 1500
MAX_ATTEMPTS = 2

# Categories the agent is allowed to assign. Deliberately excludes the four
# publication-type categories and Uncategorized: the agent must commit to a
# content category, and expresses doubt through `confidence` instead.
CONTENT_CATEGORIES = {
    "Radiobiology":
        "Cellular and molecular response to ultra-high dose rate, in vitro "
        "studies, DNA damage and repair, immune and vascular response, and "
        "whole-animal studies with a tissue or tumour endpoint. If the "
        "contribution is a computational model of the mechanism rather than a "
        "measurement, use Modeling & Mechanisms.",
    "Physics & Dosimetry":
        "Detector response at ultra-high dose rate, recombination and "
        "saturation correction, reference and relative dosimetry, calibration "
        "and traceability, pulse-resolved and temporal dosimetry, beam "
        "monitoring. If the contribution is the accelerator or delivery "
        "hardware itself, use Beam Delivery & Technology.",
    "Modeling & Mechanisms":
        "Monte Carlo transport, chemical kinetic and physicochemical models, "
        "oxygen depletion and radical chemistry modelling, microdosimetry, and "
        "machine learning applied to predicting the FLASH effect. A simulation "
        "that merely supports an experimental result belongs with that "
        "experiment's category.",
    "Beam Delivery & Technology":
        "Accelerator and RF design, beam transport and optics, pulse structure "
        "and control, scanning and collimation, source development across "
        "electron, photon, proton and ion modalities, and engineering "
        "feasibility of UHDR delivery.",
    "Treatment Planning & Optimization":
        "Dose-rate-aware optimization, dose rate metric definitions, planning "
        "objectives and constraints for UHDR, TPS development and "
        "commissioning, comparative planning studies, and plan quality "
        "evaluation. Delivering the plan on hardware is Beam Delivery.",
    "Clinical & Translational":
        "Human trials and first-in-human reports, case reports and series, "
        "trial design and protocol, outcome and toxicity reporting, "
        "client-owned veterinary clinical studies, regulatory pathway, "
        "reimbursement and implementation.",
}

# Categories assigned deterministically by publication type upstream. The agent
# is not consulted for these and must not overwrite them.
PUBTYPE_CATEGORIES = {
    "Reviews & Consensus", "Perspectives & Commentary",
    "Point-Counterpoint", "Opinions & Debate",
}

# Below this, the agent's category is recorded but the keyword category is kept
# as the live value. Raise it if you find the agent overconfident.
CONFIDENCE_FLOOR = 0.60

PROMPT = """You are triaging one publication for the AAPM BESC FLASH Working \
Group living literature corpus.

## Categories

Assign exactly one. Use only these names, spelled exactly as shown:

{categories}

## Registered claims

Assertions the wiki currently makes. Check whether this paper's own reported \
findings contradict, qualify, or supersede any of them.

{claims}

## Publication

Title: {title}
Journal: {journal} ({year})
Keyword-model category: {kw_category}

Abstract:
{abstract}

## Return

A single JSON object, no prose, no code fences:

{{
  "category": "...",
  "summary": "...",
  "key_findings": ["...", "..."],
  "confidence": 0.0,
  "contradictions": [
    {{"claim_id": "...", "nature": "contradicts|qualifies|supersedes",
      "explanation": "..."}}
  ],
  "reviewer_note": ""
}}

## Style for `summary`

Three to five sentences. Third person. Name the model system, beam quality, \
dose, and dose rate whenever the abstract gives them -- those are the details a \
reader of this corpus came for. Report effect sizes and endpoints as stated; do \
not round, soften, or editorialize. Never write that a result is important, \
promising, exciting, or novel. Do not use "FLASH" as a verb.

## Judgment

- The keyword-model category is shown for context only. Disagree with it freely \
when the abstract warrants; disagreements are reviewed, not suppressed.
- Flag a contradiction only when the paper's own reported findings are \
inconsistent with the registered claim. A study that simply does not replicate \
a claim, or that examines a different system, is not a contradiction -- put that \
in `reviewer_note` instead.
- If the abstract is too thin to categorize confidently, set `confidence` below \
0.5 and say what is missing in `reviewer_note`. A low-confidence honest answer \
is more useful than a confident guess.
"""


def load_claims() -> list[dict]:
    if not CLAIMS.exists():
        return []
    try:
        import yaml
    except ImportError:
        print("::warning::pyyaml not installed; contradiction checking disabled",
              file=sys.stderr)
        return []
    return yaml.safe_load(CLAIMS.read_text(encoding="utf-8")) or []


def needs_triage(rec: dict, done: dict) -> bool:
    prior = done.get(str(rec.get("pmid")))
    if prior and prior.get("schema") == SCHEMA_VERSION:
        return False
    if rec.get("category") in PUBTYPE_CATEGORIES:
        return False
    if not rec.get("abstract"):
        return False  # nothing to reason over
    return True


def validate(p: dict, claim_ids: set[str]) -> list[str]:
    errs = []
    if p.get("category") not in CONTENT_CATEGORIES:
        errs.append(f"category must be one of: {', '.join(sorted(CONTENT_CATEGORIES))}")
    if not isinstance(p.get("summary"), str) or len(p.get("summary", "").split()) < 25:
        errs.append("summary missing or shorter than 25 words")
    c = p.get("confidence")
    if not isinstance(c, (int, float)) or not 0 <= c <= 1:
        errs.append("confidence must be a number between 0 and 1")
    for f in p.get("contradictions") or []:
        if f.get("claim_id") not in claim_ids:
            errs.append(f"unknown claim_id {f.get('claim_id')!r}")
        if not f.get("explanation"):
            errs.append("contradiction missing explanation")
    return errs


def parse(text: str) -> dict:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("```")[1]
        if t.lstrip().startswith("json"):
            t = t.lstrip()[4:]
    return json.loads(t.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int,
                    default=int(os.environ.get("TRIAGE_LIMIT", "250")),
                    help="max records to triage this run (cost ceiling)")
    ap.add_argument("--dry-run", action="store_true",
                    help="triage and report, but write nothing")
    args = ap.parse_args()

    data = json.loads(LIBRARY.read_text(encoding="utf-8"))
    records = data["records"]
    done = json.loads(TRIAGE.read_text(encoding="utf-8")) if TRIAGE.exists() else {}
    claims = load_claims()
    claim_ids = {c["id"] for c in claims}

    pending = [r for r in records if needs_triage(r, done)]
    capped = pending[:args.limit]
    print(f"{len(records)} records; {len(pending)} need triage; "
          f"processing {len(capped)} (limit {args.limit}).", file=sys.stderr)

    if capped:
        from anthropic import Anthropic
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        cat_block = "\n".join(f"- {k}: {v}" for k, v in CONTENT_CATEGORIES.items())
        claim_block = "\n".join(
            f"- [{c['id']}] {c['claim'].strip()}" for c in claims
            if c.get("status", "active") == "active"
        ) or "(none registered yet)"

        failed = []
        for i, rec in enumerate(capped, 1):
            pmid = str(rec.get("pmid"))
            print(f"  [{i}/{len(capped)}] {pmid} {rec['title'][:60]}", file=sys.stderr)
            base = PROMPT.format(
                categories=cat_block, claims=claim_block,
                title=rec["title"], journal=rec.get("journal", ""),
                year=rec.get("year", ""),
                kw_category=rec.get("category", "Uncategorized"),
                abstract=rec["abstract"],
            )
            payload, errs = None, ["not attempted"]
            for attempt in range(MAX_ATTEMPTS):
                msg = base if attempt == 0 else (
                    base + "\n\nYour previous answer was rejected:\n"
                    + "\n".join(f"- {e}" for e in errs)
                    + "\nReturn corrected JSON only."
                )
                try:
                    resp = client.messages.create(
                        model=MODEL, max_tokens=MAX_TOKENS,
                        system=("Return a single JSON object and nothing else. "
                                "No preamble, no commentary, no code fences."),
                        messages=[{"role": "user", "content": msg}],
                    )
                    payload = parse("".join(
                        b.text for b in resp.content if b.type == "text"))
                    errs = validate(payload, claim_ids)
                    if not errs:
                        break
                except Exception as exc:
                    errs, payload = [f"{type(exc).__name__}: {exc}"], None

            if payload is None or errs:
                failed.append((pmid, rec["title"], errs))
                continue

            done[pmid] = {
                "schema": SCHEMA_VERSION,
                "model": MODEL,
                "triaged": datetime.date.today().isoformat(),
                "category": payload["category"],
                "category_keyword": rec.get("category", "Uncategorized"),
                "summary": payload["summary"],
                "key_findings": payload.get("key_findings", []),
                "confidence": payload["confidence"],
                "contradictions": payload.get("contradictions") or [],
                "reviewer_note": payload.get("reviewer_note", ""),
            }

        if failed:
            print(f"::warning::{len(failed)} record(s) failed triage validation",
                  file=sys.stderr)
            for pmid, title, errs in failed:
                print(f"  {pmid} {title[:50]} -- {'; '.join(errs)}", file=sys.stderr)

    # ---- merge triage into the library ----
    disagreements, flagged, low_conf, merged = [], [], [], 0
    for rec in records:
        t = done.get(str(rec.get("pmid")))
        if not t or t.get("schema") != SCHEMA_VERSION:
            continue
        if rec.get("category") in PUBTYPE_CATEGORIES:
            continue  # never override publication-type routing
        merged += 1
        rec["category_keyword"] = t["category_keyword"]
        rec["summary"] = t["summary"]
        rec["triage"] = {k: t[k] for k in
                         ("confidence", "contradictions", "reviewer_note", "model")}
        if t["confidence"] >= CONFIDENCE_FLOOR:
            if t["category"] != t["category_keyword"]:
                disagreements.append((rec, t))
            rec["category"] = t["category"]
        else:
            low_conf.append((rec, t))
        if t["contradictions"]:
            flagged.append((rec, t))

    if args.dry_run:
        print(f"[dry run] would merge {merged}; {len(disagreements)} disagreements, "
              f"{len(flagged)} flags, {len(low_conf)} low-confidence.", file=sys.stderr)
        return 0

    TRIAGE.write_text(json.dumps(done, indent=1, sort_keys=True), encoding="utf-8")
    LIBRARY.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

    # ---- report fragment appended to the refresh PR body ----
    REFRESH.mkdir(exist_ok=True)
    out = ["", "## Agent triage", "",
           f"{merged} record(s) carry triage; {len(flagged)} contradiction "
           f"flag(s); {len(disagreements)} category disagreement(s); "
           f"{len(low_conf)} below the {CONFIDENCE_FLOOR:.2f} confidence floor.", ""]

    if flagged:
        out += ["### Contradiction flags — read first", ""]
        for rec, t in flagged:
            out.append(f"**{rec['title']}** (PMID {rec['pmid']})")
            for f in t["contradictions"]:
                out.append(f"- {f['nature']} `{f['claim_id']}` — {f['explanation']}")
            out.append("")

    if disagreements:
        out += ["<details><summary>Category changed by the agent</summary>", ""]
        out += [f"- PMID {r['pmid']}: {t['category_keyword']} → **{t['category']}** "
                f"({t['confidence']:.2f}) — {r['title'][:70]}"
                for r, t in disagreements]
        out += ["", "</details>", ""]

    if low_conf:
        out += ["<details><summary>Low confidence — keyword category kept</summary>", ""]
        out += [f"- PMID {r['pmid']}: agent said {t['category']} "
                f"({t['confidence']:.2f}); kept {t['category_keyword']}. "
                f"{t['reviewer_note']}" for r, t in low_conf]
        out += ["", "</details>", ""]

    (REFRESH / "triage_report.md").write_text("\n".join(out), encoding="utf-8")

    print(f"merged {merged}; {len(flagged)} flags, {len(disagreements)} "
          f"disagreements, {len(low_conf)} low-confidence.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
