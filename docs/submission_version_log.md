# Submission Version Log

## v1

- Initial anonymous ICLR-style artifact.
- Route-choice simulator with TAO, entropy-threshold belief, QMDP, and mode oracle policies.
- Canonical PDF: `C:/Users/wangz/Downloads/11.pdf`.

## v2 - 2026-06-12

- Replaced the mode oracle framing with an exact myopic VOI oracle baseline.
- Added support-misspecification stress and generated `results/support_misspecification_summary.csv`.
- Added `results/support_misspecification_table.tex` and manuscript table.
- Updated abstract, policy description, results, limitations, and claim docs.
- Terminal decision: workshop-only / revise.

## v3 - 2026-06-14

- Wrote `docs/full_scale_execution_plan.md` before substantive v3 edits.
- Added `experiments/full_scale_tao_uncertainty.py` and made `scripts/run_experiments.py` a stable wrapper.
- Added five experiment families: product-route scaling, multi-action inspection, support calibration, long-horizon gates, and continuous/noisy bounded losses.
- Added full-scale CSV summaries, seed summaries, figures, LaTeX tables, metadata, and progress checkpoints under `results/full_scale/`.
- Corrected a calibration-baseline bug in the correct-support VOI reference and reran the suite.
- Rewrote `main.tex` into a 26-page v3 manuscript.
- Updated README, claims, reviewer attacks, attack log, rigor, reproducibility, final audit, and readiness docs.
- Final local PDF: 26 pages, built by `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
