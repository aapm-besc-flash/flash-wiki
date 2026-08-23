# Methodology & provenance

## Corpus definition
Every record derives from one explicit, version-controlled PubMed query executed via the
NCBI E-utilities API. The query is tuned for **high recall** with a downstream precision
filter — the appropriate trade-off for a document meant to capture *all* FLASH work.

```
(("ultra-high dose rate"[tiab] OR "ultrahigh dose rate"[tiab] OR "ultra-high dose rates"[tiab] OR "ultrahigh dose rates"[tiab] OR "FLASH radiotherapy"[tiab] OR "FLASH-RT"[tiab] OR "FLASH radiation"[tiab] OR "FLASH irradiation"[tiab] OR "FLASH effect"[tiab] OR "FLASH proton"[tiab] OR "FLASH electron"[tiab] OR "very high energy electron"[tiab] OR "very high energy electrons"[tiab] OR "VHEE"[tiab] OR ("FLASH"[tiab] AND ("dose rate"[tiab] OR "radiotherapy"[tiab] OR "radiation therapy"[tiab] OR "irradiation"[tiab] OR "Gy/s"[tiab] OR "conventional dose rate"[tiab]))) OR ((FLASH[tiab] OR eFLASH[tiab] OR pFLASH[tiab] OR "FLASH-RT"[tiab] OR UHDR[tiab] OR "UHDR-RT"[tiab] OR "ultra high dose rate*"[tiab] OR "ultra-high dose rate*"[tiab] OR "ultrahigh dose rate*"[tiab] OR "ultra fast dose rate*"[tiab] OR "ultrafast dose rate*"[tiab]) AND (radiotherap*[tiab] OR "radiation therap*"[tiab] OR irradiat*[tiab] OR radiobiolog*[tiab] OR dosimetr*[tiab] OR "Radiotherapy"[mh] OR "Radiotherapy Dosage"[mh] OR "Radiotherapy, High-Energy"[mh] OR "Radiation Dosage"[mh])))
```

## Relevance screening
The broad final clause deliberately over-captures, pulling in unrelated "flash" papers
(flash memory, flash nanoprecipitation, photochemistry). A relevance gate then requires
each record to contain a radiotherapy-specific signal; those that do not are moved to an
auditable screening list (`flash_screened_out.csv`) rather than deleted, so a curator can
reinstate any wrongly excluded paper.

## Categorization
Records are auto-classified into the categories at left by a transparent, weighted keyword
model over each paper's title, abstract and MeSH terms; reviews and consensus documents are
routed by PubMed publication type. Every paper also carries secondary tags. Auto-assignment
is a first pass — a category editor can override any assignment in the master spreadsheet,
and the correction propagates on the next site rebuild.

## Summaries
Each record shows the authors' own peer-reviewed **abstract** as its authoritative source,
plus a one-line **TL;DR** extracted mechanically from the opening of that abstract. Neither
is machine-written: the TL;DR is the authors' own sentences, verbatim.

Records that have passed agent triage additionally carry a **Summary — AI-generated,
curator-reviewed**. This is a model's reading of the abstract, stating what the study did
and found rather than what motivated it. It is labelled wherever it appears and is never
shown in place of the abstract, so a reader can always check it against the source in one
click. Every such summary reaches this site only through a pull request merged by a human
curator, and each is stored with a confidence score; low-confidence output is held back for
review rather than published.

Coverage is partial and growing. Triage processes a capped batch of records per monthly run,
so older records acquire summaries gradually. A record without one has simply not been
reached yet — it does not indicate a problem with the paper.

## Update cadence
A scheduled monthly harvest adds new PMIDs and refreshes existing records; a curator reviews
the new and newly-screened records (~30 min), then one command rebuilds this site. Each
update is committed to version control, giving a dated, citable history of the corpus.
