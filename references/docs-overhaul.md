# Docs Overhaul Workflow Pack

## Use When

Use when the user wants a broad documentation refresh, docs rewrite, homepage refresh, documentation launch, or coordinated docs PR package.

If the user asks only for README or Documentation PR, route to that single-artifact standard.

## Default Output Location

Write local drafts under `.github-writing/docs-overhaul/<version-or-date>/`. If no version/date is known, use `.github-writing/docs-overhaul/TBD/`.

Do not push docs, open PRs, or publish docs sites unless explicitly requested.

## Decision Rule

If docs changes are release-facing, include a changelog docs entry. If the user only wants a repository README homepage refresh, route to Repository homepage refresh and do not create a full docs launch.

## Required Package Question

Ask this when the Decision Rule cannot safely choose a package option:

```text
Which docs overhaul package should I prepare?

A. Docs PR pack (Recommended): Documentation PR + README updates + changelog docs entry if release-facing.
B. Repository homepage refresh: README + file index + contribution/docs entry.
C. Full docs launch: README + CONTRIBUTING docs + Documentation PR + release/changelog notes only when confirmed.

Add any supplements in the same reply: target audience, docs site URL, outdated sections, new file index, screenshots, release impact, language requirements, or style preference.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Docs PR pack | `documentation-pr.md`, `readme.md`; `changelog.md` only when release-facing |
| Repository homepage refresh | `readme.md`, `contributing.md` when contribution/docs entry is needed |
| Full docs launch | `readme.md`, `contributing.md`, `documentation-pr.md`; `release-notes.md` or `changelog.md` only with release impact |

Read `weapons.md` when file indexes, badges, diagrams, or visual tables are needed.

## Evidence Rules

- Do not invent docs site URLs, screenshots, generated docs commands, link-check results, or release impact.
- Match existing docs style when editing an existing docs set.

## Suggested File Names

- `README.md`
- `documentation-pr.md`
- `docs-overhaul-plan.md`
- `changelog-docs-entry.md`
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
- [ ] README applicability scope is included when README is selected.
- [ ] Docs validation is evidenced or marked not run.
- [ ] No docs publishing or PR action is performed by default.
