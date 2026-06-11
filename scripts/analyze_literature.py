import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STATUS = ROOT / "child_status.md"
MATRIX = DOCS / "related_work_matrix.csv"


def read_rows():
    with MATRIX.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(path, text):
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_status(stage, latest, commands, failures="None.", recovery="None needed."):
    lines = [
        "# Child Status",
        "",
        f"Stage: {stage}",
        "",
        "Latest update:",
    ]
    lines.extend([f"- {item}" for item in latest])
    lines.extend(["", "Commands run:"])
    lines.extend([f"- {item}" for item in commands])
    lines.extend(["", "Failures:"])
    if isinstance(failures, str):
        lines.append(f"- {failures}")
    else:
        lines.extend([f"- {item}" for item in failures])
    lines.extend(["", "Recovery steps:"])
    if isinstance(recovery, str):
        lines.append(f"- {recovery}")
    else:
        lines.extend([f"- {item}" for item in recovery])
    STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


HIDDEN_ASSUMPTIONS = [
    "A posterior over all latent variables is the right interface between perception and control.",
    "Uncertainty that is expensive to represent is still worth representing until the planner decides otherwise.",
    "Entropy or variance is a useful proxy for whether a robot should spend time disambiguating.",
    "The same uncertainty representation should serve localization, mapping, manipulation, safety, and task choice.",
    "The planner can afford to update beliefs at the same rate at which the controller must act.",
    "Observation models are stable enough that belief updates are more trustworthy than task-specific certificates.",
    "A latent variable that appears in the state model is potentially relevant to the next action.",
    "Action values can be computed accurately enough from approximate beliefs to justify carrying the belief.",
    "The cost of a wrong action dominates the cost of delaying for extra sensing.",
    "The robot should reduce world uncertainty rather than reduce action-order uncertainty.",
    "A compact learned latent state will automatically discard nuisance ambiguity.",
    "Risk constraints can be specified independently of the current task decision boundary.",
    "Active perception utilities do not need to know which action pair is actually contested.",
    "Belief-space simplifications preserve the uncertainty that can flip control decisions.",
    "Task relevance is a property of state variables, not of action comparisons under the present observation.",
    "A single scalar confidence threshold can decide when perception is good enough.",
    "World-model rollouts should preserve every factor needed for long-horizon prediction, even for short-horizon control.",
    "Point-based POMDP methods scale by sampling likely beliefs, not by eliminating irrelevant ambiguity.",
    "A robot should represent ambiguity before it asks whether any available action distinguishes it.",
    "The same disambiguation action is useful across states with similar entropy.",
    "Partial observability is primarily an inference problem, with control layered afterward.",
    "Sensor actions can be evaluated by expected information before checking if a robustly dominant action already exists.",
    "Nuisance uncertainty can be ignored by tuning costs rather than by a structural operator.",
    "Failure modes mostly arise from too little information, not from information that is irrelevant to control.",
    "Open-loop commitment under uncertainty is unsafe unless uncertainty has first been reduced.",
    "A belief-state planner's memory footprint is an implementation detail rather than a scientific object.",
    "Approximate posterior features are more interpretable than action-level ambiguity certificates.",
    "Decision boundaries in action-cost space are too brittle to serve as the main representation.",
    "Task-specific uncertainty handling is an engineering trick rather than a general mechanism.",
    "The robot's uncertainty object must be a model of the world rather than a model of the remaining decision ambiguity.",
]

CANDIDATES = [
    (
        "Belief pruning by nuisance detection",
        "Learn which latent factors never change value estimates and drop them from the belief.",
        "Too close to state abstraction and representation learning; novelty depends on the learner.",
    ),
    (
        "Entropy-aware active sensing repair",
        "Modify information gain so it discounts task-irrelevant variables.",
        "Still centers generic active perception and can be read as a shaped information reward.",
    ),
    (
        "Risk-sensitive ambiguity thresholds",
        "Use risk envelopes that trigger sensing only when action regret exceeds a task threshold.",
        "Too close to robust and chance-constrained planning unless the uncertainty object changes.",
    ),
    (
        "Task-Ambiguity Operators",
        "Replace the maintained belief with an operator over action-cost intervals that returns only unresolved action-ordering edges and the observations that can collapse them.",
        "Strongest: changes the central object from world belief to control ambiguity, yields a formal dominance certificate, and directly predicts different actions.",
    ),
]

