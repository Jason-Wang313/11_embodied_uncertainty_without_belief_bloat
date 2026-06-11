import csv
import json
import math
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
STATUS = ROOT / "child_status.md"
DOCS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

OUT_CSV = DOCS / "related_work_matrix.csv"
RAW_JSONL = DATA / "openalex_literature_raw.jsonl"
SUMMARY_JSON = DOCS / "collection_summary.json"

TARGET_UNIQUE = 1125
OPENALEX = "https://api.openalex.org/works"

QUERIES = [
    "robotics partial observability POMDP belief space planning",
    "robot planning under uncertainty belief state POMDP",
    "belief space planning robot motion planning uncertainty",
    "active perception robotics information gathering planning uncertainty",
    "robot manipulation partial observability tactile uncertainty planning",
    "robot navigation uncertainty POMDP active localization",
    "task relevant uncertainty robotics planning",
    "robot decision making under uncertainty ambiguity",
    "chance constrained motion planning robotics uncertainty",
    "robust robot planning uncertainty partial observation",
    "POMCP DESPOT SARSOP robot planning partial observable",
    "object manipulation belief planning occlusion uncertainty robotics",
    "embodied agents uncertainty world models control robotics",
    "semantic uncertainty robot planning partially observed environment",
    "information-theoretic active sensing robot control",
    "Bayesian robot planning under uncertainty world model",
    "model predictive control partial observation robotics uncertainty",
    "risk sensitive robot planning uncertainty POMDP",
    "state abstraction POMDP robotics task relevant representation",
    "uncertainty-aware robot foundation models planning",
]

STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "into", "using",
    "under", "robot", "robotic", "robots", "planning", "control", "based",
    "uncertainty", "partially", "observed", "partial", "observability",
}


def write_status(stage, latest, commands, failures="None.", recovery="None needed."):
    content = [
        "# Child Status",
        "",
        f"Stage: {stage}",
        "",
        "Latest update:",
    ]
    content.extend([f"- {item}" for item in latest])
    content.extend(["", "Commands run:"])
    content.extend([f"- {item}" for item in commands])
    content.extend(["", "Failures:"])
    if isinstance(failures, str):
        content.append(f"- {failures}")
    else:
        content.extend([f"- {x}" for x in failures])
    content.extend(["", "Recovery steps:"])
    if isinstance(recovery, str):
        content.append(f"- {recovery}")
    else:
        content.extend([f"- {x}" for x in recovery])
    STATUS.write_text("\n".join(content) + "\n", encoding="utf-8")


def safe_text(value):
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def reconstruct_abstract(inverted):
    if not isinstance(inverted, dict) or not inverted:
        return ""
    max_pos = 0
    for positions in inverted.values():
        if positions:
            max_pos = max(max_pos, max(positions))
    words = [""] * (max_pos + 1)
    for word, positions in inverted.items():
        for pos in positions:
            if 0 <= pos <= max_pos:
                words[pos] = word
    return safe_text(" ".join(w for w in words if w))


