#!/usr/bin/env python3
"""
Stage 3: turn validated triage output into files. Deterministic again.

Writes one markdown stub per accepted record, appends BibTeX, updates the
corpus index, and composes a PR body that puts contradiction flags and
low-confidence items at the top where a reviewer will actually see them.
"""

from __future__ import annotations

import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
WIKI = ROOT / "wiki"
BIB = ROOT / "references.bib"


def load_json(path, default):
    return json.load(path.open()) if path.exists() else default


def bibtex(item: dict) -> str:
    entry = "misc" if item["is_preprint"] else "article"
    fields = {
        "title": item["title"],
        "author": item["authors"].replace(", ", " and "),
        "journal": item["journal"],
        "year": item["year"],
        "doi": item["doi"],
        "note": "Preprint" if item["is_preprint"] else "",
    }
    body = "".join(
        f"  {k} = {{{v}}},\n" for k, v in fields.items() if v
    )
    return f"@{entry}{{{item['citekey']},\n{body}}}\n\n"


def page(item: dict, taxonomy: dict) -> str:
    t = item["triage"]
    labels = ", ".join(taxonomy["domains"][d]["label"] for d in t["domains"])
    front = {
        "title": item["title"],
        "citekey": item["citekey"],
        "doi": item["doi"],
        "pmid": item["pmid"],
        "year": item["year"],
        "journal": item["journal"],
        "domains": t["domains"],
        "relevance": t["relevance"],
        "preprint": item["is_preprint"],
        "harvested": item["harvested"],
        "triage_confidence": t["confidence"],
        "review_status": "unreviewed",
    }
    out = ["---", yaml.safe_dump(front, sort_keys=False).strip(), "---", ""]
    out += [f"# {item['title']}", ""]
    out += [f"*{item['journal'] or 'Preprint'} ({item['year']})* &middot; {labels}", ""]
    if item["is_preprint"]:
        out += ["> **Preprint — not peer reviewed.**", ""]
    out += ["## Summary", "", t["summary"], ""]
    if t.get("key_findings"):
        out += ["## Key findings", ""]
        out += [f"- {k}" for k in t["key_findings"]] + [""]
    if t.get("methods_note"):
        out += ["## Methods", "", t["methods_note"], ""]
    if t.get("contradictions"):
        out += ["## Flagged against registered claims", ""]
        for c in t["contradictions"]:
            out += [f"- **{c['nature']}** `{c['claim_id']}` — {c['explanation']}"]
        out += [""]
    if t.get("reviewer_note"):
        out += ["## Reviewer note", "", t["reviewer_note"], ""]
    out += ["## Editor commentary", "", "<!-- Human commentary goes here. -->", ""]
    out += ["---", "", f"[Source]({item['url']}) · `{item['citekey']}`", ""]
    out += [
        "*Drafted by the harvest workflow. Summary and classification are "
        "machine-generated and require review before this page is considered "
        "part of the wiki.*",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    results = load_json(DATA / "triage.json", [])
    if not results:
        (DATA / "pr_body.md").write_text("No records survived triage.\n")
        return 0

    taxonomy = yaml.safe_load((ROOT / "config" / "taxonomy.yml").open())
    corpus = load_json(DATA / "corpus.json", {})
    errors = load_json(DATA / "triage_errors.json", [])

    written, skipped, flagged, low_conf = [], [], [], []
    bib_additions = []

    for item in results:
        t = item["triage"]
        if t["relevance"] == "out-of-scope":
            # Still recorded, so it is never re-harvested and re-triaged.
            corpus[item["key"]] = {"title": item["title"], "status": "out-of-scope"}
            skipped.append(item)
            continue

        primary = t["domains"][0]
        path = WIKI / primary / f"{item['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page(item, taxonomy))
        written.append((item, path.relative_to(ROOT)))

        bib_additions.append(bibtex(item))
        corpus[item["key"]] = {
            "title": item["title"],
            "citekey": item["citekey"],
            "domains": t["domains"],
            "path": str(path.relative_to(ROOT)),
            "status": "unreviewed",
        }
        if t.get("contradictions"):
            flagged.append(item)
        if t["confidence"] < 0.5:
            low_conf.append(item)

    if bib_additions:
        with BIB.open("a") as fh:
            fh.write("".join(bib_additions))

    (DATA / "corpus.json").write_text(json.dumps(corpus, indent=2, sort_keys=True))

    # ---- PR body: attention-ordered, not chronological ----
    b = ["## Literature harvest", ""]
    b += [
        f"{len(written)} page(s) drafted · {len(skipped)} judged out-of-scope · "
        f"{len(errors)} failed validation",
        "",
        "Every page below is machine-drafted and marked `review_status: unreviewed`. "
        "Merging is your sign-off.",
        "",
    ]

    if flagged:
        b += ["### ⚠️ Contradiction flags — read these first", ""]
        for item in flagged:
            b += [f"**{item['title']}** (`{item['citekey']}`)"]
            for c in item["triage"]["contradictions"]:
                b += [f"- {c['nature']} `{c['claim_id']}` — {c['explanation']}"]
            b += [""]

    if low_conf:
        b += ["### Low-confidence classification", ""]
        b += [
            f"- {i['title']} — confidence {i['triage']['confidence']:.2f}"
            for i in low_conf
        ] + [""]

    b += ["### Pages added", ""]
    for item, rel in written:
        doms = "/".join(item["triage"]["domains"])
        b += [f"- `{doms}` — [{item['title']}]({item['url']})"]
    b += [""]

    if skipped:
        b += ["<details><summary>Judged out-of-scope</summary>", ""]
        b += [f"- {i['title']}" for i in skipped]
        b += ["", "</details>", ""]

    if errors:
        b += ["<details><summary>Failed validation (excluded)</summary>", ""]
        b += [f"- {e['item']['title']} — {'; '.join(e['problems'])}" for e in errors]
        b += ["", "</details>", ""]

    b += [
        "---",
        "",
        "**Reviewer checklist**",
        "",
        "- [ ] Domain assignments correct",
        "- [ ] Summaries match what the abstracts actually say",
        "- [ ] Contradiction flags checked against the source",
        "- [ ] Out-of-scope decisions spot-checked",
        "- [ ] `review_status` flipped to `reviewed` on accepted pages",
        "",
    ]
    (DATA / "pr_body.md").write_text("\n".join(b))

    print(f"Wrote {len(written)} pages; {len(flagged)} flagged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
