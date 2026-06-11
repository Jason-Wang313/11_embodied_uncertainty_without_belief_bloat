# Novelty Decision

## Candidate Directions
## Belief pruning by nuisance detection
- Mechanism: Learn which latent factors never change value estimates and drop them from the belief.
- Decision: Too close to state abstraction and representation learning; novelty depends on the learner.

## Entropy-aware active sensing repair
- Mechanism: Modify information gain so it discounts task-irrelevant variables.
- Decision: Still centers generic active perception and can be read as a shaped information reward.

## Risk-sensitive ambiguity thresholds
- Mechanism: Use risk envelopes that trigger sensing only when action regret exceeds a task threshold.
- Decision: Too close to robust and chance-constrained planning unless the uncertainty object changes.

## Task-Ambiguity Operators
- Mechanism: Replace the maintained belief with an operator over action-cost intervals that returns only unresolved action-ordering edges and the observations that can collapse them.
- Decision: Strongest: changes the central object from world belief to control ambiguity, yields a formal dominance certificate, and directly predicts different actions.

## Chosen Thesis
Robots under partial observability should not maintain generic belief detail unless that detail can change the control decision. A Task-Ambiguity Operator replaces belief bloat with action-indexed ambiguity: it certifies robust action dominance when possible and triggers disambiguating control only for latent distinctions that can flip an action ordering.

## Why This Survives the Hostile Set
The hostile set covers belief maintenance, approximate POMDP solvers, active information gathering, robust planning, and state abstraction. TAO is not a faster implementation of those mechanisms. It changes the scientific object from "what does the robot believe about the world?" to "which action comparisons remain undecidable for this task under the current observations?"
