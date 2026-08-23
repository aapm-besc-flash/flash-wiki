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

Records listed as forced re-categorizations in CURATOR_OVERRIDES are likewise
never changed. A human read those papers and decided; that adjudication
outranks the agent. If the agent disagrees confidently it is reported in the
PR under "Agent disagrees with a curator decision", but the category stands.

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
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LIB = ROOT / "library"
LIBRARY = LIB / "flash_library.json"
TRIAGE = LIB / "triage.json"
CLAIMS = LIB / "claims.yml"
REFRESH = ROOT / ".refresh"

SCHEMA_VERSION = 1

# Records between saves to library/triage.json. A long run that only writes at
# the end loses everything to a timeout, a rate limit, or a dropped connection.
# Because already-triaged PMIDs are skipped, checkpointing also means the next
# run resumes exactly where this one stopped.
CHECKPOINT_EVERY = 25
MODEL = os.environ.get("TRIAGE_MODEL", "claude-sonnet-5")
MAX_TOKENS = 1500
MAX_ATTEMPTS = 2

# Batch API: half price for input and output, in exchange for asynchronous
# delivery. This job is monthly, unattended and latency-indifferent, so the
# trade is free money. Anthropic allows up to 24h; batches this size finish in
# minutes, but the budget below bounds the GitHub job.
BATCH_POLL_SECONDS = 20
BATCH_BUDGET_SECONDS = int(os.environ.get("BATCH_BUDGET_SECONDS", "3600"))

# If a batch is submitted but the job dies or times out before results are
# collected, the spend is already incurred. Persisting the id lets the next run
# claim those results instead of paying twice.
PENDING_BATCH = LIB / ".triage_batch.json"

# Per-million-token prices used only to print an estimate in the PR body.
# Batch pricing is half of standard; override if the model or pricing changes.
_PRICES = {           # $/Mtok at BATCH rates (half of standard)
    "claude-sonnet-5": (1.50, 7.50),
    "claude-haiku-4-5-20251001": (0.50, 2.50),
}
PRICE_IN, PRICE_OUT = _PRICES.get(MODEL, (1.50, 7.50))

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


def _curator_pinned() -> set[str]:
    """PMIDs the WG lead has re-categorized by hand in flash_harvest.py.

    These are adjudications, not guesses: someone read the paper and decided.
    They must outrank the agent exactly as they outrank the keyword model, or
    the same argument gets re-litigated every month by a model that never saw
    the reasoning. Parsed rather than imported so this script keeps working if
    flash_harvest.py grows an import-time dependency (an API key, a network
    call) that triage does not need.

    Only forced *re-categorizations* are returned. Forced removals (value None)
    never enter the corpus, so there is nothing here to protect.
    """
    src = (pathlib.Path(__file__).with_name("flash_harvest.py")
           .read_text(encoding="utf-8"))
    block = re.search(r"CURATOR_OVERRIDES\s*=\s*\{(.*?)\n\}", src, re.S)
    if not block:
        print("::warning::CURATOR_OVERRIDES not found in flash_harvest.py; "
              "curator re-categorizations are NOT protected this run.",
              file=sys.stderr)
        return set()
    return {m.group(1) for m in
            re.finditer(r'"(\d+)"\s*:\s*"[^"]+"', block.group(1))}

