# 12 CONTRIBUTING 测试

# Contributing to MUI

Thank you for helping improve MUI. This guide summarizes the contribution workflow for the `mui/material-ui` monorepo.

## Code of Conduct

Please follow the MUI Code of Conduct linked from the repository's existing contribution materials.

## Before You Start

- Search existing issues before opening a new one.
- For large changes, open an issue first so maintainers can confirm the direction.
- Keep pull requests focused on one bug fix, feature, or documentation change.
- Check whether someone else is already working on the issue before starting.

## Local Setup

MUI uses pnpm. The repository's `package.json` specifies:

- Node.js: `>=22.18.0`
- pnpm: `10.33.4`

```bash
git clone https://github.com/mui/material-ui.git
cd material-ui
pnpm install
```

Start the documentation development environment:

```bash
pnpm start
```

The existing contribution guide states that the documentation site is available locally at:

```text
http://localhost:3000
```

## Branch and PR Workflow

1. Fork the repository.
2. Clone your fork and add the upstream remote.
3. Sync your local `master` branch with upstream `master`.
4. Create a topic branch.
5. Make a focused change.
6. Push your branch and open a pull request.

```bash
git checkout master
git pull upstream master
git checkout -b my-topic-branch
git push -u origin HEAD
```

## Development Commands

Use only the commands that match the files you changed.

```bash
pnpm prettier
pnpm eslint
pnpm typescript
pnpm test:unit
pnpm test:browser
pnpm test:regressions
pnpm docs:api
pnpm docs:typescript:formatted
```

The repository also defines:

```bash
pnpm test
pnpm test:coverage
pnpm test:e2e
pnpm docs:build
```

## Pull Request Checklist

- [ ] The PR targets the correct branch.
- [ ] The change is focused and does not bundle unrelated work.
- [ ] Tests were added or updated when behavior changed.
- [ ] TypeScript declarations were updated when props or public types changed.
- [ ] API documentation was regenerated when API surfaces changed.
- [ ] Demos were updated when user-facing component behavior changed.
- [ ] Formatting and linting commands relevant to the change were run.

## Documentation Contributions

Documentation improvements are welcome. For docs changes:

- Keep examples small and runnable.
- Prefer examples that show real component usage.
- Run the documentation site locally when changing examples or demos.
- Run docs-related checks when API docs or TypeScript demos change.

## CI

The repository contains GitHub workflows including `ci.yml`, `ci-check.yml`, `codeql.yml`, `publish.yml`, and `publish-canaries.yml`.

Do not assume a PR is ready just because it works locally. Wait for the repository CI checks to finish and address any failures.

## Unknowns

- TODO: Add repository-specific release permissions if maintainers want external contributors to understand the release process.
- TODO: Add coverage expectations only if the project documents a required threshold.
