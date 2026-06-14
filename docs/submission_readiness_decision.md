# Submission Readiness Decision

Paper: 11 - Embodied Uncertainty Without Belief Bloat
Date: 2026-06-14
Version: v3 full-scale hardening
Decision: strong revise / final under current batch standard

## Rationale

The v3 paper is no longer the seven-page workshop draft. It now has a 26-page manuscript, two finite-state formal claims, five generated experiment families, stronger baselines, support-calibration stress, long-horizon receding-control evidence, continuous/noisy interval probes, and updated reproducibility artifacts.

The supported contribution is a controller-facing Task-Ambiguity Operator that exposes unresolved action-order comparisons and can ignore high-volume nuisance uncertainty when it cannot change control. The evidence is strongest as a mechanism study: TAO matches exact myopic VOI in simple settings, avoids entropy-driven nuisance scans, and quantifies failure under support misspecification.

The paper should still not be sold as hardware-ready main robotics evidence. It lacks hardware, standard robotics benchmarks, learned support calibration, and high-dimensional continuous-control validation. Exact value-of-information remains the right reference when a solved downstream belief/value model is available.

## Terminal Recommendation

For the current 60-paper hardening standard: final. Copy only the verified 26-page PDF to `C:/Users/wangz/Downloads/11.pdf`, remove local `main.pdf`, commit, push, and move to Paper12 only after clean/upstream verification.

For external positioning: submit as a strong mechanism/workshop or focused conference paper unless additional hardware or benchmark validation is added.