PROMPT = """You are triaging one publication for the AAPM BESC FLASH Working \
Group living literature corpus.

## Categories

Assign exactly one. Use only these names, spelled exactly as shown:

{categories}

## Registered claims

Assertions the wiki currently makes. Check whether this paper's own reported \
findings contradict, qualify, or supersede any of them.

{claims}

`claim_id` must be copied exactly from the bracketed ids above. Do not invent an \
id, do not renumber, and do not reference a claim that is not listed. If nothing \
in this paper bears on any registered claim -- the usual case -- return \
`"contradictions": []`.

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
  "contradictions": [],
  "reviewer_note": ""
}}

`contradictions` is usually `[]`. When it is not, each entry looks like:

{{"claim_id": "<exact id from the list above>",
  "nature": "contradicts|qualifies|supersedes",
  "explanation": "..."}}

## Hard constraints

These are checked mechanically; violating one costs a full retry.

- `category` must be exactly one of the names listed above. The publication-type
  categories -- Reviews & Consensus, Perspectives & Commentary,
  Point-Counterpoint, Opinions & Debate -- are assigned upstream and are NOT
  valid answers here, even for a paper that is plainly a review.
- `summary` must be at least 25 words.
- `confidence` is a number between 0 and 1, not a percentage or a string.

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


class Usage:
    """Real token accounting. Estimating this was a mistake made repeatedly."""

    def __init__(self):
        self.inp = self.out = self.calls = 0

    def add(self, u):
        if not u:
            return
        self.inp += getattr(u, "input_tokens", 0) or 0
        self.out += getattr(u, "output_tokens", 0) or 0
        self.calls += 1

    @property
    def dollars(self):
        return (self.inp * PRICE_IN + self.out * PRICE_OUT) / 1e6

    def line(self):
        return (f"{self.calls} call(s) - {self.inp:,} input + {self.out:,} output "
                f"tokens - about ${self.dollars:.2f} at batch pricing")


def _requests(items, claim_ids, cat_block, claim_block, corrections=None):
    """Build batch request payloads. corrections maps pmid -> list[str]."""
    # Plain dicts rather than the SDK's typed Request/MessageCreateParams
    # helpers: those symbols have moved between anthropic releases, and this
    # file must keep working when CI resolves a newer version.
    out = []
    for rec in items:
        pmid = str(rec.get("pmid"))
        body = PROMPT.format(
            categories=cat_block, claims=claim_block,
            title=rec["title"], journal=rec.get("journal", ""),
            year=rec.get("year", ""),
            kw_category=rec.get("category", "Uncategorized"),
            abstract=rec["abstract"],
        )
        errs = (corrections or {}).get(pmid)
        if errs:
            body += ("\n\nYour previous answer was rejected:\n"
                     + "\n".join(f"- {e}" for e in errs)
                     + "\nReturn corrected JSON only.")
        out.append({
            "custom_id": f"pmid-{pmid}",
            "params": {
                "model": MODEL,
                "max_tokens": MAX_TOKENS,
                "system": ("Return a single JSON object and nothing else. "
                           "No preamble, no commentary, no code fences."),
                "messages": [{"role": "user", "content": body}],
            },
        })
    return out


def _collect(client, batch_id, usage):
    """Poll one batch to completion; return {pmid: payload_or_error}."""
    waited = 0
    while True:
        b = client.messages.batches.retrieve(batch_id)
        if b.processing_status == "ended":
            break
        if waited >= BATCH_BUDGET_SECONDS:
            print(f"::warning::batch {batch_id} still running after "
                  f"{waited}s; leaving it for the next run to collect.",
                  file=sys.stderr)
            return None
        time.sleep(BATCH_POLL_SECONDS)
        waited += BATCH_POLL_SECONDS
        if waited % 120 == 0:
            print(f"  batch {batch_id}: {b.processing_status} ({waited}s)",
                  file=sys.stderr)

    out = {}
    for entry in client.messages.batches.results(batch_id):
        pmid = entry.custom_id.removeprefix("pmid-")
        r = entry.result
        if r.type != "succeeded":
            out[pmid] = ("error", [f"batch result: {r.type}"])
            continue
        usage.add(getattr(r.message, "usage", None))
        try:
            out[pmid] = ("ok", parse("".join(
                b.text for b in r.message.content if b.type == "text")))
        except Exception as exc:
            out[pmid] = ("error", [f"{type(exc).__name__}: {exc}"])
    return out


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

    usage = Usage()
    failed = []
    cat_block = "\n".join(f"- {k}: {v}" for k, v in CONTENT_CATEGORIES.items())
    claim_block = "\n".join(
        f"- [{c['id']}] {c['claim'].strip()}" for c in claims
        if c.get("status", "active") == "active"
    ) or "(none registered yet)"
    by_pmid = {str(r.get("pmid")): r for r in records}

    # ---- claim results from a batch a previous run paid for but never read ----
    results = {}
    if PENDING_BATCH.exists():
        from anthropic import Anthropic
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        prev = json.loads(PENDING_BATCH.read_text())
        print(f"recovering unread batch {prev['id']} from {prev['submitted']}",
              file=sys.stderr)
        got = _collect(client, prev["id"], usage)
        if got is None:
            print("::warning::previous batch still not ready; nothing done this run.",
                  file=sys.stderr)
            return 0
        results.update(got)
        PENDING_BATCH.unlink()
        capped = [r for r in capped if str(r.get("pmid")) not in results]

    if capped:
        from anthropic import Anthropic
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        reqs = _requests(capped, claim_ids, cat_block, claim_block)
        batch = client.messages.batches.create(requests=reqs)
        PENDING_BATCH.write_text(json.dumps(
            {"id": batch.id, "submitted": datetime.datetime.now(
                datetime.timezone.utc).isoformat(), "n": len(reqs)}, indent=1))
        print(f"submitted batch {batch.id} with {len(reqs)} request(s)",
              file=sys.stderr)
        got = _collect(client, batch.id, usage)
        if got is None:
            return 0          # id persisted; next run collects it
        PENDING_BATCH.unlink()
        results.update(got)

    if results:
        from anthropic import Anthropic
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

        # ---- validate, then one corrective batch for whatever failed ----
        good, retry = {}, {}
        for pmid, (kind, val) in results.items():
            if kind != "ok":
                retry[pmid] = val
                continue
            errs = validate(val, claim_ids)
            if errs:
                retry[pmid] = errs
            else:
                good[pmid] = val

        if retry and MAX_ATTEMPTS > 1:
            items = [by_pmid[p] for p in retry if p in by_pmid]
            print(f"{len(items)} record(s) failed validation; one corrective batch",
                  file=sys.stderr)
            # Log the reasons. Retries are the single largest cost multiplier
            # in this job, so the failure mode needs to be measured rather than
            # guessed at from the bill.
            from collections import Counter
            why = Counter(e.split(":")[0][:60]
                          for errs in retry.values() for e in errs)
            for reason, n in why.most_common():
                print(f"    {n:3d}x {reason}", file=sys.stderr)
            if items:
                b2 = client.messages.batches.create(
                    requests=_requests(items, claim_ids, cat_block, claim_block,
                                       corrections=retry))
                PENDING_BATCH.write_text(json.dumps(
                    {"id": b2.id, "submitted": datetime.datetime.now(
                        datetime.timezone.utc).isoformat(), "n": len(items)}, indent=1))
                got2 = _collect(client, b2.id, usage)
                if got2 is not None:
                    PENDING_BATCH.unlink()
                    for pmid, (kind, val) in got2.items():
                        if kind != "ok":
                            continue
                        errs = validate(val, claim_ids)
                        if not errs:
                            good[pmid] = val
                            retry.pop(pmid, None)

        for pmid, errs in retry.items():
            if pmid not in good:
                failed.append((pmid, by_pmid.get(pmid, {}).get("title", "?"), errs))

        for i, (pmid, payload) in enumerate(good.items(), 1):
            rec = by_pmid[pmid]
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

            if not args.dry_run and i % CHECKPOINT_EVERY == 0:
                TRIAGE.write_text(
                    json.dumps(done, indent=1, sort_keys=True), encoding="utf-8")
                print(f"  checkpoint: {len(done)} record(s) saved",
                      file=sys.stderr)

        if failed:
            print(f"::warning::{len(failed)} record(s) failed triage validation",
                  file=sys.stderr)
            for pmid, title, errs in failed:
                print(f"  {pmid} {title[:50]} -- {'; '.join(errs)}", file=sys.stderr)

    # ---- merge triage into the library ----
    pinned = _curator_pinned()
    disagreements, flagged, low_conf, merged = [], [], [], 0
    overruled = []
    for rec in records:
        pmid = str(rec.get("pmid"))
        t = done.get(pmid)
        if not t or t.get("schema") != SCHEMA_VERSION:
            continue
        if rec.get("category") in PUBTYPE_CATEGORIES:
            continue  # never override publication-type routing
        if pmid in pinned:
            # Hand-adjudicated by the WG lead. Record what the agent thought so
            # a persistently confident disagreement is visible and can be
            # reconsidered deliberately, but do not change the category.
            rec["summary"] = t["summary"]
            rec["triage"] = {k: t[k] for k in
                             ("confidence", "contradictions", "reviewer_note",
                              "model")}
            if (t["category"] != rec.get("category")
                    and t["confidence"] >= CONFIDENCE_FLOOR):
                overruled.append((rec, t))
            continue
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
              f"{len(flagged)} flags, {len(low_conf)} low-confidence, "
              f"{len(overruled)} curator-pinned left unchanged.", file=sys.stderr)
        return 0

    TRIAGE.write_text(json.dumps(done, indent=1, sort_keys=True), encoding="utf-8")
    LIBRARY.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

    # ---- report fragment appended to the refresh PR body ----
    REFRESH.mkdir(exist_ok=True)
    out = ["", "## Agent triage", "",
           f"{merged} record(s) carry triage; {len(flagged)} contradiction "
           f"flag(s); {len(disagreements)} category disagreement(s); "
           f"{len(low_conf)} below the {CONFIDENCE_FLOOR:.2f} confidence floor; "
           f"{len(overruled)} curator-pinned record(s) left unchanged.", ""]

    # Measured, not estimated. Printed so the run's real cost is visible in the
    # PR rather than inferred from a billing dashboard days later.
    if usage.calls:
        out += [f"**API usage this run.** {usage.line()}.", ""]
    elif not args.dry_run:
        out += ["**API usage this run.** No model calls were made.", ""]

    if overruled:
        out += ["### Agent disagrees with a curator decision — no change made",
                "",
                "These PMIDs are hand-adjudicated in `CURATOR_OVERRIDES`. The "
                "curator category stands. Listed only so a repeated, confident "
                "disagreement can be reconsidered on purpose rather than by "
                "accident.", ""]
        out += [f"- PMID {r['pmid']}: kept **{r['category']}**, agent said "
                f"{t['category']} ({t['confidence']:.2f}) — {r['title'][:70]}"
                for r, t in overruled]
        out += [""]

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
