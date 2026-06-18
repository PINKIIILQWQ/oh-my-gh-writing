# CHANGELOG Standard

## Use When

Use when writing version history for users who need to understand what changed across releases.

## Output Boundary

A CHANGELOG is release history, not a marketing announcement. It must be based on real versions, dates, PRs/issues, commits, release notes, or generated changelog output. Without evidence, do not write issue numbers, release dates, removal timelines, or migration links.

## Standard Structure

```markdown
## [Unreleased]

## [Version] - YYYY-MM-DD

### Added
- New capability.

### Changed
- Behavior, API, docs, or internal implementation change.

### Fixed
- Fixed issue.

### Removed
- Removed behavior and migration path.

### Deprecated
- Deprecated feature and timeline.

### Security
- Security fix or advisory link.
```

Keep only categories that have content. Do not output empty `Performance`, `Deprecation`, `Security`, or breaking-change sections.

## Missing Information

- If the date is missing, use `YYYY-MM-DD` or `TBD`; do not guess.
- If PR/issue numbers are missing, omit them; do not write `#123` placeholders.
- If the change type is uncertain, use `Changed` instead of forcing `Breaking` or `Security`.

## Automation Source Boundary

If the target repository uses Conventional Changelog, semantic-release, commit-and-tag-version, standard-version, or similar tools, treat generated changelog output as a factual source. You may improve wording or add a user-readable summary, but do not change generated version, tag, compare link, breaking-change, or commit-group meaning without evidence.

## Do Not Invent

- Do not invent bug numbers, contributors, migration links, deprecation timelines, removal versions, or security advisories.
- Do not copy release-note marketing tone into a changelog.
- Do not force reference-project category names onto the target project.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| Keep a Changelog | `[Unreleased]`, categories, version/date structure |
| Conventional Commits | Commit metadata and breaking-change semantics |
| Conventional Changelog | Generated changelog boundaries |
| npm CLI CHANGELOG | Real release-history discipline |
| ESLint / Node.js / React CHANGELOGs | Mature project examples |

## Checklist

- [ ] `[Unreleased]` or explicit version and date are present.
- [ ] Changes are grouped by useful categories.
- [ ] PR/issue references are included only when known.
- [ ] No bug number, migration link, timeline, or security advisory is invented.
