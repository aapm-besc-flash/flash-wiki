#!/usr/bin/env python3
"""
FLASH-RT Living Literature Pipeline  —  AAPM BESC FLASH Working Group
--------------------------------------------------------------------
Harvests the FLASH radiotherapy corpus from PubMed via NCBI E-utilities,
auto-categorizes each record into the WG taxonomy, and exports:
  - flash_library.csv / .xlsx   (master structured database - source of truth)
  - flash_library.ris           (Zotero / EndNote / Mendeley import)
  - flash_library.json          (machine-readable, for the MkDocs site build)

Re-run any time to refresh the living document (idempotent; dedup by PMID).
Add NCBI_API_KEY env var to raise the rate limit to 10 req/s.

Usage:  python3 pipeline/flash_harvest.py   (run from the folder root)
"""
import os, sys, time, json, csv, re, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from datetime import date

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "AAPM_FLASH_WG"
EMAIL = "pgmaxim@gmail.com"

# Folder layout. This script lives in <root>/pipeline/; the corpus exports live
# in <root>/library/ and the RIS archive in <root>/ris_archive/. Paths are
# resolved from this file's location, so the pipeline can be launched from any
# working directory.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.join(ROOT, "library")
RIS_ARCHIVE = os.path.join(ROOT, "ris_archive")

def _load_api_key():
    """NCBI API key raises the rate limit from 3 to 10 requests/second.
    Looked up in this order:
      1. NCBI_API_KEY environment variable
      2. a file named 'ncbi_api_key.txt' next to this script (one line: the key)
    The key file keeps the secret out of the code. If you use git, add
    'ncbi_api_key.txt' to .gitignore so the key is never committed.
    """
    k = os.environ.get("NCBI_API_KEY", "").strip()
    if k:
        return k
    p = os.path.join(HERE, "ncbi_api_key.txt")
    if os.path.exists(p):
        try:
            for line in open(p, encoding="utf-8"):
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
        except Exception:
            pass
    return ""

API_KEY = _load_api_key()

# ---- The canonical FLASH-RT search string (edit here to tune the corpus) ----
#
# PLURALS ARE NOT OPTIONAL. PubMed phrase search matches an exact token
# sequence and does no stemming, so "ultra high dose rate" does NOT retrieve
# "...at ultra-high dose-rates". A recall audit against the reference lists of
# 16 FLASH reviews (2023-2026) found this had silently excluded the foundational
# 1969-1978 ultra-high-dose-rate radiobiology - Berry, Epp, Nias, Town - the
# very papers the modern field cites as its origin. ~250 records carry only the
# plural form. Any new phrase added below must be added in both numbers.
#
# VHEE is included explicitly: very-high-energy-electron papers frequently never
# use the words "FLASH" or "ultra-high dose rate" in title/abstract, so the rest
# of this query cannot see them.
QUERY = (
    '("ultra-high dose rate"[tiab] OR "ultrahigh dose rate"[tiab] OR '
    '"ultra high dose rate"[tiab] OR "ultra-high dose-rate"[tiab] OR '
    '"ultrahigh dose-rate"[tiab] OR '
    # --- plural forms of the above ---
    '"ultra-high dose rates"[tiab] OR "ultrahigh dose rates"[tiab] OR '
    '"ultra high dose rates"[tiab] OR "ultra-high dose-rates"[tiab] OR '
    # --- named modality ---
    '"FLASH radiotherapy"[tiab] OR "FLASH-RT"[tiab] OR '
    '"FLASH radiation"[tiab] OR "FLASH irradiation"[tiab] OR "FLASH effect"[tiab] OR '
    '"FLASH proton"[tiab] OR "FLASH electron"[tiab] OR '
    # --- very high energy electrons (often never say "FLASH") ---
    '"very high energy electron"[tiab] OR "very high energy electrons"[tiab] OR '
    '"VHEE"[tiab] OR '
    # --- broad fallback: the word FLASH beside a radiotherapy term ---
    '("FLASH"[tiab] AND ("dose rate"[tiab] OR "radiotherapy"[tiab] OR '
    '"radiation therapy"[tiab] OR "irradiation"[tiab] OR "Gy/s"[tiab] OR '
    '"conventional dose rate"[tiab])))'
)  # High-recall query. Materials-science / photochemistry "flash" homonyms that
   # slip through the broad fallback are caught downstream by the relevance gate
   # (see categorize()) and routed to flash_screened_out.csv for human audit.

