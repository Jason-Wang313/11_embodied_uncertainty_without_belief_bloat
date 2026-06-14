# Full-Scale Experiment Report

## Scope
- Five experiment families: product-state route task, multi-action inspection, support calibration, long-horizon receding gates, and continuous/noisy loss intervals.
- Thirty deterministic seed replicates per setting.
- Episode rows are aggregated by seed; summaries report mean and 95 percent confidence intervals across seeds.
- Runs compute support sizes analytically and do not enumerate product-state beliefs.

## Key Findings
- Product route, 64 nuisance bits: TAO cost 2.000 versus entropy-threshold cost 14.800; TAO scans 0.000 nuisance bits versus 64.000.
- Multi-action inspection, 12 actions and 32 nuisance bits: TAO edge sensing cost 2.165 versus entropy-gain cost 6.005.
- Support miss stress at 10 percent miss rate: nominal TAO success 0.898; conservative TAO success 0.981 with confirm rate 1.000.
- Twelve-gate receding task with 32 nuisance bits: receding TAO cost 24.000 versus entropy-threshold cost 100.800.
- Continuous/noisy probe at width 0.40 and shift 0.03: TAO regret 0.000; mean-loss regret 0.051.

## Generated Artifacts
- `results/full_scale/family_a_product_route_summary.csv`
- `results/full_scale/family_b_multi_action_summary.csv`
- `results/full_scale/family_c_calibration_summary.csv`
- `results/full_scale/family_d_long_horizon_summary.csv`
- `results/full_scale/family_e_continuous_summary.csv`
- `results/full_scale/figure_product_route_scaling.pdf`
- `results/full_scale/figure_multi_action_scaling.pdf`
- `results/full_scale/figure_support_calibration.pdf`
- `results/full_scale/figure_long_horizon.pdf`
- `results/full_scale/figure_continuous_probe.pdf`

## Plot Status
- All full-scale figures were generated successfully.
