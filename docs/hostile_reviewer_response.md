# Hostile Reviewer Response

The v3 paper should not be presented as a universal replacement for POMDP planning. Exact myopic value-of-information is included and matches TAO in the simple route and multi-action settings. That is the intended boundary: TAO is a controller-facing ambiguity certificate and sensing interface, not a claim of superiority over solved value-of-information.

The useful result is that the TAO object can be empty or sparse under high nuisance uncertainty. At 64 nuisance bits, TAO has cost 2.000 in the decision-ambiguous route task and scans 0 nuisance bits, while entropy-threshold sensing costs 14.800 and scans 64 nuisance bits. In the 12-action task with 32 nuisance bits, TAO edge sensing costs 2.165 versus 6.005 for entropy-gain sensing. In the 12-gate receding task, TAO costs 24.000 versus 100.800 for entropy-threshold sensing.

The central weakness is support calibration. V3 adds a direct stress: nominal TAO success is 0.898 at 10% support miss and 0.801 at 20%. Conservative confirmation recovers 0.981 and 0.961 success at those miss rates but pays extra sensing cost. Any real robot version needs calibrated support estimators, conservative support inflation, confirmation, or fallback planning.

The paper should therefore be read as a formal mechanism plus full-scale synthetic evidence. It is much stronger than the v2 workshop draft, but still does not claim hardware validation, standard robotics benchmark superiority, learned support calibration, or high-dimensional continuous-control deployment.
