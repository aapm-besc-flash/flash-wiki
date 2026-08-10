"""Diagnose the eSearch HTTP 400. Prints no secret material."""
import os, sys, urllib.parse, urllib.request, urllib.error

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
key = os.environ.get("NCBI_API_KEY", "")
k = key.strip()

print(f"key: raw_len={len(key)} stripped_len={len(k)} "
      f"alnum={k.isalnum()} lower={k.islower()}")
if len(key) != len(k):
    print("  NOTE: value has surrounding whitespace (stripped before use)")
for ch in set(k):
    if not ch.isalnum():
        print(f"  NON-ALNUM CHARACTER PRESENT: {ch!r}")


def probe(label, params):
    url = f"{EUTILS}/esearch.fcgi?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            body = r.read().decode("utf-8", "replace")
        print(f"{label}: HTTP {r.status} OK  ({len(body)} bytes)")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400].replace("\n", " ")
        print(f"{label}: HTTP {e.code} -> {detail}")
    except Exception as e:
        print(f"{label}: {type(e).__name__}: {e}")


base = {"db": "pubmed", "retmode": "json"}

probe("1 simple term, no key", {**base, "term": "flash radiotherapy", "retmax": 1})
probe("2 simple term, with key", {**base, "term": "flash radiotherapy", "retmax": 1,
                                  "api_key": k})

sys.path.insert(0, "pipeline")
from flash_harvest import QUERY, TOOL, EMAIL  # noqa: E402

print(f"QUERY length: {len(QUERY)} chars")
probe("3 real query, no key, retmax 1",
      {**base, "term": QUERY, "retmax": 1, "tool": TOOL, "email": EMAIL})
probe("4 real query, no key, retmax 100000",
      {**base, "term": QUERY, "retmax": 100000, "tool": TOOL, "email": EMAIL})
probe("5 real query, with key, retmax 100000",
      {**base, "term": QUERY, "retmax": 100000, "tool": TOOL, "email": EMAIL,
       "api_key": k})
