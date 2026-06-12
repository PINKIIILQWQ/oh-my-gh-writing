---
scenario: CONTRIBUTING
mode: concise
case-sources: https://github.com/psf/black, https://github.com/python/mypy
input-prompt: ../../prompts/12-contributing.md
---

# Contributing to [Component Library]

Welcome! We appreciate your interest in contributing.

## Quick Start
```bash
git clone https://github.com/your-org/component-lib.git
cd component-lib
npm install
npm run dev
```

## Development
- **Components**: `src/components/` (React + TypeScript)
- **Tests**: `npm run test` (Vitest)
- **Lint**: `npm run lint` (ESLint + Prettier)
- **Type check**: `npm run typecheck` (tsc --noEmit)

## Pull Request Process
1. Create a feature branch from `main`
2. Add tests for new components
3. Run `npm run check` (lint + typecheck + test)
4. Open PR against `main`
5. Request review from at least one maintainer

## Commit Convention
`<type>(<scope>): <description>`
Types: feat, fix, docs, refactor, test, chore