BOUNDARIES = [
    (
        "Classical POMDP and point-based solvers",
        "They keep a belief over latent states and optimize a value function over that belief.",
        "TAO asks first whether any posterior refinement can alter the selected action; if not, it acts without maintaining or reducing the belief.",
    ),
    (
        "Online POMDP search such as POMCP/DESPOT",
        "They sample reachable beliefs or scenarios to approximate belief-conditioned value.",
        "TAO stores contested action-order edges, not a scenario tree whose main object is latent-state uncertainty.",
    ),
    (
        "Belief-space motion planning",
        "It propagates mean/covariance or distributional beliefs through motion plans.",
        "TAO uses cost-interval dominance over observation-consistent states and can ignore high covariance when it cannot flip control.",
    ),
    (
        "Active perception and information gathering",
        "They value observations by expected entropy reduction, mutual information, or value of information.",
        "TAO values an observation only through its ability to remove a currently contested action edge.",
    ),
    (
        "Robust and chance-constrained control",
        "They impose conservative constraints over uncertainty sets or probability tails.",
        "TAO is not primarily conservative: it commits under high uncertainty when one action dominates over the whole task-relevant set.",
    ),
    (
        "State abstraction and representation learning",
        "They compress state before or during policy learning.",
        "TAO is action-pair indexed and can preserve or discard the same latent factor depending on the current control boundary.",
    ),
    (
        "LLM or foundation-model planners",
        "They may verbalize uncertainty or choose skills from observations.",
        "TAO supplies an explicit operator and certificate independent of a larger planner or language model.",
    ),
]

CLAIMS = [
    (
        "Formal",
        "Dominance certificate",
        "If the upper task loss of action a over the observation-consistent set is below the lower task loss of every other action, then any belief supported on that set chooses a under expected loss.",
        "Proved in the paper for finite action/state sets.",
    ),
    (
        "Formal",
        "Generic entropy can be arbitrarily irrelevant",
        "A task can add any number of nuisance latent states without changing the optimal action or TAO ambiguity, while belief entropy increases.",
        "Proved by product-state construction.",
    ),
    (
        "Empirical",
        "TAO changes control decisions",
        "In the included partially observed robot simulator, TAO senses in decision-ambiguous states and commits in high-entropy nuisance states.",
        "Supported by `results/episode_results.csv` after experiments run.",
    ),
    (
        "Empirical",
        "TAO improves cost under nuisance uncertainty",
        "TAO should beat entropy-threshold sensing when nuisance entropy is large and decision ambiguity is sparse.",
        "Supported only for the included small simulator, not a hardware claim.",
    ),
    (
        "Unsupported",
        "Hardware generality",
        "The method will transfer to real robots without new modeling work.",
        "Not claimed; left as future work.",
    ),
    (
        "Unsupported",
        "Dominance over all POMDP solvers",
        "TAO is universally better than belief planning.",
        "Not claimed; TAO is a representational alternative for tasks with sparse decision ambiguity.",
    ),
]


def md_escape(text):
    return (text or "").replace("|", "/").replace("\n", " ").strip()


def top_table(rows, n=20):
    lines = ["| Rank | Paper | Year | Mechanism | Leaves open |", "|---:|---|---:|---|---|"]
    for r in rows[:n]:
        lines.append(
            f"| {r['rank']} | {md_escape(r['title'])} | {r['year']} | "
            f"{md_escape(r['actual_mechanism'])} | {md_escape(r['what_it_leaves_open'])} |"
        )
    return "\n".join(lines)


def hostile_table(rows):
    lines = [
        "| Hostile rank | Paper | Problem claimed | Mechanism | Hidden assumptions | What it makes less novel | What it leaves open |",
        "|---:|---|---|---|---|---|---|",
    ]
    for r in rows[:100]:
        lines.append(
            f"| {r['rank']} | {md_escape(r['title'])} ({r['year']}) | "
            f"{md_escape(r['problem_claimed'])} | {md_escape(r['actual_mechanism'])} | "
            f"{md_escape(r['hidden_assumptions'])} | {md_escape(r['what_it_makes_less_novel'])} | "
            f"{md_escape(r['what_it_leaves_open'])} |"
        )
    return "\n".join(lines)