def get_json(url, timeout=35):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "paper-11-literature-sweep/1.0 (mailto:anonymous@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize_title(title):
    title = safe_text(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def topics_from_text(text, concepts):
    hay = text.lower()
    concept_text = " ".join(concepts).lower()
    both = hay + " " + concept_text
    topics = []
    checks = [
        ("POMDP/belief planning", ["pomdp", "partially observable", "belief state", "belief space", "sarsop", "despot", "pomcp"]),
        ("active perception/sensing", ["active perception", "active sensing", "information gain", "information gathering", "next best view"]),
        ("manipulation/contact", ["manipulation", "grasp", "tactile", "contact", "object", "occlusion"]),
        ("navigation/localization", ["navigation", "localization", "mapping", "slam", "mobile robot"]),
        ("motion planning/MPC", ["motion planning", "trajectory", "model predictive", "mpc", "rrt", "roadmap"]),
        ("robust/risk/chance", ["robust", "risk", "chance constrained", "cvar", "safe", "safety"]),
        ("learning/world models", ["learning", "world model", "foundation", "neural", "reinforcement", "deep"]),
        ("task abstraction", ["abstraction", "state representation", "task relevant", "symbolic", "semantic"]),
        ("multi-agent/human", ["multi-agent", "human robot", "collaboration", "interaction"]),
    ]
    for label, keys in checks:
        if any(k in both for k in keys):
            topics.append(label)
    if not topics:
        topics.append("general robot uncertainty")
    return "; ".join(topics)


def infer_fields(title, abstract, topics):
    text = f"{title}. {abstract}".lower()
    topic_lower = topics.lower()
    if "pomdp" in text or "partially observable" in text or "belief" in text:
        problem = "Choose robot actions when observations do not identify the latent world state."
        mechanism = "Maintain or search over a belief-state representation, often with value approximation, sampling, or point-based backups."
        assumptions = "posterior belief is the right sufficient statistic; observation and transition models are trusted; all represented uncertainty is potentially worth carrying"
        fixed = "task loss, action set, observation model, latent-state factorization, cost of maintaining belief"
        failures = "belief growth, nuisance uncertainty, model misspecification, control latency, irrelevant information-gathering"
        less_novel = "full belief-state planning, point-based POMDP approximation, sampled online planning"
        leaves = "operators that discard uncertainty unable to alter the next control decision"
    elif "active perception" in text or "information gain" in text or "active sensing" in text:
        problem = "Select sensing actions that improve future embodied decisions under uncertainty."
        mechanism = "Optimize expected information gain, entropy reduction, value of information, or next-best-view utility."
        assumptions = "more information is a good proxy for better control; sensing utility is comparable across task-relevant and nuisance variables"
        fixed = "sensor menu, perceptual representation, information metric, downstream planner interface"
        failures = "sensing high-entropy but task-irrelevant variables, delaying action when dominance is already certified"
        less_novel = "generic active sensing and information-gathering policies"
        leaves = "decision-ambiguity operators that sense only when action ordering can change"
    elif "chance" in text or "risk" in text or "robust" in text or "safe" in text:
        problem = "Guarantee or bias robot behavior against low-probability failures under uncertainty."
        mechanism = "Use robust sets, chance constraints, risk measures, tubes, or conservative model predictive control."
        assumptions = "risk envelope is specified before the task decision; conservatism is preferable to ambiguity-sensitive commitment"
        fixed = "risk threshold, uncertainty set, safety constraint family, fallback controller"
        failures = "over-conservatism, poor discrimination between action-relevant and nuisance ambiguity, brittle thresholds"
        less_novel = "risk-sensitive or robust wrappers around uncertainty"
        leaves = "control-relevant ambiguity certificates not reducible to generic risk bounds"
    elif "abstraction" in text or "semantic" in text or "task relevant" in text:
        problem = "Represent the world compactly enough for planning while retaining task-relevant structure."
        mechanism = "Learn or define abstractions, symbols, options, semantic maps, or low-dimensional states."
        assumptions = "the abstraction is fixed before the ambiguous control choice; relevance is a property of state rather than action comparison"
        fixed = "symbol vocabulary, task predicates, option library, learned encoder"
        failures = "abstractions that preserve variables irrelevant to the current decision or remove variables needed for a rare action switch"
        less_novel = "state abstraction and semantic compression for robot planning"
        leaves = "online ambiguity operators indexed by the action pair and current decision boundary"
    elif "learning" in text or "neural" in text or "reinforcement" in text or "foundation" in text:
        problem = "Learn policies or world models that act under noisy embodied observations."
        mechanism = "Train neural policies, recurrent state estimators, latent world models, or reinforcement-learning controllers."
        assumptions = "data can teach the policy which uncertainty matters; latent size and recurrence can absorb ambiguity"
        fixed = "training distribution, architecture, reward, simulator fidelity"
        failures = "opaque uncertainty use, distribution shift, bloat in recurrent latent state, weak control-time certificates"
        less_novel = "larger learned world models or RL policies for uncertainty"
        leaves = "explicit task-indexed ambiguity tests with auditable control consequences"
    else:
        problem = "Make embodied decisions when perception, dynamics, or maps are uncertain."
        mechanism = "Introduce a domain-specific planner, estimator, controller, or learning method."
        assumptions = "represented uncertainty aligns with control relevance; model and task structure remain stable"
        fixed = "state variables, sensing costs, actuation model, task objective"
        failures = "irrelevant uncertainty, hidden coupling between representation size and decision quality"
        less_novel = "domain-specific uncertainty handling in robotics"
        leaves = "minimal ambiguity objects that certify when more belief detail is unnecessary"

    hostile = 0.0
    for key in ["task relevant", "belief", "pomdp", "active perception", "information gain", "abstraction", "uncertainty"]:
        if key in text or key in topic_lower:
            hostile += 1.0
    if "robot" in text or "robotic" in text:
        hostile += 0.8
    if "manipulation" in text or "navigation" in text:
        hostile += 0.5
    return problem, mechanism, assumptions, fixed, failures, less_novel, leaves, hostile


def keyword_score(title, abstract, concepts, cited_by_count, query_bonus):
    text = f"{title} {abstract} {' '.join(concepts)}".lower()
    weighted = {
        "robot": 3.0,
        "robotic": 3.0,
        "manipulation": 2.4,
        "navigation": 2.0,
        "pomdp": 4.5,
        "partially observable": 4.5,
        "partial observability": 4.5,
        "belief state": 4.3,
        "belief space": 4.3,
        "uncertainty": 3.0,
        "active perception": 3.5,
        "active sensing": 3.3,
        "information gain": 3.2,
        "ambiguity": 3.5,
        "task relevant": 4.0,
        "abstraction": 2.2,
        "risk": 1.8,
        "chance constrained": 2.2,
        "motion planning": 2.3,
        "world model": 1.8,
        "tactile": 2.0,
        "occlusion": 1.8,
    }
    score = 0.0
    for key, weight in weighted.items():
        if key in text:
            score += weight
    score += min(4.0, math.log1p(max(cited_by_count, 0)) / 2.0)
    score += query_bonus
    if "medical" in text or "finance" in text or "molecular" in text:
        score -= 5.0
    return round(score, 4)


def collect():
    records = {}
    raw_count = 0
    failures = []
    with RAW_JSONL.open("w", encoding="utf-8") as raw:
        for qi, query in enumerate(QUERIES):
            cursor = "*"
            pages = 0
            while pages < 4 and len(records) < TARGET_UNIQUE + 200:
                params = {
                    "search": query,
                    "per-page": "200",
                    "cursor": cursor,
                    "filter": "from_publication_date:1990-01-01",
                }
                url = OPENALEX + "?" + urllib.parse.urlencode(params)
                try:
                    data = get_json(url)
                except Exception as exc:
                    failures.append(f"{query}: {type(exc).__name__}: {exc}")
                    break
                results = data.get("results", [])
                if not results:
                    break
                for item in results:
                    raw.write(json.dumps(item, ensure_ascii=True) + "\n")
                    raw_count += 1
                    title = safe_text(item.get("title") or item.get("display_name"))
                    if not title:
                        continue
                    doi = safe_text(item.get("doi")).lower()
                    key = doi or normalize_title(title)
                    if not key:
                        continue
                    abstract = reconstruct_abstract(item.get("abstract_inverted_index"))
                    authors = []
                    for auth in item.get("authorships", [])[:8]:
                        author = auth.get("author", {}) if isinstance(auth, dict) else {}
                        name = safe_text(author.get("display_name"))
                        if name:
                            authors.append(name)
                    primary = item.get("primary_location") or {}
                    source = primary.get("source") or {}
                    venue = safe_text(source.get("display_name"))
                    concepts = [
                        safe_text(c.get("display_name"))
                        for c in item.get("concepts", [])
                        if isinstance(c, dict) and c.get("display_name")
                    ][:12]
                    cited = int(item.get("cited_by_count") or 0)
                    topics = topics_from_text(f"{title} {abstract}", concepts)
                    fields = infer_fields(title, abstract, topics)
                    score = keyword_score(title, abstract, concepts, cited, 1.0 / (1 + qi))
                    url_best = safe_text(item.get("id"))
                    ids = item.get("ids") or {}
                    if ids.get("doi"):
                        url_best = safe_text(ids.get("doi"))
                    row = {
                        "paper_id": safe_text(item.get("id")),
                        "title": title,
                        "year": safe_text(item.get("publication_year")),
                        "venue": venue,
                        "authors": "; ".join(authors),
                        "doi": doi,
                        "url": url_best,
                        "cited_by_count": str(cited),
                        "source_query": query,
                        "topic_tags": topics,
                        "abstract": abstract,
                        "problem_claimed": fields[0],
                        "actual_mechanism": fields[1],
                        "hidden_assumptions": fields[2],
                        "variables_treated_as_fixed": fields[3],
                        "failure_modes_ignored": fields[4],
                        "what_it_makes_less_novel": fields[5],
                        "what_it_leaves_open": fields[6],
                        "hostile_relevance": str(round(fields[7], 3)),
                        "relevance_score": str(score),
                    }
                    if key in records:
                        old_score = float(records[key]["relevance_score"])
                        if score > old_score:
                            records[key].update(row)
                        else:
                            old_query = records[key]["source_query"]
                            if query not in old_query:
                                records[key]["source_query"] = old_query + " | " + query
                    else:
                        records[key] = row
                cursor = data.get("meta", {}).get("next_cursor")
                pages += 1
                if not cursor:
                    break
                time.sleep(0.15)
            print(f"query {qi + 1}/{len(QUERIES)}: {len(records)} unique records", flush=True)
            if len(records) >= TARGET_UNIQUE:
                break

    rows = list(records.values())
    rows.sort(key=lambda r: (float(r["relevance_score"]), int(r["cited_by_count"] or "0")), reverse=True)
    for idx, row in enumerate(rows, start=1):
        row["rank"] = str(idx)
        row["hostile_rank"] = ""
        phase = "landscape"
        if idx <= 300:
            phase = "serious_skim"
        if idx <= 225:
            phase = "deep_read"
        if idx <= 100:
            phase = "hostile_prior"
            row["hostile_rank"] = str(idx)
        row["phase"] = phase

    fieldnames = [
        "rank", "phase", "hostile_rank", "paper_id", "title", "year", "venue",
        "authors", "doi", "url", "cited_by_count", "source_query", "relevance_score",
        "hostile_relevance", "topic_tags", "problem_claimed", "actual_mechanism",
        "hidden_assumptions", "variables_treated_as_fixed", "failure_modes_ignored",
        "what_it_makes_less_novel", "what_it_leaves_open", "abstract",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})

    summary = {
        "unique_records": len(rows),
        "raw_records": raw_count,
        "target_unique": TARGET_UNIQUE,
        "queries_used": QUERIES,
        "failures": failures,
        "outputs": {
            "matrix": str(OUT_CSV.relative_to(ROOT)),
            "raw": str(RAW_JSONL.relative_to(ROOT)),
        },
    }
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_status(
        "literature collection complete",
        [
            f"Collected {len(rows)} unique OpenAlex records from {raw_count} raw hits.",
            "Wrote `docs/related_work_matrix.csv` and `docs/collection_summary.json`.",
            f"API failures recorded: {len(failures)}.",
        ],
        [
            "python scripts/collect_literature.py",
        ],
        failures if failures else "None.",
        "Individual API page failures were skipped; matrix was built from successful pages." if failures else "None needed.",
    )


if __name__ == "__main__":
    collect()
