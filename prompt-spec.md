# Prompt Specification — Recruiter Opportunity Classifier

## 1. Purpose

Classify inbound recruiter messages into a small, reusable fit category for a senior AI/cloud/integration professional, while avoiding unsupported inference and preserving human review for consequential decisions.

## 2. Final prompt

```text
Classify this recruiter message as one of:
StrongMatch, PossibleMatch, NotMatch, NeedInfo.

Definitions:
- StrongMatch = the role's primary responsibility is directly aligned with AI, cloud architecture, enterprise integration, or solution architecture.
- PossibleMatch = there is meaningful technical overlap, but the role's primary responsibility differs from the target profile.
- NotMatch = there is little or no relevant overlap.
- NeedInfo = the message does not contain enough role information to judge.

Decision rule:
Judge fit by the role's primary responsibility, not by incidental technologies, buzzwords, or domain context.

Safety/fairness rule:
Use only job-relevant information explicitly present in the message. Do not infer demographic characteristics or suitability from names or background.

Input:
"""
{input}
"""

Return exactly one allowed label and no other text.
```

## 3. Success criteria

1. **Mechanical** — Output is exactly one of: `StrongMatch`, `PossibleMatch`, `NotMatch`, `NeedInfo`.
2. **Mechanical** — Output contains no extra commentary, Markdown, punctuation, or explanation.
3. **Mechanical** — Clearly aligned AI/cloud/integration/solution-architecture roles are not classified below `PossibleMatch`.
4. **Mechanical** — Inputs with insufficient detail are classified as `NeedInfo`.
5. **Human** — Borderline cases are judged by primary role responsibility rather than incidental technology mentions.

## 4. Test set

### T1 — representative

```text
Senior AI Engineer working with Azure OpenAI, RAG, Python, APIs, and agentic workflows. Remote LATAM.
```

Expected:

```text
StrongMatch
```

### T2 — representative

```text
Senior Java Developer focused on Spring Boot, REST APIs, PostgreSQL, and Azure App Service. No AI responsibilities are listed.
```

Expected:

```text
PossibleMatch
```

### T3 — ambiguous / borderline

```text
Technical Product Manager for an AI platform. Engineering experience is preferred, but the role primarily owns roadmap, stakeholder alignment, product planning, and prioritization.
```

Expected:

```text
PossibleMatch
```

### T4 — held back / edge case

```text

```

Expected:

```text
NeedInfo
```

### T5 — held back / insufficient information

```text
We have a senior technology opportunity that may be a strong fit. Let me know if you want more details.
```

Expected:

```text
NeedInfo
```

`T4` and `T5` were held back during tuning and used only after v3 was selected.

## 5. Known limitations

Observed during the lab:

- **Baseline over-weighted AI context:** v1 labeled an AI Product Manager role `StrongMatch` even though product management was the primary responsibility.
- **Fix:** the primary-responsibility rule corrected the failure in v2.
- **Small evaluation set:** only five fixed cases were used; this is insufficient to establish production reliability.
- **Run-to-run variation:** the surprising T3 baseline result was re-run once and repeated the same failure. Larger-scale repeat testing is still needed.
- **Hallucination risk:** when asked for an internal statistic without a source, the model invented `42%`.
- **Grounding result:** exact refusal wording prevented fabrication when the statistic was absent from the supplied source.
- **Citation verification:** the tested quote matched the source character by character.
- **Self-check:** successfully detected an injected unsupported `42%` claim.
- **Format drift:** JSON probe was `5/5 clean` in this test, but this does not guarantee future parseability.
- **Bias substitution:** three name-only variants produced identical `Advance` outputs; no observable bias appeared in this small substitution test.
- **Safety:** the harmful request was declined and the legitimate electrical-safety request was not over-refused.
- **Autonomy limitation:** the classifier should not autonomously reject or advance real candidates without human review.

## 6. Version history

```text
v1 — Baseline definitions only.
Result: 2/3 tuning inputs passed.
Observed failure: AI Product Manager incorrectly classified StrongMatch.

v2 — Added one rule: judge by primary responsibility, not incidental technologies or context.
Result: 3/3 tuning inputs passed.

v3 — Added one output constraint: return exactly one allowed label and no other text.
Result: 3/3 tuning inputs passed.
Held-back T4/T5: 2/2 passed.
```

## 7. Review requirement

### Human review required

Yes, whenever the output affects a real candidate or employment opportunity.

### Reviewer

Recruiter or hiring manager.

### Reviewer checks

- The classification reflects the actual job responsibilities.
- Relevant experience was not omitted or misunderstood.
- `NeedInfo` cases are clarified rather than guessed.
- No demographic or other irrelevant inferred characteristic influenced the decision.
- The model output is advisory and does not replace accountable human judgment.
