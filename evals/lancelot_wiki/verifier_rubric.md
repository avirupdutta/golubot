# Lancelot Wiki Evaluation Verifier Rubric

Use this rubric to grade Lancelot's JSONL answers against the local USASF Brain wiki. This artifact intentionally does not include an answer key.

## Inputs

- `questions.json`: benchmark question metadata.
- Lancelot response: strict JSONL, one object per question.
- Local wiki: `backend/knowledge-bases/USASF-Brain`.

## Per-Question Scoring

Score each answer out of 10 points:

- Factual accuracy (0-4): The answer matches the wiki, uses the current or highest-authority rule, and does not hallucinate.
- Source grounding (0-2): Evidence cites relevant wiki sources and each cited supporting claim actually supports the answer.
- Completeness (0-2): The answer covers the key facts required by the question without omitting important qualifiers.
- Ambiguity handling (0-1): The answer identifies open questions, conflicts, superseded facts, or uncertainty when present.
- Format compliance (0-1): The answer is valid JSONL and follows the required schema.

## Global Checks

- Verify there are exactly 100 JSONL objects.
- Verify every `question_id` from LQ-001 through LQ-100 appears exactly once.
- Penalize unsupported web-search-only answers for source grounding when the question is answerable from the wiki.
- Penalize confident answers that ignore wiki uncertainty, removed tiers, superseded cutoffs, or pending clarifications.
- Do not reward verbosity. Reward direct answers with precise evidence.

## Difficulty Expectations

- Easy questions usually require direct lookup.
- Medium questions usually require a workflow summary or comparison from one to two wiki pages.
- Hard questions require multi-hop synthesis across concepts, registers, modules, or meeting notes.
- Expert questions require careful treatment of conflicts, superseded facts, open questions, or evaluator behavior.

## Question Inventory

