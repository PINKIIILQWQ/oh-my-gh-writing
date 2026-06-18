# CONTRIBUTING Standard

## Use When

Use when creating or revising contribution guidelines for a repository.

## Output Boundary

CONTRIBUTING files describe how people should contribute to the target project. Commands, package managers, test suites, CI, release permissions, support channels, and governance rules must come from repository files, user input, or official project docs.

## Standard Structure

1. **Welcome / scope:** what contributions are accepted.
2. **Before opening an issue or PR:** search existing issues, discuss large changes, security/private reporting boundary.
3. **Development setup:** install, build, test, and local run commands only when known.
4. **Branch / commit / PR expectations:** commit style, PR description, screenshots, docs, tests.
5. **Review process:** maintainer review, requested changes, merge expectations.
6. **Code of conduct / license:** links only when files exist or user requests them.

## Missing Information

- If setup commands are unknown, write `Development setup: TBD` or omit the section.
- If security reporting is unknown, avoid inventing an email or private process.
- If the project is private/internal, keep the contribution section slim.

## Do Not Invent

- Do not invent Node/npm/pnpm versions, test commands, devcontainers, Storybook, Playwright, semantic-release, coverage thresholds, release permissions, security contacts, or governance.
- Do not require a code of conduct unless it exists or the user asks for one.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub contributing docs | Public contribution flow |
| React CONTRIBUTING | Project-specific workflow and tests |
| Kubernetes contributor guide | Large-project review and ownership boundaries |
| Node.js contribution docs | Setup, tests, and governance discipline |
| Tailwind CSS contributing docs | Focused contribution expectations |

## Checklist

- [ ] Contribution scope is clear.
- [ ] Setup/test commands are evidenced or marked `TBD`.
- [ ] Issue/PR expectations are actionable.
- [ ] No non-existent governance, CI, or release process is invented.
