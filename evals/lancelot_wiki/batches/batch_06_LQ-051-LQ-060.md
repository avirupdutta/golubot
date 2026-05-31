# Lancelot Wiki Benchmark Batch 06 of 10

Question range: `LQ-051` to `LQ-060`.

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

LQ-051: Explain how JDP, Cerebrum, VID, and Codebuddy relate to each other in the identity-verification flow.
LQ-052: What are the typical VID completion time, manual review time, and unresolvable resubmission rate?
LQ-053: What data does Maxient receive from USASF, and how is the active member count characterized?
LQ-054: What open question remains around the Parent/Minor age-verification provider, and what is the current answer?
LQ-055: Compare Timeline and Audit Log retention or purpose, using the wiki's distinction between user-visible history and forensic audit data.
LQ-056: A parent registers a standard Minor Athlete who later turns 18 before April 1. What account, fee, background-check, training, and timing rules apply across Parent/Minor and Transitional Athlete sources?
LQ-057: A minor athlete turns 18 on or after April 1. What does the wiki say about background-check requirements for that season, and what still needs to happen?
LQ-058: A club has 127 unique athletes who have taken the floor. Explain the Division I classification, override UI behavior, and who can override on the backend.
LQ-059: A club has 129 unique athletes who have taken the floor. Explain the Division I classification and why the override request UI does or does not appear.
LQ-060: An Adult Athlete has paid but has not completed training, quiz, or JDP clearance. Explain the correct status and dashboard access implications.
