# Lancelot Wiki Benchmark Batch 01 of 10

Question range: `LQ-001` to `LQ-010`.

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

LQ-001: What is the Adult Athlete membership fee, and what total fee should be shown when the background-verification fee is included?
LQ-002: What is the Minor Athlete membership fee per season?
LQ-003: What is the Coach membership fee, and what is the Junior Coach fee?
LQ-004: What is the Legality Official training fee?
LQ-005: What is the default OTP expiry window?
LQ-006: How many OTP resend attempts are allowed per hour, and what is the minimum gap between resend attempts?
LQ-007: After how many wrong OTP submissions does lockout occur, and how long does the lockout last?
LQ-008: What does Green Light status mean in the USASF wiki?
LQ-009: What public-facing term must be used instead of blacklist?
LQ-010: Which provider handles background checks and identity verification for USASF?
