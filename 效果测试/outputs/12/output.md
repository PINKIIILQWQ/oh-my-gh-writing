# Contributing to Component Library

First off, thanks for taking the time to contribute! 🎉

## Code of Conduct
This project follows a Code of Conduct. Please read it before contributing.

## Getting Started
### Prerequisites
- Node.js 18+
- npm 9+

### Setup
```bash
git clone https://github.com/your-org/component-lib.git
cd component-lib
npm install
npm run dev    # Storybook dev server at http://localhost:6006
```

## Development Workflow
### Branch naming
- `feat/button-variant` — new feature
- `fix/modal-focus-trap` — bug fix
- `docs/contributing-guide` — documentation

### Code style
- TypeScript strict mode
- ESLint (flat config) + Prettier
- Run `npm run format` before committing

### Testing
- Vitest for unit tests
- Playwright for e2e tests in Storybook
- Aim for 80%+ coverage on new code

## Pull Request Checklist
- [ ] Code follows style guidelines
- [ ] Tests added for new functionality
- [ ] TypeScript types added/updated
- [ ] Storybook story added (for components)
- [ ] `npm run check` passes (lint + typecheck + test)
- [ ] Documentation updated (if API changes)

## Release Process
Maintainers merge PRs → `semantic-release` publishes npm package.
Commit messages determine version bumps (feat → minor, fix → patch).
