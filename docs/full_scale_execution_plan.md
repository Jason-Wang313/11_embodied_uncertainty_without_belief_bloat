# Paper 11 Full-Scale Execution Plan

Paper: Embodied Uncertainty Without Belief Bloat
Repository: `11_embodied_uncertainty_without_belief_bloat`
Date: 2026-06-14

## Current Claim

The paper argues that a partially observed robot should not maintain, refine, or sense generic belief detail unless that detail can change the current control decision. The proposed Task-Ambiguity Operator (TAO) maps an observation-consistent support set and task loss to action-order ambiguity edges. An empty edge set certifies robust dominance; a nonempty edge set identifies the latent distinctions that can flip an action ordering.

## Current State

- Current manuscript is approximately seven pages and is not final under the current 25-page internal standard.
- Existing evidence is a small route-choice simulator with TAO, entropy-threshold belief, QMDP, myopic VOI oracle, nuisance-bit sweeps, and support-misspecification stress.
- Existing audit marks the paper workshop-only because the evidence is synthetic, narrow, and missing broader baselines, calibration studies, long-horizon tests, continuous/noisy losses, and richer robotics-style task families.
- The old `C:\Users\wangz\Downloads\11.pdf` must be treated as stale until a new final 25+ page version passes verification.

## Reviewer Attacks To Resolve

1. TAO is just value of information under another name.
2. TAO is just state abstraction or relevance filtering.
3. The toy route task is too easy and deterministic.
4. The entropy baseline is too weak if it is the only main foil.
5. Interval dominance can be overly conservative and may defer too often.
6. Support-set errors can make the certificate confidently wrong.
7. The paper lacks uncertainty estimates over seeds and task families.
8. The paper lacks failure cases and parameter sensitivity.
9. The paper lacks a clear boundary to POMDP planners, QMDP, robust minimax, risk/entropy heuristics, and value-of-information policies.
10. The code and docs need final reproducibility status, not just draft artifacts.

## Experimental Expansion

Build one RAM-light experiment script that streams results to disk and keeps only aggregate rows in memory. Use deterministic seed schedules and compact CSV outputs. Generate figures and LaTeX tables from summaries only.

### Experiment Family A: Product-State Route Task

Purpose: Preserve the original mechanism test but strengthen it with seed sweeps, confidence intervals, and more policies.

Settings:
- Nuisance bits: 0, 2, 4, 8, 16, 32, 48, 64.
- Scenarios: nuisance-only, decision-ambiguous, partially ambiguous with biased mode priors, asymmetric route losses.
- Seeds: at least 30 independent seeds per setting.

Policies:
- TAO dominance.
- TAO regret-width sensing.
- Exact myopic VOI oracle.
- Entropy-threshold belief.
- Random nuisance-first sensor.
- Uncertainty-count threshold.
- QMDP.
- Robust minimax over support.
- Belief-pruned top-k support.

Metrics:
- Mean cost, success rate, wrong-route rate, sensing cost, nuisance sensing count, mode sensing count.
- Max carried belief states, mean carried belief states, TAO edge count, regret width.
- 95 percent confidence intervals across seeds.

### Experiment Family B: Multi-Action Inspection Task

Purpose: Show TAO is not restricted to a two-route binary mode.

Settings:
- Actions: 3, 5, 8, 12 candidate skills/routes.
- Latent task modes: 3, 5, 8, 12.
- Nuisance variables: independent irrelevant factors and distractor factors with weak cost influence.
- Sensor menu: mode-specific sensors, coarse group sensors, nuisance sensors, noisy sensors.

Baselines:
- TAO edge-count sensor.
- TAO regret-width sensor.
- Myopic VOI oracle.
- Entropy-gain sensor.
- Mutual-information proxy.
- Minimax robust action.
- QMDP/mean-belief action.

Metrics:
- Cost and success.
- Sensing steps.
- Fraction of episodes where TAO certifies dominance immediately.
- Fraction of entropy-gain steps wasted on nuisance or weak distractors.
- Time per decision and representation size proxy.

### Experiment Family C: Support Calibration And Misspecification

Purpose: Make the main dependency honest and quantified.

Settings:
- Support miss rate: 0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.30.
- Support inflation rate: 0, 0.05, 0.10, 0.20, 0.50.
- Sensor false positive/false negative asymmetry.
- Loss-bound slack levels.

Policies:
- TAO.
- Conservative TAO with slack margins.
- Calibrated TAO using inflated support.
- VOI oracle with correct support.
- Entropy and minimax baselines.

Metrics:
- Success, wrong action, cost, deferral/sensing rate.
- Calibration-failure slope.
- Conservative margin tradeoff: safety gained versus sensing/cost added.

### Experiment Family D: Long-Horizon Receding Decisions

Purpose: Address the attack that single-step route choice does not represent embodied control.

