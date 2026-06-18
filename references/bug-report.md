# Bug Report Standard

## Use When

Use for a reproducible defect where the user can describe expected behavior, actual behavior, environment, and reproduction steps.

## Output Boundary

Bug reports describe symptoms and reproduction evidence. Do not turn a bug report into a fix proposal, PR description, or root-cause conclusion unless the user provides proof.

## Standard Structure

1. **Summary:** one concise sentence naming the broken behavior and user impact.
2. **Environment:** product/package version, OS, browser/runtime, package manager, and relevant config when known.
3. **Steps to reproduce:** numbered, minimal, executable steps.
4. **Expected behavior:** what should happen.
5. **Actual behavior:** what happens instead, including exact error text or logs when provided.
6. **Impact:** severity, frequency, affected users, or workaround status.
7. **Additional context:** screenshots, logs, suspected cause, links, or related issues only when provided.

## Missing Information

- If a version, OS, browser, package manager, or reproduction step is missing, write `TBD` or ask only when it blocks reproducibility.
- If the root cause is unknown, write `Suspected cause` or omit root-cause language.
- If screenshots or logs are mentioned but not provided, write `Logs/screenshots: TBD`.

## Do Not Invent

- Do not invent versions, stack traces, repository paths, issue numbers, screenshots, logs, or root causes.
- Do not mark the bug as confirmed unless the user, repository, logs, or tool output proves it.
- Do not write fix implementation details unless the user asked for a PR or fix plan.

## Good Output Shape

```markdown
## Summary
Exporting a CSV from the reports page opens a blank screen instead of downloading the file.

## Steps to reproduce
1. Open Reports.
2. Click Export CSV.
3. Observe the blank page.
```

## Common Failure

- Writing "Root cause: CSV serializer crashes" without logs, diff, or user evidence.
- Omitting expected vs actual behavior.
- Filling version, browser, or OS fields with guesses.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Issue Forms docs | Required fields, dropdowns, validation boundaries |
| React issue templates | Environment and reproduction discipline |
| Kubernetes bug reports | Version, component, and reproduction context |
| TypeScript issue templates | Playground/reproduction links and expected/actual behavior |
| Node.js issue templates | Platform/runtime details and minimal repros |

## Checklist

- [ ] Summary names the defect and impact.
- [ ] Reproduction steps are numbered and concrete.
- [ ] Expected and actual behavior are distinct.
- [ ] Environment fields are present or marked `TBD`.
- [ ] Unknown root cause is not written as fact.
