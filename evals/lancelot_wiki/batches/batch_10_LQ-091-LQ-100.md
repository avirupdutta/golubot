# Lancelot Wiki Benchmark Batch 10 of 10

Question range: `LQ-091` to `LQ-100`.

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

LQ-091: EA Buddy minimum age is described as season-configurable and believed as low as 10, with exact value pending. What answer should preserve that uncertainty?
LQ-092: The wiki distinguishes Adult Athlete Active workflow state from the public-list Active axis. How should Lancelot avoid conflating them?
LQ-093: A same-name, same-DOB duplicate profile collision occurs with possible nickname and free-email issues. What heuristic and fallback approach does the wiki support?
LQ-094: A blocked individual completes onboarding and payment before dashboard access. Explain the Jurisdiction Trap rationale and where the user is gated.
LQ-095: A user asks whether the parent's own name/email in Parent/Minor onboarding runs through hold-list checks. What should Lancelot answer based on the open question?
LQ-096: A Code of Conduct countdown depends on Days. What does the wiki define, and what national-holiday uncertainty remains?
LQ-097: A close-in-age exception is claimed as a defense based on good-faith belief about age. What conditions are required and what defenses are explicitly invalid?
LQ-098: A club changes brand affiliation mid-season. Explain what the jump-ship flow supports, what timing restriction applies, and why it is invitation-driven.
LQ-099: A Worlds roster change happens after the lock date. What does the wiki say about the lock timing and how changes are handled afterward?
LQ-100: A verifier sees Lancelot cite only web search for a USASF Brain question. How should the verifier score source grounding and why?
