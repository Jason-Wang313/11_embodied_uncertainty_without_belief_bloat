# Embodied Uncertainty Without Belief Bloat

This repository contains an anonymous ICLR-style paper draft and runnable evidence for paper 11 in the robotics/embodied-intelligence batch.

## Thesis

Partially observed robots should not maintain generic belief detail unless it can change a control decision. A Task-Ambiguity Operator (TAO) replaces a world-belief interface with action-indexed ambiguity: it certifies robust action dominance when possible and triggers sensing only for latent distinctions that can flip an action ordering.

## Key Files

- `main.tex` and `references.bib`: paper source.
- `scripts/collect_literature.py`: OpenAlex literature sweep script.
- `scripts/analyze_literature.py`: literature synthesis and novelty-boundary script.
- `scripts/run_experiments.py`: runnable simulator and plot generator.
- `docs/related_work_matrix.csv`: 1143-paper landscape matrix.
- `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, `docs/reviewer_attacks.md`: novelty and risk analysis.
- `results/summary.csv`, `results/episode_results.csv`, `results/support_misspecification_summary.csv`, `results/*.pdf`: experiment outputs and figures.

## Reproduce Evidence

```powershell
python scripts\run_experiments.py
```

This regenerates:

- `results/episode_results.csv`
- `results/summary.csv`
- `results/support_misspecification_summary.csv`
- `results/cost_nuisance_only.pdf`
- `results/cost_decision_ambiguous.pdf`
- `results/representation_bloat.pdf`
- `docs/experiment_report.md`

## Rebuild Paper

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final orchestrator-required PDF is saved outside the repo at:

```text
C:/Users/wangz/Downloads/11.pdf
```

## Submission-Hardening v2

The v2 pass adds an exact myopic value-of-information oracle and a support-misspecification stress. TAO matches the VOI oracle in the toy route task, so the claim is a controller-facing ambiguity interface rather than superiority over solved POMDP value-of-information. When the true mode is excluded from support after sensing, success falls to 0.884 at a 10% support miss rate and 0.795 at 20%, making support calibration the main boundary.
