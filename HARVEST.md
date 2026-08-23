# Literature harvest pipeline

Three stages. Only the middle one uses a model.

```
harvest.py      Europe PMC query -> normalize -> dedupe        deterministic
triage_agent.py classify, summarize, flag contradictions        model
render.py       validate -> wiki pages, BibTeX, corpus, PR      deterministic
```

Git stays the source of truth. The agent never writes to `main` — it writes to
a branch and opens a PR. Merging is the human approval step, and it is the
thing that makes this defensible for a working-group deliverable: every
machine-generated edit is a diff with your name on the merge.

## Setup

1. Copy the tree into the repo, preserving paths.
2. Repo → Settings → Secrets → Actions → new secret `ANTHROPIC_API_KEY`.
3. Settings → Actions → General → Workflow permissions → enable
   *Allow GitHub Actions to create and approve pull requests*.
4. **Rewrite `config/taxonomy.yml`** with your real ten domains. The `scope`
   text is passed to the model verbatim and determines placement quality more
   than anything else here.
5. Seed `data/claims.yml` with 10–20 real assertions.
6. If the repo already has content, seed `data/corpus.json` with what is
   already covered — otherwise the first run re-drafts everything.

## First run

Actions → Literature harvest → Run workflow → `dry_run: true`,
`since: 2026-06-01`.

Nothing is written. Download the `triage-*` artifact and read `triage.json`.
You are checking three things: are the domain assignments right, do the
summaries say what the abstracts say, and are the contradiction flags real.
Fix `taxonomy.yml` scopes and `prompts/triage.md` until they are, then run
without `dry_run`.

## Operating notes

**Cost.** Roughly one Sonnet call per new record, a couple of thousand tokens
each. A weekly window in this field is single-digit to low-double-digit
records. Pennies per run.

**When triage is wrong**, fix the taxonomy scope or the prompt — both are
version-controlled, so prompt changes appear as reviewable diffs alongside
the output they produced. That traceability is deliberate.

**Preprints** are harvested and marked. When a preprint later appears as a
journal article, `harvest.py` prefers the version of record, but only within
a single run — a preprint indexed months ago is already in the corpus and
will not be superseded automatically. Worth a periodic manual sweep.

**Failure modes to watch.** Over-inclusion is the common one: the query pulls
conventional-dose-rate papers that merely cite FLASH, and the agent has to
throw them out one at a time. Tighten `include_terms` rather than relying on
the model to filter. The expensive failure is a plausible, confident, wrong
summary — which is exactly what the PR gate exists to catch, so do not
merge these unread.

## Extending

The natural next step is a second workflow that reads the claims register and
the reviewed pages and proposes *edits to the claims themselves* when the
accumulated evidence has moved — same shape, same PR gate. Build that only
after the harvest has been running cleanly for a couple of months; it depends
on the claims register being well curated, and that takes a while to settle.
