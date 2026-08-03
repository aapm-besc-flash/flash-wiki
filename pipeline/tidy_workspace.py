#!/usr/bin/env python3
"""
Sweep stray and superseded files out of the FLASH Wiki folder.
--------------------------------------------------------------
Runs automatically at the end of Run_Monthly_Update; safe to run on its own.

Nothing is ever deleted. Everything obsolete is MOVED to:

    _archive/YYYY-MM-DD/<reason>/

so a bad month can always be recovered by dragging a folder back. This also
sidesteps a practical problem: OneDrive frequently refuses to delete synced
files from a script, but renaming/moving them always works.

Usage:  python3 tidy_workspace.py [--dry-run]
"""
import os, sys, shutil
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ARCHIVE = os.path.join(ROOT, "_archive", date.today().isoformat())

DRY = "--dry-run" in sys.argv

# Files/folders that legitimately live at the top level. Anything else found
# there is swept. Keeping this as an allow-list (rather than a list of junk
# patterns) means new kinds of clutter are caught without editing this script.
KEEP_TOP = {
    "README.md", "SETUP_GUIDE.md", "FLASH_Wiki.html",
    "FLASH_Wiki_Framework.docx", "FLASH_Wiki_Project_Handover.pptx",
    "Run_Monthly_Update.command",
    "library", "website", "ris_archive", "notebooklm_sources",
    "pipeline", "_archive",
}

# Deliverables are also kept by extension, so a renamed or newly added report,
# deck or guide is not archived out from under the user on the next run.
KEEP_TOP_EXT = {".docx", ".pptx", ".xlsx", ".pdf"}

# Clutter that accumulates inside the working subfolders.
SWEEP_PATTERNS = (".pyc",)
SWEEP_NAMES = {"__pycache__", ".DS_Store", "Thumbs.db", ".ipynb_checkpoints"}


def _move(src, reason):
    dest_dir = os.path.join(ARCHIVE, reason)
    name = os.path.basename(src)
    dest = os.path.join(dest_dir, name)
    print(f"  {'[dry-run] ' if DRY else ''}{name}  ->  _archive/"
          f"{date.today().isoformat()}/{reason}/")
    if DRY:
        return
    os.makedirs(dest_dir, exist_ok=True)
    if os.path.exists(dest):                     # repeat run on the same day
        dest = dest + "_" + str(int(os.path.getmtime(src)))
    try:
        os.rename(src, dest)
    except OSError:                              # cross-device or locked
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, dest)
        shutil.rmtree(src, ignore_errors=True) if os.path.isdir(src) \
            else os.remove(src)


def sweep_top_level():
    moved = 0
    for name in sorted(os.listdir(ROOT)):
        if name in KEEP_TOP or name.startswith(".git"):
            continue
        # Never sweep a user-facing deliverable (report, deck, spreadsheet, PDF).
        if os.path.splitext(name)[1].lower() in KEEP_TOP_EXT:
            continue
        path = os.path.join(ROOT, name)
        # Categorise so the archive is browsable rather than a dumping ground.
        if name.endswith(".log"):
            reason = "old_logs"
        elif "_prev" in name or name.endswith(".zip"):
            reason = "prev_snapshots"
        elif os.path.isdir(path):
            reason = "superseded_builds"
        else:
            reason = "stray_files"
        _move(path, reason)
        moved += 1
    return moved


def sweep_caches():
    moved = 0
    for base, dirs, files in os.walk(ROOT):
        if os.path.join(ROOT, "_archive") in base:
            continue
        for d in list(dirs):
            if d in SWEEP_NAMES:
                _move(os.path.join(base, d), "caches")
                dirs.remove(d)
                moved += 1
        for f in files:
            if f in SWEEP_NAMES or f.endswith(SWEEP_PATTERNS):
                _move(os.path.join(base, f), "caches")
                moved += 1
    return moved


def prune_archive(keep=6):
    """Keep the newest `keep` dated archive folders; report the rest.

    Deliberately does NOT delete - the WG lead decides when old months go.
    Old archives are only listed so they are easy to find and remove by hand.
    """
    root = os.path.join(ROOT, "_archive")
    if not os.path.isdir(root):
        return
    dated = sorted(d for d in os.listdir(root)
                   if os.path.isdir(os.path.join(root, d)) and d[:2] == "20")
    old = dated[:-keep] if len(dated) > keep else []
    if old:
        print(f"\n  {len(old)} archive folder(s) older than the last {keep} runs "
              f"- safe to delete by hand:")
        for d in old:
            print(f"    _archive/{d}")


def main():
    print("=== tidy: sweeping stray files into _archive/"
          f"{date.today().isoformat()}/ ===")
    n = sweep_top_level() + sweep_caches()
    print(f"  {n} item(s) archived" if n else "  nothing to tidy - folder is clean")
    prune_archive()


if __name__ == "__main__":
    main()
