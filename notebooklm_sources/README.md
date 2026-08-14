# NotebookLM source pack

Regenerated automatically 2026-08-14 by `build_notebooklm.py` (part of the monthly refresh). NotebookLM cannot read files from disk, so uploading is manual — but you only ever need to upload the small delta file after the first time.

## First time — build the notebook

1. Go to notebooklm.google.com → **New notebook**.
2. Drag in every `.md` file in *this* folder (not the `monthly_additions` subfolder).
3. Ask questions — see `FLASH_00_Overview_and_Methodology.md` for suggestions.

## Every month afterwards — one drag

The refresh writes a dated file into **`monthly_additions/`** containing *only* the papers added since the previous run. Drag that one file into the existing notebook. The category files do not need re-uploading.

> Once or twice a year, it is worth rebuilding the notebook from scratch with the current category files and deleting the accumulated delta files — that keeps the source count low and removes any records whose categories were later corrected.

## Current sources

| Source file | Papers | ~Words |
|---|---|---|
| FLASH_Radiobiology.md | 442 | 124,198 |
| FLASH_Physics___Dosimetry.md | 259 | 93,123 |
| FLASH_Modeling___Mechanisms.md | 171 | 54,587 |
| FLASH_Beam_Delivery___Technology.md | 122 | 37,917 |
| FLASH_Treatment_Planning___Optimization.md | 54 | 20,786 |
| FLASH_Clinical___Translational.md | 40 | 12,280 |
| FLASH_Reviews___Consensus.md | 204 | 51,505 |
| FLASH_Perspectives___Commentary.md | 18 | 937 |
| FLASH_Point_Counterpoint.md | 4 | 238 |
| FLASH_Opinions___Debate.md | 1 | 76 |

All sources are well within NotebookLM's per-source limit (~500,000 words). NotebookLM's free tier allows 50 sources per notebook; this pack uses 11.

## Monthly addition files

- `monthly_additions/FLASH_NEW_2026-08-10.md`
- `monthly_additions/FLASH_NEW_2026-08-12.md`
- `monthly_additions/FLASH_NEW_2026-08-14.md`