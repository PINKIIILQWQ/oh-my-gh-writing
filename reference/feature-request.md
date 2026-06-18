# Feature Request Standard

## Use When

Use when the user wants future support for a new capability, API, integration, command, workflow, or user-facing behavior and no implemented diff exists.

## Output Boundary

Feature requests describe the desired future state. Do not write as if the feature has already shipped. Do not include PR testing claims or implementation status unless provided.

## Standard Structure

1. **Problem / Motivation:** what limitation or user pain exists today.
2. **Proposed solution:** the requested capability and expected behavior.
3. **Use cases:** 2-3 concrete examples with input, action, and expected outcome.
4. **Alternatives considered:** existing workaround, different API, or reason current behavior is insufficient.
5. **Compatibility / impact:** affected users, API surface, migration risk, or rollout notes when known.
6. **Open questions:** decisions that require maintainer input.

## Missing Information

- If the target API, command, package, or UI surface is unknown, write `TBD`.
- If the user only describes a broad idea, ask for scope only when it changes the artifact structure.
- If use cases are missing, include a small `Use cases to confirm` list.

## Do Not Invent

- Do not claim the feature is implemented.
- Do not invent performance numbers, roadmap dates, labels, owners, issue numbers, or compatibility commitments.
- Do not prescribe one implementation as final when the request is still exploratory.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Issue Forms docs | Structured request fields |
| Angular feature requests | Motivation, use case, alternatives |
| React issue templates | Reproducible user stories and constraints |
| TypeScript suggestions | Proposal, examples, compatibility |
| Kubernetes enhancements | Motivation, scope, open questions |

## Checklist

- [ ] Motivation is clear.
- [ ] Proposed behavior is concrete.
- [ ] Use cases are included.
- [ ] Alternatives or current workaround are stated.
- [ ] Open questions are not hidden as assumptions.
