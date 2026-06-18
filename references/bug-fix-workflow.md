# Bug Fix Workflow Pack

## Use When

Use when the user wants to handle a bug from report or triage through a fix PR, verification notes, or review guidance.

If the user asks only for a bug report or bug-fix PR, route to that single-artifact standard.

## Default Output Location

Write local drafts under `.github-writing/bug-fix-workflow/<version-or-date>/`. If no version/date is known, use `.github-writing/bug-fix-workflow/TBD/`.

Do not open issues, branches, PRs, or reviews unless explicitly requested.

## Decision Rule

If no fix diff exists, do not generate Bug Fix PR as final; generate Issue-only triage.

## Required Package Question

Ask this when the Decision Rule cannot safely choose a package option:

```text
Which bug-fix workflow package should I prepare?

A. Triage-to-PR pack (Recommended): triage summary + Bug Fix PR + verification notes.
B. Issue-only triage: Bug Report + investigation checklist.
C. PR-ready fix: Bug Fix PR + tests/verification + reviewer notes.

Add any supplements in the same reply: affected version, reproduction steps, logs, root-cause evidence, fix summary, test output, linked issue, or release impact.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Triage-to-PR pack | `bug-report.md`, `bug-fix-pr.md`, `code-review.md` when reviewer notes are needed |
| Issue-only triage | `bug-report.md` |
| PR-ready fix | `bug-fix-pr.md`, `code-review.md` |

Read `shared-principles.md` when root cause, test results, or affected versions are discussed.

## Evidence Rules

- Root cause, affected versions, test results, logs, issue links, and fix verification require evidence.
- Use `Suspected cause` when causality is not proven.

## Suggested File Names

- `bug-triage.md`
- `bug-fix-pr.md`
- `verification-notes.md`
- `review-notes.md`
- `package-manifest.md`

## Package Manifest

Every workflow package should include `package-manifest.md` with:

- Selected package option.
- Generated files and intended target paths.
- Assumptions and evidence sources.
- `TODO` / `TBD` fields.
- Files safe to write directly.
- Files requiring maintainer confirmation before use.

## Checklist

- [ ] Package option is selected.
- [ ] Root cause is proven or framed as suspected.
- [ ] Tests are evidenced or marked not run.
- [ ] No issue or PR is opened by default.
