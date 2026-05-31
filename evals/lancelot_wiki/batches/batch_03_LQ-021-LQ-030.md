# Lancelot Wiki Benchmark Batch 03 of 10

Question range: `LQ-021` to `LQ-030`.

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

LQ-021: Summarize the shared member onboarding scaffold in order, including where agreements, payment, dashboard entry, and compliance gates occur.
LQ-022: Compare Adult Athlete onboarding with Parent/Minor onboarding across account ownership, fees, JDP/background checks, training, and post-payment compliance.
LQ-023: Compare Adult Exceptional Athlete onboarding with Adult Athlete onboarding across fees, background checks, training, and documentation requirements.
LQ-024: Explain the Adult Athlete post-payment state before all compliance gates are cleared. What can the user access and what remains incomplete?
LQ-025: Describe the Transitional Athlete account-claim process and the current 45-day claim-window rule.
LQ-026: Describe the Junior Coach and Junior NCR 18th birthday claim-window rule and how it relates to the Transitional Athlete rule.
LQ-027: Compare Jr Coach, Jr NCR, and EA Buddy onboarding or designation requirements, including whether EA Buddy is a standalone profile type.
LQ-028: Explain the two-stage hold-list pattern and what happens at Stage 1 versus Stage 2.
LQ-029: Compare Hard Block and Soft Hold outcomes in authentication or hold-list handling.
LQ-030: What duplicate-detection heuristic is described from the profile review meeting? Include the primary match and tiebreakers.
