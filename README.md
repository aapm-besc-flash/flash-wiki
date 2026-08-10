# FLASH Radiotherapy Living Wiki

A continuously updated, categorized corpus of MEDLINE-indexed FLASH radiotherapy
literature, maintained by the **AAPM BESC FLASH Working Group**.

Generated 2026-08-02 - 1,309 curated FLASH-RT records.

## Repository layout

| Path | Contents |
| --- | --- |
| `library/` | The corpus - `flash_library.json` (source of truth), plus `.csv`, `.ris`, `.xlsx` exports and `flash_screened_out.csv` |
| `pipeline/` | Harvest and build scripts |
| `docs/` | Generated MkDocs pages - **do not edit by hand**, they are overwritten on every rebuild |
| `mkdocs.yml` | Site configuration - also generated |
| `.github/workflows/` | `deploy.yml` (publish) and `refresh-corpus.yml` (monthly harvest) |

## How updates work

The corpus refreshes itself. `refresh-corpus.yml` runs on the 1st of each month:
it snapshots the current PMID set, re-harvests PubMed, rebuilds the site, and
opens a **pull request** summarizing what changed - records added, and records
that dropped out.

Nothing is published without a human merging that PR. Merging to `main` triggers
`deploy.yml`, which republishes the site.

**The dropped-records list is the one to read.** A record leaving the corpus
almost always means a screening rule changed, not that anything happened at
PubMed. Anything that belongs in the corpus goes into `CURATOR_OVERRIDES` in
`pipeline/flash_harvest.py`.

You can also trigger a refresh any time from the **Actions** tab ->
*Monthly corpus refresh* -> *Run workflow*.

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
