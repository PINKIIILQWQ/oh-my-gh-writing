# Proposal to Implementation Workflow Pack

## Use When

Use when the user wants to turn an idea into discussion, design, issue, and implementation materials.

If the user asks only for an RFC, Discussion, Feature Request, or Feature PR, route to that single-artifact standard.

## Default Output Location

Write local drafts under `.github-writing/proposal-to-implementation/<version-or-date>/`. If no version/date is known, use `.github-writing/proposal-to-implementation/TBD/`.

Do not open discussions, issues, or PRs unless explicitly requested.

## Required Package Question

Ask this before drafting unless the user already chose:

```text
Which proposal package should I prepare?

A. Proposal pack (Recommended): Discussion + RFC + Feature Request.
B. Implementation pack: RFC + Feature PR.
C. Full lifecycle pack: Discussion + RFC + Feature Request + Feature PR.

Add any supplements in the same reply: target audience, current constraints, preferred solution, alternatives, implementation status, compatibility concerns, or decision deadline.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Proposal pack | `discussion.md`, `rfc.md`, `feature-request.md` |
| Implementation pack | `rfc.md`, `feature-pr.md` |
| Full lifecycle pack | `discussion.md`, `rfc.md`, `feature-request.md`, `feature-pr.md` |

## Evidence Rules

- Keep undecided ideas as questions, alternatives, or open issues.
- Do not write implementation status unless a diff, branch, or user statement proves it.
- Compatibility, rollout, and migration claims require evidence.

## Suggested File Names

- `discussion.md`
- `rfc.md`
- `feature-request.md`
- `feature-pr.md`
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
- [ ] Discussion does not decide the solution prematurely.
- [ ] RFC exposes alternatives and open questions.
- [ ] Feature PR appears only when implementation exists or user asked for a draft.
