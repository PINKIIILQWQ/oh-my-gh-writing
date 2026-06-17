<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
    <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
  </picture>
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue" alt="License"></a>
  <a href="#-scenario-index"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad" alt="Scenarios"></a>
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Agent%20Skills-Open%20Standard-8A2BE2" alt="Agent Skills"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Format-Agent%20Skills-22AA66" alt="Format"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs Welcome"></a>
</p>

<p align="center">
  <b>A GitHub writing operating system for AI agents — 18 scenarios · evidence boundaries · clean output</b><br>
  <sub>A portable Agent Skill that routes to the right standard for Issues, PRs, Reviews, Commits, READMEs, and more</sub>
</p>

---

## Overview

**oh-my-gh-writing** is not a README generator or a standalone app — it is a portable GitHub writing skill for AI agents. Based on the [Agent Skills](https://agentskills.io) open standard, agents load it and automatically match 18 GitHub document types with consistent quality, evidence boundaries, and submission-ready formatting.

---

## Scenario Index

| # | Category | Scenarios | Standard File |
|---|----------|-----------|---------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` etc. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` etc. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` etc. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` etc. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` etc. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` etc. |

Full routing rules in [`SKILL.md`](SKILL.md).

---

## Agent Support

This skill follows the [Agent Skills](https://agentskills.io) open standard. See below for which agents can load `SKILL.md` natively and which require adaptation.

### Direct Load (Native Agent Skills Support)

Drop the `SKILL.md` directory into the designated path.

| Agent | Install Method | Adaptation Scope | Docs |
|-------|---------------|-----------------|------|
| <img src="https://code.claude.com/favicon.ico" width="16" height="16"> **Claude Code** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing` → invoke with `/oh-my-gh-writing` | Full 18-scenario support. Agent loads `SKILL.md` and matching `reference/*.md` on demand | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| <img src="https://cursor.com/favicon.ico" width="16" height="16"> **Cursor** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.cursor/skills/oh-my-gh-writing` | Full Agent Skills format support | [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills) |
| <img src="https://roocode.com/favicon.ico" width="16" height="16"> **Roo Code** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.roo/skills/oh-my-gh-writing` | Agent Skills format loading | [docs.roocode.com/features/skills](https://docs.roocode.com/features/skills) |
| <img src="https://code.visualstudio.com/favicon.ico" width="16" height="16"> **VS Code** | Configure via GitHub Copilot Agent Skills feature | Agent Skills standard support | [code.visualstudio.com/docs/copilot/customization/agent-skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| <img src="https://github.com/favicon.ico" width="16" height="16"> **GitHub Copilot** | Configure Agent Skills in GitHub repository settings | Agent Skills format support | [docs.github.com/en/copilot/concepts/agents/about-agent-skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| <img src="https://geminicli.com/favicon.ico" width="16" height="16"> **Gemini CLI** | Configure into Gemini CLI skills directory | Agent Skills open standard support | [geminicli.com/docs/cli/skills](https://geminicli.com/docs/cli/skills/) |
| <img src="https://developers.openai.com/favicon.ico" width="16" height="16"> **OpenAI Codex** | Configure into Codex skills directory | Agent Skills format support | [developers.openai.com/codex/skills](https://developers.openai.com/codex/skills/) |
| <img src="https://opencode.ai/favicon.ico" width="16" height="16"> **OpenCode** | Configure into skills directory | Agent Skills open standard | [opencode.ai/docs/skills](https://opencode.ai/docs/skills/) |
| <img src="https://block.github.io/goose/favicon.ico" width="16" height="16"> **Goose** | Configure into Goose skills directory | Agent Skills support | [block.github.io/goose/docs/guides/context-engineering/using-skills](https://block.github.io/goose/docs/guides/context-engineering/using-skills/) |
| <img src="https://docs.openhands.dev/favicon.ico" width="16" height="16"> **OpenHands** | Configure into skills directory | Agent Skills standard support | [docs.openhands.dev/overview/skills](https://docs.openhands.dev/overview/skills) |
| <img src="https://www.jetbrains.com/favicon.ico" width="16" height="16"> **Junie (JetBrains)** | Configure into Junie skills directory | Agent Skills support | [junie.jetbrains.com/docs/agent-skills](https://junie.jetbrains.com/docs/agent-skills.html) |
| <img src="https://ampcode.com/favicon.ico" width="16" height="16"> **Amp** | Configure into Amp skills directory | Agent Skills support | [ampcode.com/manual#agent-skills](https://ampcode.com/manual#agent-skills) |
| <img src="https://www.letta.com/favicon.ico" width="16" height="16"> **Letta** | Configure into Letta skills directory | Agent Skills support | [docs.letta.com/letta-code/skills](https://docs.letta.com/letta-code/skills/) |
| <img src="https://factory.ai/favicon.ico" width="16" height="16"> **Factory** | Configure into Factory skills directory | Agent Skills support | [docs.factory.ai/cli/configuration/skills](https://docs.factory.ai/cli/configuration/skills) |
| <img src="https://www.tabnine.com/favicon.ico" width="16" height="16"> **Tabnine** | Configure into Tabnine skills directory | Agent Skills support | [docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills) |
| <img src="https://www.trae.ai/favicon.ico" width="16" height="16"> **TRAE** | Configure into TRAE skills directory | Agent Skills support | [trae.ai/blog/trae_tutorial_0115](https://www.trae.ai/blog/trae_tutorial_0115) |
| <img src="https://autohand.ai/favicon.ico" width="16" height="16"> **Autohand Code CLI** | Configure into autohand skills directory | Agent Skills support | [autohand.ai/docs/working-with-autohand-code/agent-skills](https://autohand.ai/docs/working-with-autohand-code/agent-skills.html) |
| <img src="https://www.qodo.ai/favicon.ico" width="16" height="16"> **Qodo** | Configure into Qodo skills directory | Agent Skills support | [qodo.ai/blog/how-i-use-qodos-agent-skills](https://www.qodo.ai/blog/how-i-use-qodos-agent-skills-to-auto-fix-issues-in-pull-requests/) |
| <img src="https://github.com/mistralai/mistral-vibe/raw/main/assets/logo.svg" width="16" height="16"> **Mistral Vibe** | Configure into mistral-vibe skills directory | Agent Skills support | [github.com/mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) |
| <img src="https://commandcode.ai/favicon.ico" width="16" height="16"> **Command Code** | Configure into Command Code skills directory | Agent Skills support | [commandcode.ai/docs/skills](https://commandcode.ai/docs/skills) |

### Adapted Import (Rule Copying Required)

These agents do not support `SKILL.md` natively. Copy the rules into their own format.

| Agent | Install Method | Adaptation Scope | Docs |
|-------|---------------|-----------------|------|
| <img src="https://docs.cline.bot/favicon.ico" width="16" height="16"> **Cline** | Write `SKILL.md` content into `.clinerules` file; add `reference/*.md` content as project background instructions | Covers rule text for all 18 scenarios, but no automatic routing. User must specify scenario manually | [docs.cline.bot](https://docs.cline.bot/improving-your-prompting/custom-instructions) |
| <img src="https://codeium.com/favicon.ico" width="16" height="16"> **Windsurf** | Write rules into `.windsurfrules` file | Covers core principles and output validation, but no scenario routing | [codeium.com/windsurf](https://codeium.com/windsurf) |
| <img src="https://aider.chat/favicon.ico" width="16" height="16"> **Aider** | Write core rules into `.aider.conf.yml` or `CONVENTIONS.md` | Covers evidence boundaries and output cleanliness rules | [aider.chat/docs/usage/conventions](https://aider.chat/docs/usage/conventions.html) |
| <img src="https://continue.dev/favicon.ico" width="16" height="16"> **Continue** | Write rules into `.continuerc.json` or project-level config | Covers documentation core standards | [docs.continue.dev/customize](https://docs.continue.dev/customize) |

---

## Quick Start

```text
/oh-my-gh-writing Write a Bug Report
/oh-my-gh-writing Write a PR description for these changes
/oh-my-gh-writing Review this PR's changes
/oh-my-gh-writing Write a CHANGELOG entry
```

On adapted agents, specify the scenario and the agent applies the matching standards to produce a GitHub-ready artifact.

---

## Core Principles

- **Evidence Boundaries** — Versions, PR numbers, test results, and install commands must have a source; mark unknown facts as `TODO`
- **Precise Routing** — Route by user intent; a Feature Request is never written as a shipped PR
- **Clean Output** — Artifacts paste directly into GitHub — no conversational prefaces, no outer fences, no test metadata
- **One Artifact, One Job** — Never blend multiple issues or release notes into one output
- **Usable First** — Draft with `TODO` placeholders rather than blocking on missing information

---

## Project Structure

```
oh-my-gh-writing/
├── SKILL.md                    # Agent runtime router and shared rules
├── INDEX.md                    # Repository navigation index
├── reference/                  # 18 scenario standards + tool references
│   ├── bug-report.md
│   ├── feature-request.md
│   ├── enhancement.md
│   ├── discussion.md
│   ├── feature-pr.md
│   ├── bug-fix-pr.md
│   ├── refactor-pr.md
│   ├── documentation-pr.md
│   ├── code-review.md
│   ├── standard-commit.md
│   ├── readme.md
│   ├── contributing.md
│   ├── changelog.md
│   ├── release-notes.md
│   ├── migration-guide.md
│   ├── rfc.md
│   ├── issue-form-yaml.md
│   ├── pr-template.md
│   ├── weapons.md              # GitHub Markdown tools
│   ├── emoji-guide.md          # Emoji usage guide
│   ├── output-validation.md    # Output validation checklist
│   └── source-catalog.md       # Reference source catalog
├── CONTRIBUTING.md             # Contribution guide
├── assets/                     # Project assets
├── LICENSE                     # MIT
├── README.md                   # 简体中文
├── README.ja.md                # 日本語
├── README.ko.md                # 한국어
├── README.es.md                # Español
├── README.fr.md                # Français
├── README.de.md                # Deutsch
└── README.pt.md                # Português
```

---

## Multilingual README

This README is available in 8 languages:

| File | Language |
|------|----------|
| [`README.md`](README.md) | 简体中文 |
| [`README.en.md`](README.en.md) | English |
| [`README.ja.md`](README.ja.md) | 日本語 |
| [`README.ko.md`](README.ko.md) | 한국어 |
| [`README.es.md`](README.es.md) | Español |
| [`README.fr.md`](README.fr.md) | Français |
| [`README.de.md`](README.de.md) | Deutsch |
| [`README.pt.md`](README.pt.md) | Português |

Need more languages? Tell the agent "as many languages as possible" on a README task.

---

## Contributing

PRs welcome for scenario rules, reference sources, or output validation improvements. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## License

[MIT](LICENSE)
