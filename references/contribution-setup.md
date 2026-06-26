# Contribution Setup Workflow Pack

## Use When

Use when the user wants a project ready for outside contributors, issue intake, PR review, or community contribution flow.

If the user asks only for `CONTRIBUTING.md`, route to `contributing.md`.

If the user asks only to check what contributor files are missing or whether the repository is ready for outside contributions, produce an audit report only. Do not create `.github/`, root repository files, or `.github-writing/` drafts unless the user explicitly asks to draft, create, write, apply, or update the files.

## Default Output Location

Write local drafts under `.github-writing/contribution-setup/<version-or-date>/`. If no version/date is known, use `.github-writing/contribution-setup/TBD/`.

Do not create GitHub labels, settings, PRs, or repository files unless explicitly requested.
Do not write target files during audit-only requests.

## Decision Rule

If the user asks to accept outside contributors and no existing process is known, default to Community intake pack. If setup/test commands or governance are unknown, mark them `TBD` instead of inventing.

For audit-only requests, do not select a package or ask the package-selection question. Report existing files, missing recommended files, optional files, and why each recommendation matters.

## Required Package Question

Ask this when the Decision Rule cannot safely choose a package option:

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

## Optional Contribution Infrastructure

Recommend but do not generate these by default:

- `SUPPORT.md` when the project has real support channels that should be shown before issue creation.
- `SECURITY.md` when private vulnerability reporting is supported.
- `CODEOWNERS` when review ownership is shared and owners have write access.
- `.github/DISCUSSION_TEMPLATE/*.yml` when Discussions are enabled and the user wants structured idea, question, or announcement intake.
- `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, or `AGENTS.md` when AI agents are expected to contribute and repository-specific build/test guidance is known.

## Evidence Rules

- Setup commands, test commands, code owner rules, release permissions, support channels, security reporting, AI-agent instructions, discussion category slugs, and governance require repository evidence or user input.
- Unknown optional workflow details should be omitted rather than turned into requirements.

## Suggested File Names

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/DISCUSSION_TEMPLATE/*.yml` only when Discussions categories are known
- `.github/pull_request_template.md`
- `SUPPORT.md`, `SECURITY.md`, `CODEOWNERS`, or AI instruction files only when requested or evidenced
- `README-contributing-entry.md`
- `package-manifest.md`

## Package Manifest

Every workflow package should include `package-manifest.md` with:

- Selected package option.
- Generator: `oh-my-gh-writing` version from `VERSION`.
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
- [ ] Audit-only requests do not create files or package drafts.
