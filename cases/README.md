# Public Case Evidence

`cases/` stores sanitized public evidence for how `oh-my-gh-writing` behaves on realistic GitHub writing tasks.

This directory is not a runtime reference:

- `SKILL.md` must not automatically load files from `cases/`.
- Case files are not source material for user artifacts.
- Cases are public evidence and maintenance material only.
- Do not place private artifacts, raw local validation logs, or unreviewed copied content here.

## Case Structure

Use one directory per reviewed case:

```text
cases/
  001-bug-report/
    input.md
    source.md
    with-skill.md
    baseline-summary.md
    grading.md
    attribution.md
```

## Required Files

| File | Purpose |
|------|---------|
| `input.md` | The user-style prompt or task given to the agent |
| `source.md` | Sanitized source artifact, link, excerpt, or repository context used for the task |
| `with-skill.md` | Output produced with this skill enabled |
| `baseline-summary.md` | Short summary of baseline behavior without this skill; do not store large raw output by default |
| `grading.md` | Human review notes, pass/fail labels, exposed issues, and follow-up decisions |
| `attribution.md` | Source URL, license/attribution notes, sanitization status, and permission notes |

## Grading Labels

Use the same labels as `evals/README.md` when possible:

- `PASS`
- `PASS_AFTER_CLEANUP`
- `ROUTING_FAIL`
- `FORMAT_FAIL`
- `FACT_CHECK_REQUIRED`
- `DRAFT_ONLY`

## Rules

- Prefer 5 carefully reviewed cases over a large uncurated gallery.
- Keep raw agent traces out of this directory unless they are sanitized and intentionally reviewed.
- Attribute public sources clearly.
- State whether copied snippets are excerpts, paraphrases, or links only.
- Remove source-specific facts that could be mistaken for general skill rules.
- Record whether a case is allowed to be cited in README or release notes.
