# Public Case Evidence

`cases/` stores sanitized public evidence for how `oh-my-gh-writing` behaves on realistic GitHub writing tasks.

Current cases are synthetic, sanitized tasks. They test routing, artifact shape, and evidence boundaries; they are not real repository outcome reports or raw agent logs.

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
    with-skill.md OR with-skill.<target-extension>
    baseline-summary.md
    grading.md
    attribution.md
```

## Current Cases

These cases were generated or curated from skill runs, then manually reviewed and sanitized for public evidence drafts. They are not raw validation logs, runtime references, or source material for user artifacts.

Target: 5 carefully reviewed cases over time.
Current: 5 review-draft cases.

| Case | Focus | Status | Baseline |
|------|-------|--------|----------|
| `001-bug-report/` | Bug Report routing and missing-evidence handling | Review draft | TODO |
| `002-feature-request-routing/` | Feature Request vs Feature PR routing | Review draft | TODO |
| `003-version-release-workflow/` | Version Release workflow pack and draft-only behavior | Review draft; do not cite publicly yet | TODO |
| `004-issue-form-yaml/` | Issue Form YAML without invented repository metadata | Review draft | TODO |
| `005-project-launch-audit/` | Project Launch audit-only readiness review | Review draft; README excerpt approved | TODO |

## Required Files

| File | Purpose |
|------|---------|
| `input.md` | The user-style prompt or task given to the agent |
| `source.md` | Sanitized source artifact, link, excerpt, or repository context used for the task |
| `with-skill.md` or `with-skill.<target-extension>` | Output produced with this skill enabled; use the target extension for file artifacts such as YAML |
| `baseline-summary.md` | Short summary of baseline behavior without this skill; do not store large raw output by default |
| `grading.md` | Human review notes, pass/fail labels, README excerpt type when cited, exposed issues, and follow-up decisions |
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
- Do not call review drafts "validated comparison cases" until baseline behavior is collected.
- Keep raw agent traces out of this directory unless they are sanitized and intentionally reviewed.
- Attribute public sources clearly.
- State whether copied snippets are excerpts, paraphrases, or links only.
- For synthetic cases, `source.md` should describe the constructed task and `attribution.md` may stay short. Avoid repeating boilerplate beyond what is needed for safety.
- Remove source-specific facts that could be mistaken for general skill rules.
- Record whether a case is allowed to be cited in README or release notes.

## Validation

Run from the repository root:

```bash
python3 scripts/validate-cases.py
```

The validator checks required files, accepted `with-skill.*` output suffixes, grading labels, case index registration, README citation permission, README excerpt type, and obvious baseline/status conflicts.
