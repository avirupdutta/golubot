Evaluate this Lancelot answer batch using verifier_rubric.md.

Use questions.json to map question IDs to questions.
Use @backend/knowledge-bases/USASF-Brain as the source of truth.
Do not rely on Lancelot’s citations blindly; verify each cited source and claim.

Return:
1. Per-question score out of 10
2. Accuracy notes
3. Source-grounding notes
4. Format issues
5. Total score and percentage

verify - [lancelot_answers_batch_01.jsonl](evals/lancelot_wiki/responses/lancelot_answers_batch_01.jsonl)