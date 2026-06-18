# Refactor PR Standard

## Use When

Use when a branch, diff, or pull request reorganizes, renames, splits, simplifies, or cleans up code without intended behavior changes.

## Output Boundary

Refactor PRs must make the no-behavior-change claim explicit and honest. If behavior changes, route to Feature PR or Bug Fix PR.

## Standard Structure

1. **Summary:** what was reorganized or simplified.
2. **Motivation:** maintainability, readability, ownership, performance-neutral cleanup, or preparation for future work.
3. **Behavior impact:** state whether behavior is intended to remain unchanged.
4. **Changes:** moved files, renamed APIs, split modules, removed dead code, or internal boundaries.
5. **Testing:** commands, CI, manual verification, or `Not run`.
6. **Risk:** affected area and review focus.

## Missing Information

- If behavior impact is uncertain, write `Behavior impact: To confirm`.
- If tests are missing, write `Tests: Not run (not provided)`.

## Do Not Invent

- Do not claim no behavior change if the diff suggests otherwise.
- Do not invent tests, benchmarks, file paths, issue IDs, or migration notes.
- Do not frame a feature or bug fix as a refactor.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| Google Engineering Practices | Reviewable refactor boundaries |
| React and TypeScript PRs | Behavior-preserving cleanup summaries |
| Kubernetes PR templates | Risk and release-note discipline |

## Checklist

- [ ] Behavior impact is explicit.
- [ ] Review focus is clear.
- [ ] Tests are evidenced or marked not run.
- [ ] Feature or bug-fix behavior is not hidden as refactor.
