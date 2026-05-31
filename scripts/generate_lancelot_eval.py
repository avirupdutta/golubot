"""Generate the Lancelot wiki evaluation benchmark artifacts."""

from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path


OUTPUT_DIR = Path(
    os.environ.get("LANCELOT_EVAL_OUTPUT_DIR", "evals/lancelot_wiki")
)

DIFFICULTY_COUNTS = {
    "easy": 20,
    "medium": 35,
    "hard": 30,
    "expert": 15,
}

VALID_CATEGORIES = {
    "onboarding",
    "identity",
    "roster",
    "payments",
    "worlds",
    "admin",
    "integrations",
    "open-questions",
    "cross-module",
}

VALID_STYLES = {
    "fact",
    "comparison",
    "workflow",
    "conflict-resolution",
    "multi-hop-analysis",
}

BATCH_SIZE = 10


QuestionSeed = tuple[str, str, str, str]


QUESTION_SEEDS: list[QuestionSeed] = [
    # Easy: direct wiki/register lookups.
    ("easy", "payments", "fact", "What is the Adult Athlete membership fee, and what total fee should be shown when the background-verification fee is included?"),
    ("easy", "payments", "fact", "What is the Minor Athlete membership fee per season?"),
    ("easy", "payments", "fact", "What is the Coach membership fee, and what is the Junior Coach fee?"),
    ("easy", "payments", "fact", "What is the Legality Official training fee?"),
    ("easy", "identity", "fact", "What is the default OTP expiry window?"),
    ("easy", "identity", "fact", "How many OTP resend attempts are allowed per hour, and what is the minimum gap between resend attempts?"),
    ("easy", "identity", "fact", "After how many wrong OTP submissions does lockout occur, and how long does the lockout last?"),
    ("easy", "identity", "fact", "What does Green Light status mean in the USASF wiki?"),
    ("easy", "identity", "fact", "What public-facing term must be used instead of blacklist?"),
    ("easy", "integrations", "fact", "Which provider handles background checks and identity verification for USASF?"),
    ("easy", "integrations", "fact", "What is the Maxient feed delimiter and how many fields are in each line?"),
    ("easy", "integrations", "fact", "What is the maximum length of the Immutable Member ID required by Maxient?"),
    ("easy", "roster", "fact", "What is the cheer crossover limit at a single USASF sanctioned competition?"),
    ("easy", "worlds", "fact", "At Worlds, how many teams can a cheer athlete be on and how many teams can a dance athlete be on?"),
    ("easy", "worlds", "fact", "What is the approximate prepared-club Worlds appointment duration?"),
    ("easy", "admin", "fact", "What is the Division I athlete threshold?"),
    ("easy", "admin", "fact", "For which Division I over-threshold counts does the club-facing override request option appear?"),
    ("easy", "onboarding", "fact", "How many distinct onboarding flows are listed in the Onboarding Workflows concept page?"),
    ("easy", "onboarding", "fact", "Which onboarding flow is invite-only and has no public signup?"),
    ("easy", "onboarding", "fact", "Which profile types are described as having a zero-dollar Exceptional Athlete fee?"),
    # Medium: workflow and comparison questions.
    ("medium", "onboarding", "workflow", "Summarize the shared member onboarding scaffold in order, including where agreements, payment, dashboard entry, and compliance gates occur."),
    ("medium", "onboarding", "comparison", "Compare Adult Athlete onboarding with Parent/Minor onboarding across account ownership, fees, JDP/background checks, training, and post-payment compliance."),
    ("medium", "onboarding", "comparison", "Compare Adult Exceptional Athlete onboarding with Adult Athlete onboarding across fees, background checks, training, and documentation requirements."),
    ("medium", "onboarding", "workflow", "Explain the Adult Athlete post-payment state before all compliance gates are cleared. What can the user access and what remains incomplete?"),
    ("medium", "onboarding", "workflow", "Describe the Transitional Athlete account-claim process and the current 45-day claim-window rule."),
    ("medium", "onboarding", "workflow", "Describe the Junior Coach and Junior NCR 18th birthday claim-window rule and how it relates to the Transitional Athlete rule."),
    ("medium", "onboarding", "comparison", "Compare Jr Coach, Jr NCR, and EA Buddy onboarding or designation requirements, including whether EA Buddy is a standalone profile type."),
    ("medium", "identity", "workflow", "Explain the two-stage hold-list pattern and what happens at Stage 1 versus Stage 2."),
    ("medium", "identity", "comparison", "Compare Hard Block and Soft Hold outcomes in authentication or hold-list handling."),
    ("medium", "identity", "fact", "What duplicate-detection heuristic is described from the profile review meeting? Include the primary match and tiebreakers."),
    ("medium", "identity", "workflow", "Explain how minor profiles bypass JDP and what compliance mechanism is used instead."),
    ("medium", "identity", "comparison", "Distinguish Active and Eligible in the two-axis member state model."),
    ("medium", "identity", "workflow", "Explain why minors do not have their own login and how profile ownership changes when they turn 18."),
    ("medium", "roster", "workflow", "Describe the three connected concerns introduced by the Roster SRS update: Age Grid / Division Rules, Team Management, and Event Rosters."),
    ("medium", "roster", "workflow", "Explain the Age Grid Editor lifecycle and how seasons move from draft to published."),
    ("medium", "roster", "workflow", "What is an eligibility snapshot, and why do mid-season rule amendments not invalidate existing snapshots?"),
    ("medium", "roster", "workflow", "List the five individual eligibility rules for roster assignment described in the Roster System concept page."),
    ("medium", "roster", "comparison", "Compare cheer, dance, and cheer-to-dance crossover rules."),
    ("medium", "roster", "workflow", "Describe the temporary replacement rule, including notice timing, eligibility, cross-tier limits, and approval requirements."),
    ("medium", "roster", "workflow", "Explain nightly re-validation and how unresolved flags affect event roster submission."),
    ("medium", "payments", "comparison", "Compare Self Pay, Club Pay, and zero-dollar flows as they appear across the shared onboarding scaffold and profile-specific variations."),
    ("medium", "payments", "fact", "What is the Club Pay request expiry window for Coach onboarding, and how is it configured?"),
    ("medium", "payments", "fact", "What are the EP Cheer tier fees from Bronze through Diamond?"),
    ("medium", "payments", "fact", "What are the EP Dance tier fees, and what happened to the Dance Gold tier?"),
    ("medium", "worlds", "workflow", "Summarize the Worlds appointment timeline: when scheduling opens, when appointments occur, when the event starts, and when rosters lock."),
    ("medium", "worlds", "fact", "What are the approximate Worlds attendance counts for US teams, athletes, and non-US athletes?"),
    ("medium", "worlds", "comparison", "Compare cheer and dance limits for Worlds team participation and warm-up room entries."),
    ("medium", "worlds", "fact", "What state ID exception is noted for New Jersey and Massachusetts Worlds athletes?"),
    ("medium", "admin", "workflow", "Explain what happens when an admin makes a mid-season division rule change under Admin BL-5."),
    ("medium", "admin", "fact", "What is the new platform launch season target?"),
    ("medium", "integrations", "workflow", "Explain how JDP, Cerebrum, VID, and Codebuddy relate to each other in the identity-verification flow."),
    ("medium", "integrations", "fact", "What are the typical VID completion time, manual review time, and unresolvable resubmission rate?"),
    ("medium", "integrations", "workflow", "What data does Maxient receive from USASF, and how is the active member count characterized?"),
    ("medium", "open-questions", "fact", "What open question remains around the Parent/Minor age-verification provider, and what is the current answer?"),
    ("medium", "cross-module", "comparison", "Compare Timeline and Audit Log retention or purpose, using the wiki's distinction between user-visible history and forensic audit data."),
    # Hard: multi-hop synthesis.
    ("hard", "cross-module", "multi-hop-analysis", "A parent registers a standard Minor Athlete who later turns 18 before April 1. What account, fee, background-check, training, and timing rules apply across Parent/Minor and Transitional Athlete sources?"),
    ("hard", "cross-module", "multi-hop-analysis", "A minor athlete turns 18 on or after April 1. What does the wiki say about background-check requirements for that season, and what still needs to happen?"),
    ("hard", "cross-module", "multi-hop-analysis", "A club has 127 unique athletes who have taken the floor. Explain the Division I classification, override UI behavior, and who can override on the backend."),
    ("hard", "cross-module", "multi-hop-analysis", "A club has 129 unique athletes who have taken the floor. Explain the Division I classification and why the override request UI does or does not appear."),
    ("hard", "cross-module", "multi-hop-analysis", "An Adult Athlete has paid but has not completed training, quiz, or JDP clearance. Explain the correct status and dashboard access implications."),
    ("hard", "cross-module", "multi-hop-analysis", "A Minor Exceptional Athlete is added under a Parent Account. Explain account ownership, fee, JDP, training, and age-verification expectations."),
    ("hard", "cross-module", "multi-hop-analysis", "A user wants to call the compliance list a blacklist in a user-facing email. What should Lancelot answer, and what evidence should it cite?"),
    ("hard", "cross-module", "multi-hop-analysis", "A dance athlete wants to compete in Intermediate Pom and Premier Jazz at the same event. Is this allowed, and what rule determines the answer?"),
    ("hard", "cross-module", "multi-hop-analysis", "A dance athlete wants to compete in Intermediate Pom and Premier Pom at the same event. Is this allowed, and what rule determines the answer?"),
    ("hard", "cross-module", "multi-hop-analysis", "A cheer athlete is rostered on four teams at one sanctioned competition. Explain the applicable limit and likely eligibility result."),
    ("hard", "cross-module", "multi-hop-analysis", "A Worlds cheer athlete is listed on two Worlds teams. Explain the Worlds-specific rule and how it differs from regular sanctioned competition crossover limits."),
    ("hard", "cross-module", "multi-hop-analysis", "An event producer misses closeout and bid assignment 72 hours after an event ends. What deadlines or reminders should the system enforce?"),
    ("hard", "cross-module", "multi-hop-analysis", "A prepared club arrives at Worlds with three cheer teams. Estimate the appointment duration using the base and add-on timing rules, and cite the assumptions."),
    ("hard", "cross-module", "multi-hop-analysis", "A roster rule changes mid-season. Explain how eligibility snapshots, impact reports, roster ineligibility, and notifications interact."),
    ("hard", "cross-module", "multi-hop-analysis", "An athlete assignment was valid under old age-grid rules but the current draft changes the age range. What happens to the existing assignment versus new assignments?"),
    ("hard", "cross-module", "multi-hop-analysis", "A cross-tier temporary replacement is requested 36 hours before an event for four athletes on one team. Explain which parts pass and which require or exceed admin approval rules."),
    ("hard", "cross-module", "multi-hop-analysis", "A coach holds more than one profile role. Explain the multi-profile additional role discount and background-check waiver implications."),
    ("hard", "cross-module", "multi-hop-analysis", "A Club Owner also has additional roles. Explain the documented Club Owner fee, NCR fee, and additional-role discount behavior."),
    ("hard", "cross-module", "multi-hop-analysis", "An Event Producer applies for Dance Gold. Explain the current wiki state for Dance Gold and how Lancelot should express confidence."),
    ("hard", "cross-module", "multi-hop-analysis", "An established EP hosted 130 All Star Cheer teams last season and previously held Platinum or Gold. Which Cheer tier facts are relevant, and what fee applies if the Diamond criteria are met?"),
    ("hard", "cross-module", "multi-hop-analysis", "A parent asks whether their minor needs training videos or JDP before being eligible. Answer using Parent/Minor, Identity Validation, and Onboarding Workflow evidence."),
    ("hard", "cross-module", "multi-hop-analysis", "A Junior Coach invite is created for a 12-year-old. What does the wiki say is known, configurable, or still pending about minimum age?"),
    ("hard", "cross-module", "multi-hop-analysis", "An EA Buddy is proposed for a unified team. What does the wiki say about EA Buddy designation and unified-team restrictions?"),
    ("hard", "cross-module", "multi-hop-analysis", "A non-member adult participant is involved in conduct tracking. What model gap or platform need does the glossary identify?"),
    ("hard", "cross-module", "multi-hop-analysis", "A member asks why their status is Eligible but not Active. Explain the two-axis state model and likely missing conditions."),
    ("hard", "cross-module", "multi-hop-analysis", "A user receives an email OTP link and asks whether it is separate from OTP. Explain the magic-link relationship to OTP and expiry."),
    ("hard", "cross-module", "multi-hop-analysis", "A user uploads a profile photo and an age-verification document. What file types and size cap should be enforced?"),
    ("hard", "cross-module", "multi-hop-analysis", "A Maxient integration engineer asks which ID field is stable across seasons and what launch implication the wiki highlights."),
    ("hard", "cross-module", "multi-hop-analysis", "A training-system engineer asks whether All-Star University is being replaced. Summarize what the wiki says about LearnDash, external users, and API integration."),
    ("hard", "cross-module", "multi-hop-analysis", "A compliance analyst asks how Green Light relates to training and background verification. Explain using both Identity Validation and Glossary evidence."),
    # Expert: conflicts, superseded details, and open clarifications.
    ("expert", "open-questions", "conflict-resolution", "The provisional Transitional Athlete SRS used a June 1 cutoff, but later notes mention a 45-day claim window and April 1 BGC cutoff. Resolve the current rule set and identify what is superseded."),
    ("expert", "open-questions", "conflict-resolution", "The Onboarding Workflows page says Parent/Minor age verification vendor was originally unnamed, but later says NSID today. How should Lancelot answer if asked for the vendor?"),
    ("expert", "open-questions", "conflict-resolution", "Adult Athlete fee information appears as $49 membership, $19 background verification, and a $68 total display. Explain the correct user-facing payment answer and any nuance."),
    ("expert", "open-questions", "conflict-resolution", "Dance EP tier information includes a removed Gold tier and pending written confirmation. How should Lancelot answer a question asking for all Dance tiers?"),
    ("expert", "open-questions", "conflict-resolution", "Junior Coach minimum age is described as configurable and believed to be 12 or 13, while another register lists a 12 to 17 working range. How should Lancelot answer without overclaiming?"),
    ("expert", "open-questions", "conflict-resolution", "EA Buddy minimum age is described as season-configurable and believed as low as 10, with exact value pending. What answer should preserve that uncertainty?"),
    ("expert", "open-questions", "conflict-resolution", "The wiki distinguishes Adult Athlete Active workflow state from the public-list Active axis. How should Lancelot avoid conflating them?"),
    ("expert", "open-questions", "multi-hop-analysis", "A same-name, same-DOB duplicate profile collision occurs with possible nickname and free-email issues. What heuristic and fallback approach does the wiki support?"),
    ("expert", "open-questions", "multi-hop-analysis", "A blocked individual completes onboarding and payment before dashboard access. Explain the Jurisdiction Trap rationale and where the user is gated."),
    ("expert", "open-questions", "conflict-resolution", "A user asks whether the parent's own name/email in Parent/Minor onboarding runs through hold-list checks. What should Lancelot answer based on the open question?"),
    ("expert", "open-questions", "multi-hop-analysis", "A Code of Conduct countdown depends on Days. What does the wiki define, and what national-holiday uncertainty remains?"),
    ("expert", "open-questions", "multi-hop-analysis", "A close-in-age exception is claimed as a defense based on good-faith belief about age. What conditions are required and what defenses are explicitly invalid?"),
    ("expert", "open-questions", "multi-hop-analysis", "A club changes brand affiliation mid-season. Explain what the jump-ship flow supports, what timing restriction applies, and why it is invitation-driven."),
    ("expert", "open-questions", "multi-hop-analysis", "A Worlds roster change happens after the lock date. What does the wiki say about the lock timing and how changes are handled afterward?"),
    ("expert", "open-questions", "multi-hop-analysis", "A verifier sees Lancelot cite only web search for a USASF Brain question. How should the verifier score source grounding and why?"),
]


