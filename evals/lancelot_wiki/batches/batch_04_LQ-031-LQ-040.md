# Lancelot Wiki Benchmark Batch 04 of 10

Question range: `LQ-031` to `LQ-040`.

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

LQ-031: Explain how minor profiles bypass JDP and what compliance mechanism is used instead.
LQ-032: Distinguish Active and Eligible in the two-axis member state model.
LQ-033: Explain why minors do not have their own login and how profile ownership changes when they turn 18.
LQ-034: Describe the three connected concerns introduced by the Roster SRS update: Age Grid / Division Rules, Team Management, and Event Rosters.
LQ-035: Explain the Age Grid Editor lifecycle and how seasons move from draft to published.
LQ-036: What is an eligibility snapshot, and why do mid-season rule amendments not invalidate existing snapshots?
LQ-037: List the five individual eligibility rules for roster assignment described in the Roster System concept page.
LQ-038: Compare cheer, dance, and cheer-to-dance crossover rules.
LQ-039: Describe the temporary replacement rule, including notice timing, eligibility, cross-tier limits, and approval requirements.
LQ-040: Explain nightly re-validation and how unresolved flags affect event roster submission.