def _url(endpoint, **params):
    params.update(tool=TOOL, email=EMAIL)
    if API_KEY:
        params["api_key"] = API_KEY
    return f"{EUTILS}/{endpoint}?" + urllib.parse.urlencode(params)

def _get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))

def esearch_ids():
    url = _url("esearch.fcgi", db="pubmed", term=QUERY, retmax=100000, retmode="json")
    data = json.loads(_get(url))
    ids = data["esearchresult"]["idlist"]
    print(f"esearch returned {len(ids)} PMIDs (count={data['esearchresult']['count']})")
    return ids

# --------------------------- Taxonomy engine ---------------------------------
# Primary category = highest weighted keyword score over title+abstract+MeSH.
# Reviews/consensus detected from PublicationType. Multi-tag secondary topics.
CATEGORIES = {
    "Radiobiology": [
        ("normal tissue", 3), ("tissue sparing", 4), ("FLASH effect", 3), ("in vivo", 2),
        ("in vitro", 2), ("mouse", 2), ("mice", 2), ("zebrafish", 3), ("tumor", 2),
        ("tumour", 2), ("cell survival", 3), ("apoptosis", 2), ("immune", 2),
        ("hypoxia", 2), ("oxygen", 1), ("radiobiolog", 4), ("clonogenic", 3),
        ("intestinal", 2), ("cognitive", 3), ("neurocognit", 3), ("fibrosis", 2),
        ("skin toxicity", 3), ("lung", 1), ("brain", 1), ("survival fraction", 3),
        ("DNA damage", 2), ("sparing effect", 3),
    ],
    "Physics & Dosimetry": [
        ("dosimet", 5), ("dosimeter", 5), ("detector", 4), ("calorimet", 4),
        ("ionization chamber", 5), ("ion chamber", 5), ("radiochromic", 4),
        ("film", 2), ("EBT", 3), ("scintillat", 4), ("alanine", 4),
        ("dose measurement", 3), ("beam monitoring", 4), ("reference dosimetry", 5),
        ("recombination", 3), ("Faraday cup", 4), ("dose per pulse", 3),
        ("calibration", 3), ("real-time dose", 3), ("diamond detector", 4),
    ],
    "Beam Delivery & Technology": [
        ("accelerator", 4), ("linac", 4), ("linear accelerator", 4), ("cyclotron", 4),
        ("synchrotron", 3), ("beam line", 3), ("beamline", 3), ("laser-driven", 4),
        ("laser driven", 4), ("very high energy electron", 4), ("VHEE", 5),
        ("pencil beam scanning", 3), ("nozzle", 3), ("machine", 1), ("prototype", 2),
        ("conversion", 2), ("kilovoltage", 2), ("X-ray tube", 3), ("carbon ion", 2),
        ("proton facility", 3), ("delivery system", 3), ("triode", 3),
    ],
    "Modeling & Mechanisms": [
        ("Monte Carlo", 5), ("simulation", 3), ("oxygen depletion", 5),
        ("radiolytic", 4), ("radiolysis", 4), ("radical", 3), ("reactive oxygen", 3),
        ("kinetic model", 5), ("computational", 3), ("track structure", 4),
        ("chemical model", 4), ("mechanism", 2), ("peroxyl", 3), ("mechanistic", 3),
        ("rate constant", 3), ("modeling", 3), ("modelling", 3), ("G-value", 4),
        ("TOPAS", 4), ("Geant4", 4), ("diffusion", 2), ("radiochemical", 4),
    ],
    "Treatment Planning & Optimization": [
        ("treatment planning", 5), ("plan optimization", 5), ("optimization", 2),
        ("dose rate optimization", 5), ("intensity modulated", 3), ("IMPT", 3),
        ("planning study", 4), ("objective function", 3), ("robust optimization", 4),
        ("transmission beam", 3), ("shoot-through", 4), ("plan quality", 3),
        ("dose-averaged dose rate", 4), ("dose rate map", 4),
    ],
    "Clinical & Translational": [
        ("clinical trial", 5), ("first-in-human", 5), ("first in human", 5),
        ("patient", 2), ("veterinary", 4), ("canine", 3), ("feline", 3),
        ("cat ", 1), ("dog ", 1), ("case report", 3), ("phase I", 4), ("phase 1", 4),
        ("FAST-01", 5), ("FAST-02", 5), ("clinical translation", 4), ("safety", 1),
        ("melanoma", 2), ("bone metastas", 3), ("feasibility", 2), ("workflow", 2),
    ],
}
REVIEW_PT = {"Review", "Systematic Review", "Consensus Development Conference",
             "Guideline", "Practice Guideline", "Meta-Analysis"}
