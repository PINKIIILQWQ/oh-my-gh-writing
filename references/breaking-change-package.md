# Breaking Change Package Workflow Pack

## Use When

Use when the user wants to communicate, design, implement, or release a breaking change.

If the user asks only for a migration guide or release notes, route to that single-artifact standard.

## Default Output Location

Write local drafts under `.github-writing/breaking-change-package/<version-or-date>/`. If no version/date is known, use `.github-writing/breaking-change-package/TBD/`.

Do not publish, tag, open PRs, or modify remote state unless explicitly requested.

## Decision Rule

If breaking-change intent is not confirmed, ask before creating Migration Guide or major-release claims. Default to Pre-implementation pack when design is still under discussion.

## Required Package Question

Ask this when the Decision Rule cannot safely choose a package option:

```text
Which breaking-change package should I prepare?

A. Major release pack (Recommended): RFC + Migration Guide + CHANGELOG + Release Notes.
B. Pre-implementation pack: RFC + Feature/Refactor PR notes.
C. Release-only pack: Migration Guide + CHANGELOG + Release Notes.

Add any supplements in the same reply: old behavior, new behavior, affected users, deprecation timeline, migration commands, compatibility window, rollback path, or target release.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Major release pack | `rfc.md`, `migration-guide.md`, `changelog.md`, `release-notes.md` |
| Pre-implementation pack | `rfc.md`; add `migration-guide.md` only when breaking intent is confirmed; add `feature-pr.md` or `refactor-pr.md` only when a branch, diff, or explicit PR draft request exists |
| Release-only pack | `migration-guide.md`, `changelog.md`, `release-notes.md` |

Read `shared-principles.md` because breaking-change facts are high risk.

## Evidence Rules

- Breaking-change status, affected versions, timelines, migration steps, rollback, and compatibility windows require evidence.
- If breaking-change intent is unclear, ask before adding `!`, `BREAKING CHANGE`, or major-release claims.

## Suggested File Names

- `rfc.md`
- `migration-guide.md`
- `changelog-entry.md`
- `release-notes.md`
- `breaking-change-summary.md`
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
- [ ] Breaking-change facts are evidenced.
- [ ] Migration path is concrete or marked `To confirm`.
- [ ] No release or tag action is performed by default.
