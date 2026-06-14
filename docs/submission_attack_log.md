# Submission Attack Log

## Paper 11: Embodied Uncertainty Without Belief Bloat

Date: 2026-06-14
Version: v3 full-scale hardening
Decision: strong revise / mechanism paper; not a hardware-ready main robotics claim

## Harsh Attacks And Fixes

1. TAO is just value of information.
   - Fix: kept exact myopic VOI as a strong reference and explicitly state that it matches TAO in simple tasks.
2. The route task is tiny.
   - Fix: added five experiment families, including multi-action, long-horizon, calibration, and continuous/noisy probes.
3. Entropy baseline is too convenient.
   - Fix: added QMDP, mean-belief, minimax, robust hedge, random sensor, uncertainty-count, support-inflated TAO, conservative TAO, and VOI references.
4. Support sets may be wrong.
   - Fix: added support-miss and support-inflation stress. Nominal TAO success falls to 0.898 at 10% miss; conservative confirmation recovers 0.981.
5. Interval dominance is conservative.
   - Fix: added regret-width TAO and explicit limitation language.
6. Single-step control is insufficient.
   - Fix: added 2/4/8/12-gate receding-horizon family and horizon-2 TAO variant.
7. Tabular losses are too clean.
   - Fix: added continuous/noisy bounded-loss interval probe.
8. Runtime was too high in naive simulations.
   - Fix: replaced analytically identical product and multi-action loops with exact aggregate accounting while keeping the full setting grid.
9. Correct-support VOI table was initially wrong.
   - Fix: corrected the support/mode update bug and reran the full suite.
10. The old paper was under length and under scope.
   - Fix: rewrote `main.tex` into a 26-page full manuscript with expanded methods, results, limitations, appendices, and artifact audit notes.

## Remaining Honest Weaknesses

- No hardware experiment.
- No standard robotics benchmark.
- No learned support estimator or calibration model.
- No high-dimensional continuous-control validation.
- Exact VOI remains the correct comparison when downstream value computation is available.