PERSPECTIVE_PT = {"Editorial", "Comment", "Letter", "Published Erratum",
                  "Retraction of Publication", "Retracted Publication",
                  "Retraction Notice", "Expression of Concern", "News"}
# PubMed frequently tags correspondence as a plain "Journal Article"; the title
# is the reliable tell.
PERSPECTIVE_TITLE_RX = re.compile(
    r"^\s*(retraction|erratum|correction|editorial|comment on|reply to)\b"
    r"|\bletter (in response|to the editor)\b"
    r"|\bin regard(s)? to\b|\bin reply to\b|\bin response to\b"
    r"|\bauthors?['’]? (reply|response)\b",
    re.I,
)

# --------------------- Point/Counterpoint & opinion detection -----------------
# Medical Physics runs a standing "Point/Counterpoint" column and JACMP runs the
# "Three discipline collaborative radiation therapy (3DCRT) special debate" and
# related head-to-head advocacy pieces. PubMed tags these as plain Journal
# Articles, so PublicationType alone never catches them. Detect on the
# journal + title-rhetoric signature instead.
PC_JOURNALS = ("medical physics", "journal of applied clinical medical physics")
PC_TITLE_PATTERNS = [
    r"point\s*/\s*counterpoint", r"\bcounterpoint\b", r"special debate",
    r"\bdebate\b", r"\bpro\b\s+and\s+\bcon\b",
    # rhetorical either/or headline forms characteristic of the column
    r"\bor\s+(a\s+)?(passing\s+fad|flash\s+in\s+the\s+pan|fad)\b",
    r"paradigm\s+shift\s+or\b", r"newsflash\s+or\b",
    r"\bis\s+a\s+more\s+promising\s+advancement\b",
    r"\bneeds\s+ongoing\s+basic\s+and\s+animal\s+research\b",
    r"\binstead\s+of\b.*\bis\s+a\s+more\s+promising\b",
]
# Opinion / perspective essays that are not systematic or narrative reviews and
# not part of a formal debate column.
OPINION_TITLE_PATTERNS = [
    r"challenges\s+and\s+(its\s+)?future", r"\bthe\s+way\s+forward\b",
    r"\bwhere\s+do\s+we\s+(go|stand)\b", r"\bquo\s+vadis\b",
    r"\bpromise\s+and\s+peril", r"\bhype\s+or\b", r"\breality\s+check\b",
    r"\bopinion\b", r"\bviewpoint\b", r"\breflections\s+on\b",
    r"\bcurrent\s+status\s+and\s+(future\s+)?(perspectives|outlook|directions)\b",
]

def _is_point_counterpoint(title, journal, pubtypes):
    j = (journal or "").lower()
    t = (title or "").lower()
    if not any(pj in j for pj in PC_JOURNALS):
        return False
    return any(re.search(p, t) for p in PC_TITLE_PATTERNS)

def _is_opinion(title, pubtypes):
    t = (title or "").lower()
    return any(re.search(p, t) for p in OPINION_TITLE_PATTERNS)

