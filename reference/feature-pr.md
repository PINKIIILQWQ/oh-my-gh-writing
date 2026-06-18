# Feature PR Standard

## Use When

Use when a branch, diff, or pull request implements a new capability, API, command, integration, UI, or user-facing behavior.

## Output Boundary

Feature PR descriptions explain what changed, why, and how it was verified. Do not write a future feature request when an implementation already exists. Do not claim tests passed unless the user, diff, CI, or tool output proves it.

## Standard Structure

1. **Summary:** 1-3 bullets describing the new capability.
2. **Motivation:** why the change is needed.
3. **Changes:** user-facing behavior, API/config changes, docs, and internal changes as separate bullets when useful.
4. **Testing:** commands, CI, manual checks, or `Not run` with reason.
5. **Screenshots / demos:** only when provided or generated.
6. **Compatibility / migration:** breaking changes, defaults, flags, or rollout notes when relevant.
7. **Linked issues:** only real issue links or IDs.

## Missing Information

- If no diff is available, ask for implementation details or route to Feature Request.
- If tests are unknown, write `Tests: Not run (not provided)` or `TBD`.
- If screenshots are expected but unavailable, omit the section or write `Screenshots: TBD`.

## Do Not Invent

- Do not invent issue IDs, test results, CI status, screenshots, benchmarks, file paths, or release notes.
- Do not mark checklist items as completed without evidence.
- Do not describe unimplemented future work as shipped behavior.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub pull request docs | PR purpose and review context |
| React PR style | Summary and test discipline |
| Kubernetes PR templates | Release note and compatibility boundaries |
| TypeScript PRs | API and behavior explanations |
| Tailwind CSS PRs | User-facing change summaries |

## Checklist

- [ ] Summary describes implemented behavior.
- [ ] Testing claims have evidence or are marked not run.
- [ ] Compatibility and migration risk are addressed when relevant.
- [ ] Linked issues are real or omitted.
