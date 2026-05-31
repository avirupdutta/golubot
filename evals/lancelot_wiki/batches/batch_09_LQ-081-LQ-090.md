# Lancelot Wiki Benchmark Batch 09 of 10

Question range: `LQ-081` to `LQ-090`.

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

LQ-081: A user receives an email OTP link and asks whether it is separate from OTP. Explain the magic-link relationship to OTP and expiry.
LQ-082: A user uploads a profile photo and an age-verification document. What file types and size cap should be enforced?
LQ-083: A Maxient integration engineer asks which ID field is stable across seasons and what launch implication the wiki highlights.
LQ-084: A training-system engineer asks whether All-Star University is being replaced. Summarize what the wiki says about LearnDash, external users, and API integration.
LQ-085: A compliance analyst asks how Green Light relates to training and background verification. Explain using both Identity Validation and Glossary evidence.
LQ-086: The provisional Transitional Athlete SRS used a June 1 cutoff, but later notes mention a 45-day claim window and April 1 BGC cutoff. Resolve the current rule set and identify what is superseded.
LQ-087: The Onboarding Workflows page says Parent/Minor age verification vendor was originally unnamed, but later says NSID today. How should Lancelot answer if asked for the vendor?
LQ-088: Adult Athlete fee information appears as $49 membership, $19 background verification, and a $68 total display. Explain the correct user-facing payment answer and any nuance.
LQ-089: Dance EP tier information includes a removed Gold tier and pending written confirmation. How should Lancelot answer a question asking for all Dance tiers?
LQ-090: Junior Coach minimum age is described as configurable and believed to be 12 or 13, while another register lists a 12 to 17 working range. How should Lancelot answer without overclaiming?