# Radiation-oncology relevance signal: a genuine FLASH-RT record almost always
# carries at least one of these in title+abstract+MeSH.
RAD_SIGNAL = [
    "radiotherap", "radiation therap", "radiation oncolog", "dose rate", "dose-rate",
    "gy/s", "gy s", "dosimet", "radiobiol", "normal tissue", "flash-rt",
    "flash effect", "flash radiation", "ultra-high dose", "ultrahigh dose",
    "ultra high dose", "proton therap", "radiation-induced", "radiation induced",
    "conventional dose", "radiation dose", "tumor control", "tumour control",
    "veterinar", "radiochem", "radiolytic", "radiolysis", "sparing", "hypofraction",
    "linac", "carbon ion", "vhee", "very high energy electron", "clonogenic",
]
# Materials-science / chemistry homonyms of "flash" that must be screened out.
# SOFT list: screens only when there is no radiation signal at all.
OFFTOPIC = [
    "nanoprecipitation", "flash memory", "flash-anneal",
    "flash anneal", "photocatal", "metal-organic framework", "metal organic framework",
    " mof ", "semiconductor", "transistor", "chromatograph", "flash point",
    "flash flood", "flash sintering", "thin film", "thin-film",
    "fluorescent probe", "borabuckybowl", "cycloadduct", "isocyanate", "dielectric",
    "synaptic", "photochem", "microwave-assisted", "quantum dot", "perovskite",
    "electrocatal", "supercapacitor", "flash graphene", "flash nano",
]

# HARD list (match ANYWHERE in title+abstract+MeSH): senses of "flash" that
# never occur in a genuine FLASH-RT paper. Safe to screen on regardless of how
# much radiation vocabulary the abstract contains, because these papers often
# do discuss radiotherapy or radiation dose in an unrelated context (hot flashes
# in irradiated breast-cancer patients, glucose sensors in radiology suites).
HARD_OFFTOPIC_ANY = [
    # menopausal vasomotor symptoms
    "hot flash", "hot flush", "vasomotor symptom",
    # flash/continuous glucose monitoring devices
    "flash glucose",
    # preparative & physical chemistry
    "flash vacuum pyrolysis", "flash chromatograph", "flash column",
    "flash photolysis of", "flash point", "flash flood", "flash sintering",
    "flash joule", "flash graphene",
    # solid-state / storage
    "flash memory", "nand flash",
    # battery / electrolyte flash synthesis
    "vanadium electroly", "redox flow batter",
    # virtual-bolus breast planning (the "flash" there is a field extension)
    "virtual bolus",
]

# Radiotherapy *aperture* flash — "skin flash", "auto flash", "flash margin" —
# is an MLC/field-extension concept in breast planning, unrelated to UHDR.
# CASE MATTERS: "skin FLASH sparing effect" is a genuine ultra-high-dose-rate
# result, while "skin flash tool" is the planning aperture. The field writes the
# modality in all caps, so the negative lookahead below excludes it. Applied to
# the ORIGINAL-CASE text, never the lowercased copy.
APERTURE_FLASH_RX = re.compile(
    r"\b(?:skin|auto|pseudo|integrated|manual)[\s\-](?!FLASH\b)[Ff]lash\b"
    r"|(?<!FLASH )\b[Ff]lash\s+margin\b"
)

# Flash X-ray: the historical pulsed ultra-high-dose-rate lineage the WG tracks.
# Presence of the phrase RESCUES a record from the UHDR-signature gate (these
# papers predate the modern vocabulary), but does not by itself set a category —
# "FLASH X-ray-induced testicular injury" is radiobiology, not hardware.
FLASH_XRAY_RX = re.compile(
    r"\bflash[\s\-]?x[\s\-]?ray\b|\bflash radiograph|\bfield[\s\-]emission x[\s\-]?ray",
    re.I,
)
# Only a title about the apparatus itself belongs in Beam Delivery & Technology.
FLASH_XRAY_HARDWARE_RX = re.compile(
    r"(flash[\s\-]?x[\s\-]?ray|x[\s\-]?ray flash)[^.]{0,40}"
    r"\b(tube|generator|source|apparatus|device|diode|triode|unit|machine)\b"
    r"|\b(tube|generator|source|apparatus|diode|triode)\b[^.]{0,40}"
    r"(flash[\s\-]?x[\s\-]?ray|x[\s\-]?ray flash)",
    re.I,
)

# HARD list (match in the TITLE only): terms that reliably declare an off-topic
# paper when they appear in the title, but which are legitimate *methods* words
# inside a FLASH-RT abstract. "Transmission electron microscopy" is the canonical
# trap — FLASH radiobiology papers routinely image mitochondrial ultrastructure
# by TEM, so screening on it corpus-wide discards genuine studies.
HARD_OFFTOPIC_TITLE = [
    "electropolish", "focused ion beam", "transmission electron microsc",
    "cryo-em", "lamella",
    "carbene", "photopolymeri", "oxime ester", "cycloadd", "photoisomeri",
    "borosilicate glass", "rare-earth ion", "rare earth ion",
    "persistent luminescence", "quantum dot", "perovskite", "supercapacitor",
    "lithium sulfur", "graphdiyne", "corannulene",
    "superparamagnetic iron oxide", "uspio",
    "flash burn", "extreme heat and cold",
]

