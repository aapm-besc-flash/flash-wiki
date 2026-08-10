#!/usr/bin/env python3
"""
CI helper for the monthly corpus refresh.

Two modes:

    python pipeline/ci_refresh_report.py snapshot .refresh/before.json
        Capture the PMID set (plus minimal metadata) of the CURRENT corpus,
        before the harvest overwrites library/flash_library.json.

    python pipeline/ci_refresh_report.py report .refresh/before.json .refresh/pr_body.md
        Diff the post-harvest corpus against that snapshot and write a
        Markdown pull-request body describing what changed.

The DROPPED list is the one that matters.  Records leaving the corpus are
almost always a screening-rule change rather than a PubMed retraction, so every
dropped record deserves a look before the PR is merged.
"""

import json
import os
import sys
from datetime import date

LIBRARY = os.path.join("library", "flash_library.json")

# Cap table length so the PR body stays under GitHub's 65,536-character limit.
MAX_ROWS = 100


def load_corpus(path):
    """
    Return {pmid: slim_record}.

    flash_library.json wraps the corpus in an envelope:
        {"generated": ..., "query": ..., "n": ..., "records": [ {...}, ... ]}
    where each record carries its own "pmid" field.  Snapshot files written by
    this script are already in {pmid: {...}} form, so both shapes are accepted.
    """
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)

    if isinstance(data, dict) and "records" in data:
        records = data["records"]
    else:
        records = data

    if isinstance(records, dict):
        # Already keyed by PMID (a snapshot file, or a future dict-shaped export).
        return {str(pmid): slim(rec) for pmid, rec in records.items()}

    out = {}
    for rec in records:
        pmid = str(rec.get("pmid", "") or "").strip()
        if pmid:
            out[pmid] = slim(rec)
    return out


def slim(record):
    return {
        "title": record.get("title", "") or "",
        "journal": record.get("journal", "") or "",
        "year": record.get("year", "") or "",
        "category": record.get("category", "") or "",
    }


def cmd_snapshot(out_path):
    corpus = load_corpus(LIBRARY)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(corpus, fh)
    print(f"snapshot: {len(corpus)} records -> {out_path}")


def esc(text):
    """Neutralise pipes and newlines so a title can sit inside a Markdown table."""
    return " ".join(str(text).split()).replace("|", "\\|")


def table(rows, source):
    if not rows:
        return "_None._\n"
    lines = [
        "| PMID | Year | Journal | Title |",
        "| --- | --- | --- | --- |",
    ]
    for pmid in rows[:MAX_ROWS]:
        rec = source[pmid]
        lines.append(
            f"| [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/) "
            f"| {esc(rec['year'])} | {esc(rec['journal'])} | {esc(rec['title'])} |"
        )
    if len(rows) > MAX_ROWS:
        lines.append(f"\n_...and {len(rows) - MAX_ROWS} more (truncated)._")
    return "\n".join(lines) + "\n"


def cmd_report(before_path, out_path):
    before = load_corpus(before_path)
    after = load_corpus(LIBRARY)

    def sort_key(source):
        # Newest first; year is a string and may be blank on ahead-of-print records.
        return lambda p: (str(source[p]["year"] or ""), p)

    added = sorted(set(after) - set(before), key=sort_key(after), reverse=True)
    dropped = sorted(set(before) - set(after), key=sort_key(before), reverse=True)

    net = len(after) - len(before)
    sign = "+" if net >= 0 else ""

    body = f"""## Monthly corpus refresh - {date.today().isoformat()}

| | Records |
| --- | ---: |
| Before | {len(before):,} |
| After | {len(after):,} |
| **Net change** | **{sign}{net:,}** |

{len(added)} added - {len(dropped)} dropped

### Added ({len(added)})

{table(added, after)}
### Dropped ({len(dropped)})

> Records that left the corpus. A drop is usually caused by a screening-rule
> change rather than anything happening at PubMed - check these before merging.

{table(dropped, before)}
---

### Curator checklist

- [ ] Scan the **Dropped** table. Anything that belongs in the corpus goes into
      `CURATOR_OVERRIDES` in `pipeline/flash_harvest.py`.
- [ ] Spot-check ~10 **Added** records for category assignment. Corrections also
      go in `CURATOR_OVERRIDES`.
- [ ] Skim `library/flash_screened_out.csv` for false negatives.
- [ ] Confirm the site build step succeeded (see the Actions log for this run).

Merging this PR pushes to `main`, which triggers `deploy.yml` and republishes
the site.
"""

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(body)

    print(f"report: +{len(added)} / -{len(dropped)} (net {sign}{net}) -> {out_path}")

    # Expose counts to later workflow steps.
    summary = os.environ.get("GITHUB_OUTPUT")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"added={len(added)}\n")
            fh.write(f"dropped={len(dropped)}\n")
            fh.write(f"total={len(after)}\n")
            fh.write(f"changed={'true' if (added or dropped) else 'false'}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    mode = sys.argv[1]
    if mode == "snapshot":
        cmd_snapshot(sys.argv[2] if len(sys.argv) > 2 else ".refresh/before.json")
    elif mode == "report":
        cmd_report(
            sys.argv[2] if len(sys.argv) > 2 else ".refresh/before.json",
            sys.argv[3] if len(sys.argv) > 3 else ".refresh/pr_body.md",
        )
    else:
        sys.exit(f"unknown mode: {mode}")
