# Reviewer Attacks

## Attack 1: This is just POMDP value of information.
Response: V2 adds an exact myopic VOI oracle, and TAO matches it in the toy route task. The claim is not that TAO beats exact VOI after solving the belief problem; it is that TAO supplies a controller-facing action-edge certificate whose null result is 'act now' even at high entropy.

## Attack 2: This is just state abstraction.
Response: State abstraction chooses a compact state. TAO is indexed by the current action comparison; the same latent variable can be discarded for one action pair and preserved for another.

## Attack 3: The interval dominance certificate is too conservative.
Response: Yes, it is a sufficient certificate. The paper reports the tradeoff and adds a soft regret-width version for sensing decisions while keeping the formal claim honest.

## Attack 4: Toy experiments do not prove robotics relevance.
Response: Correct; they isolate a mechanism. The paper frames the evidence as a runnable counterexample to belief-bloat assumptions, not as deployment validation.

## Attack 5: Generic uncertainty can be task-aware if the reward is designed correctly.
Response: The hostile point is acknowledged. TAO differs because the uncertainty object itself is action-order ambiguity, not entropy or posterior mass with a tuned reward.

## Attack 6: POMDP solvers already know which observations matter through value.
Response: Only after solving/searching in belief space. TAO supplies a cheaper front-end certificate that can avoid belief expansion when dominance is already guaranteed.

## Attack 7: Known models are assumed.
Response: The current paper assumes a finite task loss table or learned bounded loss intervals; model learning is outside scope.

## Attack 8: Worst-case intervals can overcommit or undersense if support sets are wrong.
Response: The paper explicitly requires calibrated support sets. V2 adds a support-misspecification stress: success falls to 0.884 at 10% support misses and 0.795 at 20% when the true mode is excluded after sensing.

## Attack 9: The method may fail in long-horizon tasks where later ambiguity matters.
Response: The experiment includes short receding-horizon control; long-horizon TAO composition is future work.

## Attack 10: Ambiguity operators are another verifier.
Response: They are not a post-hoc verifier. They are the state object consumed by the controller and determine whether it commits, senses, or hedges.