# A genuine FLASH-RT record carries an explicit ultra-high-dose-rate signature:
# either a UHDR phrase, or the token "FLASH" bound to a radiotherapy noun.
UHDR_RX = re.compile(
    r"ultra[\s\-]?high[\s\-]dose[\s\-]?rate"
    r"|ultra[\s\-]?high[\s\-]dosage"
    r"|\buhdr\b"
    r"|\bflash[\s\-]?(rt|radiotherap\w*|radiation\w*|irradiat\w*|therap\w*"
        r"|effect|proton\w*|electron\w*|beam\w*|dose\w*|ion beam\w*)"
    r"|\b(rt|radiotherap\w*|irradiat\w*|proton\w*|electron\w*|beam\w*)[\s\-]flash\b"
    r"|\bgy\s*/\s*s\b|\bgy\s*s\^?-1|\bgy per second"
    r"|dose[\s\-]per[\s\-]pulse"
    r"|conventional dose[\s\-]rate"
    r"|very[\s\-]high[\s\-]energy electron|\bvhee\b",
    re.I,
)

# The field writes the modality as the all-caps acronym FLASH. The homonyms are
# written in ordinary prose case ("flash photolysis", "hot flashes", "Flash
# Production of..."), so an all-caps FLASH token is a high-precision signal that
# survives cases the phrase patterns miss ("the potential of FLASH", "FLASH vs
# conventional"). Matched against the ORIGINAL, non-lowercased text.
FLASH_ACRONYM_RX = re.compile(r"\bFLASH\b")

# ---------------------- Curator overrides (human adjudication) ----------------
# Decisions made by the WG lead during manual review of the corpus. These are
# authoritative and survive every re-harvest. Value = target category, or None
# to force the record into flash_screened_out.csv.
# Keep this table small and documented; prefer fixing the rules above when a
# decision generalizes.
CURATOR_OVERRIDES = {
    # --- forced removals (not FLASH radiotherapy) ---
    "42175777": None,  # Flash electropolishing for TEM / FIB defects in tungsten
    "34640004": None,  # Rare-earth borosilicate glass from agricultural waste
    "10331759": None,  # USPIO-enhanced MRI of bone-marrow histopathology
    "30811010": None,  # Flash glucose monitors and radiological examinations
    "21552166": None,  # Hot flashes and insomnia in breast cancer
    "33667077": None,  # Ethynylhydroxycarbene (physical chemistry)
    "40503425": None,  # VMAT breast "skin flash" planning (aperture flash, not UHDR)
    "12999656": None,  # 1952 thermal flash-burn skin physiology
    # --- forced re-categorizations ---
    "13663981": "Beam Delivery & Technology",  # X-ray flash tube, ultrahigh dosage (1959)
    "5307280":  "Radiobiology",  # Repair time of chromosome breaks, pulsed x-rays UHDR
    "5539709":  "Radiobiology",  # Photobacterium fischeri, UHDR pulsed electron beam
    "11155330": "Radiobiology",  # Chromosome aberrations, pulsed vs continuous neutrons
    "16209185": "Radiobiology",  # BARS-6 pulse reactor cytogenetics in lymphocytes
    # Recovered by the 2026-08 recall audit (plural "dose-rates" / VHEE terms).
    # These predate the modern vocabulary and several carry no abstract at all,
    # so keyword scoring has nothing to work with - assign them by hand.
    "10874936": "Radiobiology",  # Nias 1974, HE electrons at UHDR, Artemia dry eggs
    "18380325": "Radiobiology",  # Temperature & chromosome aberrations, pulsed irradiation
    "41179706": "Radiobiology",  # UHDR regulates mtDNA-induced interferon-beta secretion
    "34563608": "Treatment Planning & Optimization",  # Multibeam & hypofractionation delivery
    # --- debate / opinion column assignments ---
    "35104025": "Point-Counterpoint",  # JACMP 3DCRT special debate
    "37431574": "Point-Counterpoint",  # JACMP: FLASH instead of proton arc therapy
    "40184041": "Point-Counterpoint",  # Med Phys P/C: Paradigm shift or a passing fad?
    "31246281": "Point-Counterpoint",  # Med Phys P/C: Newsflash or flash in the pan?
    "40214346": "Opinions & Debate",   # FLASH radiotherapy: Challenges and its future
}

