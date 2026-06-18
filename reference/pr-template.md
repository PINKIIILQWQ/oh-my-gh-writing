# PR Template Standard

## Use When

Use when creating or revising a GitHub Pull Request template such as `.github/PULL_REQUEST_TEMPLATE.md` or `.github/pull_request_template.md`.

## Output Boundary

PR templates guide future contributors. They should be broadly usable, concise, and not tied to fictional CI, release, label, or cherry-pick workflows.

## Standard Structure

Common sections:

1. **Summary:** what changed and why.
2. **Type of change:** feature, fix, docs, refactor, test, chore.
3. **Testing:** commands, CI, manual checks, or not run.
4. **Screenshots / recordings:** only for UI changes.
5. **Checklist:** docs, tests, breaking changes, linked issues.
6. **Related issues:** `Fixes #...` as an empty prompt, not prefilled.

Recommended template style:

```markdown
## Summary

## Type of change
- [ ] Feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Refactor

## Testing
- [ ] Not run
- [ ] Manual test
- [ ] Automated tests

## Checklist
- [ ] I have updated docs where needed.
- [ ] I have added or updated tests where needed.
- [ ] I have noted any breaking changes.
```

## Missing Information

- If the repository has no known test command, ask contributors to describe testing rather than listing a command.
- If release-note automation is unknown, provide a blank area or comment, not a fixed rule.

## Do Not Invent

- Do not write project-specific test commands, release processes, labels, cherry-pick flows, or automatic release-note formats unless evidenced.
- Do not pre-check boxes.
- Do not make every optional item required.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub PR template docs | File placement and template behavior |
| Kubernetes PR template | Release-note and test checklist boundaries |
| React / TypeScript PR templates | Concise contributor prompts |

## Checklist

- [ ] Template is concise.
- [ ] Checkboxes are unchecked.
- [ ] No non-existent test, release, label, or cherry-pick process is invented.
- [ ] It can be pasted directly into a PR template file.
