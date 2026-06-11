import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
DOCS = ROOT / "docs"
STATUS = ROOT / "child_status.md"
RESULTS.mkdir(exist_ok=True)
DOCS.mkdir(exist_ok=True)

EPISODES = 2000
NUISANCE_BITS = [0, 2, 4, 8, 16, 32]
SCENARIOS = ["nuisance_only", "decision_ambiguous"]
POLICIES = ["tao", "entropy_threshold", "qmdp", "mode_only_oracle"]
ROUTE_COST_OK = 1.0
ROUTE_COST_BAD = 12.0
MODE_SENSOR_COST = 1.0
NUISANCE_SENSOR_COST = 0.2
ENTROPY_THRESHOLD = 0.5


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


def cost_of_route(action, mode):
    route = 0 if action == "route_0" else 1
    return ROUTE_COST_OK if route == mode else ROUTE_COST_BAD


def tao_edges(possible_modes):
    actions = ["route_0", "route_1"]
    intervals = {}
    for action in actions:
        values = [cost_of_route(action, m) for m in possible_modes]
        intervals[action] = (min(values), max(values))
    edges = []
    for i, a in enumerate(actions):
        for b in actions[i + 1 :]:
            amin, amax = intervals[a]
            bmin, bmax = intervals[b]
            if not (amax < bmin or bmax < amin):
                edges.append((a, b))
    dominant = None
    for a in actions:
        amin, amax = intervals[a]
        if all(amax < intervals[b][0] for b in actions if b != a):
            dominant = a
    return edges, dominant, intervals


def expected_best_route(mode_known, true_mode=None):
    if mode_known:
        return f"route_{true_mode}"
    return "route_0"


def simulate_episode(policy, scenario, nuisance_bits, rng):
    true_mode = rng.randint(0, 1)
    mode_known = scenario == "nuisance_only"
    possible_modes = [true_mode] if mode_known else [0, 1]
    unknown_nuisance = nuisance_bits
    total_cost = 0.0
    steps = 0
    mode_senses = 0
    nuisance_senses = 0
    first_action = None
    max_steps = nuisance_bits + 4
    ambiguity_widths = []
    belief_states_carried = []
    route_action = None

    while steps < max_steps:
        steps += 1
        belief_states = (2 if not mode_known else 1) * (2 ** unknown_nuisance)
        belief_states_carried.append(belief_states)
        edges, dominant, intervals = tao_edges(possible_modes)
        ambiguity_widths.append(len(edges))

        if policy == "tao":
            if dominant is not None:
                action = dominant
            else:
                action = "inspect_mode"
        elif policy == "entropy_threshold":
            entropy_bits = (0 if mode_known else 1) + unknown_nuisance
            if entropy_bits > ENTROPY_THRESHOLD:
                if unknown_nuisance > 0:
                    action = "scan_nuisance"
                elif not mode_known:
                    action = "inspect_mode"
                else:
                    action = expected_best_route(mode_known, true_mode)
            else:
                action = expected_best_route(mode_known, true_mode)
        elif policy == "qmdp":
            action = expected_best_route(mode_known, true_mode)
        elif policy == "mode_only_oracle":
            if not mode_known:
                action = "inspect_mode"
            else:
                action = expected_best_route(mode_known, true_mode)
        else:
            raise ValueError(policy)

        if first_action is None:
            first_action = action

        if action == "inspect_mode":
            total_cost += MODE_SENSOR_COST
            mode_senses += 1
            mode_known = True
            possible_modes = [true_mode]
        elif action == "scan_nuisance":
            total_cost += NUISANCE_SENSOR_COST
            nuisance_senses += 1
            unknown_nuisance = max(0, unknown_nuisance - 1)
        elif action in ("route_0", "route_1"):
            route_action = action
            total_cost += cost_of_route(action, true_mode)
            success = int(action == f"route_{true_mode}")
            wrong = int(not success)
            return {
                "policy": policy,
                "scenario": scenario,
                "nuisance_bits": nuisance_bits,
                "cost": total_cost,
                "success": success,
                "wrong_route": wrong,
                "steps": steps,
                "mode_senses": mode_senses,
                "nuisance_senses": nuisance_senses,
                "first_action": first_action,
                "route_action": route_action,
                "max_belief_states_carried": max(belief_states_carried),
                "mean_belief_states_carried": sum(belief_states_carried) / len(belief_states_carried),
                "max_tao_edges": max(ambiguity_widths),
                "mean_tao_edges": sum(ambiguity_widths) / len(ambiguity_widths),
            }

    return {
        "policy": policy,
        "scenario": scenario,
        "nuisance_bits": nuisance_bits,
        "cost": total_cost + ROUTE_COST_BAD,
        "success": 0,
        "wrong_route": 1,
        "steps": steps,
        "mode_senses": mode_senses,
        "nuisance_senses": nuisance_senses,
        "first_action": first_action or "none",
        "route_action": route_action or "none",
        "max_belief_states_carried": max(belief_states_carried) if belief_states_carried else 0,
        "mean_belief_states_carried": sum(belief_states_carried) / len(belief_states_carried) if belief_states_carried else 0,
        "max_tao_edges": max(ambiguity_widths) if ambiguity_widths else 0,
        "mean_tao_edges": sum(ambiguity_widths) / len(ambiguity_widths) if ambiguity_widths else 0,
    }