def relevance(text):
    return sum(1 for k in RAD_SIGNAL if k in text)

SCREEN = "⚠ Screen (likely off-topic)"

def _screened(reason):
    """Screened-out verdict. The reason travels in tags[1] so the audit CSV can
    tell the curator *why* a record was rejected."""
    return SCREEN, [SCREEN, reason]

def categorize(title, abstract, mesh, pubtypes, journal="", pmid=""):
    text = f" {title} {abstract} {' '.join(mesh)} ".lower()
    pts = set(pubtypes)

    # --- curator overrides win over every automatic rule ---
    if pmid in CURATOR_OVERRIDES:
        forced = CURATOR_OVERRIDES[pmid]
        if forced is None:
            return _screened("curator override: manually excluded")
        return forced, [forced]

    tl = f" {title} ".lower()
    raw = f" {title} {abstract} "

    # --- flash X-ray *apparatus* papers: hardware, by title ---
    if FLASH_XRAY_HARDWARE_RX.search(f" {title} "):
        return "Beam Delivery & Technology", ["Beam Delivery & Technology"]

    # --- hard gate 1: senses of "flash" that never occur in FLASH-RT ---
    hits = [k for k in HARD_OFFTOPIC_ANY if k in text]
    if hits:
        return _screened(f"off-topic sense of 'flash': {hits[0]}")

    # --- hard gate 2: aperture "flash" in breast/vulvar planning (case-aware) --
    m = APERTURE_FLASH_RX.search(raw)
    if m and not UHDR_RX.search(text):
        return _screened(f"aperture/planning 'flash': {m.group(0).strip()}")

    # --- hard gate 3: off-topic subject declared in the title ---
    hits = [k for k in HARD_OFFTOPIC_TITLE if k in tl]
    if hits:
        return _screened(f"off-topic title subject: {hits[0]}")

    # --- soft gate: homonym vocabulary with no radiation signal whatsoever ---
    rad = relevance(text)
    soft = [k for k in OFFTOPIC if k in text]
    if rad == 0 and soft:
        return _screened(f"no radiation signal + off-topic term: {soft[0]}")

    # --- UHDR signature gate: records that reached us only through the loose
    # FLASH[tiab] AND (dose rate | radiotherapy | ...) arm of the query, with no
    # ultra-high-dose-rate signature anywhere, are the classic false positives.
    # The radiation-signal floor keeps borderline radiation-oncology papers in
    # the corpus for human review rather than silently discarding them. ---
    if (not UHDR_RX.search(text) and not FLASH_ACRONYM_RX.search(raw)
            and not FLASH_XRAY_RX.search(raw) and rad < 2):
        return _screened(f"no ultra-high-dose-rate signature (rad signal={rad})")

    scores = {}
    for cat, kws in CATEGORIES.items():
        s = 0
        for kw, w in kws:
            if kw.lower() in text:
                s += w
        scores[cat] = s
    tags = sorted([c for c, s in scores.items() if s >= 3], key=lambda c: -scores[c])
    primary = max(scores, key=scores.get) if max(scores.values()) > 0 else "Uncategorized"

    # --- editorial-format categories take precedence over keyword scoring ------
    # Order matters: a formal debate column outranks a generic review tag, and an
    # opinion essay outranks the fall-through "Uncategorized" bucket.
    if _is_point_counterpoint(title, journal, pubtypes):
        primary = "Point-Counterpoint"
        tags = ["Point-Counterpoint"] + [t for t in tags if t != primary]
    elif REVIEW_PT & pts:
        primary = "Reviews & Consensus"
        if "Reviews & Consensus" not in tags:
            tags = ["Reviews & Consensus"] + tags
    elif _is_opinion(title, pubtypes) and not (REVIEW_PT & pts):
        primary = "Opinions & Debate"
        tags = ["Opinions & Debate"] + [t for t in tags if t != primary]
    elif primary == "Uncategorized" and ((PERSPECTIVE_PT & pts)
                                         or PERSPECTIVE_TITLE_RX.search(title or "")):
        # editorials / letters / commentary about FLASH with no strong topic keyword
        primary = "Perspectives & Commentary"
        tags = ["Perspectives & Commentary"]
    elif primary == "Uncategorized" and rad == 0:
        # no topic keywords AND no radiation signal -> flag for human screening
        return _screened("no topic keywords and no radiation signal")

    if not tags:
        tags = [primary]
    return primary, tags

