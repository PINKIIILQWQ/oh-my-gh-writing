# Version Release Workflow Pack

## Use When

Use when the user asks for release materials, software update content, version launch docs, major release communication, or a release pack.

If the user explicitly asks for one artifact only, such as "write release notes" or "update CHANGELOG", route to that single-artifact standard instead.

## Default Output Location

Write local drafts under `.github-writing/version-release/<version-or-date>/`. If version/date is unknown, use `.github-writing/version-release/TBD/`.

Do not publish releases, create GitHub releases, push tags, open PRs, or modify remote state unless explicitly requested.

## Required Package Question

Ask this before drafting unless the user already chose:

```text
Which release package should I prepare?

A. Standard release pack (Recommended): CHANGELOG + Release Notes; add Migration Guide only if breaking or upgrade changes exist.
B. Major/breaking release pack: CHANGELOG + Release Notes + Migration Guide + breaking-change summary.
C. GitHub release draft only: Release Notes + tag/compare placeholders.

Add any supplements in the same reply: version, release date, previous version, target branch, known breaking changes, compare URL, changelog source, audience, or files to update.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Standard release pack | `changelog.md`, `release-notes.md`; `migration-guide.md` only when breaking/upgrade changes exist |
| Major/breaking release pack | `changelog.md`, `release-notes.md`, `migration-guide.md` |
| GitHub release draft only | `release-notes.md` |

Read `shared-principles.md` because release materials are fact-heavy.

## Evidence Rules

- Version, date, tag, compare URL, release URL, contributors, breaking changes, migration commands, and compatibility ranges require evidence.
- Generated changelog or release-drafter output is a source; preserve generated version/tag/compare semantics.
- Unknown facts become `TBD` or `To confirm`.

## Suggested File Names

- `CHANGELOG.md` or `CHANGELOG.patch.md`
- `RELEASE_NOTES.md`
- `MIGRATION.md`
- `release-draft.md`
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
- [ ] Output path is local `.github-writing/...` unless user requested otherwise.
- [ ] Only selected artifact references are loaded.
- [ ] No publishing, tagging, or PR creation is implied by default.