def summarize(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[(r["scenario"], r["nuisance_bits"], r["policy"])].append(r)
    summary = []
    for (scenario, k, policy), items in sorted(groups.items()):
        n = len(items)
        def mean(field):
            return sum(float(x[field]) for x in items) / n
        summary.append({
            "scenario": scenario,
            "nuisance_bits": k,
            "policy": policy,
            "episodes": n,
            "mean_cost": mean("cost"),
            "success_rate": mean("success"),
            "wrong_route_rate": mean("wrong_route"),
            "mean_steps": mean("steps"),
            "mean_mode_senses": mean("mode_senses"),
            "mean_nuisance_senses": mean("nuisance_senses"),
            "mean_max_belief_states_carried": mean("max_belief_states_carried"),
            "mean_tao_edges": mean("mean_tao_edges"),
        })
    return summary


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def make_plots(summary):
    failures = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        return [f"matplotlib unavailable: {type(exc).__name__}: {exc}"]

    colors = {
        "tao": "#006D77",
        "entropy_threshold": "#B23A48",
        "qmdp": "#6D597A",
        "mode_only_oracle": "#2A9D8F",
    }
    labels = {
        "tao": "TAO",
        "entropy_threshold": "Entropy belief",
        "qmdp": "QMDP",
        "mode_only_oracle": "Mode oracle",
    }
    for scenario in SCENARIOS:
        fig, ax = plt.subplots(figsize=(6.2, 3.8))
        for policy in POLICIES:
            xs = [int(r["nuisance_bits"]) for r in summary if r["scenario"] == scenario and r["policy"] == policy]
            ys = [float(r["mean_cost"]) for r in summary if r["scenario"] == scenario and r["policy"] == policy]
            ax.plot(xs, ys, marker="o", linewidth=2, color=colors[policy], label=labels[policy])
        ax.set_xlabel("Irrelevant nuisance bits")
        ax.set_ylabel("Mean episode cost")
        ax.set_title("Decision ambiguity" if scenario == "decision_ambiguous" else "Nuisance uncertainty only")
        ax.grid(True, alpha=0.25)
        ax.legend(frameon=False)
        fig.tight_layout()
        for ext in ["pdf", "png"]:
            fig.savefig(RESULTS / f"cost_{scenario}.{ext}", dpi=200)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    k_values = NUISANCE_BITS
    belief_sizes = [2 ** k for k in k_values]
    tao_sizes = [0 for _ in k_values]
    ax.plot(k_values, belief_sizes, marker="o", linewidth=2, color="#B23A48", label="Belief support states")
    ax.plot(k_values, tao_sizes, marker="s", linewidth=2, color="#006D77", label="TAO contested edges")
    ax.set_yscale("symlog", linthresh=1)
    ax.set_xlabel("Irrelevant nuisance bits, known task mode")
    ax.set_ylabel("Representation size")
    ax.set_title("Belief grows while action ambiguity is empty")
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    for ext in ["pdf", "png"]:
        fig.savefig(RESULTS / f"representation_bloat.{ext}", dpi=200)
    plt.close(fig)
    return failures


def write_report(summary, failures):
    best_rows = [r for r in summary if r["policy"] == "tao"]
    entropy_rows = [r for r in summary if r["policy"] == "entropy_threshold"]
    lines = [
        "# Experiment Report",
        "",
        "## Setup",
        f"- Episodes per setting: {EPISODES}",
        f"- Nuisance bits: {NUISANCE_BITS}",
        "- Hidden task mode selects which route succeeds; nuisance bits never affect route costs.",
        "- TAO keeps the contested action edge set; the entropy baseline keeps a full factored belief and senses while total entropy remains above threshold.",
        "",
        "## Key Result",
        "TAO commits immediately when task mode is known, no matter how many nuisance bits remain unknown. In decision-ambiguous states, TAO inspects the task mode once and then commits. The entropy baseline scans nuisance bits because they dominate generic uncertainty.",
        "",
        "## Summary Table",
        "| Scenario | Nuisance bits | Policy | Mean cost | Success | Nuisance senses | Max belief states | Mean TAO edges |",
        "|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    for r in summary:
        lines.append(
            f"| {r['scenario']} | {r['nuisance_bits']} | {r['policy']} | "
            f"{float(r['mean_cost']):.3f} | {float(r['success_rate']):.3f} | "
            f"{float(r['mean_nuisance_senses']):.3f} | {float(r['mean_max_belief_states_carried']):.1f} | "
            f"{float(r['mean_tao_edges']):.3f} |"
        )
    lines.extend([
        "",
        "## Plot Status",
    ])
    if failures:
        lines.extend([f"- {f}" for f in failures])
    else:
        lines.extend([
            "- `results/cost_nuisance_only.pdf`",
            "- `results/cost_decision_ambiguous.pdf`",
            "- `results/representation_bloat.pdf`",
        ])
    (DOCS / "experiment_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    rng = random.Random(11011)
    rows = []
    for scenario in SCENARIOS:
        for nuisance_bits in NUISANCE_BITS:
            for policy in POLICIES:
                for _ in range(EPISODES):
                    rows.append(simulate_episode(policy, scenario, nuisance_bits, rng))

    episode_fields = [
        "policy", "scenario", "nuisance_bits", "cost", "success", "wrong_route",
        "steps", "mode_senses", "nuisance_senses", "first_action", "route_action",
        "max_belief_states_carried", "mean_belief_states_carried", "max_tao_edges",
        "mean_tao_edges",
    ]
    write_csv(RESULTS / "episode_results.csv", rows, episode_fields)
    summary = summarize(rows)
    summary_fields = [
        "scenario", "nuisance_bits", "policy", "episodes", "mean_cost",
        "success_rate", "wrong_route_rate", "mean_steps", "mean_mode_senses",
        "mean_nuisance_senses", "mean_max_belief_states_carried", "mean_tao_edges",
    ]
    write_csv(RESULTS / "summary.csv", summary, summary_fields)
    failures = make_plots(summary)
    write_report(summary, failures)
    metadata = {
        "episodes": EPISODES,
        "scenarios": SCENARIOS,
        "nuisance_bits": NUISANCE_BITS,
        "policies": POLICIES,
        "plot_failures": failures,
    }
    (RESULTS / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_status(
        "experiments complete",
        [
            f"Ran {len(rows)} simulated episodes across {len(summary)} aggregate settings.",
            "Wrote `results/episode_results.csv`, `results/summary.csv`, and `docs/experiment_report.md`.",
            f"Plot failures: {len(failures)}.",
        ],
        ["python scripts/run_experiments.py"],
        failures if failures else "None.",
        "Experiment CSVs remain valid if plots failed." if failures else "None needed.",
    )


if __name__ == "__main__":
    main()
