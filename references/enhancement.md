# Enhancement Standard

## Use When

Use when the user wants to improve existing behavior rather than add a wholly new capability.

## Output Boundary

Enhancements refine an existing feature. If the request introduces a new API, major workflow, or product surface, route to Feature Request. If the change is already implemented in a diff, route to the appropriate PR scenario.

## Standard Structure

1. **Current behavior:** what exists now and why it falls short.
2. **Desired improvement:** the specific refinement requested.
3. **Affected users / workflows:** who benefits and when.
4. **Examples:** before/after behavior, config, command, or UI copy when known.
5. **Risks / compatibility:** possible regressions, migration concerns, or backwards compatibility notes.
6. **Acceptance criteria:** observable outcomes or maintainers' decision points.

## Missing Information

- Use `TBD` for unknown versions, commands, config keys, or affected platforms.
- Ask a follow-up only if the current behavior cannot be distinguished from a new feature request.

## Do Not Invent

- Do not claim a fix or implementation exists.
- Do not invent benchmarks, compatibility commitments, config keys, or labels.
- Do not overstate impact when the user only described a local inconvenience.

## Good Output Shape

```markdown
## Current behavior
Search results reset whenever the filter panel is closed.

## Desired improvement
Preserve active filters while the user navigates within the search page.

## Acceptance criteria
- Existing filters remain selected after closing and reopening the panel.
```

## Common Failure

- Treating a wholly new API or workflow as a small enhancement.
- Claiming benchmark or UX improvements without evidence.
- Omitting the current behavior, which makes the improvement impossible to judge.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Issue Forms docs | Distinguishing request types |
| React and TypeScript templates | Current/expected behavior framing |
| Kubernetes issue templates | Scope and impact discipline |
| GitHub Community discussions | Separating discussion from implementation |

## Checklist

- [ ] Existing behavior is described.
- [ ] Requested improvement is specific.
- [ ] Affected workflow is named.
- [ ] Compatibility or regression risk is addressed when relevant.
- [ ] The request is not accidentally written as an implemented PR.
