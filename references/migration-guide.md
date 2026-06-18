# Migration Guide Standard

## Use When

Use when guiding users from an old API, configuration, behavior, dependency, or release to a new one.

## Output Boundary

Migration Guides only describe real upgrade paths. Environment variables, codemods, GA dates, shutdown dates, compatibility periods, rollback paths, and support matrices must come from user input, repository files, release notes, official docs, or tool output.

## Standard Structure

Required sections:

1. **Who needs this:** affected and unaffected users.
2. **Before / After:** old usage and new usage using code, config, commands, or behavior descriptions.
3. **Step-by-step migration:** ordered, executable steps.
4. **Known breaking changes:** only confirmed incompatibilities.

Conditional sections:

5. **Codemod / automation:** only when a real tool or command exists.
6. **Rollback:** only when a rollback path is provided; otherwise `Rollback: To confirm`.
7. **Deprecation timeline:** only with evidence for versions, dates, or support windows.
8. **Compatibility matrix:** only when platform, version, or dependency ranges are known.

## Missing Information

- If old/new API mapping is missing, add a `To confirm` mapping table.
- If no automation exists, omit codemod sections.
- If rollback is unknown, write `Rollback: To confirm`.

## Do Not Invent

- Do not invent environment variables, commands, compatibility periods, shutdown dates, migration tools, data migration steps, or supported platforms.
- Do not treat release notes as a full migration guide unless they actually contain migration steps.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitLab update docs | Operational upgrade path |
| pandas whatsnew | Versioned migration notes |
| React 19 Upgrade Guide | API migration explanation |
| Vue 3 Migration Guide | Before/after migration details |
| Django upgrade docs | Stepwise upgrade process |

## Checklist

- [ ] Migration steps are ordered.
- [ ] Old and new usage are clearly mapped.
- [ ] Breaking changes are evidenced.
- [ ] Rollback, codemod, timeline, and compatibility matrix appear only with evidence.
