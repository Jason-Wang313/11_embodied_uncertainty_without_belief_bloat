# Claims

| Type | Claim | Exact statement | Status |
|---|---|---|---|
| Formal | Dominance certificate | If one action's upper task loss over the observation-consistent support is below every other action's lower task loss, then every belief supported on that set prefers that action under expected loss. | Proved in `main.tex` for finite action/state sets. |
| Formal | Belief bloat can be irrelevant | Product-state nuisance variables can grow support size and entropy exponentially without changing any TAO interval or contested edge. | Proved in `main.tex`; tested in product-route scaling. |
| Empirical | TAO ignores decision-inert nuisance uncertainty | In the product route task at 64 nuisance bits, TAO cost is 2.000 and scans 0 nuisance bits; entropy-threshold cost is 14.800 and scans 64 nuisance bits. | Supported by `results/full_scale/family_a_product_route_summary.csv`. |
| Empirical | TAO extends beyond binary action choice | In the 12-action, 32-nuisance-bit inspection task, TAO edge sensing cost is 2.165 with success 1.000; entropy-gain cost is 6.005. | Supported by `results/full_scale/family_b_multi_action_summary.csv`. |
| Empirical | TAO composes in a receding local controller | In the 12-gate, 32-nuisance-bit task, receding TAO cost is 24.000; entropy-threshold cost is 100.800. | Supported by `results/full_scale/family_d_long_horizon_summary.csv`. |
| Empirical | Interval TAO can operate on bounded continuous losses | In the width 0.40, shift 0.03 continuous/noisy probe, TAO interval regret is 0.000 with oracle-action match 0.999. | Supported by `results/full_scale/family_e_continuous_summary.csv`; not a hardware or high-dimensional claim. |
| Boundary | Exact VOI is a strong reference | Exact myopic VOI matches TAO in the simple route and multi-action tasks. | Supported; narrows the novelty to interface/certificate rather than superiority over solved VOI. |
| Stress | Support calibration is required | At 10% support miss, nominal TAO success is 0.898; conservative confirmation recovers 0.981 success. | Supported by `results/full_scale/family_c_calibration_summary.csv`. |
| Unsupported | Hardware generality | The method transfers directly to real robots without support calibration or physical loss bounds. | Not claimed. |
| Unsupported | Universal POMDP dominance | TAO is generally better than belief planning or value-of-information planning. | Not claimed. |

## Claim Discipline

The paper claims a formal action-order ambiguity interface and full-scale synthetic mechanism evidence. It does not claim hardware validation, standard robotics benchmark superiority, learned support calibration, or universal replacement of POMDP solvers.
