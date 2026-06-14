# Reviewer Attacks

## Attack 1: This is just POMDP value of information.

Response: v3 includes an exact myopic VOI oracle. It matches TAO in the simple route and multi-action settings, which is the intended boundary. The claim is the controller-facing action-edge interface and dominance certificate, not superiority over solved VOI.

## Attack 2: This is just state abstraction.

Response: TAO is local to an observation, action set, and loss. The same latent factor can be relevant for one action comparison and irrelevant for another. The output is a contested action graph, not a global compact state.

## Attack 3: The entropy baseline is weak.

Response: Entropy baselines isolate the belief-bloat failure. v3 also includes VOI, QMDP, mean-belief, minimax, robust hedge, random sensor, uncertainty-count, support-inflated TAO, and conservative TAO.

## Attack 4: The original route task was too small.

Response: v3 adds five experiment families: product-state route scaling to 64 nuisance bits, multi-action inspection, support calibration, long-horizon gates, and continuous/noisy bounded losses.

## Attack 5: Support sets are hard to calibrate.

Response: Correct. v3 makes this a central stress test. Nominal TAO success is 0.898 at 10% support miss and 0.801 at 20%; conservative confirmation recovers 0.981 and 0.961 success at extra sensing cost.

## Attack 6: Interval dominance is too conservative.

Response: Correct. The paper presents dominance as sufficient, not necessary. The regret-width variant and fallback policies are engineering extensions, not new guarantees.

## Attack 7: Long-horizon tasks need future information value.

Response: Correct. The gate-chain task shows receding local use, not full POMDP optimality. TAO should hand off to a horizon-aware planner when future information value dominates immediate action order.

## Attack 8: Continuous control is not solved.

Response: Correct. v3 adds a continuous/noisy interval probe, but it remains one-dimensional and synthetic. High-dimensional continuous control is left open.

## Attack 9: The method assumes known losses.

Response: Correct. The theorem assumes valid loss bounds. Learned loss-bound calibration is future work.

## Attack 10: The work lacks hardware.

Response: Correct. The paper claims mechanism evidence and a reproducible synthetic suite, not deployment validation.
