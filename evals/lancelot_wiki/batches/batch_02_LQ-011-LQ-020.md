# Lancelot Wiki Benchmark Batch 02 of 10

Question range: `LQ-011` to `LQ-020`.

Answer only the questions in this batch. Use strict JSONL, one object per question. Do not include prose before or after the JSONL. Preserve the original question_id values.

Required JSON object shape:

```json
{"question_id":"LQ-001","answer":"...","confidence":"high|medium|low","evidence":[{"source":"wiki path or page title","supporting_claim":"..."}],"unknowns_or_conflicts":[],"needs_follow_up":false}
```

Rules:
- Answer only from the wiki unless a question explicitly asks for outside context.
- Cite at least one wiki source for every answer. Prefer a wiki page path or page title.
- Use `confidence: high` only when the wiki evidence is direct and unambiguous.
- Use `confidence: medium` when synthesis is required but evidence is still clear.
- Use `confidence: low` when the wiki is ambiguous, stale, superseded, internally conflicting, or contains an open question.
- Put unresolved facts, conflicts, or superseded-rule notes in `unknowns_or_conflicts`.
- Do not invent missing facts. Say what the wiki does and does not establish.
- Keep answers concise but complete enough for an evaluator to verify.

Questions:

LQ-011: What is the Maxient feed delimiter and how many fields are in each line?
LQ-012: What is the maximum length of the Immutable Member ID required by Maxient?
LQ-013: What is the cheer crossover limit at a single USASF sanctioned competition?
LQ-014: At Worlds, how many teams can a cheer athlete be on and how many teams can a dance athlete be on?
LQ-015: What is the approximate prepared-club Worlds appointment duration?
LQ-016: What is the Division I athlete threshold?
LQ-017: For which Division I over-threshold counts does the club-facing override request option appear?
LQ-018: How many distinct onboarding flows are listed in the Onboarding Workflows concept page?
LQ-019: Which onboarding flow is invite-only and has no public signup?
LQ-020: Which profile types are described as having a zero-dollar Exceptional Athlete fee?
