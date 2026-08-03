#!/usr/bin/env python3
"""
Build NotebookLM-ready source documents from flash_library.json.

Outputs, all inside notebooklm_sources/:
  * FLASH_00_Overview_and_Methodology.md  - corpus overview + suggested questions
  * FLASH_<Category>.md                   - one full digest per category
  * monthly_additions/FLASH_NEW_<date>.md - ONLY the papers added since the last
                                            run, so each month you drag in a single
                                            small file instead of re-uploading
                                            everything. Nothing is written when
                                            there are no new papers.

NotebookLM cannot sync from disk, so uploads are manual by necessity; the delta
file is what keeps that to one drag per month.

State is kept in notebooklm_sources/_seen_pmids.json (delete it to force a full
rebuild with no delta).

Usage: python3 pipeline/build_notebooklm.py  (run from the folder root)
"""
import os, json, datetime
from collections import Counter, defaultdict

# Lives in <root>/pipeline/; reads <root>/library/ and writes
# <root>/notebooklm_sources/.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.join(ROOT, "library")
DATA = json.load(open(os.path.join(LIB, "flash_library.json"), encoding="utf-8"))
RECS = DATA["records"]
GEN = DATA["generated"]
OUT = os.path.join(ROOT, "notebooklm_sources")
os.makedirs(OUT, exist_ok=True)

# Preferred display order. Any category present in the corpus but absent from
# this list is appended automatically (see below) — so a taxonomy change in
# flash_harvest.py can never silently drop papers from the NotebookLM sources.
CATEGORY_ORDER = [
    "Radiobiology", "Physics & Dosimetry", "Modeling & Mechanisms",
    "Beam Delivery & Technology", "Treatment Planning & Optimization",
    "Clinical & Translational", "Reviews & Consensus",
    "Perspectives & Commentary", "Point-Counterpoint", "Opinions & Debate",
    "Uncategorized",
]

# Self-healing: append any unlisted category found in the data, and drop any
# listed category that no longer has papers.
_present = {r.get("category", "Uncategorized") for r in RECS}
CATEGORY_ORDER = [c for c in CATEGORY_ORDER if c in _present] + \
                 sorted(c for c in _present if c not in CATEGORY_ORDER)

def fname(c):
    return "FLASH_" + "".join(ch if ch.isalnum() else "_" for ch in c).strip("_") + ".md"

def render(r, i):
    """Render one publication as a NotebookLM-friendly block."""
    au = ", ".join(r["authors"][:8]) + (" et al." if len(r["authors"]) > 8 else "")
    ids = [f"PMID {r['pmid']}"]
    if r["doi"]: ids.append(f"DOI {r['doi']}")
    if r["pmc"]: ids.append(f"PMC {r['pmc']} (open access)")
    return "\n".join([
        f"## {i}. {r['title']}",
        f"Authors: {au}",
        f"Journal: {r['journal']} ({r['year']})",
        f"Identifiers: {'; '.join(ids)}",
        f"URL: {r['url']}",
        f"Category: {r['category']} | Tags: {', '.join(r['tags'])}",
        f"\nAbstract: {r['abstract'] or '(no abstract available)'}\n",
        "---\n",
    ])

# ---- delta tracking: which PMIDs have we already emitted? ----------------
SEEN_PATH = os.path.join(OUT, "_seen_pmids.json")
prev_seen = set()
first_run = not os.path.exists(SEEN_PATH)
if not first_run:
    try:
        prev_seen = set(json.load(open(SEEN_PATH, encoding="utf-8")).get("pmids", []))
    except Exception:
        first_run = True
current = {r["pmid"] for r in RECS}
new_pmids = current - prev_seen

by_cat = defaultdict(list)
for r in RECS:
    by_cat[r["category"]].append(r)

manifest = []
for c in CATEGORY_ORDER:
    recs = by_cat.get(c)
    if not recs:
        continue
    recs = sorted(recs, key=lambda x: (x.get("year") or "0"), reverse=True)
    lines = [f"# FLASH Radiotherapy Literature — {c}",
             f"AAPM BESC FLASH Working Group. Corpus generated {GEN}. {len(recs)} papers.\n",
             "Each entry below is one peer-reviewed publication: title, authors, "
             "journal/year, identifiers, and the authors' abstract.\n", "---\n"]
    lines += [render(r, i) for i, r in enumerate(recs, 1)]
    txt = "\n".join(lines)
    path = os.path.join(OUT, fname(c))
    open(path, "w", encoding="utf-8").write(txt)
    manifest.append((c, len(recs), len(txt.split()), os.path.basename(path)))

# ---- monthly delta file: only what's new since the last run --------------
delta_note = ""
if first_run:
    delta_note = ("first run - no delta file written (the category files below "
                  "already contain everything)")
elif not new_pmids:
    delta_note = "no new papers since the last run - no delta file written"
