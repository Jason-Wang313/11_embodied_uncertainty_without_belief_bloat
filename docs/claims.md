# Claims

| Type | Claim | Exact statement | Status |
|---|---|---|---|
| Formal | Dominance certificate | If the upper task loss of action a over the observation-consistent set is below the lower task loss of every other action, then any belief supported on that set chooses a under expected loss. | Proved in the paper for finite action/state sets. |
| Formal | Generic entropy can be arbitrarily irrelevant | A task can add any number of nuisance latent states without changing the optimal action or TAO ambiguity, while belief entropy increases. | Proved by product-state construction. |
| Empirical | TAO changes control decisions | In the included partially observed robot simulator, TAO senses in decision-ambiguous states and commits in high-entropy nuisance states. | Supported by `results/episode_results.csv` after experiments run. |
| Empirical | TAO improves cost under nuisance uncertainty | TAO should beat entropy-threshold sensing when nuisance entropy is large and decision ambiguity is sparse. | Supported only for the included small simulator, not a hardware claim. |
| Unsupported | Hardware generality | The method will transfer to real robots without new modeling work. | Not claimed; left as future work. |
| Unsupported | Dominance over all POMDP solvers | TAO is universally better than belief planning. | Not claimed; TAO is a representational alternative for tasks with sparse decision ambiguity. |

## Claim Discipline
The paper will claim a formal dominance certificate and a small runnable demonstration. It will not claim state-of-the-art robotics performance, broad hardware transfer, or universal superiority over POMDP methods.
