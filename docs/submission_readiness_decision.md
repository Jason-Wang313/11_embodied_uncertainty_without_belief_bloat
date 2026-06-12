# Submission Readiness Decision

Paper: 11 - Embodied Uncertainty Without Belief Bloat
Date: 2026-06-12
Decision: workshop-only / revise

## Rationale

The paper has a clean formal object, two finite-state propositions, a runnable simulator, a stronger v2 VOI comparator, and a v2 support-calibration stress. The supported contribution is a controller-facing ambiguity interface that can ignore nuisance uncertainty when action ordering is already certified.

The paper is not ready for a strong main-conference robotics submission because the evidence is a small route-choice simulator and lacks hardware, standard benchmarks, learned support calibration, and long-horizon continuous-control validation. The v2 VOI oracle also shows the result is an interface claim, not an optimal-planning win.

## Terminal Recommendation

Submit only to a workshop or keep revising toward calibrated support estimation and robotics benchmarks.
