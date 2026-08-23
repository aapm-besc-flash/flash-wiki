#!/usr/bin/env python3
"""
Stage 2: the only stage where a model is involved.

Three jobs, all of which require judgment and none of which are scriptable:
  1. place each record in the taxonomy
  2. write a short summary in the wiki's voice
  3. flag where a record appears to contradict a registered claim

Everything the model returns is validated against the taxonomy and the claims
register before it is allowed downstream. A record that fails validation twice
is written to triage_errors.json and excluded -- it does not reach the PR.
"""

from __future__ import annotations

import json
import os
import pathlib
import sys

import yaml
from anthropic import Anthropic

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

MODEL = os.environ.get("TRIAGE_MODEL", "claude-sonnet-5")
MAX_TOKENS = 2000
MAX_ATTEMPTS = 2


def load_yaml(path):
    with path.open() as fh:
        return yaml.safe_load(fh)


def load_json(path, default):
    return json.load(path.open()) if path.exists() else default


def claims_for(domains: list[str], claims: list[dict], limit: int = 40) -> list[dict]:
    """
    Only the claims plausibly at risk are sent, not the whole register.

    This is the design decision that keeps the step affordable and accurate:
    you cannot hand the model the entire wiki every run, so the wiki maintains
    a distilled register of its own load-bearing assertions in data/claims.yml
    and the agent is asked to check against the relevant slice of it.
    """
    hits = [c for c in claims if set(c.get("domains", [])) & set(domains)]
    return [
        {"id": c["id"], "claim": c["claim"], "domains": c.get("domains", [])}
        for c in hits[:limit]
    ]


def build_prompt(template: str, item: dict, taxonomy: dict, claims: list[dict]) -> str:
    domain_block = "\n".join(
        f"- {k}: {v['label']} -- {v['scope']}" for k, v in taxonomy["domains"].items()
    )
    claim_block = (
        "\n".join(f"- [{c['id']}] {c['claim']}" for c in claims)
        or "(no registered claims in these domains yet)"
    )
    return (
        template.replace("{{DOMAINS}}", domain_block)
        .replace("{{CLAIMS}}", claim_block)
        .replace("{{TITLE}}", item["title"])
        .replace("{{JOURNAL}}", item["journal"] or "unknown venue")
        .replace("{{YEAR}}", item["year"])
        .replace("{{PREPRINT}}", "yes -- not peer reviewed" if item["is_preprint"] else "no")
        .replace("{{ABSTRACT}}", item["abstract"])
    )


def validate(payload: dict, taxonomy: dict, allowed_claim_ids: set[str]) -> list[str]:
    """Return a list of problems. Empty list means the payload is usable."""
    problems = []
    domains = payload.get("domains")
    if not isinstance(domains, list) or not 1 <= len(domains) <= 2:
        problems.append("domains must be a list of 1-2 entries")
    else:
        for d in domains:
            if d not in taxonomy["domains"]:
                problems.append(f"unknown domain '{d}'")

    summary = payload.get("summary", "")
    if not isinstance(summary, str) or len(summary.split()) < 25:
        problems.append("summary too short or missing")

    if payload.get("relevance") not in {"core", "peripheral", "out-of-scope"}:
        problems.append("relevance must be core|peripheral|out-of-scope")

    conf = payload.get("confidence")
    if not isinstance(conf, (int, float)) or not 0 <= conf <= 1:
        problems.append("confidence must be a number in [0,1]")

    for flag in payload.get("contradictions", []):
        if flag.get("claim_id") not in allowed_claim_ids:
            problems.append(f"contradiction cites unknown claim_id '{flag.get('claim_id')}'")
        if not flag.get("explanation"):
            problems.append("contradiction missing explanation")

    return problems


def parse_json(text: str) -> dict:
    """Tolerate a fenced block; reject anything else."""
    t = text.strip()
    if t.startswith("```"):
        t = t.split("```")[1]
        if t.startswith("json"):
            t = t[4:]
    return json.loads(t.strip())


def main() -> int:
    items = load_json(DATA / "new_items.json", [])
    if not items:
        print("Nothing to triage.", file=sys.stderr)
        return 0

    taxonomy = load_yaml(ROOT / "config" / "taxonomy.yml")
    claims = load_yaml(ROOT / "data" / "claims.yml") or []
    template = (ROOT / "prompts" / "triage.md").read_text()
    all_claim_ids = {c["id"] for c in claims}

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    results, errors = [], []

    for i, item in enumerate(items, 1):
        print(f"[{i}/{len(items)}] {item['title'][:70]}", file=sys.stderr)

        # First pass with the full claim register slice for all domains, since
        # we don't yet know which domains the model will choose.
        relevant = claims_for(list(taxonomy["domains"]), claims)
        prompt = build_prompt(template, item, taxonomy, relevant)

        payload, problems = None, ["not attempted"]
        for attempt in range(MAX_ATTEMPTS):
            msg = prompt if attempt == 0 else (
                prompt
                + "\n\nYour previous response was rejected for these reasons:\n"
                + "\n".join(f"- {p}" for p in problems)
                + "\nReturn corrected JSON only."
            )
            try:
                resp = client.messages.create(
                    model=MODEL,
                    max_tokens=MAX_TOKENS,
                    system=(
                        "You are a triage assistant for a radiation-oncology "
                        "working-group wiki. Return a single JSON object and "
                        "nothing else -- no preamble, no code fences, no commentary."
                    ),
                    messages=[{"role": "user", "content": msg}],
                )
                payload = parse_json("".join(
                    b.text for b in resp.content if b.type == "text"
                ))
                problems = validate(payload, taxonomy, all_claim_ids)
                if not problems:
                    break
            except Exception as exc:  # network, parse, or API failure
                problems = [f"{type(exc).__name__}: {exc}"]
                payload = None

        if payload is None or problems:
            errors.append({"item": item, "problems": problems})
            continue

        results.append({**item, "triage": payload})

    (DATA / "triage.json").write_text(json.dumps(results, indent=2))
    if errors:
        (DATA / "triage_errors.json").write_text(json.dumps(errors, indent=2))

    print(f"Triaged {len(results)}; {len(errors)} failed validation.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
