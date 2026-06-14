# Embodied Uncertainty Without Belief Bloat

This repository contains the full-scale v3 anonymous ICLR-style paper artifact for paper 11 in the robotics/embodied-intelligence batch.

## Thesis

Partially observed robots should not maintain or sense generic belief detail unless that detail can change a control decision. A Task-Ambiguity Operator (TAO) replaces a world-belief interface with action-indexed ambiguity: it certifies robust action dominance when possible and triggers sensing only for latent distinctions that can flip an action ordering.

## Full-Scale v3 Status

- Final manuscript source: `main.tex`.
- Final local build: 26 pages.
- Canonical final PDF path: `C:/Users/wangz/Downloads/11.pdf`.
- Full-scale plan: `docs/full_scale_execution_plan.md`.
- Full-scale runner: `experiments/full_scale_tao_uncertainty.py`.
- Stable reproduction command: `python scripts/run_experiments.py`.

## Evidence Added In v3

The v3 pass adds five experiment families:

- Product-state route scaling to 64 nuisance bits.
- Multi-action inspection with 3, 5, 8, and 12 actions.
- Support calibration and misspecification stress.
- Long-horizon receding decision gates.
- Continuous/noisy loss-interval probe.

Headline results:

- Product route at 64 nuisance bits: TAO cost 2.000 versus entropy-threshold cost 14.800.
- Multi-action, 12 actions and 32 nuisance bits: TAO edge sensing cost 2.165 versus entropy-gain cost 6.005.
- Support miss at 10%: nominal TAO success 0.898; conservative TAO success 0.981 with confirmation.
- Twelve-gate receding task with 32 nuisance bits: receding TAO cost 24.000 versus entropy-threshold cost 100.800.
- Continuous/noisy probe at width 0.40 and shift 0.03: TAO regret 0.000; mean-loss regret 0.051.

## Reproduce Evidence

```powershell
python scripts\run_experiments.py
```

This regenerates:

- `results/full_scale/family_a_product_route_summary.csv`
- `results/full_scale/family_b_multi_action_summary.csv`
- `results/full_scale/family_c_calibration_summary.csv`
- `results/full_scale/family_d_long_horizon_summary.csv`
- `results/full_scale/family_e_continuous_summary.csv`
- `results/full_scale/*.pdf`
- `results/full_scale/table_*.tex`
- `docs/experiment_report.md`

## Rebuild Paper

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Scope Boundary

TAO is a controller-facing ambiguity interface, not a universal POMDP solver. Exact myopic value-of-information matches TAO in the simple route and multi-action tasks. The paper's claim is that TAO exposes a cheap action-order certificate and avoids nuisance belief bloat when support and loss bounds are calibrated. It does not claim hardware validation, standard benchmark superiority, or learned support calibration.
