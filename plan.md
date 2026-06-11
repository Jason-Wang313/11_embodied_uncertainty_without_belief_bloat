# Plan

## Objective
Create a complete robotics/embodied-intelligence research paper for paper 11, grounded in a broad literature sweep, with runnable evidence, honest novelty claims, compiled PDF at `C:/Users/wangz/Downloads/11.pdf`, and a pushed public GitHub repository if credentials permit.

## Stages
1. Inspect existing folder state and reusable artifacts from attempt 2.
2. Create and maintain `child_status.md` with commands, failures, and recovery.
3. Build a literature pipeline:
   - collect at least 1000 related robotics/uncertainty/planning papers into `docs/related_work_matrix.csv`;
   - produce a 300-paper serious skim, 200-250-paper deep read subset, and 100-paper hostile prior-work set;
   - extract problem, mechanism, assumptions, fixed variables, ignored failures, novelty pressure, and open gaps for important papers.
4. Synthesize field assumptions, candidate directions, hostile novelty boundary, and chosen thesis in `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, and `docs/reviewer_attacks.md`.
5. Implement runnable evidence for the strongest direction with reproducible scripts and generated figures/tables.
6. Write an anonymous ICLR-style paper using the latest official ICLR template available at runtime.
7. Compile with direct `pdflatex`/`bibtex` passes where available; document failures if compilation is blocked.
8. Save final PDF exactly to `C:/Users/wangz/Downloads/11.pdf`.
9. Create/push public GitHub repo `11_embodied_uncertainty_without_belief_bloat` if GitHub authentication is available; otherwise document the blocking condition.
10. Write `docs/final_audit.md` covering the required 13 audit points.

## Safety Rules
- Use resumable scripts and cached intermediate files for long work.
- Avoid fragile inline PowerShell/Python for complex data handling; write checked-in helper scripts.
- Give long-running commands explicit generous timeouts and status/progress files.
- Never delete existing useful artifacts unless they are demonstrably invalid.
- Treat external lookup, LaTeX, and GitHub failures as recoverable; record them and continue.
