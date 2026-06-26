# Release Notes Standard

## Use When

Use when writing a release announcement for users, developers, or maintainers.

## Output Boundary

Release Notes are reader-facing release communication. Version, date, release URL, contributors, screenshots, GIFs, migration commands, and Full Changelog links must come from a real release, tag, compare URL, repository files, tool output, or user input.

## Standard Structure

For patch or minor releases:

1. **Version:** version and date; use `TBD` when unknown.
2. **Highlights:** 1-3 changes users most need to know.
3. **Fixes / Changes:** only evidenced fixes or changes.
4. **Upgrade notes:** only when needed.
5. **Full changelog:** only when a real release, tag, or compare URL exists.

For major releases:

1. **Version heading:** version and date.
2. **Summary:** 1-2 sentences describing release value.
3. **New features:** each feature includes name, impact, and usage when known.
4. **Breaking changes:** impact and migration path.
5. **Upgrade guide:** steps required to move from the previous version.
6. **Full Changelog:** only with a real release, compare URL, or known repository range.

## Missing Information

- If version or date is missing, write `TBD`; do not guess.
- If no real compare URL exists, omit Full Changelog.
- If no image assets exist, omit screenshots/GIFs.

## Automation Source Boundary

If release notes come from Conventional Changelog, semantic-release, commit-and-tag-version, or an existing GitHub Release draft, preserve generated version, tag, compare URL, breaking-change groups, and commit range. You may add human highlights, but do not write unevidenced commit impact as release fact.

If the target repository uses GitHub automatically generated release notes, inspect `.github/release.yml` when available. Preserve evidenced category rules, excluded labels, excluded authors, contributor lists, and Full Changelog links from the generated draft or configuration. Do not invent contributors, compare ranges, excluded labels, or generated categories.

## Do Not Invent

- Do not invent release URLs, contributors, migration commands, built-in plugin lists, screenshots/GIFs, platform support, or benchmarks.
- Do not rewrite changelog entries into unsupported promotional claims.

## Good Output Shape

```markdown
## v1.2.0 - TBD

### Highlights
- Adds CSV export for reports.

### Fixes
- Fixes login redirect loops after session expiry.
```

## Common Failure

- Adding a release date, compare URL, or contributor list without evidence.
- Turning internal changelog bullets into marketing claims.
- Adding migration steps for a release with no breaking-change evidence.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Releases docs | Release publishing model and release notes |
| GitHub generated release notes docs | `.github/release.yml` categories, exclusions, contributors, and Full Changelog boundaries |
| Conventional Changelog | Generated release boundaries |
| Astro 5.0 release | Major-release framing |
| npm CLI v11 release | CLI release communication |
| Svelte 5 / Buf / Deno releases | Highlights, breaking changes, upgrade notes |

## Checklist

- [ ] Version and date are present or marked `TBD`.
- [ ] Highlights or feature list is present.
- [ ] Breaking changes or upgrade notes appear when relevant.
- [ ] Full Changelog link appears only when known.
- [ ] No migration command, release URL, screenshot, contributor, platform claim, or benchmark is invented.