def build_questions() -> list[dict[str, str]]:
    questions = [
        {
            "id": f"LQ-{index:03d}",
            "difficulty": difficulty,
            "category": category,
            "question": question,
            "expected_answer_style": style,
        }
        for index, (difficulty, category, style, question) in enumerate(
            QUESTION_SEEDS, start=1
        )
    ]
    validate_questions(questions)
    return questions


def validate_questions(questions: list[dict[str, str]]) -> None:
    if len(questions) != 100:
        raise ValueError(f"Expected 100 questions, found {len(questions)}")

    ids = [question["id"] for question in questions]
    expected_ids = [f"LQ-{index:03d}" for index in range(1, 101)]
    if ids != expected_ids:
        raise ValueError("Question IDs must be sequential from LQ-001 to LQ-100")

    difficulty_counts = Counter(question["difficulty"] for question in questions)
    if difficulty_counts != DIFFICULTY_COUNTS:
        raise ValueError(
            f"Unexpected difficulty distribution: {dict(difficulty_counts)}"
        )

    for question in questions:
        if question["category"] not in VALID_CATEGORIES:
            raise ValueError(f"Invalid category for {question['id']}")
        if question["expected_answer_style"] not in VALID_STYLES:
            raise ValueError(f"Invalid answer style for {question['id']}")
        if not question["question"].strip():
            raise ValueError(f"Empty question text for {question['id']}")


