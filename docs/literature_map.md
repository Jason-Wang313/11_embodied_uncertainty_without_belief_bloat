# Literature Map

## Sweep Protocol
- Landscape sweep: 1143 unique records from OpenAlex searches over robotics, partial observability, POMDPs, belief-space planning, active perception, robust planning, and task relevance.
- Serious skim: top 300 records by robotics/partial-observability relevance and citation signal.
- Deep read proxy: top 225 records, manually audited through abstracts/mechanism fields and hostile-boundary extraction.
- Hostile prior-work set: top 100 records most likely to make this paper non-novel.
- Year span: 1994-2026.

## Field Box
The field box is partially observed robotics: mobile manipulation, object search, navigation, active sensing, belief-space motion planning, and robot control where perception does not identify the latent state needed for action. The sweep shows the dominant object is still a belief, distribution, sampled scenario set, risk envelope, or learned latent state. The less explored object is the set of action comparisons that remain undecidable for the current task.

## Topic Distribution
- learning/world models: 576
- POMDP/belief planning: 560
- multi-agent/human: 364
- robust/risk/chance: 278
- manipulation/contact: 244
- navigation/localization: 211
- motion planning/MPC: 199
- task abstraction: 96
- general robot uncertainty: 47
- active perception/sensing: 46

## Representative Hostile Papers
| Rank | Paper | Year | Mechanism | Leaves open |
|---:|---|---:|---|---|
| 1 | Online Planning for Target Object Search in Clutter under Partial Observability | 2019 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 2 | Decision-Making for Path Planning of Mobile Robots Under Uncertainty: A Review of Belief-Space Planning Simplifications | 2025 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 3 | Planning under Uncertainty for Robotic Tasks with Mixed Observability | 2010 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 4 | Motion planning under uncertainty for robotic tasks with long time horizons | 2010 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 5 | SARSOP: Efficient Point-Based POMDP Planning by Approximating Optimally Reachable Belief Spaces | 2008 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 6 | Mori-zwanzig approach for belief abstraction with application to belief space planning | 2024 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 7 | Decentralized control of Partially Observable Markov Decision Processes using belief space macro-actions | 2015 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 8 | Decentralized control of multi-robot partially observable Markov decision processes using belief space macro-actions | 2017 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 9 | Uncertainty based online planning for UAV target finding in cluttered and GPS-denied environments | 2016 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 10 | PODDP: Partially Observable Differential Dynamic Programming for Latent Belief Space Planning | 2019 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 11 | Global Motion Planning under Uncertain Motion, Sensing, and Environment Map | 2011 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 12 | Tractable POMDP-planning for robots with complex non-linear dynamics | 2020 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 13 | Decentralized Control of Partially Observable Markov Decision Processes using Belief Space Macro-actions | 2015 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 14 | Global Motion Planning under Uncertain Motion, Sensing, and Environment Map | 2012 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 15 | Finding Approximate POMDP solutions Through Belief Compression | 2005 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 16 | Motion planning under uncertainty using iterative local optimization in belief space | 2012 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 17 | POMDPs for robotic tasks with mixed observability | 2009 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 18 | Bounded Policy Synthesis for POMDPs with Safe-Reachability Objectives | 2018 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 19 | POMHDP: Search-Based Belief Space Planning Using Multiple Heuristics | 2019 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 20 | Bounded Policy Synthesis for POMDPs with Safe-Reachability Objectives | 2018 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 21 | SLAP: Simultaneous Localization and Planning Under Uncertainty via Dynamic Replanning in Belief Space | 2018 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 22 | A Probabilistic Model for Cobot Decision Making to Mitigate Human Fatigue in Repetitive Co-Manipulation Tasks | 2023 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 23 | Myopic Policy Bounds for Information Acquisition POMDPs | 2016 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 24 | Reinforcement Learning for Uncooperative Space Objects Smart Imaging Path-Planning | 2021 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |
| 25 | Drone-Based Autonomous Motion Planning System for Outdoor Environments under Object Detection Uncertainty | 2021 | Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups. | operators that discard uncertainty unable to alter the next control decision |

## Reading Conclusion
The strongest paper direction is not "add uncertainty" to a planner. The stronger direction is to demote generic uncertainty from the central mechanism. Existing work repeatedly assumes the robot should maintain, sample, compress, or reduce a world-belief object. The open boundary is to maintain an action-indexed ambiguity object that is allowed to be empty even when the robot is highly uncertain about the world.

## Hidden Assumptions That May Be False
1. A posterior over all latent variables is the right interface between perception and control.
2. Uncertainty that is expensive to represent is still worth representing until the planner decides otherwise.
3. Entropy or variance is a useful proxy for whether a robot should spend time disambiguating.
4. The same uncertainty representation should serve localization, mapping, manipulation, safety, and task choice.
5. The planner can afford to update beliefs at the same rate at which the controller must act.
6. Observation models are stable enough that belief updates are more trustworthy than task-specific certificates.
7. A latent variable that appears in the state model is potentially relevant to the next action.
8. Action values can be computed accurately enough from approximate beliefs to justify carrying the belief.
9. The cost of a wrong action dominates the cost of delaying for extra sensing.
10. The robot should reduce world uncertainty rather than reduce action-order uncertainty.
11. A compact learned latent state will automatically discard nuisance ambiguity.
12. Risk constraints can be specified independently of the current task decision boundary.
13. Active perception utilities do not need to know which action pair is actually contested.
14. Belief-space simplifications preserve the uncertainty that can flip control decisions.
15. Task relevance is a property of state variables, not of action comparisons under the present observation.
16. A single scalar confidence threshold can decide when perception is good enough.
17. World-model rollouts should preserve every factor needed for long-horizon prediction, even for short-horizon control.
18. Point-based POMDP methods scale by sampling likely beliefs, not by eliminating irrelevant ambiguity.
19. A robot should represent ambiguity before it asks whether any available action distinguishes it.
20. The same disambiguation action is useful across states with similar entropy.
21. Partial observability is primarily an inference problem, with control layered afterward.
22. Sensor actions can be evaluated by expected information before checking if a robustly dominant action already exists.
23. Nuisance uncertainty can be ignored by tuning costs rather than by a structural operator.
24. Failure modes mostly arise from too little information, not from information that is irrelevant to control.
25. Open-loop commitment under uncertainty is unsafe unless uncertainty has first been reduced.
26. A belief-state planner's memory footprint is an implementation detail rather than a scientific object.
27. Approximate posterior features are more interpretable than action-level ambiguity certificates.
28. Decision boundaries in action-cost space are too brittle to serve as the main representation.
29. Task-specific uncertainty handling is an engineering trick rather than a general mechanism.
30. The robot's uncertainty object must be a model of the world rather than a model of the remaining decision ambiguity.
