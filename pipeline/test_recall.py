#!/usr/bin/env python3
"""
Recall guard for the FLASH corpus.
----------------------------------
Checks that a hand-picked set of landmark FLASH / ultra-high-dose-rate papers
is present in library/flash_library.json. Run after any edit to QUERY or to the
screening rules in flash_harvest.py.

    python3 pipeline/test_recall.py

Why this file exists
--------------------
A recall audit in Aug 2026 compared the corpus against the reference lists of
16 FLASH reviews (2023-2026). It found the query was silently missing the
foundational 1969-1978 ultra-high-dose-rate radiobiology, because PubMed phrase
search does not stem: "ultra high dose rate" never matches "...dose-rates".
Roughly 250 records carry only the plural. Nothing in the pipeline would have
revealed that - the papers simply never appeared, so they were absent from
flash_screened_out.csv too.

These PMIDs are the tripwire. If one disappears, the query or the screening
logic has regressed.

To extend: add any paper the WG considers non-negotiable. Keep the comment
explaining WHY each entry is a meaningful test, not just what it is.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# PMID -> (short label, what it guards against)
MUST_BE_PRESENT = {
    # --- historic UHDR radiobiology: guards the PLURAL phrase forms ---
    "4975207":  ("Survival of mammalian cells at ultra-high dose-rates (1969)",
                 "plural 'dose-rates'"),
    "5015264":  ("Reproductive survival after UHDR irradiation (1972)",
                 "plural 'dose-rates'"),
    "4607987":  ("Oxygen depletion at ultra-high dose-rates (1974)",
                 "plural 'dose-rates'"),
    "10874936": ("Nias 1974, HE electrons at UHDR, Artemia dry eggs",
                 "plural + no abstract, needs curator override"),
    "22008289": ("Tumour cell survival after proton irradiation at UHDR (2011)",
                 "plural 'dose rates'"),
    # --- VHEE: these papers often never say FLASH or UHDR at all ---
    "25207591": ("VHEE dosimetry for radiotherapy (2014)", "VHEE term in query"),
    "33057078": ("Laser-driven VHEE for radiotherapy (2020)", "VHEE term in query"),
    # --- modern landmarks: guard the core FLASH terms and the screening gates ---
    "38711960": ("Anesthetic oxygen & sex in the FLASH sparing effect",
                 "case-aware 'skin FLASH' vs planning 'skin flash'"),
    "39070145": ("Sparing effect of UHDR irradiation on the oesophagus",
                 "TEM as a methods word must not screen radiobiology"),
}

# These must NOT be in the corpus - they are the homonyms the filter exists for.
MUST_BE_ABSENT = {
    "21552166": "hot flashes / insomnia in breast cancer",
    "30811010": "flash glucose monitoring vs radiological exams",
    "42175777": "flash electropolishing for TEM",
    "40698312": "automated 'skin flash' breast planning technique",
}


def main():
    path = os.path.join(ROOT, "library", "flash_library.json")
    if not os.path.exists(path):
        sys.exit(f"FAIL: {path} not found - run flash_harvest.py first")
    recs = json.load(open(path, encoding="utf-8"))["records"]
    lib = {r["pmid"]: r for r in recs}

    fails = []
    print(f"Corpus: {len(lib)} records\n")

    print("Landmark papers that must be PRESENT:")
    for pmid, (label, guards) in MUST_BE_PRESENT.items():
        ok = pmid in lib
        cat = lib[pmid]["category"] if ok else "-"
        print(f"  {'ok  ' if ok else 'FAIL'}  {pmid:9s} {label[:52]:52s} [{cat}]")
        if not ok:
            fails.append(f"MISSING {pmid} ({label}) - guards: {guards}")

    print("\nHomonyms that must be ABSENT:")
    for pmid, label in MUST_BE_ABSENT.items():
        ok = pmid not in lib
        print(f"  {'ok  ' if ok else 'FAIL'}  {pmid:9s} {label}")
        if not ok:
            fails.append(f"PRESENT but should be screened: {pmid} ({label})")

    print()
    if fails:
        print(f"{len(fails)} FAILURE(S):")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print("All recall checks passed.")


if __name__ == "__main__":
    main()
