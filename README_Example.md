<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/oh-my-gh-writing-logo.png">
    <img alt="oh-my-gh-writing" src="./assets/oh-my-gh-writing-logo.png" width="120">
  </picture>
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  GitHub writing skill for AI agents — route, load, draft, validate.
</p>

<p align="center">
  <a href="./SKILL.md"><img src="https://img.shields.io/badge/format-SKILL.md-22AA66?style=flat-square" alt="Format: SKILL.md"></a>
  <a href="./INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat-square" alt="18 Scenarios"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License: MIT"></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome"></a>
  <a href="./SKILL.md"><img src="https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2?style=flat-square" alt="Agent: Claude Code"></a>
</p>

---

## 🧭 Overview

oh-my-gh-writing is a **portable Claude Code skill** for producing near-submission-ready GitHub artifacts. It doesn't generate prompts or templates from scratch — it routes each request to the correct scenario standard, loads the matching rules, enforces evidence boundaries, and validates output before delivery.

Built for agents that write on GitHub: Issues, PRs, reviews, docs, releases, and templates.

## ✨ Features

- **Scenario routing** — 18 GitHub writing scenarios, each with a dedicated rule file
- **Evidence boundaries** — no invented versions, CI status, screenshots, or unverified facts
- **Progressive disclosure** — loads only what's needed for the current task
- **Output validation** — built-in checklist catches format pollution, routing errors, and fact gaps
- **Language fidelity** — matches the target repository's language, never leaks skill instructions

## 🚀 Quick Start

Clone the skill to your Claude Code skills directory:

```bash
git clone https://github.com/<your-org>/oh-my-gh-writing.git ~/.claude/skills/oh-my-gh-writing
```

Then invoke it through Claude Code:

```
> Write a Bug Report for a Vite "Module not found" build failure
> Review this PR: https://github.com/owner/repo/pull/123
> Write a README for this project
```

The skill identifies the scenario, loads the matching standard, and drafts the artifact — no manual setup required.

## 🎯 Scenarios

### Issues

| Scenario | Use case | Reference |
|----------|----------|-----------|
| Bug Report | Report a reproducible defect | [`reference/bug-report.md`](./reference/bug-report.md) |
| Feature Request | Propose a new capability or API | [`reference/feature-request.md`](./reference/feature-request.md) |
| Enhancement | Improve existing behavior | [`reference/enhancement.md`](./reference/enhancement.md) |
| Discussion | Open-ended community input | [`reference/discussion.md`](./reference/discussion.md) |

### Pull Requests

| Scenario | Use case | Reference |
|----------|----------|-----------|
| Feature PR | New feature pull request | [`reference/feature-pr.md`](./reference/feature-pr.md) |
| Bug Fix PR | Defect-fixing pull request | [`reference/bug-fix-pr.md`](./reference/bug-fix-pr.md) |
| Refactor PR | Behavior-preserving cleanup | [`reference/refactor-pr.md`](./reference/refactor-pr.md) |
| Documentation PR | Docs-only changes | [`reference/documentation-pr.md`](./reference/documentation-pr.md) |

### Review & Commits

| Scenario | Use case | Reference |
|----------|----------|-----------|
| Code Review | Review code changes | [`reference/code-review.md`](./reference/code-review.md) |
| Standard Commit | Write commit messages | [`reference/standard-commit.md`](./reference/standard-commit.md) |

### Documentation

| Scenario | Use case | Reference |
|----------|----------|-----------|
| README | Project homepage | [`reference/readme.md`](./reference/readme.md) |
| CONTRIBUTING | Contribution guidelines | [`reference/contributing.md`](./reference/contributing.md) |
| CHANGELOG | Version history | [`reference/changelog.md`](./reference/changelog.md) |

### Releases & Design

| Scenario | Use case | Reference |
|----------|----------|-----------|
| Release Notes | Release announcements | [`reference/release-notes.md`](./reference/release-notes.md) |
| Migration Guide | Upgrade steps | [`reference/migration-guide.md`](./reference/migration-guide.md) |
| RFC | Design proposals | [`reference/rfc.md`](./reference/rfc.md) |

### Templates

| Scenario | Use case | Reference |
|----------|----------|-----------|
| Issue Form YAML | GitHub issue forms | [`reference/issue-form-yaml.md`](./reference/issue-form-yaml.md) |
| PR Template | Pull request templates | [`reference/pr-template.md`](./reference/pr-template.md) |

## ⚙️ How It Works

```
User request
    │
    ▼
┌─────────────────┐
│  Route scenario  │  SKILL.md — scenario matching & routing rules
└────────┬────────┘
         ▼
┌─────────────────┐
│  Load standard   │  reference/*.md — per-scenario rules
└────────┬────────┘
         ▼
┌─────────────────┐
│  Enforce facts   │  shared-principles.md — evidence boundaries
└────────┬────────┘
         ▼
┌─────────────────┐
│  Validate output │  output-validation.md — submission-ready check
└────────┬────────┘
         ▼
   GitHub artifact
```

## 📂 File Index

| Path | Role |
|------|------|
| [`SKILL.md`](./SKILL.md) | Runtime router — scenario matching, workflow, reference index |
| [`INDEX.md`](./INDEX.md) | Navigation index — full scenario table, reading paths |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Contribution rules, source guidelines, case process |
| [`LICENSE`](./LICENSE) | MIT License |
| [`reference/`](./reference) | 24 reference files — per-scenario standards + appendix |
| [`assets/`](./assets) | Project images and display assets |
| [`reference/shared-principles.md`](./reference/shared-principles.md) | 19 cross-cutting output quality rules |
| [`reference/output-validation.md`](./reference/output-validation.md) | Pre-submission validation checklist |
| [`reference/weapons.md`](./reference/weapons.md) | GitHub Markdown guide — badges, alerts, Mermaid, emoji |
| [`reference/source-catalog.md`](./reference/source-catalog.md) | Public reference sources index |

## 🧠 Design Principles

- **SKILL.md stays thin.** It routes; it doesn't contain scenario rules.
- **One standard per scenario.** Each `reference/*.md` covers exactly one artifact type.
- **Evidence is the floor.** No fact appears without a source — user input, repo files, tool output, or verified links.
- **Output is submission-ready.** The validation pass strips chat wrappers, format pollution, and unverified claims.
- **Progressive by default.** No eager loads, no large context dumps — the agent fetches what it needs.

## 🤝 Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for contribution principles, reference source guidelines, and case contribution process.

Key areas:

- Fix or improve scenario rules in `reference/*.md`
- Add GitHub Markdown utilities (badges, alerts, Mermaid patterns)
- Submit case reports showing where the skill works well or fails
- Update source quality in `reference/source-catalog.md`

## 📄 License

[MIT](./LICENSE) © 2026 oh-my-gh-writing contributors.
