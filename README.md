<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">✨ oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Skill-v0.1.0-2563eb?style=flat" alt="Skill v0.1.0"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 artifact standards"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 workflow packs"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

**oh-my-gh-writing** is an Agent Skill for GitHub writing. It helps AI agents draft cleaner GitHub issues, pull request descriptions, reviews, commits, README files, changelogs, release notes, migration guides, RFCs, issue forms, PR templates, and multi-artifact workflow packs.

The core idea is simple: route the request first, load only the matching writing standard, keep uncertain facts explicit, and output a GitHub artifact or local draft package that needs less cleanup.

## 🚀 Quick Start

Recommended manual install:

```bash
# Codex-style / hosts that support .agents/skills
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

If your host supports the open [Agent Skills](https://agentskills.io) `skills` CLI:

```bash
npx skills add PINKIIILQWQ/oh-my-gh-writing -g
npx skills add PINKIIILQWQ/oh-my-gh-writing -g -a codex
npx skills add PINKIIILQWQ/oh-my-gh-writing -g -a claude-code
```

`-g` installs globally for your user. Omit it for a project-local install when your host supports local skills.

Example prompts:

```text
Write a README for this repository.
Turn this bug report into a GitHub Issue.
Write a PR description from the current diff.
Prepare the full v1.2.0 release materials.
Make this repository ready for outside contributors.
```

## ✨ Why oh-my-gh-writing?

- **Workflow packs, not just templates**: release prep, project launch, contribution setup, bug-fix workflow, proposal-to-implementation, breaking-change communication, and docs overhaul are treated as multi-file GitHub writing jobs.
- **Artifact routing before writing**: separates Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR, Refactor PR, and Documentation PR so agents do not turn one GitHub artifact into another.
- **Evidence boundaries by default**: versions, commands, CI names, compatibility claims, issue numbers, PR numbers, and release facts must come from user input, repository files, diffs, or official sources.
- **Progressive reference loading**: `SKILL.md` stays lightweight; detailed rules live in `references/*.md` and are loaded only when needed.
- **Cleaner output**: rules explicitly guard against chat prefaces, outer Markdown fences, stale test titles, copied residue, unchecked checklist items, and invented facts.
- **Grounded in real GitHub practice**: the rulebase is shaped by GitHub Docs, Conventional Commits, Keep a Changelog, Google Engineering Practices, and mature open-source project patterns.

## 🛡️ What This Prevents

- PR descriptions that claim tests passed without evidence.
- Bug reports that invent root causes or affected versions.
- READMEs that advertise unsupported platforms or missing install paths.
- Release notes that invent migration commands, dates, contributors, or compare links.
- Issue forms that copy labels, SIGs, version lists, or required checkboxes from unrelated projects.

## 🎯 Applicability

This project is a portable Markdown rulebase for AI agents and rule-based coding tools. It is most useful when the tool can read `SKILL.md` plus local `references/*.md` files, but the same standards can be adapted into project rules, custom instructions, or a knowledge base.

| Use mode | Best for | What works well | Limit |
| --- | --- | --- | --- |
| Skill directory | Codex, Claude Code, folder-compatible skill hosts | Routing, progressive reference loading, validation rules | Requires local file access |
| Project rules | Cursor, Continue, Copilot, Windsurf / Devin-style rules | Reusing selected standards inside a project | Needs manual adaptation to each host format |
| Knowledge base | Teams or agents that search Markdown docs | Standards, examples of structure, source catalog | Routing depends on the host tool |

## 🧭 What It Covers

| Type | Coverage |
| --- | --- |
| 18 artifact standards | Bug Report, Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR, Refactor PR, Documentation PR, Code Review, Standard Commit, README, CONTRIBUTING, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form YAML, PR Template |
| 7 workflow packs | Version Release, Project Launch, Contribution Setup, Bug Fix Workflow, Proposal to Implementation, Breaking Change Package, Docs Overhaul |
| Quality appendices | Shared principles, output validation, badge patterns, emoji guide, GitHub Markdown tools, source catalog |

Workflow packs are thin orchestrators. They ask which package shape you want, then load only the selected single-artifact standards. By default they write local drafts under `.github-writing/...`; they do not publish releases, push tags, open PRs, or modify remote state unless you explicitly ask.

## 🤖 Agent Support

### Direct / Folder-Compatible Install

| Agent / Tool | Support type | Recommended setup | Maintainer verified | Last checked | Notes |
| --- | --- | --- | --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | Native skill directory | `$HOME/.agents/skills/oh-my-gh-writing` or project `.agents/skills/oh-my-gh-writing` | Yes | 2026-06-18 | Full folder recommended |
| [Claude Code](https://code.claude.com/docs/en/skills) | Native skill directory | `~/.claude/skills/oh-my-gh-writing` | Not yet | 2026-06-18 | Based on current docs; keep the full folder |
| [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | Folder-compatible / single-file limited | Hermes skills directory | Not yet | 2026-06-18 | HTTP single-file install only covers `SKILL.md`, not `references/` |

### Adaptation Targets

| Tool | Support type | Recommended adaptation | Maintainer verified | Last checked | Notes |
| --- | --- | --- | --- | --- | --- |
| [Gemini CLI / Antigravity](https://geminicli.com/docs/cli/skills/) | Check current docs | Use a skill directory or rules only if current docs confirm support | Not yet | 2026-06-18 | Availability is changing |
| [Cursor](https://cursor.com/docs) | Project rules / knowledge base | Adapt the router and selected references | Not yet | 2026-06-18 | Keep only relevant scenario rules |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Repository instructions / agent skill files | Adapt to `.github/copilot-instructions.md` or `.github/instructions/*.instructions.md` | Not yet | 2026-06-18 | Does not directly consume the full folder by default |
| [Continue](https://docs.continue.dev/customize/rules) | Rules | Adapt to `.continue/rules/*.md` | Not yet | 2026-06-18 | Split by scenario |
| [Windsurf / Devin Desktop](https://docs.windsurf.com) | Check current docs | Adapt to memories/rules if supported | Not yet | 2026-06-18 | Confirm the path before use |

## 📂 Files

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Thin runtime router and workflow rules |
| [`INDEX.md`](INDEX.md) | Navigation for 18 artifact standards and 7 workflow packs |
| [`references/`](references) | Scenario standards, workflow packs, and quality appendices |
| [`references/readme.md`](references/readme.md) | README writing standard used by this skill |
| [`references/source-catalog.md`](references/source-catalog.md) | Public source catalog and maintenance notes |
| [`evals/`](evals) | Trigger and output-quality eval fixtures for future skill iteration |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidance |
| [`assets/`](assets) | Logo and local README assets |

## 🧪 Evaluation

This repository includes lightweight eval fixtures for skill maintenance:

- [`evals/trigger-queries.json`](evals/trigger-queries.json) checks whether the skill description should activate for realistic GitHub-writing prompts and avoid near-miss prompts.
- [`evals/evals.json`](evals/evals.json) records output-quality tasks for routing, cleanliness, evidence boundaries, and workflow-pack behavior.
- [`evals/expected/`](evals/expected) stores short clean outputs that illustrate passable artifact shape.

## 🧪 Example: Evidence-Bounded PR Testing

Input:

```text
Write a feature PR for CSV export. I have not run tests.
```

Output excerpt:

```markdown
## Testing

Not run (not provided).
```

## 📚 Sources

The standards reference the [Agent Skills specification](https://agentskills.io/specification), [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/), and selected patterns from mature open-source repositories such as React, Kubernetes, TypeScript, Node.js, Tailwind CSS, Angular, and VS Code. See [`references/source-catalog.md`](references/source-catalog.md).

The source catalog is not copied into user artifacts; it records structural patterns and maintenance evidence only.

## 📄 License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
