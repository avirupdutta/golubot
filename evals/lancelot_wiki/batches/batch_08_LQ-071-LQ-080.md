# Lancelot Wiki Benchmark Batch 08 of 10

Question range: `LQ-071` to `LQ-080`.

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

LQ-071: A cross-tier temporary replacement is requested 36 hours before an event for four athletes on one team. Explain which parts pass and which require or exceed admin approval rules.
LQ-072: A coach holds more than one profile role. Explain the multi-profile additional role discount and background-check waiver implications.
LQ-073: A Club Owner also has additional roles. Explain the documented Club Owner fee, NCR fee, and additional-role discount behavior.
LQ-074: An Event Producer applies for Dance Gold. Explain the current wiki state for Dance Gold and how Lancelot should express confidence.
LQ-075: An established EP hosted 130 All Star Cheer teams last season and previously held Platinum or Gold. Which Cheer tier facts are relevant, and what fee applies if the Diamond criteria are met?
LQ-076: A parent asks whether their minor needs training videos or JDP before being eligible. Answer using Parent/Minor, Identity Validation, and Onboarding Workflow evidence.
LQ-077: A Junior Coach invite is created for a 12-year-old. What does the wiki say is known, configurable, or still pending about minimum age?
LQ-078: An EA Buddy is proposed for a unified team. What does the wiki say about EA Buddy designation and unified-team restrictions?
LQ-079: A non-member adult participant is involved in conduct tracking. What model gap or platform need does the glossary identify?
LQ-080: A member asks why their status is Eligible but not Active. Explain the two-axis state model and likely missing conditions.
