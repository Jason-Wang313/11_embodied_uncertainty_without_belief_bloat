# Child Status

Stage: final PDF copied and local build PDF removed

Latest update:
- Paper11 v3 full-scale manuscript built successfully at 26 pages.
- Canonical PDF verified at `C:/Users/wangz/Downloads/11.pdf` with 26 pages and v3 text.
- Local `main.pdf` removed after canonical copy.
- Full-scale experiments completed with five families, 30 seed replicates per setting, and zero plot failures.

Commands run:
- `python scripts/run_experiments.py`
- `python -m py_compile experiments/full_scale_tao_uncertainty.py scripts/run_experiments.py`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `bibtex main`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdfinfo C:/Users/wangz/Downloads/11.pdf`

Failures:
- Initial naive full-scale runner timed out before Family A finished.
- A calibration-baseline bug initially made the correct-support VOI reference inherit the wrong observed mode.

Recovery steps:
- Replaced analytically identical Product Route and Multi-Action loops with exact aggregate accounting while preserving the full setting grid.
- Corrected the correct-support VOI baseline and reran the full experiment suite.
