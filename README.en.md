<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-scenario-index)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** is a GitHub writing operating system for AI agents. It is not a README generator or a standalone app — it is a portable skill that, once loaded, routes agent output to the right scenario (Issue, PR, Review, Commit, README, CHANGELOG, RFC, etc.) with consistent quality, evidence boundaries, and submission-ready formatting.

---

## Scenario Index

| # | Category | Scenarios | Standard |
|---|----------|-----------|----------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` etc. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` etc. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` etc. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` etc. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` etc. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` etc. |

Full routing rules in [`SKILL.md`](SKILL.md).

---

## Installation

### Claude Code (direct load)

```bash
# Clone the repository
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

Then use `/oh-my-gh-writing` inside Claude Code.

### Other AI Agents

| Agent | Support | Action |
|-------|---------|--------|
| Cline / Roo Code | Adapted import | Copy `SKILL.md` content into the project custom instructions; load matching `reference/*.md` as needed |

> This skill is designed natively for Claude Code. Other agents require adaptation to their own rules system.

---

## Quick Start

```text
/oh-my-gh-writing Write a Bug Report
/oh-my-gh-writing Write a PR description for these changes
/oh-my-gh-writing Review this PR's changes
/oh-my-gh-writing Write a CHANGELOG entry
```

The agent routes to the right scenario, loads the matching `reference/*.md` rules, and outputs a submission-ready GitHub artifact.

---

## Core Principles

- **Evidence Boundaries** — Versions, PR numbers, test results, and install commands must have a source; mark unknown facts as `TODO`
- **Precise Routing** — Route by user intent; a Feature Request is never written as a shipped PR
- **Output Cleanliness** — Artifacts paste directly into GitHub — no conversational prefaces, no outer fences, no test metadata
- **One Artifact, One Job** — Never blend multiple issues or release notes into one output
- **Usable First** — Draft with `TODO` placeholders rather than blocking on missing information

---

## Project Structure

```
oh-my-gh-writing/
├── SKILL.md                    # Agent runtime router and shared rules
├── INDEX.md                    # Repository navigation index
├── reference/
│   ├── bug-report.md           # Bug Report standard
│   ├── feature-request.md      # Feature Request standard
│   ├── enhancement.md          # Enhancement standard
│   ├── discussion.md           # Discussion standard
│   ├── feature-pr.md           # Feature PR standard
│   ├── bug-fix-pr.md           # Bug Fix PR standard
│   ├── refactor-pr.md          # Refactor PR standard
│   ├── documentation-pr.md     # Documentation PR standard
│   ├── code-review.md          # Code Review standard
│   ├── standard-commit.md      # Commit message standard
│   ├── readme.md               # README writing standard
│   ├── contributing.md         # CONTRIBUTING writing standard
│   ├── changelog.md            # CHANGELOG standard
│   ├── release-notes.md        # Release Notes standard
│   ├── migration-guide.md      # Migration Guide standard
│   ├── rfc.md                  # RFC standard
│   ├── issue-form-yaml.md      # Issue Form YAML standard
│   ├── pr-template.md          # PR Template standard
│   ├── weapons.md              # GitHub Markdown tools (Badge / Mermaid / Alert etc.)
│   ├── emoji-guide.md          # Emoji usage guide
│   ├── output-validation.md    # Output validation checklist
│   └── source-catalog.md       # Reference source catalog
├── assets/                     # Project assets
├── CONTRIBUTING.md             # Contribution guide
└── LICENSE                     # MIT
```

---

## Contributing

PRs are welcome for scenario rules, reference sources, or output validation improvements. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## License

[MIT](LICENSE)
