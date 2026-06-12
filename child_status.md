# Child Status

Stage: experiments complete

Latest update:
- Ran 96000 simulated episodes across 48 aggregate settings.
- Wrote `results/episode_results.csv`, `results/summary.csv`, and `docs/experiment_report.md`.
- Plot failures: 0.

Commands run:
- python scripts/run_experiments.py

Failures:
- None.

Recovery steps:
- None needed.

## Submission-Hardening v2

End time: 2026-06-12 22:40:41 +01:00
Stage: terminal workshop-only / revise

Added facts:
- Added exact myopic VOI oracle baseline. TAO matches the VOI oracle in this toy route task, narrowing the novelty claim to controller interface/certificate rather than optimal-planning superiority.
- Added support-misspecification stress. TAO success is 0.884 at 10% support misses and 0.795 at 20% when the true mode is excluded after sensing.
- Generated `results/support_misspecification_episode_results.csv`, `results/support_misspecification_summary.csv`, and `results/support_misspecification_table.tex`.
- Updated manuscript abstract, policy description, results, limitations, table, and v2 marker.
- Added submission attack/version/readiness/reproducibility/rigor docs.
- Rebuilt the PDF with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied canonical PDF to `C:/Users/wangz/Downloads/11.pdf` (268,493 bytes).
- Removed local `main.pdf` after copying the canonical PDF.
- No new Desktop PDF copy was created during v2 hardening.

Latest terminal decision:
- Workshop-only / revise. The mechanism is formal and runnable, but evidence remains a small route-choice simulator without hardware, standard benchmarks, learned support calibration, or long-horizon continuous-control validation.
