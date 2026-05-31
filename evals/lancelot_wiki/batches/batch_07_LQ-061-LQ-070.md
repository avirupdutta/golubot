# Lancelot Wiki Benchmark Batch 07 of 10

Question range: `LQ-061` to `LQ-070`.

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

LQ-061: A Minor Exceptional Athlete is added under a Parent Account. Explain account ownership, fee, JDP, training, and age-verification expectations.
LQ-062: A user wants to call the compliance list a blacklist in a user-facing email. What should Lancelot answer, and what evidence should it cite?
LQ-063: A dance athlete wants to compete in Intermediate Pom and Premier Jazz at the same event. Is this allowed, and what rule determines the answer?
LQ-064: A dance athlete wants to compete in Intermediate Pom and Premier Pom at the same event. Is this allowed, and what rule determines the answer?
LQ-065: A cheer athlete is rostered on four teams at one sanctioned competition. Explain the applicable limit and likely eligibility result.
LQ-066: A Worlds cheer athlete is listed on two Worlds teams. Explain the Worlds-specific rule and how it differs from regular sanctioned competition crossover limits.
LQ-067: An event producer misses closeout and bid assignment 72 hours after an event ends. What deadlines or reminders should the system enforce?
LQ-068: A prepared club arrives at Worlds with three cheer teams. Estimate the appointment duration using the base and add-on timing rules, and cite the assumptions.
LQ-069: A roster rule changes mid-season. Explain how eligibility snapshots, impact reports, roster ineligibility, and notifications interact.
LQ-070: An athlete assignment was valid under old age-grid rules but the current draft changes the age range. What happens to the existing assignment versus new assignments?