def txt(el):
    return "".join(el.itertext()).strip() if el is not None else ""

def parse_article(art):
    def find(p):
        return art.find(p)
    pmid = txt(find(".//PMID"))
    title = txt(find(".//ArticleTitle"))
    # abstract may have multiple labeled sections
    abs_parts = []
    for ab in art.findall(".//Abstract/AbstractText"):
        lbl = ab.get("Label")
        t = txt(ab)
        abs_parts.append(f"{lbl}: {t}" if lbl else t)
    abstract = " ".join(abs_parts)
    journal = txt(find(".//Journal/Title"))
    year = txt(find(".//JournalIssue/PubDate/Year")) or txt(find(".//JournalIssue/PubDate/MedlineDate"))[:4]
    # authors
    authors = []
    for a in art.findall(".//AuthorList/Author"):
        ln = txt(a.find("LastName")); ini = txt(a.find("Initials"))
        if ln:
            authors.append(f"{ln} {ini}".strip())
    doi = ""
    for aid in art.findall(".//ArticleId"):
        if aid.get("IdType") == "doi":
            doi = txt(aid)
    pmc = ""
    for aid in art.findall(".//ArticleId"):
        if aid.get("IdType") == "pmc":
            pmc = txt(aid)
    pubtypes = [txt(pt) for pt in art.findall(".//PublicationType")]
    mesh = [txt(m) for m in art.findall(".//MeshHeading/DescriptorName")]
    primary, tags = categorize(title, abstract, mesh, pubtypes,
                               journal=journal, pmid=pmid)
    return {
        "pmid": pmid, "doi": doi, "pmc": pmc, "year": year, "title": title,
        "authors": authors, "journal": journal, "abstract": abstract,
        "pubtypes": pubtypes, "mesh": mesh, "category": primary, "tags": tags,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }

def efetch(ids):
    out = []
    B = 200
    for i in range(0, len(ids), B):
        batch = ids[i:i+B]
        url = _url("efetch.fcgi", db="pubmed", id=",".join(batch), retmode="xml")
        xml = _get(url)
        root = ET.fromstring(xml)
        for art in root.findall(".//PubmedArticle"):
            try:
                out.append(parse_article(art))
            except Exception as e:
                print("parse error:", e)
        print(f"  fetched {min(i+B,len(ids))}/{len(ids)}")
        time.sleep(0.0 if API_KEY else 0.34)
    return out

def ris_escape(s):
    return (s or "").replace("\r", " ").replace("\n", " ")

def write_ris(records, path):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            ty = "JOUR"
            f.write(f"TY  - {ty}\n")
            f.write(f"TI  - {ris_escape(r['title'])}\n")
            for a in r["authors"]:
                f.write(f"AU  - {ris_escape(a)}\n")
            if r["year"]:
                f.write(f"PY  - {r['year']}\n")
            f.write(f"JO  - {ris_escape(r['journal'])}\n")
            if r["abstract"]:
                f.write(f"AB  - {ris_escape(r['abstract'])}\n")
            if r["doi"]:
                f.write(f"DO  - {r['doi']}\n")
            f.write(f"AN  - {r['pmid']}\n")
            f.write(f"UR  - {r['url']}\n")
            # store WG category as keyword for Zotero tagging
            f.write(f"KW  - FLASH:{r['category']}\n")
            for t in r["tags"]:
                if t != r["category"]:
                    f.write(f"KW  - FLASH:{t}\n")
            f.write("ER  - \n\n")