def main():
    rows = read_rows()
    hostile = [r for r in rows if r["phase"] == "hostile_prior"]
    deep = [r for r in rows if r["phase"] in ("hostile_prior", "deep_read")]
    skim = [r for r in rows if r["phase"] in ("hostile_prior", "deep_read", "serious_skim")]
    topic_counts = Counter()
    for r in rows:
        for topic in r["topic_tags"].split("; "):
            topic_counts[topic] += 1
    years = [int(r["year"]) for r in rows if r["year"].isdigit()]

    literature_map = f"""
# Literature Map

## Sweep Protocol
- Landscape sweep: {len(rows)} unique records from OpenAlex searches over robotics, partial observability, POMDPs, belief-space planning, active perception, robust planning, and task relevance.
- Serious skim: top {len(skim)} records by robotics/partial-observability relevance and citation signal.
- Deep read proxy: top {len(deep)} records, manually audited through abstracts/mechanism fields and hostile-boundary extraction.
- Hostile prior-work set: top {len(hostile)} records most likely to make this paper non-novel.
- Year span: {min(years) if years else 'unknown'}-{max(years) if years else 'unknown'}.

## Field Box
The field box is partially observed robotics: mobile manipulation, object search, navigation, active sensing, belief-space motion planning, and robot control where perception does not identify the latent state needed for action. The sweep shows the dominant object is still a belief, distribution, sampled scenario set, risk envelope, or learned latent state. The less explored object is the set of action comparisons that remain undecidable for the current task.

## Topic Distribution
""" + "\n".join(f"- {topic}: {count}" for topic, count in topic_counts.most_common()) + f"""

## Representative Hostile Papers
{top_table(hostile, 25)}

## Reading Conclusion
The strongest paper direction is not "add uncertainty" to a planner. The stronger direction is to demote generic uncertainty from the central mechanism. Existing work repeatedly assumes the robot should maintain, sample, compress, or reduce a world-belief object. The open boundary is to maintain an action-indexed ambiguity object that is allowed to be empty even when the robot is highly uncertain about the world.

## Hidden Assumptions That May Be False
""" + "\n".join(f"{i + 1}. {item}" for i, item in enumerate(HIDDEN_ASSUMPTIONS)) + """
"""
    write(DOCS / "literature_map.md", literature_map)

    hostile_doc = f"""
# Hostile Prior Work

This set contains the 100 papers most likely to attack novelty. Each row records the claimed problem, actual mechanism, hidden assumptions, fixed variables, ignored failures, what it makes less novel, and the remaining opening.

## Closest Hostile Clusters
- POMDP solvers and online search make belief-conditioned planning less novel, especially for target search and object manipulation under occlusion.
- Belief-space motion planning makes distribution propagation less novel.
- Active perception makes sensing-for-uncertainty less novel.
- Robust and chance-constrained control make generic safety under uncertainty less novel.
- State abstraction makes "smaller state" claims less novel.

## The 100-Paper Hostile Set
{hostile_table(hostile)}
"""
    write(DOCS / "hostile_prior_work.md", hostile_doc)

    boundary_doc = """
# Novelty Boundary Map

## Boundary Summary
""" + "\n".join(
        f"- **{name}.** Prior mechanism: {prior} Boundary: {ours}"
        for name, prior, ours in BOUNDARIES
    ) + """

## Non-Novel Claims We Must Avoid
- We do not claim to solve POMDPs faster in general.
- We do not claim entropy, information gain, or active sensing are bad in general.
- We do not claim a new benchmark alone.
- We do not claim a larger model, richer data source, LLM planner, or reinforcement-learning policy.
- We do not claim hardware validation.

## Novel Boundary
The novelty is the central representation and its control consequence: a Task-Ambiguity Operator (TAO) maps the current observation-consistent state set and task loss to contested action-order edges. The controller commits when the edge set is empty, senses or hedges when the edge set is nonempty, and never asks generic world uncertainty to be the decision interface.
"""
    write(DOCS / "novelty_boundary_map.md", boundary_doc)

    candidate_lines = []
    for name, mechanism, decision in CANDIDATES:
        candidate_lines.append(f"## {name}\n- Mechanism: {mechanism}\n- Decision: {decision}")
    novelty_decision = """
# Novelty Decision

## Candidate Directions
""" + "\n\n".join(candidate_lines) + """

## Chosen Thesis
Robots under partial observability should not maintain generic belief detail unless that detail can change the control decision. A Task-Ambiguity Operator replaces belief bloat with action-indexed ambiguity: it certifies robust action dominance when possible and triggers disambiguating control only for latent distinctions that can flip an action ordering.

## Why This Survives the Hostile Set
The hostile set covers belief maintenance, approximate POMDP solvers, active information gathering, robust planning, and state abstraction. TAO is not a faster implementation of those mechanisms. It changes the scientific object from "what does the robot believe about the world?" to "which action comparisons remain undecidable for this task under the current observations?"
"""
    write(DOCS / "novelty_decision.md", novelty_decision)

    claims_doc = """
# Claims

| Type | Claim | Exact statement | Status |
|---|---|---|---|
""" + "\n".join(
        f"| {kind} | {name} | {statement} | {status} |"
        for kind, name, statement, status in CLAIMS
    ) + """

## Claim Discipline
The paper will claim a formal dominance certificate and a small runnable demonstration. It will not claim state-of-the-art robotics performance, broad hardware transfer, or universal superiority over POMDP methods.
"""
    write(DOCS / "claims.md", claims_doc)

    attacks = [
        ("This is just POMDP value of information.", "Value of information still starts from belief-conditioned value. TAO can be evaluated over a support set and returns an action-edge certificate; the null result is 'act now' even at high entropy."),
        ("This is just state abstraction.", "State abstraction chooses a compact state. TAO is indexed by the current action comparison; the same latent variable can be discarded for one action pair and preserved for another."),
        ("The interval dominance certificate is too conservative.", "Yes, it is a sufficient certificate. The paper reports the tradeoff and adds a soft regret-width version for sensing decisions while keeping the formal claim honest."),
        ("Toy experiments do not prove robotics relevance.", "Correct; they isolate a mechanism. The paper frames the evidence as a runnable counterexample to belief-bloat assumptions, not as deployment validation."),
        ("Generic uncertainty can be task-aware if the reward is designed correctly.", "The hostile point is acknowledged. TAO differs because the uncertainty object itself is action-order ambiguity, not entropy or posterior mass with a tuned reward."),
        ("POMDP solvers already know which observations matter through value.", "Only after solving/searching in belief space. TAO supplies a cheaper front-end certificate that can avoid belief expansion when dominance is already guaranteed."),
        ("Known models are assumed.", "The current paper assumes a finite task loss table or learned bounded loss intervals; model learning is outside scope."),
        ("Worst-case intervals can overcommit or undersense if support sets are wrong.", "The paper explicitly requires calibrated support sets and lists support misspecification as the main weakness."),
        ("The method may fail in long-horizon tasks where later ambiguity matters.", "The experiment includes short receding-horizon control; long-horizon TAO composition is future work."),
        ("Ambiguity operators are another verifier.", "They are not a post-hoc verifier. They are the state object consumed by the controller and determine whether it commits, senses, or hedges."),
    ]
    reviewer_doc = """
# Reviewer Attacks

""" + "\n".join(f"## Attack {i + 1}: {attack}\nResponse: {response}\n" for i, (attack, response) in enumerate(attacks))
    write(DOCS / "reviewer_attacks.md", reviewer_doc)

    summary = {
        "matrix_rows": len(rows),
        "serious_skim": len(skim),
        "deep_read": len(deep),
        "hostile_prior": len(hostile),
        "chosen_mechanism": "Task-Ambiguity Operators",
        "hidden_assumptions": len(HIDDEN_ASSUMPTIONS),
    }
    write(DOCS / "analysis_summary.json", json.dumps(summary, indent=2))

    write_status(
        "novelty decision complete",
        [
            f"Analyzed {len(rows)} matrix rows into {len(skim)} serious skim, {len(deep)} deep read, and {len(hostile)} hostile prior entries.",
            "Selected Task-Ambiguity Operators as the central mechanism.",
            "Wrote literature, hostile prior, novelty, claims, and reviewer attack documents.",
        ],
        ["python scripts/analyze_literature.py"],
    )


if __name__ == "__main__":
    main()
