# Submission Attack Log

## Paper 11: Embodied Uncertainty Without Belief Bloat

Date: 2026-06-12
Decision: workshop-only / revise before main-conference submission

## Harsh Attacks

1. TAO is just value of information.
   - Response: added an exact myopic VOI oracle and stated that it matches TAO in the toy task. The novelty is interface and certificate, not beating solved VOI.
2. The entropy baseline is intentionally weak.
   - Response: kept it as a failure-mode baseline and added the stronger VOI comparator.
3. Support sets are hard to calibrate.
   - Response: added a support-misspecification stress. Success falls to 0.884 at 10% support misses and 0.795 at 20%.
4. The simulator is tiny.
   - Response: kept terminal decision workshop-only; no hardware or benchmark claim is made.
5. Interval dominance can be conservative.
   - Response: retained this as a limitation and did not claim completeness or optimality.

## Remaining Non-Recoverable Weaknesses In This Pass

- No hardware or standard robotics benchmark.
- No learned support estimator.
- No continuous-control or long-horizon validation.
- Exact VOI matches TAO in the toy, so novelty must stay at the representation/interface level.