def write_ris_archive(records, archive=None):
    """Versioned RIS exports under <root>/ris_archive/.

    Two files per run:
      flash_library_YYYY-MM.ris   full corpus as it stood that month
      flash_library_YYYY-MM_new.ris   only PMIDs absent from the previous
                                      month's archive

    Why both: flash_library.ris is overwritten every run, so there is no record
    of what the corpus looked like when a manuscript cited it. The dated file is
    that audit trail. The delta exists because a full RIS import into an
    existing Zotero/EndNote library duplicates every item — importing only the
    delta adds the month's new papers without creating 1,300 duplicates.

    Re-running in the same month overwrites that month's files rather than
    accumulating, so the archive stays one entry per month.
    """
    archive = archive or RIS_ARCHIVE
    os.makedirs(archive, exist_ok=True)
    stamp = date.today().strftime("%Y-%m")

    full = os.path.join(archive, f"flash_library_{stamp}.ris")
    write_ris(records, full)

    # Previous month's archive = the most recent dated file that is not this
    # month's. Compare by PMID to isolate genuinely new records.
    prior = sorted(f for f in os.listdir(archive)
                   if re.fullmatch(r"flash_library_\d{4}-\d{2}\.ris", f)
                   and f != os.path.basename(full))
    if prior:
        seen = set()
        with open(os.path.join(archive, prior[-1]), encoding="utf-8") as f:
            for line in f:
                if line.startswith("AN  - "):
                    seen.add(line[6:].strip())
        new = [r for r in records if r["pmid"] not in seen]
        delta = os.path.join(archive, f"flash_library_{stamp}_new.ris")
        write_ris(new, delta)
        print(f"wrote ris_archive/flash_library_{stamp}.ris ({len(records)} records) "
              f"and _new.ris ({len(new)} new since {prior[-1][14:21]})")
    else:
        print(f"wrote ris_archive/flash_library_{stamp}.ris ({len(records)} records) "
              f"- first archive entry, no delta")

def main():
    print("=== FLASH-RT living-literature harvest ===")
    ids = esearch_ids()
    records = efetch(ids)
    # dedup by pmid
    seen = {}
    for r in records:
        seen[r["pmid"]] = r
    allrecs = sorted(seen.values(), key=lambda r: (r["year"] or "0"), reverse=True)
    # Split clean corpus from screened-out homonyms (auditable, never deleted)
    screened = [r for r in allrecs if r["category"].startswith("⚠")]
    records = [r for r in allrecs if not r["category"].startswith("⚠")]
    print(f"Parsed {len(allrecs)} unique records "
          f"({len(records)} in library, {len(screened)} screened out)")

    outdir = LIB
    os.makedirs(outdir, exist_ok=True)
    # screening file for human audit
    with open(os.path.join(outdir, "flash_screened_out.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pmid","year","title","journal","screen_reason","url"])
        for r in screened:
            reason = r["tags"][1] if len(r["tags"]) > 1 else ""
            w.writerow([r["pmid"], r["year"], r["title"], r["journal"],
                        reason, r["url"]])
    # JSON
    meta = {"generated": str(date.today()), "query": QUERY, "n": len(records),
            "records": records}
    with open(os.path.join(outdir, "flash_library.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    # CSV
    cols = ["pmid","year","title","authors","journal","category","tags","doi","pmc","url"]
    with open(os.path.join(outdir, "flash_library.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in records:
            w.writerow([r["pmid"], r["year"], r["title"], "; ".join(r["authors"]),
                        r["journal"], r["category"], "; ".join(r["tags"]),
                        r["doi"], r["pmc"], r["url"]])
    # RIS - current snapshot (overwritten every run)
    write_ris(records, os.path.join(outdir, "flash_library.ris"))
    # RIS - dated archive + monthly delta, for reference-manager imports
    write_ris_archive(records)

    # category breakdown
    from collections import Counter
    cc = Counter(r["category"] for r in records)
    print("\nCategory breakdown:")
    for c, n in cc.most_common():
        print(f"  {n:5d}  {c}")
    years = Counter(r["year"] for r in records if r["year"])
    openacc = sum(1 for r in records if r["pmc"])
    print(f"\nOpen-access full text (PMC): {openacc}/{len(records)}")
    print("Files written: flash_library.json / .csv / .ris")

if __name__ == "__main__":
    main()
