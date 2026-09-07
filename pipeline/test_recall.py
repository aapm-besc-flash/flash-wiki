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
# Precision guard. Recall has been measured since Aug 2026; precision had not,
# and a two-source citation audit on 6 Sep 2026 found 63 false positives in a
# 1,310-record corpus -- a measured precision of 95.2%.
#
# Those 63, plus three same-class records the new rules also caught, are listed
# here so the fix is permanent rather than a snapshot. Any future loosening of
# the screening rules -- a widened query, a relaxed gate, a well-meant tweak --
# fails CI at this file instead of quietly re-admitting vision-science and
# photochemistry papers. Grouped by homonym class so a failure names the class
# that regressed.
MUST_BE_ABSENT = {
    # --- original four, from earlier manual review ---
    "21552166": "hot flashes / insomnia in breast cancer",
    "30811010": "flash glucose monitoring vs radiological exams",
    "42175777": "flash electropolishing for TEM",
    "40698312": "automated 'skin flash' breast planning technique",

    # --- product / acronym named Flash (4) ---
    "42287986": "Breast cancer patients' questions about radiotherapy-induced skin ",
    "31437345": "Defining a national reference level for intraoperative radiation e",
    "25672612": "Evaluation of the Flash effect in breast irradiation using TomoDir",
    "22225292": "Dosimetric characteristics and quality control tests for the colli",

    # --- photodynamic therapy (1) ---
    "41241814": "Flash Photodynamic Therapy - How the Saturation of Photosensitizer",

    # --- materials processing (4) ---
    "37607534": "Flash-Thermal Shock Synthesis of High-Entropy Alloys Toward High-P",
    "32274315": "Low-Thermal-Budget Doping of 2D Materials in Ambient Air Exemplifi",
    "31259486": "Janus Graphene Liquid Crystalline Fiber with Tunable Properties En",
    "19601624": "Flash reduction and patterning of graphite oxide and its polymer c",

    # --- other verified homonym (5) ---
    "37568795": "Influence of the Hypersensitivity to Low Dose Phenomenon on the Tu",
    "35116657": "Impact of high-dose rate radiotherapy on B and natural killer (NK)",
    "11294635": "Roles of amino acid residues near the chromophore of photoactive y",
    "11252979": "[Drugs and drug abusers].",
    "5820640": "A comparison of the effects of ultraviolet and ionizing radiations",

    # --- MRI FLASH sequence (7) ---
    "34874313": "Phantom assessment of three-dimensional geometric distortion of a ",
    "32638078": "Imaged-guided and muscle sparing laparoscopic anorectoplasty using",
    "25827180": "FLASH proton density imaging for improved surface coil intensity c",
    "12758237": "Quantitative tissue perfusion measurements in head and neck carcin",
    "10560342": "Comparison of MRI with CT for the radiotherapy planning of prostat",
    "8756151": "[Contrast medium assisted dynamic MR-mammography after diagnostic ",
    "8536396": "Digital subtraction in Gd-DTPA enhanced imaging of the breast.",

    # --- photobiology / optogenetics (1) ---
    "29267341": "Optogenetic conditioning of paradigm and pattern discrimination in",

    # --- flash photolysis / photochemistry (11) ---
    "28821738": "Directly monitor protein rearrangement on a nanosecond-to-millisec",
    "24447955": "Experimental investigation of a local recirculation photobioreacto",
    "22839678": "Free energy relationships for reactions of substituted benzhydryli",
    "20394449": "Mechanistic and energetic aspects of the thermal and photochemical",
    "19917265": "Visualizing changes in electron distribution in coupled chains of ",
    "12914476": "Evidence for inverted region behavior in proton transfer to carban",
    "12137524": "Dynamics of proton transfer at nonactivated carbons from laser fla",
    "10987955": "Laser flash photolysis evidence for styryl radical cation cyclizat",
    "9199783": "Comparison of Na+/K(+)-ATPase pump currents activated by ATP conce",
    "11666567": "Mechanism of (&mgr;-H)(&mgr;-alkenyl)Re(2)(CO)(8) Formation in 350",
    "24253646": "Kinetics of the dichroic reorientation of phytochrome during photo",

    # --- vision science (17) ---
    "23690204": "Liquid crystal display screens as stimulators for visually evoked ",
    "18054372": "What does the illusory-flash look like?",
    "17710142": "Speech and non-speech audio-visual illusions: a developmental stud",
    "17428990": "Early cross-modal interactions in auditory and visual cortex under",
    "2339504": "The oscillatory potentials in response to stimuli of photopic inte",
    "2781731": "Two pulses seen as three flashes: a superposition analysis.",
    "3177590": "Laser-induced chromatic adaptation.",
    "3188403": "Cone interaction occurs in the parafovea under pi 4 stimulus condi",
    "3499028": "Rod and cone system contributions to oscillatory potentials: an ex",
    "4003522": "Visual evoked potential correlates of laser flashblindness in rhes",
    "7179753": "The decrease in the threshold on the dark side of the luminance ed",
    "7269308": "Visual masking and the contrast-flash effect.",
    "1006999": "Color properties of the contrast flash effect: monoptic vs dichopt",
    "941415": "Rod-cone interaction in the after-flash effect.",
    "4421568": "Sensitization by annular surrounds: sensitization and the contrast",
    "14288519": "THE SPECIFICITY OF THE CONE INTERACTION IN THE AFTER-FLASH EFFECT.",
    "14288518": "ROD-CONE INDEPENDENCE IN THE AFTER-FLASH EFFECT.",

    # --- flash radiography / metrology (7) ---
    "23075930": "Recent results of irradiations of DIS-1 dosemeters with an XR200 X",
    "22047305": "Magnifying lens for 800 MeV proton radiography.",
    "7934252": "Sub-kilohertz flash X-ray generator utilising a glass-enclosed col",
    "18699329": "Expandable flash x-ray tube (FXT) having a 0.5-mm source size.",
    "15719954": "Compact monochromatic flash x-ray generator utilizing a disk-catho",
    "12949421": "Irradiation of intense characteristic x-rays from weakly ionized l",
    "8231324": "Disk-cathode flash X-ray tube driven by a repetitive two-stage Mar",

    # --- DESY free-electron laser (2) ---
    "20441325": "The extreme ultraviolet split and femtosecond delay unit at the pl",
    "19546907": "Characteristics of focused soft X-ray free-electron laser beam det",

    # --- historical single-fraction 'flash' (6) ---
    "11862505": "Double-flash, large-fraction radiation therapy as palliative treat",
    "8884966": "Adjuvant postoperative radiotherapy in rectal cancer: 148 cases tr",
    "6886460": "[Bladder tumors treated with radical cystectomy. Results of 78 cas",
    "6841985": "[Role of radiotherapy in the treatment of bladder cancer. Comments",
    "6580684": "Intra-arterial infusion of bromodeoxyuridine and radiotherapy in o",
    "6796625": "[Parenteral hyperalimentation and cystoprostatectomy for carcinoma",

    # --- lightning / flashover (1) ---
    "3779473": "Lightning injury caused by discharges accompanying flashovers--a c",
}


# Measured quality of the corpus, updated when an audit is run. Recall comes
# from the Aug 2026 comparison against the reference lists of 16 FLASH reviews;
# precision from the Sep 2026 two-source citation audit of all 1,310 records.
# Kept here, next to the tests that defend them, rather than in prose that drifts.
MEASURED = {
    "recall":    (0.98, "Aug 2026, vs reference lists of 16 FLASH reviews"),
    "precision": (0.952, "6 Sep 2026, two-source audit: 63 false positives in 1,310"),
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
    print(f"\n  Guarding {len(MUST_BE_PRESENT)} landmark papers and "
          f"{len(MUST_BE_ABSENT)} verified homonyms.")
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
    print(f"\n  Last measured  recall {MEASURED['recall'][0]:.1%}  "
          f"({MEASURED['recall'][1]})")
    print(f"                 precision {MEASURED['precision'][0]:.1%}  "
          f"({MEASURED['precision'][1]})")


if __name__ == "__main__":
    main()
