# Novelty Boundary Map

## Boundary Summary
- **Classical POMDP and point-based solvers.** Prior mechanism: They keep a belief over latent states and optimize a value function over that belief. Boundary: TAO asks first whether any posterior refinement can alter the selected action; if not, it acts without maintaining or reducing the belief.
- **Online POMDP search such as POMCP/DESPOT.** Prior mechanism: They sample reachable beliefs or scenarios to approximate belief-conditioned value. Boundary: TAO stores contested action-order edges, not a scenario tree whose main object is latent-state uncertainty.
- **Belief-space motion planning.** Prior mechanism: It propagates mean/covariance or distributional beliefs through motion plans. Boundary: TAO uses cost-interval dominance over observation-consistent states and can ignore high covariance when it cannot flip control.
- **Active perception and information gathering.** Prior mechanism: They value observations by expected entropy reduction, mutual information, or value of information. Boundary: TAO values an observation only through its ability to remove a currently contested action edge.
- **Robust and chance-constrained control.** Prior mechanism: They impose conservative constraints over uncertainty sets or probability tails. Boundary: TAO is not primarily conservative: it commits under high uncertainty when one action dominates over the whole task-relevant set.
- **State abstraction and representation learning.** Prior mechanism: They compress state before or during policy learning. Boundary: TAO is action-pair indexed and can preserve or discard the same latent factor depending on the current control boundary.
- **LLM or foundation-model planners.** Prior mechanism: They may verbalize uncertainty or choose skills from observations. Boundary: TAO supplies an explicit operator and certificate independent of a larger planner or language model.

## Non-Novel Claims We Must Avoid
- We do not claim to solve POMDPs faster in general.
- We do not claim entropy, information gain, or active sensing are bad in general.
- We do not claim a new benchmark alone.
- We do not claim a larger model, richer data source, LLM planner, or reinforcement-learning policy.
- We do not claim hardware validation.

## Novel Boundary
The novelty is the central representation and its control consequence: a Task-Ambiguity Operator (TAO) maps the current observation-consistent state set and task loss to contested action-order edges. The controller commits when the edge set is empty, senses or hedges when the edge set is nonempty, and never asks generic world uncertainty to be the decision interface.
