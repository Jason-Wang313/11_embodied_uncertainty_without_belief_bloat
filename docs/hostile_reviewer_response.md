# Hostile Reviewer Response

We agree that TAO should not be presented as a universal replacement for POMDP planning. In the v2 experiment, an exact myopic value-of-information oracle matches TAO in the toy route task. That is the intended boundary: TAO is a controller-facing ambiguity certificate, not a claim of superiority over solved value-of-information.

The useful result is that the TAO object can be empty under high nuisance uncertainty. At 32 nuisance bits, TAO commits with mean cost 1.0 when the task mode is known and senses the task mode once for mean cost 2.0 when it is hidden. The entropy-threshold belief baseline pays 7.4 and 8.4 respectively because it scans nuisance bits first.

The central weakness is support calibration. V2 adds a stress where the true mode is excluded from support after sensing. Success falls to 0.884 at 10% support misses and 0.795 at 20%. This means any real robot version needs calibrated support estimators or fallback mechanisms.

The paper should therefore be read as a formal mechanism and minimal counterexample. A stronger submission needs robotics benchmarks, learned support calibration, and long-horizon continuous-control validation.
