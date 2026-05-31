# Lancelot Wiki Benchmark Batch 05 of 10

Question range: `LQ-041` to `LQ-050`.

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

LQ-041: Compare Self Pay, Club Pay, and zero-dollar flows as they appear across the shared onboarding scaffold and profile-specific variations.
LQ-042: What is the Club Pay request expiry window for Coach onboarding, and how is it configured?
LQ-043: What are the EP Cheer tier fees from Bronze through Diamond?
LQ-044: What are the EP Dance tier fees, and what happened to the Dance Gold tier?
LQ-045: Summarize the Worlds appointment timeline: when scheduling opens, when appointments occur, when the event starts, and when rosters lock.
LQ-046: What are the approximate Worlds attendance counts for US teams, athletes, and non-US athletes?
LQ-047: Compare cheer and dance limits for Worlds team participation and warm-up room entries.
LQ-048: What state ID exception is noted for New Jersey and Massachusetts Worlds athletes?
LQ-049: Explain what happens when an admin makes a mid-season division rule change under Admin BL-5.
LQ-050: What is the new platform launch season target?