def render_questions_markdown(questions: list[dict[str, str]]) -> str:
    lines = [
        "# Lancelot Wiki Evaluation Questions",
        "",
        "Use this list to ask Lancelot each benchmark question. The bot-facing prompt in `lancelot_prompt.md` defines the required answer format.",
        "",
    ]
    current_difficulty = ""
    for question in questions:
        if question["difficulty"] != current_difficulty:
            current_difficulty = question["difficulty"]
            lines.extend([f"## {current_difficulty.title()}", ""])
        lines.extend(
            [
                f"### {question['id']}",
                "",
                f"- Category: `{question['category']}`",
                f"- Expected answer style: `{question['expected_answer_style']}`",
                f"- Question: {question['question']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_lancelot_prompt(questions: list[dict[str, str]]) -> str:
    schema = (
        '{"question_id":"LQ-001","answer":"...",'
        '"confidence":"high|medium|low",'
        '"evidence":[{"source":"wiki path or page title",'
        '"supporting_claim":"..."}],'
        '"unknowns_or_conflicts":[],"needs_follow_up":false}'
    )
    lines = [
        "# Lancelot Wiki Benchmark Prompt",
        "",
        "You are being evaluated on your ability to answer questions from the USASF Brain wiki.",
        "",
        "Return strict JSONL: exactly one valid JSON object per line, with no prose before or after the JSONL.",
        "",
        "Required JSON object shape:",
        "",
        "```json",
        schema,
        "```",
        "",
        "Rules:",
        "- Answer only from the wiki unless a question explicitly asks for outside context.",
        "- Cite at least one wiki source for every answer. Prefer a wiki page path or page title.",
        "- Use `confidence: high` only when the wiki evidence is direct and unambiguous.",
        "- Use `confidence: medium` when synthesis is required but evidence is still clear.",
        "- Use `confidence: low` when the wiki is ambiguous, stale, superseded, internally conflicting, or contains an open question.",
        "- Put unresolved facts, conflicts, or superseded-rule notes in `unknowns_or_conflicts`.",
        "- Do not invent missing facts. Say what the wiki does and does not establish.",
        "- Keep answers concise but complete enough for an evaluator to verify.",
        "",
        "Questions:",
        "",
    ]
    for question in questions:
        lines.append(f"{question['id']}: {question['question']}")
    return "\n".join(lines).rstrip() + "\n"


def render_batch_prompt(
    batch_questions: list[dict[str, str]], batch_number: int, total_batches: int
) -> str:
    first_id = batch_questions[0]["id"]
    last_id = batch_questions[-1]["id"]
    header = [
        f"# Lancelot Wiki Benchmark Batch {batch_number:02d} of {total_batches:02d}",
        "",
        f"Question range: `{first_id}` to `{last_id}`.",
        "",
        "Answer only the questions in this batch. Use strict JSONL, one object per question. Do not include prose before or after the JSONL. Preserve the original question_id values.",
        "",
        "Required JSON object shape:",
        "",
        "```json",
        '{"question_id":"LQ-001","answer":"...","confidence":"high|medium|low","evidence":[{"source":"wiki path or page title","supporting_claim":"..."}],"unknowns_or_conflicts":[],"needs_follow_up":false}',
        "```",
        "",
        "Rules:",
        "- Answer only from the wiki unless a question explicitly asks for outside context.",
        "- Cite at least one wiki source for every answer. Prefer a wiki page path or page title.",
        "- Use `confidence: high` only when the wiki evidence is direct and unambiguous.",
        "- Use `confidence: medium` when synthesis is required but evidence is still clear.",
        "- Use `confidence: low` when the wiki is ambiguous, stale, superseded, internally conflicting, or contains an open question.",
        "- Put unresolved facts, conflicts, or superseded-rule notes in `unknowns_or_conflicts`.",
        "- Do not invent missing facts. Say what the wiki does and does not establish.",
        "- Keep answers concise but complete enough for an evaluator to verify.",
        "",
        "Questions:",
        "",
    ]
    return (
        "\n".join(
            [
                *header,
                *[
                    f"{question['id']}: {question['question']}"
                    for question in batch_questions
                ],
            ]
        ).rstrip()
        + "\n"
    )


def render_verifier_rubric(questions: list[dict[str, str]]) -> str:
    lines = [
        "# Lancelot Wiki Evaluation Verifier Rubric",
        "",
        "Use this rubric to grade Lancelot's JSONL answers against the local USASF Brain wiki. This artifact intentionally does not include an answer key.",
        "",
        "## Inputs",
        "",
        "- `questions.json`: benchmark question metadata.",
        "- Lancelot response: strict JSONL, one object per question.",
        "- Local wiki: `backend/knowledge-bases/USASF-Brain`.",
        "",
        "## Per-Question Scoring",
        "",
        "Score each answer out of 10 points:",
        "",
        "- Factual accuracy (0-4): The answer matches the wiki, uses the current or highest-authority rule, and does not hallucinate.",
        "- Source grounding (0-2): Evidence cites relevant wiki sources and each cited supporting claim actually supports the answer.",
        "- Completeness (0-2): The answer covers the key facts required by the question without omitting important qualifiers.",
        "- Ambiguity handling (0-1): The answer identifies open questions, conflicts, superseded facts, or uncertainty when present.",
        "- Format compliance (0-1): The answer is valid JSONL and follows the required schema.",
        "",
        "## Global Checks",
        "",
        "- Verify there are exactly 100 JSONL objects.",
        "- Verify every `question_id` from LQ-001 through LQ-100 appears exactly once.",
        "- Penalize unsupported web-search-only answers for source grounding when the question is answerable from the wiki.",
        "- Penalize confident answers that ignore wiki uncertainty, removed tiers, superseded cutoffs, or pending clarifications.",
        "- Do not reward verbosity. Reward direct answers with precise evidence.",
        "",
        "## Difficulty Expectations",
        "",
        "- Easy questions usually require direct lookup.",
        "- Medium questions usually require a workflow summary or comparison from one to two wiki pages.",
        "- Hard questions require multi-hop synthesis across concepts, registers, modules, or meeting notes.",
        "- Expert questions require careful treatment of conflicts, superseded facts, open questions, or evaluator behavior.",
        "",
        "## Question Inventory",
        "",
    ]
    for question in questions:
        lines.append(
            f"- {question['id']} [{question['difficulty']} / {question['category']} / {question['expected_answer_style']}]: {question['question']}"
        )
    return "\n".join(lines).rstrip() + "\n"


def write_artifacts(output_dir: Path = OUTPUT_DIR) -> None:
    questions = build_questions()
    output_dir.mkdir(parents=True, exist_ok=True)
    batch_dir = output_dir / "batches"
    batch_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "questions.json").write_text(
        json.dumps(questions, indent=2) + "\n"
    )
    (output_dir / "questions.md").write_text(render_questions_markdown(questions))
    (output_dir / "lancelot_prompt.md").write_text(render_lancelot_prompt(questions))
    (output_dir / "verifier_rubric.md").write_text(render_verifier_rubric(questions))

    total_batches = len(questions) // BATCH_SIZE
    for batch_index, start in enumerate(range(0, len(questions), BATCH_SIZE), start=1):
        batch_questions = questions[start : start + BATCH_SIZE]
        first_id = batch_questions[0]["id"]
        last_id = batch_questions[-1]["id"]
        batch_path = batch_dir / (
            f"batch_{batch_index:02d}_{first_id}-{last_id}.md"
        )
        batch_path.write_text(
            render_batch_prompt(batch_questions, batch_index, total_batches)
        )


if __name__ == "__main__":
    write_artifacts()
