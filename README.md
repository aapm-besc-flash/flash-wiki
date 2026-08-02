# FLASH Radiotherapy Living Wiki

Generated 2026-08-02 · 1309 curated FLASH-RT records.

## Preview locally
```bash
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000
```

## Publish to GitHub Pages
1. Create a GitHub repo and push this folder.
2. The included Action (`.github/workflows/deploy.yml`) auto-deploys on every push to `main`.
   (Or run `mkdocs gh-deploy` once manually.)
3. In repo Settings → Pages, set the source to the `gh-pages` branch.

## Refresh the corpus
Re-run `../flash_harvest.py` then `../build_site.py`, commit, and push — the site redeploys.
