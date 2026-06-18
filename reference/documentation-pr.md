# Documentation PR Standard

## Use When

Use when a branch, diff, or pull request changes documentation, examples, guides, comments intended as docs, README content, or documentation configuration without code behavior changes.

## Output Boundary

Documentation PRs should not be written like code PRs. If code behavior changes, route to the relevant PR scenario.

## Standard Structure

1. **Summary:** what documentation changed.
2. **Motivation:** missing, outdated, confusing, or newly required documentation.
3. **Changed docs:** files, sections, examples, screenshots, or navigation updates.
4. **Validation:** preview build, link check, spell check, manual review, or `Not run`.
5. **Related issue / context:** only real links or IDs.

## Missing Information

- If preview or docs build status is unknown, write `Docs validation: Not run (not provided)`.
- If affected docs pages are unknown, use `TBD` rather than inventing paths.

## Do Not Invent

- Do not invent docs build results, screenshots, links, issue IDs, or code behavior.
- Do not claim user-facing runtime behavior changed unless code changes prove it.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub PR docs | Review context |
| Node.js docs PRs | Clear docs-only summaries |
| TypeScript and React docs updates | Examples and compatibility notes |
| Google Engineering Practices | Reviewability |

## Checklist

- [ ] Docs-only scope is clear.
- [ ] Changed pages or sections are named.
- [ ] Validation is evidenced or marked not run.
- [ ] No code behavior is implied without evidence.
