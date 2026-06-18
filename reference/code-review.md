# Code Review Standard

## Use When

Use when the user asks to review a pull request, diff, patch, commit range, or code changes.

## Output Boundary

Code review output prioritizes actionable findings. Lead with bugs, regressions, security risks, data-loss risks, and missing tests. Summaries are secondary. If no issues are found, say so clearly and mention residual risk or test gaps.

## Standard Structure

1. **Findings:** ordered by severity, each grounded in file/line references when available.
2. **Open questions / assumptions:** only when they affect correctness or review confidence.
3. **Change summary:** brief context after findings, not before.
4. **Test gaps:** missing or unverified tests that matter.

## Finding Format

Each finding should include:

- Severity: `Blocking`, `Major`, `Minor`, or `Nit`.
- Location: file path and line or tight range when available.
- Problem: what can go wrong.
- Reason: why the current code causes it.
- Suggested fix: concrete next action.

## Missing Information

- If no diff is available, ask for the diff or PR link.
- If line numbers are unavailable, cite function, file, or snippet context.
- If behavior cannot be confirmed, state the assumption.

## Do Not Invent

- Do not invent line numbers, tests, CI status, issue IDs, or project conventions.
- Do not provide broad style commentary unless it affects correctness, maintainability, or requested scope.
- Do not bury blocking findings under a long summary.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| Google Engineering Practices | Severity, clarity, and actionable review comments |
| GitHub PR review docs | Review flow and discussion context |
| Kubernetes and React review culture | Specific, scoped, evidence-backed comments |

## Checklist

- [ ] Findings come before summary.
- [ ] Findings are ordered by severity.
- [ ] Each finding has evidence and an actionable fix.
- [ ] No line numbers or tests are invented.
