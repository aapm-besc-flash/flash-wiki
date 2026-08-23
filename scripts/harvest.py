#!/usr/bin/env python3
"""
Stage 1: fetch candidate records and deduplicate. Fully deterministic.

Europe PMC is used instead of NCBI E-utilities because it needs no API key,
returns clean JSON, and indexes bioRxiv/medRxiv preprints alongside PubMed --
which matters for FLASH, where a lot of the interesting work is preprinted first.

Outputs data/new_items.json (records not already in the corpus).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import time

import requests
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
PAGE_SIZE = 100
MAX_PAGES = 20  # hard ceiling; a runaway query should fail loudly, not silently


def load_yaml(path: pathlib.Path) -> dict:
    with path.open() as fh:
        return yaml.safe_load(fh)


def load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    with path.open() as fh:
        return json.load(fh)


def build_query(cfg: dict, since: str) -> str:
    """Assemble a single Europe PMC query string from config/sources.yml."""
    include = " OR ".join(f'"{t}"' for t in cfg["include_terms"])
    q = f"({include})"
    if cfg.get("exclude_terms"):
        exclude = " OR ".join(f'"{t}"' for t in cfg["exclude_terms"])
        q += f" NOT ({exclude})"
    q += f' AND (FIRST_PDATE:[{since} TO {dt.date.today().isoformat()}])'
    if cfg.get("open_access_only"):
        q += " AND OPEN_ACCESS:Y"
    return q


def fetch(query: str) -> list[dict]:
    """Page through Europe PMC with cursorMark. Raises on HTTP failure."""
    out, cursor, page = [], "*", 0
    while page < MAX_PAGES:
        r = requests.get(
            EPMC,
            params={
                "query": query,
                "format": "json",
                "pageSize": PAGE_SIZE,
                "cursorMark": cursor,
                "resultType": "core",
            },
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        hits = body.get("resultList", {}).get("result", [])
        out.extend(hits)
        next_cursor = body.get("nextCursorMark")
        if not hits or next_cursor == cursor:
            break
        cursor, page = next_cursor, page + 1
        time.sleep(0.34)  # be polite
    else:
        raise RuntimeError(
            f"Hit MAX_PAGES={MAX_PAGES}. Query is too broad or the date window "
            "is too wide -- narrow it rather than raising the ceiling."
        )
    return out


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:80]


def normalize(rec: dict) -> dict:
    """Flatten a Europe PMC record to the fields downstream stages rely on."""
    doi = (rec.get("doi") or "").lower().strip()
    pmid = (rec.get("pmid") or "").strip()
    title = (rec.get("title") or "").strip().rstrip(".")
    year = (rec.get("pubYear") or "").strip()
    authors = (rec.get("authorString") or "").strip()
    first_author = authors.split(",")[0].split(" ")[0] if authors else "anon"
    return {
        "key": doi or (f"pmid:{pmid}" if pmid else f"title:{slugify(title)}"),
        "doi": doi,
        "pmid": pmid,
        "pmcid": (rec.get("pmcid") or "").strip(),
        "title": title,
        "abstract": (rec.get("abstractText") or "").strip(),
        "authors": authors,
        "journal": (rec.get("journalTitle") or rec.get("bookOrReportDetails", {}).get("publisher") or "").strip(),
        "year": year,
        "source": rec.get("source", ""),
        "is_preprint": rec.get("source") == "PPR",
        "url": f"https://doi.org/{doi}" if doi else (
            f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""
        ),
        "citekey": f"{slugify(first_author)}{year}{slugify(title.split(' ')[0])}",
        "slug": slugify(f"{year}-{first_author}-{' '.join(title.split(' ')[:6])}"),
        "harvested": dt.date.today().isoformat(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="", help="YYYY-MM-DD; blank = resume from state")
    args = ap.parse_args()

    DATA.mkdir(exist_ok=True)
    cfg = load_yaml(ROOT / "config" / "sources.yml")
    state = load_json(DATA / "state.json", {})
    corpus = load_json(DATA / "corpus.json", {})

    since = args.since or state.get("last_run") or cfg.get("bootstrap_since", "2024-01-01")
    query = build_query(cfg, since)
    print(f"Query window from {since}\n{query}\n", file=sys.stderr)

    raw = fetch(query)
    print(f"Europe PMC returned {len(raw)} records.", file=sys.stderr)

    new, seen = [], set()
    for rec in raw:
        item = normalize(rec)
        if not item["title"] or not item["abstract"]:
            continue  # no abstract means the agent has nothing to reason over
        if item["key"] in corpus or item["key"] in seen:
            continue
        seen.add(item["key"])
        new.append(item)

    # Preprint that later appeared as a journal article: keep the version of
    # record, drop the preprint, matched on normalized title.
    by_title: dict[str, dict] = {}
    for item in new:
        t = slugify(item["title"])
        prev = by_title.get(t)
        if prev is None or (prev["is_preprint"] and not item["is_preprint"]):
            by_title[t] = item
    new = list(by_title.values())

    (DATA / "new_items.json").write_text(json.dumps(new, indent=2))
    state["last_run"] = dt.date.today().isoformat()
    state["last_count"] = len(new)
    (DATA / "state.json").write_text(json.dumps(state, indent=2))

    print(f"{len(new)} new after dedupe.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
