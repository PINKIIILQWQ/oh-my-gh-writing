# Bug Fix PR Standard

## Use When

Use when a branch, diff, or pull request fixes a defect, regression, crash, incorrect output, broken workflow, or security/privacy issue.

## Output Boundary

Bug Fix PRs explain the defect, root cause when known, the fix, and verification. Do not invent the root cause or test status. If no implementation exists, route to Bug Report.

## Standard Structure

1. **Summary:** what bug was fixed and user impact.
2. **Root cause:** only if proven by code, logs, diff, or user input.
3. **Fix:** what changed and why it addresses the problem.
4. **Regression risk:** affected area, compatibility, or edge cases.
5. **Testing:** exact commands, CI, manual verification, or `Not run`.
6. **Linked issue:** only if known.

## Missing Information

- If root cause is uncertain, write `Suspected cause` or omit it.
- If tests are not provided, write `Tests: Not run (not provided)`.
- If affected versions are unknown, write `Affected versions: TBD` only when important.

## Do Not Invent

- Do not invent root causes, issue IDs, test results, CI status, screenshots, benchmark changes, or release-note labels.
- Do not claim a regression is fixed without implementation evidence.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub PR docs | Reviewable change summary |
| Kubernetes PR templates | Release-note and bug-fix boundaries |
| React and Node.js PRs | Fix explanation and tests |
| Google Engineering Practices | Reviewable bug-fix reasoning |

## Checklist

- [ ] Fixed bug and impact are clear.
- [ ] Root cause is proven or framed as suspected.
- [ ] Fix explanation maps to the bug.
- [ ] Tests are evidenced or marked not run.
