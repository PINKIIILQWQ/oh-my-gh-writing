# Contribution Setup Workflow Pack

## Use When

Use when the user wants a project ready for outside contributors, issue intake, PR review, or community contribution flow.

If the user asks only for `CONTRIBUTING.md`, route to `contributing.md`.

## Default Output Location

Write local drafts under `.github-writing/contribution-setup/<version-or-date>/`. If no version/date is known, use `.github-writing/contribution-setup/TBD/`.

Do not create GitHub labels, settings, PRs, or repository files unless explicitly requested.

## Decision Rule

If the user asks to accept outside contributors and no existing process is known, default to Community intake pack. If setup/test commands or governance are unknown, mark them `TBD` instead of inventing.

## Required Package Question

Ask this before drafting unless the user already chose:

```text
Which contribution setup package should I prepare?

A. Community intake pack (Recommended): CONTRIBUTING + Issue Forms + PR Template + README contribution entry.
B. Internal workflow pack: PR Template + review checklist + slim CONTRIBUTING.
C. First-time contributor pack: CONTRIBUTING + friendly issue templates + support/contact notes.

Add any supplements in the same reply: accepted contribution types, setup/test commands, code of conduct, security reporting path, maintainer review rules, labels, or contributor audience.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Community intake pack | `contributing.md`, `issue-form-yaml.md`, `pr-template.md`, `readme.md` |
| Internal workflow pack | `pr-template.md`, `code-review.md`, `contributing.md` |
| First-time contributor pack | `contributing.md`, `issue-form-yaml.md`, `pr-template.md` |

## Evidence Rules

- Setup commands, test commands, code owner rules, release permissions, security reporting, and governance require repository evidence or user input.
- Unknown optional workflow details should be omitted rather than turned into requirements.

## Suggested File Names

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/pull_request_template.md`
- `README-contributing-entry.md`
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
- [ ] Commands and governance are evidenced or marked `TBD`.
- [ ] Templates do not contain fake labels or required fields.
- [ ] Default output remains local draft files.
