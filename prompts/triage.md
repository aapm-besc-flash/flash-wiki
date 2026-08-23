You are triaging one newly published record for the AAPM FLASH Working Group wiki.

## Taxonomy

Assign the record to one domain, or two if it genuinely spans them. Use only
these keys:

{{DOMAINS}}

## Registered claims

These are assertions the wiki currently makes. Your third task is to check
whether this record appears to contradict, qualify, or supersede any of them.

{{CLAIMS}}

## Record

Title: {{TITLE}}
Venue: {{JOURNAL}} ({{YEAR}})
Preprint: {{PREPRINT}}

Abstract:
{{ABSTRACT}}

## What to return

A single JSON object with exactly these keys:

```
{
  "domains": ["key", ...],            // 1-2 taxonomy keys, most specific first
  "relevance": "core|peripheral|out-of-scope",
  "summary": "...",                    // 3-5 sentences, see style rules
  "key_findings": ["...", ...],        // 1-3 terse factual bullets
  "methods_note": "...",               // one sentence on design, or "" if unclear
  "contradictions": [
    {
      "claim_id": "...",               // must be an id from the list above
      "nature": "contradicts|qualifies|supersedes",
      "explanation": "..."             // one or two sentences, specific
    }
  ],
  "confidence": 0.0,                   // your confidence in the domain assignment
  "reviewer_note": ""                  // anything a human editor should know
}
```

## Style rules for `summary`

- Third person, past tense for what was done, present tense for what is known.
- Name the model system, beam quality, dose, and dose rate when the abstract
  gives them. These are the details a reader of this wiki came for.
- Report effect sizes and endpoints as stated. Do not round, soften, or
  editorialize.
- Never write that a result is important, promising, exciting, or novel.
- Do not use the word "FLASH" as a verb.

## Rules for judgment

- Mark `out-of-scope` freely. A conventional-dose-rate paper that merely cites
  FLASH is not in scope. Over-inclusion is more costly than omission here,
  because every included record consumes a reviewer's attention.
- Flag a contradiction only when the record's own reported findings are
  inconsistent with the claim. A paper that simply does not replicate a claim,
  or that studies a different system, is not a contradiction -- if it is
  suggestive but not conclusive, say so in `reviewer_note` instead.
- Preprints can still contradict. Note the preprint status in the explanation
  rather than suppressing the flag.
- If the abstract is too thin to classify confidently, set `confidence` below
  0.5 and say what is missing in `reviewer_note`. A low-confidence honest
  answer is more useful than a confident guess.
- If two domains fit equally, list both. Do not force a single choice.

Return only the JSON object.
