# Claims

| Type | Claim | Exact statement | Status |
|---|---|---|---|
| Formal | Dominance certificate | If the upper task loss of action a over the observation-consistent set is below the lower task loss of every other action, then any belief supported on that set chooses a under expected loss. | Proved in the paper for finite action/state sets. |
| Formal | Generic entropy can be arbitrarily irrelevant | A task can add any number of nuisance latent states without changing the optimal action or TAO ambiguity, while belief entropy increases. | Proved by product-state construction. |
| Empirical | TAO changes control decisions | In the included partially observed robot simulator, TAO senses in decision-ambiguous states and commits in high-entropy nuisance states. | Supported by `results/episode_results.csv` after experiments run. |
| Empirical | TAO improves cost under nuisance uncertainty | TAO should beat entropy-threshold sensing when nuisance entropy is large and decision ambiguity is sparse. | Supported only for the included small simulator, not a hardware claim. |
| Empirical | TAO matches exact myopic VOI in the toy route task | The v2 VOI oracle senses the task mode only when it can change route choice and otherwise commits; it has the same mean costs as TAO in the included simulator. | Supported by `results/summary.csv`; this narrows the novelty claim. |
| Stress | Support calibration is required | If the true task mode is excluded from support after sensing, TAO success falls as the miss rate rises. | Supported by `results/support_misspecification_summary.csv`: success 0.884 at 10% misses and 0.795 at 20%. |
| Unsupported | Hardware generality | The method will transfer to real robots without new modeling work. | Not claimed; left as future work. |
| Unsupported | Dominance over all POMDP solvers | TAO is universally better than belief planning. | Not claimed; TAO is a representational alternative for tasks with sparse decision ambiguity. |

## Claim Discipline
The paper will claim a formal dominance certificate and a small runnable demonstration. It will not claim state-of-the-art robotics performance, broad hardware transfer, calibrated support estimation, or universal superiority over POMDP value-of-information methods.
