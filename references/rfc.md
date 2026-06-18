# RFC Standard

## Use When

Use when proposing a design, architecture change, protocol, API, major behavior, governance change, or long-lived technical decision.

## Output Boundary

RFCs explore and justify a proposal. Do not write final implementation claims, accepted status, owners, dates, or compatibility promises unless provided.

## Standard Structure

1. **Summary:** concise proposal and intended outcome.
2. **Motivation:** problem, users, constraints, and why now.
3. **Goals / non-goals:** explicit boundaries.
4. **Proposal:** design, API, architecture, workflow, or policy.
5. **Alternatives:** considered options and tradeoffs.
6. **Compatibility / migration:** risks, rollout, deprecation, or upgrade impact when known.
7. **Open questions:** decisions still needed.

## Missing Information

- If the proposal is vague, ask for scope only when it changes the RFC shape.
- If compatibility or rollout is unknown, write `To confirm`.

## Do Not Invent

- Do not invent accepted status, timelines, owners, benchmarks, migrations, or deprecation dates.
- Do not hide unresolved decisions.
- Do not turn an RFC into a PR description unless the user asks.

## Good Output Shape

```markdown
## Summary
Introduce a project-level configuration file for shared CLI defaults.

## Alternatives
- Keep command-line flags only.
- Use environment variables.

## Open questions
- Which settings are safe to persist in the repository?
```

## Common Failure

- Writing open questions as accepted decisions.
- Inventing owners, deadlines, benchmark results, or migration dates.
- Describing implementation status when no diff or accepted design exists.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| Rust RFCs | Motivation, design, drawbacks, alternatives |
| Kubernetes enhancement proposals | Scope, graduation, compatibility |
| TypeScript design notes | API design and compatibility tradeoffs |
| React RFCs | Motivation and alternatives |

## Checklist

- [ ] Goals and non-goals are explicit.
- [ ] Alternatives and tradeoffs are included.
- [ ] Compatibility and migration are addressed when relevant.
- [ ] Open questions remain visible.