else:
    newrecs = sorted([r for r in RECS if r["pmid"] in new_pmids],
                     key=lambda x: (x.get("year") or "0"), reverse=True)
    addir = os.path.join(OUT, "monthly_additions")
    os.makedirs(addir, exist_ok=True)
    dn = f"FLASH_NEW_{GEN}.md"
    ncc = Counter(r["category"] for r in newrecs)
    dl = [f"# FLASH Radiotherapy — new publications as of {GEN}",
          f"AAPM BESC FLASH Working Group. {len(newrecs)} papers added to the corpus "
          f"since the previous update.\n",
          "Add this single file to the existing NotebookLM notebook to bring it "
          "up to date — the other source files do not need re-uploading.\n",
          "## New papers by category\n"]
    dl += [f"- {c}: {n}" for c, n in ncc.most_common()]
    dl.append("\n---\n")
    dl += [render(r, i) for i, r in enumerate(newrecs, 1)]
    dtxt = "\n".join(dl)
    open(os.path.join(addir, dn), "w", encoding="utf-8").write(dtxt)
    delta_note = f"monthly_additions/{dn} — {len(newrecs)} new papers"

json.dump({"updated": GEN, "pmids": sorted(current)},
          open(SEEN_PATH, "w", encoding="utf-8"))

# overview / methodology source
cc = Counter(r["category"] for r in RECS)
oa = sum(1 for r in RECS if r["pmc"])
ov = [f"# FLASH Radiotherapy Living Literature — Overview & Methodology",
      f"AAPM BESC FLASH Working Group. Corpus generated {GEN}.\n",
      f"This notebook covers {len(RECS)} Medline-indexed FLASH radiotherapy "
      f"(ultra-high dose-rate) publications, {oa} with open-access full text, "
      f"organized into the categories below. Each category is provided as a separate "
      f"source document containing full abstracts.\n", "## Categories\n"]
for c in CATEGORY_ORDER:
    if cc.get(c):
        ov.append(f"- {c}: {cc[c]} papers")
ov.append("\n## How the corpus was built\n")
ov.append("Records were harvested from PubMed via the NCBI E-utilities API using an "
          "explicit, high-recall query for FLASH / ultra-high dose-rate radiotherapy, "
          "then filtered by a radiotherapy-relevance gate that removes unrelated 'flash' "
          "homonyms (flash memory, photochemistry, etc.). Papers were auto-categorized by "
          "a weighted keyword model over title, abstract and MeSH terms; reviews and "
          "consensus documents were routed by publication type. Abstracts are the authors' "
          "own peer-reviewed text.\n")
ov.append("## Suggested questions to ask this notebook\n")
ov += ["- What dose rates and beam parameters are associated with normal-tissue sparing in vivo?",
       "- Summarize the main proposed mechanisms of the FLASH effect and the evidence for each.",
       "- What are the open challenges in reference dosimetry at ultra-high dose rate?",
       "- Compare the clinical findings from the FAST-01 and FAST-02 trials.",
       "- Which detectors have been evaluated for real-time FLASH dose monitoring?"]
open(os.path.join(OUT, "FLASH_00_Overview_and_Methodology.md"), "w", encoding="utf-8").write("\n".join(ov))

# a short human README for the folder
adds = []
addir = os.path.join(OUT, "monthly_additions")
if os.path.isdir(addir):
    adds = sorted(f for f in os.listdir(addir) if f.endswith(".md"))

rd = ["# NotebookLM source pack\n",
      f"Regenerated automatically {GEN} by `build_notebooklm.py` (part of the monthly "
      "refresh). NotebookLM cannot read files from disk, so uploading is manual — but "
      "you only ever need to upload the small delta file after the first time.\n",
      "## First time — build the notebook\n",
      "1. Go to notebooklm.google.com → **New notebook**.",
      "2. Drag in every `.md` file in *this* folder (not the `monthly_additions` "
      "subfolder).",
      "3. Ask questions — see `FLASH_00_Overview_and_Methodology.md` for suggestions.\n",
      "## Every month afterwards — one drag\n",
      "The refresh writes a dated file into **`monthly_additions/`** containing *only* "
      "the papers added since the previous run. Drag that one file into the existing "
      "notebook. The category files do not need re-uploading.\n",
      "> Once or twice a year, it is worth rebuilding the notebook from scratch with the "
      "current category files and deleting the accumulated delta files — that keeps the "
      "source count low and removes any records whose categories were later corrected.\n",
      "## Current sources\n",
      "| Source file | Papers | ~Words |", "|---|---|---|"]
for c, n, w, fn in manifest:
    rd.append(f"| {fn} | {n} | {w:,} |")
rd.append(f"\nAll sources are well within NotebookLM's per-source limit (~500,000 words). "
          f"NotebookLM's free tier allows 50 sources per notebook; this pack uses "
          f"{len(manifest)+1}.")
if adds:
    rd.append("\n## Monthly addition files\n")
    for f in adds:
        rd.append(f"- `monthly_additions/{f}`")
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write("\n".join(rd))

print(f"wrote {len(manifest)+1} NotebookLM sources -> notebooklm_sources/")
for c, n, w, fn in manifest:
    print(f"  {fn:44s} {n:4d} papers  {w:>8,} words")
print(f"delta: {delta_note}")
