# Manuscript and figure build

The current manuscript is `main.pdf`; the entry point is `main.tex`. The bibliography contains 60 records with IDs matching the literature register. The draft uses the supplied, unchanged ACM class with the `acmsmall,screen,review,anonymous` options.

## Compile the manuscript

Use a TeX distribution with the packages required by `acmart`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main.bbl` is retained so the existing bibliography can be used when rebuilding without refreshing metadata. Some bibliography records have incomplete supplementary publication fields; verified metadata is retained rather than filling missing fields with guesses.

## Rebuild the figures

From the repository root:

```bash
python -m pip install -r requirements.txt
python manuscript/figures/draw_figures.py
```

This rebuilds the three PDF/SVG pairs used in the manuscript. The main figure can also be rebuilt separately:

```bash
python manuscript/figures/illustrated_vector.py
```

The main figure's canvas is 1000 x 625 points (8:5). Its PDF has native vector geometry, selectable text, and embedded fonts; the SVG keeps text and shapes editable. The PNG is a preview rendered from the PDF, not an image embedded inside the PDF.

Preferred fonts are Times New Roman, Times New Roman Bold, and Consolas. The resolver also recognizes Liberation Serif/Mono and DejaVu alternatives. Set `SURVEY_FONT_DIR` to a directory containing compatible font files if automatic resolution fails. Using a different font family can change text widths; visually check the resulting figures before publication.

If Poppler is available, update the preview:

```bash
pdftoppm -scale-to 2000 -singlefile -png manuscript/figures/construction-overview-illustrated.pdf manuscript/figures/construction-overview-illustrated
```

## Source metadata

`source-metadata.json` preserves metadata retrieved from primary sources. `make_bibliography.py` rebuilds the bibliography from the register and curated publication/author fields. `check_metadata.py` refreshes metadata from external sources and therefore requires internet access; refresh deliberately, because publication records and preprint versions can change.

## Submission status

The current PDF is 21 pages, with the conclusion on page 18 and Data Availability starting on page 19. FSE 2027 conference fields are included as the intended venue; default volume/issue/publication fields are placeholders. An anonymous review URL has not yet been configured, so the Data Availability statement must be finalized before submission.
