# Discussion Standard

## Use When

Use for open-ended community input, proposal exploration, tradeoff discussion, or decision gathering where the solution is not settled.

## Output Boundary

Discussions invite input. Do not make final decisions, assign owners, promise timelines, or write as a PR/issue unless the user requests that artifact.

## Standard Structure

1. **Topic:** short statement of the question or decision area.
2. **Context:** why this discussion is being opened now.
3. **Options / tradeoffs:** known approaches and their pros/cons.
4. **Questions for maintainers/community:** focused prompts for feedback.
5. **Constraints:** compatibility, maintenance, security, UX, or ecosystem limits when known.
6. **Next step:** what decision or follow-up artifact may happen after discussion.

## Missing Information

- If options are unknown, ask for user intent only when it changes the discussion shape.
- If constraints are uncertain, mark them as `To confirm`.

## Do Not Invent

- Do not write the final solution as decided.
- Do not claim consensus, votes, maintainer approval, roadmap status, or implementation dates.
- Do not turn a discussion into a release announcement or PR description.

## Good Output Shape

```markdown
## Topic
Should the CLI support a project-level configuration file?

## Options
- Keep command-line flags only.
- Add a local config file.

## Questions
- Which options need to be shareable across a team?
```

## Common Failure

- Deciding for the community before feedback exists.
- Promising roadmap timing or maintainer ownership.
- Converting an exploratory discussion into a feature request or PR.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Discussions docs | Open-ended community flow |
| Kubernetes enhancement process | Problem framing and tradeoffs |
| Rust RFC discussions | Decision records and alternatives |
| TypeScript design discussions | Questions and compatibility constraints |

## Checklist

- [ ] The topic is a question or decision area.
- [ ] Options and tradeoffs are separated from conclusions.
- [ ] Feedback questions are explicit.
- [ ] No undecided point is written as final.
