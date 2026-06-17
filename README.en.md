<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · English · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** is a GitHub writing skill pack for AI agents. It routes common GitHub writing tasks, including Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms, and PR Templates, to scenario-specific standards so agents can produce clear, evidence-aware Markdown or YAML drafts that are closer to submission-ready.

It is not a README generator or a GitHub integration service. It is a portable Markdown rulebase: tools with native Agent Skills support can load it directly; tools without this format can adapt `SKILL.md` and the relevant `reference/*.md` files into rules, instructions, or knowledge bases.

## Why oh-my-gh-writing?

Good GitHub writing is not just filling a Markdown file. The hard part is deciding which scenario you are in, what facts must be verified, what must not be invented, and whether the final artifact can be pasted into an Issue, PR, Review, or README without cleanup. oh-my-gh-writing turns those decisions into a rule system that agents can load on demand.

- **18 GitHub writing scenarios**: Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template, and more.
- **Route before writing**: separates Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR, and Refactor PR to reduce issue/PR mixups.
- **Progressive reference loading**: `SKILL.md` stays lightweight while detailed standards are loaded only when needed.
- **Evidence boundaries**: versions, commands, CI, compatibility, releases, and issue/PR numbers are not guessed; unknown facts become TODO, TBD, or To confirm.
- **Cleaner artifacts**: avoids chat prefaces, outer Markdown fences, test titles, copy residue, and unrelated snippets.
- **Real open-source references**: patterns are informed by GitHub Docs, Conventional Commits, Keep a Changelog, and mature projects such as React, Kubernetes, TypeScript, Node.js, and Tailwind CSS.

## Usage Modes

**Use as a skill**: place this repository where the agent can load a folder containing `SKILL.md` and read `reference/` on demand.

**Use as rules**: if your tool cannot consume this skill format, adapt the routing table in `SKILL.md` and the relevant `reference/*.md` files into project rules, custom instructions, or a knowledge base.

| Icon | Agent / Tool | Recommended setup | Notes / Docs |
|------|--------------|-------------------|--------------|
| <img src="https://openai.com/favicon.ico" width="18" height="18" alt="OpenAI"> | Codex | Clone to `$HOME/.agents/skills/oh-my-gh-writing` or `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <img src="https://claude.ai/favicon.ico" width="18" height="18" alt="Claude"> | Claude Code | Clone or symlink to `~/.claude/skills/oh-my-gh-writing` or `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <img src="https://geminicli.com/favicon.ico" width="18" height="18" alt="Gemini CLI"> | Gemini CLI / Antigravity CLI | Gemini CLI documents `~/.gemini/skills/`, `~/.agents/skills/`, and `gemini skills install` | Confirm current [official docs](https://geminicli.com/docs/cli/skills/) before use |
| <img src="https://hermes-agent.nousresearch.com/favicon.ico" width="18" height="18" alt="Hermes"> | Hermes | Place under `~/.hermes/skills/<category>/oh-my-gh-writing` | Single-file HTTP install is only suitable for `SKILL.md`; keep `reference/` for this repository. See [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <img src="https://cursor.com/favicon.ico" width="18" height="18" alt="Cursor"> | Cursor | Adapt the router and needed scenario rules into project rules or a knowledge base | Confirm current [Cursor Docs](https://cursor.com/docs) |
| <img src="https://github.com/favicon.ico" width="18" height="18" alt="GitHub"> | GitHub Copilot | Adapt to `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, or a Copilot agent skill structure | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <img src="https://docs.continue.dev/favicon.ico" width="18" height="18" alt="Continue"> | Continue | Adapt to `.continue/rules/*.md`; scenario-specific files are more stable than one large rule file | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <img src="https://docs.windsurf.com/favicon.ico" width="18" height="18" alt="Windsurf"> | Windsurf / Devin Desktop | Current docs mention memories and rules for customization | Confirm the current path and integration method in [Windsurf / Devin Docs](https://docs.windsurf.com) |

## Quick Start

Codex:

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"
```

Claude Code:

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

Local development symlinks:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

Example requests:

```text
Write a README for this repository.
Turn this bug report into a GitHub Issue.
Write a PR description from the current diff.
Review this PR and classify findings as blocking / major / minor / nit.
```

## Scenarios

| # | Category | Scenario | Use when |
|---|----------|----------|----------|
| 1 | Issue | Bug Report | Reporting a reproducible defect |
| 2 | Issue | Feature Request | Proposing a new feature or API |
| 3 | Issue | Enhancement | Improving existing behavior |
| 4 | Issue | Discussion | Starting an open-ended community discussion |
| 5 | PR | Feature PR | Describing a new feature pull request |
| 6 | PR | Bug Fix PR | Describing a bug fix pull request |
| 7 | PR | Refactor PR | Describing behavior-preserving cleanup |
| 8 | PR | Documentation PR | Describing documentation-only changes |
| 9 | Review | Code Review | Reviewing code changes |
| 10 | Commit | Standard Commit | Writing commit messages |
| 11 | Docs | README | Creating or revising a project homepage |
| 12 | Docs | CONTRIBUTING | Creating contribution guidelines |
| 13 | Docs | CHANGELOG | Writing version history |
| 14 | Release | Release Notes | Writing release announcements |
| 15 | Release | Migration Guide | Explaining upgrade steps |
| 16 | Design | RFC | Proposing a design |
| 17 | Templates | Issue Form YAML | Creating GitHub Issue Forms |
| 18 | Templates | PR Template | Creating Pull Request templates |

Each scenario has a standard file in `reference/`. Full navigation is available in [`INDEX.md`](INDEX.md).

## Repository Structure

```text
oh-my-gh-writing/
├── README.md
├── README.*.md
├── SKILL.md
├── INDEX.md
├── CONTRIBUTING.md
├── LICENSE
├── assets/
│   └── oh-my-gh-writing-logo.png
└── reference/
    ├── *.md
    ├── readme.md
    ├── shared-principles.md
    ├── output-validation.md
    ├── source-catalog.md
    ├── weapons.md
    ├── emoji-guide.md
    └── badge-catalog.md
```

## Contributing

Contributions to scenario rules, reference sources, output validation, and small Markdown helpers are welcome. For examples or test cases, please first describe the source, scenario, test goal, and licensing or privacy boundary in an Issue or Discussion.

Keep `SKILL.md` lightweight and put scenario details in the matching `reference/*.md`. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sources

The scenario rules reference [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/), and mature open-source projects such as Angular, Kubernetes, React, TypeScript, VS Code, Node.js, and Tailwind CSS. See [`reference/source-catalog.md`](reference/source-catalog.md).

## License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