Task:
- A robot traverses a chain/grid of decision gates.
- Each gate has latent mode and nuisance variables.
- The robot can sense local mode, scan nuisance, execute one of several skills, or hedge.
- Wrong local actions induce recovery costs and can alter downstream state.

Policies:
- Receding-horizon TAO.
- Horizon-2 TAO approximation.
- Myopic VOI.
- Entropy-threshold belief.
- QMDP.
- Robust minimax.

Metrics:
- Total trajectory cost, success-through-gates, number of senses, recovery cost, downstream error rate.
- Scaling with gates and nuisance dimension.

### Experiment Family E: Continuous/Noisy Loss Probe

Purpose: Move beyond deterministic tabular losses without claiming hardware.

Task:
- Sample latent physical parameters and action losses from continuous families.
- Convert observations into bounded support intervals and evaluate interval dominance.
- Include Gaussian or bounded sensor noise and learned-bound slack proxies.

Policies:
- TAO interval dominance.
- TAO with regret-width threshold.
- Mean-loss belief action.
- Minimax robust action.
- Entropy/variance sensing heuristic.
- VOI oracle estimated by Monte Carlo.

Metrics:
- Cost, regret to oracle, false-dominance rate, unnecessary sensing rate, margin distribution.

## Figures And Tables

Required figures:
- Main cost scaling: TAO versus baselines as nuisance variables grow.
- Multi-action task cost and sensing efficiency.
- Support misspecification and conservative margin tradeoff.
- Long-horizon trajectory cost as gates/nuisance scale.
- Continuous/noisy loss false-dominance versus unnecessary sensing.
- Representation size: belief support growth versus TAO edge count.

Required tables:
- Main aggregate results with confidence intervals.
- Ablation table comparing TAO dominance, regret-width TAO, no-dominance fallback, and conservative TAO.
- Baseline table across task families.
- Stress-test table for support misspecification and support inflation.
- Runtime/memory proxy table.
- Claim-to-evidence table.

## Manuscript Expansion

Target structure:
- Abstract and introduction with a sharper thesis and exact scope.
- Formal TAO definition, dominance theorem, nuisance-product theorem, regret-width extension, and finite-support assumptions.
- Controller architecture section: act, sense, hedge, and fallback modes.
- Relationship to POMDP value of information, belief-space planning, active perception, robust control, and state abstraction.
- Experimental design section with all five experiment families.
- Results section with separate subsections for scaling, multi-action tasks, calibration, long-horizon receding control, continuous/noisy losses, and ablations.
- Limitations section that honestly emphasizes support calibration, sufficient-not-necessary dominance, synthetic tasks, and lack of hardware.
- Reproducibility appendix with commands, seeds, generated artifacts, and exact result files.

Page-count strategy:
- Build a genuine 25+ page manuscript from real content: expanded theory, detailed experimental protocol, figures/tables, failure cases, statistical reporting, related work, limitations, and appendices.
- Do not pad with empty prose. Each added page must carry claims, methods, evidence, or reproducibility detail.

## RAM-Light Execution Strategy

- Run experiments sequentially in one Python process.
- Avoid storing per-episode objects beyond the current row when possible.
- Stream episode/trial rows to CSV files.
- Maintain online aggregates by key for summaries and confidence intervals.
- Generate plots from summary CSVs, not from full episode logs where possible.
- Use compact numeric fields and avoid large in-memory state enumerations for product supports; compute representation size analytically.
- Save progress JSON after each experiment family so interrupted runs can be audited.

## Documentation Updates

Update after experiments and manuscript rebuild:
- `README.md`
- `child_status.md`
- `docs/claims.md`
- `docs/experiment_report.md`
- `docs/experiment_rigor_checklist.md`
- `docs/reproducibility_checklist.md`
- `docs/reviewer_attacks.md`
- `docs/hostile_reviewer_response.md`
- `docs/submission_attack_log.md`
- `docs/submission_version_log.md`
- `docs/final_audit.md`
- `docs/submission_readiness_decision.md`

## Acceptance Checklist

The paper is not final until all are true:
- Full-scale experiments run successfully and write deterministic result artifacts.
- Figures and LaTeX tables are regenerated from the new summaries.
- Manuscript compiles without fatal LaTeX errors, undefined references, missing citations, or missing figures.
- Final PDF has at least 25 pages.
- Claims in abstract/introduction/results match the generated evidence.
- Limitations explicitly include support calibration, interval conservatism, synthetic evaluation, no hardware, and no universal POMDP dominance.
- README reproduction command works.
- `python -m py_compile` passes on all edited scripts.
- Stale old local PDFs are removed before final copy.
- Only the final verified PDF is copied to `C:\Users\wangz\Downloads\11.pdf`.
- Local `main.pdf` is removed after final copy.
- Git status is clean after commit.
- Commit is pushed and `HEAD` matches upstream before moving to paper 12.