- LQ-001 [easy / payments / fact]: What is the Adult Athlete membership fee, and what total fee should be shown when the background-verification fee is included?
- LQ-002 [easy / payments / fact]: What is the Minor Athlete membership fee per season?
- LQ-003 [easy / payments / fact]: What is the Coach membership fee, and what is the Junior Coach fee?
- LQ-004 [easy / payments / fact]: What is the Legality Official training fee?
- LQ-005 [easy / identity / fact]: What is the default OTP expiry window?
- LQ-006 [easy / identity / fact]: How many OTP resend attempts are allowed per hour, and what is the minimum gap between resend attempts?
- LQ-007 [easy / identity / fact]: After how many wrong OTP submissions does lockout occur, and how long does the lockout last?
- LQ-008 [easy / identity / fact]: What does Green Light status mean in the USASF wiki?
- LQ-009 [easy / identity / fact]: What public-facing term must be used instead of blacklist?
- LQ-010 [easy / integrations / fact]: Which provider handles background checks and identity verification for USASF?
- LQ-011 [easy / integrations / fact]: What is the Maxient feed delimiter and how many fields are in each line?
- LQ-012 [easy / integrations / fact]: What is the maximum length of the Immutable Member ID required by Maxient?
- LQ-013 [easy / roster / fact]: What is the cheer crossover limit at a single USASF sanctioned competition?
- LQ-014 [easy / worlds / fact]: At Worlds, how many teams can a cheer athlete be on and how many teams can a dance athlete be on?
- LQ-015 [easy / worlds / fact]: What is the approximate prepared-club Worlds appointment duration?
- LQ-016 [easy / admin / fact]: What is the Division I athlete threshold?
- LQ-017 [easy / admin / fact]: For which Division I over-threshold counts does the club-facing override request option appear?
- LQ-018 [easy / onboarding / fact]: How many distinct onboarding flows are listed in the Onboarding Workflows concept page?
- LQ-019 [easy / onboarding / fact]: Which onboarding flow is invite-only and has no public signup?
- LQ-020 [easy / onboarding / fact]: Which profile types are described as having a zero-dollar Exceptional Athlete fee?
- LQ-021 [medium / onboarding / workflow]: Summarize the shared member onboarding scaffold in order, including where agreements, payment, dashboard entry, and compliance gates occur.
- LQ-022 [medium / onboarding / comparison]: Compare Adult Athlete onboarding with Parent/Minor onboarding across account ownership, fees, JDP/background checks, training, and post-payment compliance.
- LQ-023 [medium / onboarding / comparison]: Compare Adult Exceptional Athlete onboarding with Adult Athlete onboarding across fees, background checks, training, and documentation requirements.
- LQ-024 [medium / onboarding / workflow]: Explain the Adult Athlete post-payment state before all compliance gates are cleared. What can the user access and what remains incomplete?
- LQ-025 [medium / onboarding / workflow]: Describe the Transitional Athlete account-claim process and the current 45-day claim-window rule.
- LQ-026 [medium / onboarding / workflow]: Describe the Junior Coach and Junior NCR 18th birthday claim-window rule and how it relates to the Transitional Athlete rule.
- LQ-027 [medium / onboarding / comparison]: Compare Jr Coach, Jr NCR, and EA Buddy onboarding or designation requirements, including whether EA Buddy is a standalone profile type.
- LQ-028 [medium / identity / workflow]: Explain the two-stage hold-list pattern and what happens at Stage 1 versus Stage 2.
- LQ-029 [medium / identity / comparison]: Compare Hard Block and Soft Hold outcomes in authentication or hold-list handling.
- LQ-030 [medium / identity / fact]: What duplicate-detection heuristic is described from the profile review meeting? Include the primary match and tiebreakers.
- LQ-031 [medium / identity / workflow]: Explain how minor profiles bypass JDP and what compliance mechanism is used instead.
- LQ-032 [medium / identity / comparison]: Distinguish Active and Eligible in the two-axis member state model.
- LQ-033 [medium / identity / workflow]: Explain why minors do not have their own login and how profile ownership changes when they turn 18.
- LQ-034 [medium / roster / workflow]: Describe the three connected concerns introduced by the Roster SRS update: Age Grid / Division Rules, Team Management, and Event Rosters.
- LQ-035 [medium / roster / workflow]: Explain the Age Grid Editor lifecycle and how seasons move from draft to published.
- LQ-036 [medium / roster / workflow]: What is an eligibility snapshot, and why do mid-season rule amendments not invalidate existing snapshots?
- LQ-037 [medium / roster / workflow]: List the five individual eligibility rules for roster assignment described in the Roster System concept page.
- LQ-038 [medium / roster / comparison]: Compare cheer, dance, and cheer-to-dance crossover rules.
- LQ-039 [medium / roster / workflow]: Describe the temporary replacement rule, including notice timing, eligibility, cross-tier limits, and approval requirements.
- LQ-040 [medium / roster / workflow]: Explain nightly re-validation and how unresolved flags affect event roster submission.
- LQ-041 [medium / payments / comparison]: Compare Self Pay, Club Pay, and zero-dollar flows as they appear across the shared onboarding scaffold and profile-specific variations.
- LQ-042 [medium / payments / fact]: What is the Club Pay request expiry window for Coach onboarding, and how is it configured?
- LQ-043 [medium / payments / fact]: What are the EP Cheer tier fees from Bronze through Diamond?
- LQ-044 [medium / payments / fact]: What are the EP Dance tier fees, and what happened to the Dance Gold tier?
- LQ-045 [medium / worlds / workflow]: Summarize the Worlds appointment timeline: when scheduling opens, when appointments occur, when the event starts, and when rosters lock.
- LQ-046 [medium / worlds / fact]: What are the approximate Worlds attendance counts for US teams, athletes, and non-US athletes?
- LQ-047 [medium / worlds / comparison]: Compare cheer and dance limits for Worlds team participation and warm-up room entries.
- LQ-048 [medium / worlds / fact]: What state ID exception is noted for New Jersey and Massachusetts Worlds athletes?
- LQ-049 [medium / admin / workflow]: Explain what happens when an admin makes a mid-season division rule change under Admin BL-5.
- LQ-050 [medium / admin / fact]: What is the new platform launch season target?
- LQ-051 [medium / integrations / workflow]: Explain how JDP, Cerebrum, VID, and Codebuddy relate to each other in the identity-verification flow.
- LQ-052 [medium / integrations / fact]: What are the typical VID completion time, manual review time, and unresolvable resubmission rate?
- LQ-053 [medium / integrations / workflow]: What data does Maxient receive from USASF, and how is the active member count characterized?
- LQ-054 [medium / open-questions / fact]: What open question remains around the Parent/Minor age-verification provider, and what is the current answer?
- LQ-055 [medium / cross-module / comparison]: Compare Timeline and Audit Log retention or purpose, using the wiki's distinction between user-visible history and forensic audit data.
- LQ-056 [hard / cross-module / multi-hop-analysis]: A parent registers a standard Minor Athlete who later turns 18 before April 1. What account, fee, background-check, training, and timing rules apply across Parent/Minor and Transitional Athlete sources?
- LQ-057 [hard / cross-module / multi-hop-analysis]: A minor athlete turns 18 on or after April 1. What does the wiki say about background-check requirements for that season, and what still needs to happen?
- LQ-058 [hard / cross-module / multi-hop-analysis]: A club has 127 unique athletes who have taken the floor. Explain the Division I classification, override UI behavior, and who can override on the backend.
- LQ-059 [hard / cross-module / multi-hop-analysis]: A club has 129 unique athletes who have taken the floor. Explain the Division I classification and why the override request UI does or does not appear.
- LQ-060 [hard / cross-module / multi-hop-analysis]: An Adult Athlete has paid but has not completed training, quiz, or JDP clearance. Explain the correct status and dashboard access implications.
- LQ-061 [hard / cross-module / multi-hop-analysis]: A Minor Exceptional Athlete is added under a Parent Account. Explain account ownership, fee, JDP, training, and age-verification expectations.
- LQ-062 [hard / cross-module / multi-hop-analysis]: A user wants to call the compliance list a blacklist in a user-facing email. What should Lancelot answer, and what evidence should it cite?
- LQ-063 [hard / cross-module / multi-hop-analysis]: A dance athlete wants to compete in Intermediate Pom and Premier Jazz at the same event. Is this allowed, and what rule determines the answer?
- LQ-064 [hard / cross-module / multi-hop-analysis]: A dance athlete wants to compete in Intermediate Pom and Premier Pom at the same event. Is this allowed, and what rule determines the answer?
- LQ-065 [hard / cross-module / multi-hop-analysis]: A cheer athlete is rostered on four teams at one sanctioned competition. Explain the applicable limit and likely eligibility result.
- LQ-066 [hard / cross-module / multi-hop-analysis]: A Worlds cheer athlete is listed on two Worlds teams. Explain the Worlds-specific rule and how it differs from regular sanctioned competition crossover limits.
- LQ-067 [hard / cross-module / multi-hop-analysis]: An event producer misses closeout and bid assignment 72 hours after an event ends. What deadlines or reminders should the system enforce?
- LQ-068 [hard / cross-module / multi-hop-analysis]: A prepared club arrives at Worlds with three cheer teams. Estimate the appointment duration using the base and add-on timing rules, and cite the assumptions.
- LQ-069 [hard / cross-module / multi-hop-analysis]: A roster rule changes mid-season. Explain how eligibility snapshots, impact reports, roster ineligibility, and notifications interact.
- LQ-070 [hard / cross-module / multi-hop-analysis]: An athlete assignment was valid under old age-grid rules but the current draft changes the age range. What happens to the existing assignment versus new assignments?
- LQ-071 [hard / cross-module / multi-hop-analysis]: A cross-tier temporary replacement is requested 36 hours before an event for four athletes on one team. Explain which parts pass and which require or exceed admin approval rules.
- LQ-072 [hard / cross-module / multi-hop-analysis]: A coach holds more than one profile role. Explain the multi-profile additional role discount and background-check waiver implications.
- LQ-073 [hard / cross-module / multi-hop-analysis]: A Club Owner also has additional roles. Explain the documented Club Owner fee, NCR fee, and additional-role discount behavior.
- LQ-074 [hard / cross-module / multi-hop-analysis]: An Event Producer applies for Dance Gold. Explain the current wiki state for Dance Gold and how Lancelot should express confidence.
- LQ-075 [hard / cross-module / multi-hop-analysis]: An established EP hosted 130 All Star Cheer teams last season and previously held Platinum or Gold. Which Cheer tier facts are relevant, and what fee applies if the Diamond criteria are met?
- LQ-076 [hard / cross-module / multi-hop-analysis]: A parent asks whether their minor needs training videos or JDP before being eligible. Answer using Parent/Minor, Identity Validation, and Onboarding Workflow evidence.
- LQ-077 [hard / cross-module / multi-hop-analysis]: A Junior Coach invite is created for a 12-year-old. What does the wiki say is known, configurable, or still pending about minimum age?
- LQ-078 [hard / cross-module / multi-hop-analysis]: An EA Buddy is proposed for a unified team. What does the wiki say about EA Buddy designation and unified-team restrictions?
- LQ-079 [hard / cross-module / multi-hop-analysis]: A non-member adult participant is involved in conduct tracking. What model gap or platform need does the glossary identify?
- LQ-080 [hard / cross-module / multi-hop-analysis]: A member asks why their status is Eligible but not Active. Explain the two-axis state model and likely missing conditions.
- LQ-081 [hard / cross-module / multi-hop-analysis]: A user receives an email OTP link and asks whether it is separate from OTP. Explain the magic-link relationship to OTP and expiry.
- LQ-082 [hard / cross-module / multi-hop-analysis]: A user uploads a profile photo and an age-verification document. What file types and size cap should be enforced?
- LQ-083 [hard / cross-module / multi-hop-analysis]: A Maxient integration engineer asks which ID field is stable across seasons and what launch implication the wiki highlights.
- LQ-084 [hard / cross-module / multi-hop-analysis]: A training-system engineer asks whether All-Star University is being replaced. Summarize what the wiki says about LearnDash, external users, and API integration.
- LQ-085 [hard / cross-module / multi-hop-analysis]: A compliance analyst asks how Green Light relates to training and background verification. Explain using both Identity Validation and Glossary evidence.
- LQ-086 [expert / open-questions / conflict-resolution]: The provisional Transitional Athlete SRS used a June 1 cutoff, but later notes mention a 45-day claim window and April 1 BGC cutoff. Resolve the current rule set and identify what is superseded.
- LQ-087 [expert / open-questions / conflict-resolution]: The Onboarding Workflows page says Parent/Minor age verification vendor was originally unnamed, but later says NSID today. How should Lancelot answer if asked for the vendor?
- LQ-088 [expert / open-questions / conflict-resolution]: Adult Athlete fee information appears as $49 membership, $19 background verification, and a $68 total display. Explain the correct user-facing payment answer and any nuance.
- LQ-089 [expert / open-questions / conflict-resolution]: Dance EP tier information includes a removed Gold tier and pending written confirmation. How should Lancelot answer a question asking for all Dance tiers?
- LQ-090 [expert / open-questions / conflict-resolution]: Junior Coach minimum age is described as configurable and believed to be 12 or 13, while another register lists a 12 to 17 working range. How should Lancelot answer without overclaiming?
- LQ-091 [expert / open-questions / conflict-resolution]: EA Buddy minimum age is described as season-configurable and believed as low as 10, with exact value pending. What answer should preserve that uncertainty?
- LQ-092 [expert / open-questions / conflict-resolution]: The wiki distinguishes Adult Athlete Active workflow state from the public-list Active axis. How should Lancelot avoid conflating them?
- LQ-093 [expert / open-questions / multi-hop-analysis]: A same-name, same-DOB duplicate profile collision occurs with possible nickname and free-email issues. What heuristic and fallback approach does the wiki support?
- LQ-094 [expert / open-questions / multi-hop-analysis]: A blocked individual completes onboarding and payment before dashboard access. Explain the Jurisdiction Trap rationale and where the user is gated.
- LQ-095 [expert / open-questions / conflict-resolution]: A user asks whether the parent's own name/email in Parent/Minor onboarding runs through hold-list checks. What should Lancelot answer based on the open question?
- LQ-096 [expert / open-questions / multi-hop-analysis]: A Code of Conduct countdown depends on Days. What does the wiki define, and what national-holiday uncertainty remains?
- LQ-097 [expert / open-questions / multi-hop-analysis]: A close-in-age exception is claimed as a defense based on good-faith belief about age. What conditions are required and what defenses are explicitly invalid?
- LQ-098 [expert / open-questions / multi-hop-analysis]: A club changes brand affiliation mid-season. Explain what the jump-ship flow supports, what timing restriction applies, and why it is invitation-driven.
- LQ-099 [expert / open-questions / multi-hop-analysis]: A Worlds roster change happens after the lock date. What does the wiki say about the lock timing and how changes are handled afterward?
- LQ-100 [expert / open-questions / multi-hop-analysis]: A verifier sees Lancelot cite only web search for a USASF Brain question. How should the verifier score source grounding and why?
