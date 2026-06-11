# Final Audit

1. Chosen thesis: Partially observed robots should not maintain generic belief detail unless that detail can change the next control decision. Task-Ambiguity Operators expose unresolved action-order comparisons directly.

2. Field assumption broken: The dominant field assumption is that a posterior belief, particle set, covariance, scenario set, or learned latent world state is the right interface between perception and control.

3. New central mechanism: A Task-Ambiguity Operator maps an observation-consistent support set and task loss to contested action-order edges. Empty edge sets certify robust action dominance; nonempty edge sets identify which latent distinctions can flip a control choice.

4. Genuine novelty: The mechanism changes the central uncertainty object from world belief to action-indexed decision ambiguity. The novelty is not bigger models, better data, generic active learning, a verifier, or an LLM planner. It is a controller-facing operator that can be empty under high world uncertainty.

5. Closest hostile prior work: The strongest hostile cluster is POMDP and belief-space planning, especially SARSOP, POMCP, DESPOT, belief-space motion planning, mixed-observability robotic tasks, active perception, and target object search under partial observability. The single closest robotics prior in the matrix is `Online Planning for Target Object Search in Clutter under Partial Observability` (Xiao et al., 2019), because it is a robot target-search POMDP that explicitly handles occlusion and manipulation uncertainty.

6. Literature coverage: `docs/related_work_matrix.csv` contains 1143 unique OpenAlex records. The pipeline records a 300-paper serious skim, 225-paper deep read proxy, and 100-paper hostile prior-work set. Important entries include structured fields for problem claimed, mechanism, hidden assumptions, fixed variables, ignored failure modes, novelty pressure, and remaining opening. Coverage is broad but mostly abstract/metadata level rather than full-PDF human annotation for all 225 deep entries.

7. Proof/formal-claim status: Two finite-state claims are proved in `main.tex`: a belief-independent dominance certificate and a product-state nuisance construction showing that belief entropy/support can grow without changing TAO ambiguity. No theorem is claimed for continuous systems, learned support calibration, long-horizon composition, or the regret-width extension.

8. Strongest evidence: `scripts/run_experiments.py` regenerates 96000 simulated episodes. The key result is that TAO commits with cost 1.0 in nuisance-only states and cost 2.0 in decision-ambiguous states, while an entropy-threshold belief baseline pays increasing nuisance scanning cost up to 7.4 and 8.4 at 32 nuisance bits.

9. Biggest weaknesses: The experiment is intentionally small and synthetic; no hardware or standard robotics benchmark is included. TAO depends on calibrated support sets and bounded loss intervals. Interval dominance is sufficient and can be conservative. Long-horizon and continuous-control versions are left open.

10. Paper-readiness judgment: workshop. The core mechanism is clear, formally defensible, and runnable, but ICLR main-conference readiness would require stronger robotics experiments, clearer comparison to exact value-of-information POMDP planning, and support calibration evidence.

11. Exact Downloads PDF path: `C:/Users/wangz/Downloads/11.pdf`.

12. GitHub URL: `https://github.com/Jason-Wang313/11_embodied_uncertainty_without_belief_bloat`.

13. Visible Desktop PDF copy status: pending orchestrator copy.

Additional build notes:
- Paper source: `main.tex`.
- Build path used direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Final LaTeX log check found no undefined references, fatal errors, emergency stops, or LaTeX errors.
- Latest official ICLR template checked at runtime: ICLR 2026 materials were the latest official materials found; no ICLR 2027 author template was found during the runtime search.
