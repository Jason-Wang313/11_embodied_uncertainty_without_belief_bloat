# Reproducibility Checklist

- [x] Main experiment command works: `python scripts/run_experiments.py`.
- [x] Full-scale runner exists: `experiments/full_scale_tao_uncertainty.py`.
- [x] `python -m py_compile experiments/full_scale_tao_uncertainty.py scripts/run_experiments.py` passes.
- [x] Generated result files include all `results/full_scale/family_*_summary.csv` files.
- [x] Generated seed-level result files include all `results/full_scale/family_*_seed.csv` files.
- [x] Generated figures are under `results/full_scale/`.
- [x] Generated LaTeX tables are under `results/full_scale/table_*.tex`.
- [x] `results/full_scale/progress.json` reports stage `complete`.
- [x] `results/full_scale/metadata.json` records the master seed and plot status.
- [x] Manuscript builds with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- [x] Final local PDF is 26 pages before canonical copy.
- [x] Canonical PDF target is `C:/Users/wangz/Downloads/11.pdf`.
- [x] No versioned PDF should remain in Downloads.
- [x] No Desktop PDF copy is created in the v3 pass.
- [ ] Dependency versions are pinned in a lockfile.
- [ ] Hardware data exists.
- [ ] Learned support-estimator checkpoints exist.
