# LLM-Based Test Generation Survey

Research materials for **LLM-Based Test Generation: Information Sources, Generation Strategies, and Quality Evidence**.

This repository connects testing objectives and generated artifacts with information access, generation mechanisms, and the evidence used to evaluate test quality. It covers unit and requirements-based testing, test oracles, API/GUI testing, fuzzing, bug reproduction, and learned test generators.

## Read the collection

- [Literature register](papers.md): 95 source records, grouped by topic, with primary-source links, analytical notes, and inspection depth.
- [CSV register](data/papers.csv): the same 95 records in a filterable format.
- [Manuscript bibliography](manuscript/references.bib): the original 60 source IDs used by the current draft.
- [Supplemental bibliography](supplemental-references.bib): 35 newly screened citation candidates, not yet integrated into the draft.
- [Supplemental search and synthesis](supplemental-review.md): new coverage, priority evidence cards, screening decisions, and outline mapping.
- [Supplemental provenance](supplemental-search.json): authors, inspected versions, source status, and proposed section mapping for those 35 additions.
- [Search and verification notes](search-notes.md): search families, inspected passages, source restrictions, and coverage gaps.
- [Review outline](docs/survey-plan.md): research questions and the proposed synthesis structure.
- [Survey manuscript](manuscript/main.pdf): the current 21-page English draft.
- [Manuscript and figure build instructions](manuscript/README.md).

## Current research status

The collection was updated through **29 September 2026**. It contains seven surveys/roadmaps and 88 method, benchmark, empirical, and historical records. The supplement adds 35 records to the original 60-record collection. It is a preliminary curated collection supporting a **structured narrative survey**, not a completed systematic literature review or an exhaustive population of studies. The current manuscript PDF and its figures still reflect the original collection; integrating the supplement into the manuscript is pending.

The register distinguishes abstract/metadata inspection from selected full-text inspection. Independent dual screening, complete variant-level extraction, inter-rater validation, and experimental reproduction have not been completed. No cross-paper performance ranking or pooled effect size is claimed. See [research status and review access](docs/research-status.md).

## Figures

The current main figure is a native vector reconstruction with embedded PDF fonts and editable SVG text and geometry.

![Overview of LLM-based test generation](manuscript/figures/construction-overview-illustrated.png)

- [Main figure: PDF](manuscript/figures/construction-overview-illustrated.pdf) / [SVG](manuscript/figures/construction-overview-illustrated.svg)
- [Representative literature map: PDF](manuscript/figures/literature-map.pdf) / [SVG](manuscript/figures/literature-map.svg)
- [Quality evidence: PDF](manuscript/figures/quality-evidence.pdf) / [SVG](manuscript/figures/quality-evidence.svg)

The figures are conceptual syntheses and illustrative examples. The literature map displays selected examples, not research-frequency statistics.

## Rebuild and maintain

See [build instructions](manuscript/README.md). The CSV can be regenerated from `papers.md`:

```bash
python scripts/export_register.py
```

The export checks unique IDs and normalized titles, agreement with the combined manuscript and supplemental bibliographies, and consistency with the supplemental provenance. It does not establish the scientific correctness of the classifications or replace study-family screening.

## Review distribution

This is the public GitHub repository. A separate anonymous review-access endpoint has not yet been configured. Use an anonymized snapshot for double-anonymous submission, and update the manuscript's Data Availability statement with the actual anonymous URL once it exists. Do not use this author-identifying GitHub URL as the review link.

## Attribution

Paper titles, source URLs, and bibliographic records identify their original authors and publications. The repository provides a linked literature register; it does not redistribute third-party paper PDFs. The bundled ACM template files retain their [original license](manuscript/LICENSE). See [third-party attribution](docs/third-party-notices.md).

## 中文说明

本仓库整理 LLM 测试生成相关文献、检索与核验记录、综述初稿和可编辑矢量图。2026-09-29 补充 35 条后共 95 条，逐条保留检查深度；尚未完成系统综述的独立筛选、全文编码和实验复现。`papers.md` 适合阅读，`data/papers.csv` 适合筛选整理，`supplemental-review.md` 说明新增文献如何整合；`manuscript/` 的当前论文仍对应原 60 条集合，正文整合待完成。
