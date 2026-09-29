# Research status and review access

## Collection and evidence

- Latest retrieval date: 29 September 2026; this is not an exhaustive database-search cutoff.
- Source register: 95 records, including seven surveys/roadmaps and 35 screened additions to the original collection.
- Current manuscript: structured narrative synthesis, with three conceptual figures and four tables.
- Most records: abstract and bibliographic metadata checked against a primary source.
- Selected records: relevant full-text passages checked; the register identifies inspection depth.
- Pending: systematic multi-database retrieval, final study-family screening, complete variant-level coding, independent coding validation, and any quantitative synthesis.

The revised manuscript integrates all 35 additions and cites all 95 source records. It has 18 body pages (including Data Availability) and four independently paginated reference pages. Three conceptual figures retain the approved design. See [revision notes](../manuscript/revision-notes.md) for the affected arguments and verification. See [supplemental synthesis](../supplemental-review.md) for chapter mapping and source-specific evidence boundaries. Two discovered surveys remain pending primary full-text access; withdrawn VisiDroid and hardware AssertionBench were not included in the core register.

The S03 register entry now records arXiv v3 and its abstract-reported 178 publications through 31 July 2026. Its earlier v2 count of 115 and earlier full-text inspection should not be treated as a current-version full-text audit. The revised manuscript distinguishes that current abstract count from its own differently scoped register.

The repository contains no reproduced model-performance results, experiment logs, trained checkpoints, or evidence that a proposed research mechanism has been validated.

## Manuscript status

`manuscript/main.pdf` is a draft using the ACM `acmsmall,screen,review,anonymous` layout. FSE 2027 is the intended formatting reference; no acceptance or publication is implied. The template's volume, issue, article-number, and publication-date fields are placeholders, not verified publication metadata.

AI assistance was used for literature organization, synthesis drafting, and figure design. The manuscript describes the scope of that assistance. Native vector figure reconstruction removes raster-rendering artifacts; it is not evidence of independent human validation of the literature coding.

## Anonymous review materials

The user-provided anonymous endpoint is [https://anonymous.4open.science/r/llm-test-generation-survey-B437](https://anonymous.4open.science/r/llm-test-generation-survey-B437) and is now included in Data Availability. Before distributing the snapshot:

1. Use a hosting endpoint that does not expose the GitHub account, repository history, or public-repository identity.
2. Keep the literature register, search notes, bibliography, coding definitions, and the build instructions accessible to reviewers.
3. Inspect repository links, author metadata, commit history, document metadata, and acknowledgments for identity disclosure.
4. Confirm that the Data Availability URL resolves to the intended snapshot and that its material list remains accurate.

The public repository does not substitute for that anonymous access check.

## Highest-value figure extensions

The current manuscript already includes an overview, a representative literature map, and an observation-to-evidence diagram. Two useful additions are:

- An inference-time adaptation versus cross-task learning comparison, with frozen-model evaluation and information boundaries.
- A concrete oracle comparison using the sorting example to show missed obligations, rejection of legal behavior, and independent fault detection.

Research-frequency plots, PRISMA counts, and an exhaustive quality-evidence heatmap should follow actual completed retrieval and coding rather than the current seed collection.
