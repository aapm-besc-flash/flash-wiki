# FLASH Radiotherapy Living Wiki

A continuously updated, categorized corpus of MEDLINE-indexed FLASH radiotherapy
literature, maintained by the **AAPM BESC FLASH Working Group**.

Live site: **https://aapm-besc-flash.github.io/flash-wiki/** — the current record
count and category breakdown are on its front page; this file does not repeat
them because it would go stale.

## Scope

This corpus covers **the FLASH effect and ultra-high dose rate irradiation**: any
peer-reviewed work in which ultra-high dose rate delivery, or the biological effect
it produces, is an object of study -- whether or not the application is cancer
therapy.

**Included**

- Preclinical and clinical FLASH irradiation, in any species
- Beam production and delivery capable of ultra-high dose rate -- electron, proton,
  carbon ion, VHEE, X-ray -- including plasma-wakefield and laser-driven sources,
  whether or not a therapeutic application is stated
- Dosimetry, detector development and QA for UHDR beams
- Treatment planning and optimisation for UHDR delivery
- Mechanistic work: oxygen depletion, radical chemistry, immune and vascular response
- The FLASH effect studied outside the clinic -- radiation protection, nuclear-event
  dosimetry, accidental and environmental exposure at ultra-high dose rate
- Non-therapeutic UHDR applications where dose rate is a studied variable
- Historical ultra-high-dose-rate radiobiology in any organism, including the
  1960s-1970s literature that predates the modern vocabulary
- Reviews, consensus statements and commentary on the above

**Excluded**

- Other senses of the word "flash": vision science and after-image psychophysics,
  laser flash photolysis, the MRI FLASH gradient-echo sequence, flash radiography
  and metrology, lightning and flashover injury, product and model names, and the
  historical use of "flash" for a single large fraction delivered at conventional
  dose rate
- Work where dose rate is incidental rather than studied. A conventional-dose-rate
  experiment is not in scope merely because the dose rate is reported, and a paper
  is not in scope merely because it mentions FLASH in passing as a future direction.

The boundary is **dose rate as an object of study**, not clinical intent. A paper
asking what ultra-high dose rate does is in scope; a paper that happens to use a
fast beam, or that cites FLASH once in its discussion, is not.

Adopted 6 September 2026. The exclusion list is enforced mechanically in
`pipeline/flash_harvest.py` and regression-tested in `pipeline/test_recall.py`.
The final clause -- passing mention -- resists mechanical enforcement (see
*Screening limits* below) and is assessed by the triage agent and by curators.

### Screening limits

Two quality figures are measured rather than asserted, and printed by
`test_recall.py` on every run: **recall 98%** against the reference lists of 16
FLASH reviews (Aug 2026), and **precision 95.2%** from a two-source citation audit
of all 1,310 records (Sep 2026).

One known limit: papers that are squarely in radiation oncology but mention FLASH
only in passing cannot be separated from genuinely in-scope work by keyword rules.
Measured on this corpus, records of both kinds carry a median of 1-2 mentions and
usually no title mention, so any count-based threshold that removes the former also
removes the latter. These are therefore flagged by the triage agent for human
review rather than screened automatically, and confirmed cases are recorded
individually in `CURATOR_OVERRIDES`.

## Repository layout

| Path | Contents |
| --- | --- |
| `library/` | The corpus - `flash_library.json` (source of truth), plus `.csv`, `.ris`, `.xlsx` exports and `flash_screened_out.csv` |
| `pipeline/` | Harvest and build scripts |
| `docs/` | Generated MkDocs pages - **do not edit by hand**, they are overwritten on every rebuild |
| `mkdocs.yml` | Site configuration - also generated |
| `.github/workflows/` | `deploy.yml` (publish) and `refresh-corpus.yml` (monthly harvest) |

## How updates work

The corpus runs on autopilot. `refresh-corpus.yml` fires on the 1st of each
month and does everything: snapshots the PMID set, re-harvests PubMed, runs the
recall guard, sends new records to the triage agent (Haiku, batch pricing, about
a dollar a month during backfill and pennies after), rebuilds the site, the RIS
exports and the NotebookLM pack, and opens a pull request describing the change.

### When it merges itself, and when it waits

The PR **merges itself and redeploys the site** when every guard is quiet:

| Guard | What it catches |
|---|---|
| Recall guard passed | a query or screening regression (hard stop, before any API spend) |
| 0 records dropped | a rule change that quietly shrank the corpus |
| ≤ 40 records added | a broken query, which shows up as +hundreds |
| Agent triage ran | an expired key or outage that left the batch untriaged |
| 0 curator-pin conflicts | the agent disagreed with a decision a human made |
| 0 agent out-of-scope flags | a suspected false positive that needs eyes |

If any guard is not quiet, the PR is **held**, with the reason in bold at the
top of its body. You read the relevant section and merge, or fix the rule and
re-run. Held PRs are the exception, not the routine.

Auto-merged PRs still exist and still carry the full report, so the audit trail
is identical either way. **Watch the repository** (top right on GitHub) to be
emailed each one; with zero watchers, an unattended merge is invisible.

### The one manual step

NotebookLM has no API. Each PR body ends with a **NotebookLM** section that says
exactly what to do that month: usually *upload this one delta file*, occasionally
*nothing*, and — whenever papers have been removed — *rebuild the notebook*,
because a delta can add sources but can never make NotebookLM forget one.

### Guards under the guards

Two things can be edited by hand and outrank everything automatic:
`CURATOR_OVERRIDES` in `pipeline/flash_harvest.py` (force a record in, out, or
into a category) and `MUST_BE_PRESENT` / `MUST_BE_ABSENT` in
`pipeline/test_recall.py` (papers CI must always, or never, find). A curator
decision is never overridden by the agent.

You can trigger a refresh any time from **Actions** → *Monthly corpus refresh*
→ *Run workflow*. Set `triage_limit` to `0` for a free rebuild with no API calls.

## Running the pipeline manually

Only needed for development or if CI is unavailable. Order matters - the build
step reads what the harvest step writes.

```bash
pip install -r requirements.txt
export NCBI_API_KEY="your-key"        # optional; raises the rate limit to 10 req/s
python pipeline/flash_harvest.py      # -> library/
python pipeline/build_site.py         # -> library/*.xlsx, website/mkdocs_source/
```

`build_site.py` writes the site source to `website/mkdocs_source/`, while the
deploy workflow builds from the repository root. CI keeps the two in step; if
you run the build locally you must sync it yourself:

```bash
rsync -a --delete website/mkdocs_source/docs/ docs/
cp website/mkdocs_source/mkdocs.yml mkdocs.yml
```

Preview before pushing:

```bash
mkdocs serve   # http://127.0.0.1:8000
```

## The NCBI API key

`flash_harvest.py` looks for the key in two places, in order:

1. the `NCBI_API_KEY` environment variable
2. `pipeline/ncbi_api_key.txt`

In CI the key comes from the `NCBI_API_KEY` repository secret. `ncbi_api_key.txt`
is in `.gitignore` and **must never be committed**.

## Publishing

`deploy.yml` runs `mkdocs gh-deploy --force` on every push to `main`. In
**Settings -> Pages**, set the source to the `gh-pages` branch.

## Citation

See `CITATION.cff`, or use the "Cite this repository" button on the GitHub
repository page.
