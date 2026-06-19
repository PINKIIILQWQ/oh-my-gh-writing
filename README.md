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

Install the runtime skill files only. The Codex path below is maintainer-verified:

```bash
target="$HOME/.agents/skills/oh-my-gh-writing"
tmp="$(mktemp -d)"
repo="$tmp/oh-my-gh-writing"
git clone --depth 1 https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$repo"
rm -rf "$target"
mkdir -p "$target"
cp -R "$repo/SKILL.md" "$repo/INDEX.md" "$repo/references" "$target/"
rm -rf "$tmp"
```

For other documented hosts, use the same command with a different `target`:

| Host | Target path | Status |
| --- | --- | --- |
| Claude Code | `$HOME/.claude/skills/oh-my-gh-writing` | Documented, not maintainer-verified |
| Gemini CLI | `$HOME/.agents/skills/oh-my-gh-writing` | Documented, not maintainer-verified |
| Hermes | `$HOME/.hermes/skills/github/oh-my-gh-writing` | Documented, not maintainer-verified |

For repository development, clone the full repository separately:

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

Start with one of these prompts:

```text
/oh-my-gh-writing Write a README for this repository.
/oh-my-gh-writing Write a PR description from the current diff.
/oh-my-gh-writing Prepare the full v1.2.0 release materials from these merged PR summaries: fix login redirect, add CSV export, update docs. Do not publish anything.
```

If you use an Agent Skills-compatible package manager, verify that the installed skill folder contains both `SKILL.md` and `references/`. This repository intentionally keeps `evals/`, `cases/`, and `scripts/` out of runtime installs.

## 🧪 Example Prompts

| Prompt | Routes to | Expected output shape |
| --- | --- | --- |
| `/oh-my-gh-writing I am launching a new open-source project. What GitHub materials should I prepare?` | Project Launch audit | Readiness gap analysis: existing files, recommended files, optional files, and next steps. No files or `.github-writing/` drafts created. |
| `/oh-my-gh-writing Draft the public launch package for this new open-source project, but do not publish anything.` | Project Launch workflow pack | Local `.github-writing/project-launch/TBD/` drafts for README, CONTRIBUTING, issue forms, PR template, and `package-manifest.md` |
| `/oh-my-gh-writing Prepare the v1.2.0 release materials from these merged PR summaries: fix login redirect, add CSV export, update docs. Do not publish anything.` | Version Release workflow pack | Local `.github-writing/version-release/v1.2.0/` release drafts plus manifest and confirmation notes |
| `/oh-my-gh-writing Set up this repository for outside contributors.` | Contribution Setup workflow pack | CONTRIBUTING, issue form, PR template, README contribution entry, and local manifest |
| `/oh-my-gh-writing Write a bug-fix PR from this diff. Tests were not run.` | Bug Fix PR | PR body with summary, root-cause evidence if provided, testing marked as not run, and risk notes |
| `/oh-my-gh-writing Create a bug report Issue Form YAML. Labels and assignees are not confirmed.` | Issue Form YAML | YAML file content without invented labels, assignees, projects, or contact links |

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
| Project rules | Cursor, Continue, GitHub Copilot | Reusing selected standards inside a project | Needs manual adaptation to each host format |
| Knowledge base | Teams or agents that search Markdown docs | Standards, examples of structure, source catalog | Routing depends on the host tool |

## 🧭 What It Covers

| Type | Coverage |
| --- | --- |
| 18 artifact standards | Bug Report, Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR, Refactor PR, Documentation PR, Code Review, Standard Commit, README, CONTRIBUTING, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form YAML, PR Template |
| 7 workflow packs | Version Release, Project Launch, Contribution Setup, Bug Fix Workflow, Proposal to Implementation, Breaking Change Package, Docs Overhaul |
| Quality appendices | Shared principles, output validation, badge patterns, emoji guide, GitHub Markdown tools, source catalog |

Workflow packs are thin orchestrators. They infer the safest package shape when possible, ask only when the package shape is ambiguous, and record the selected option in `package-manifest.md`. By default they write local drafts under `.github-writing/...`; they do not publish releases, push tags, open PRs, or modify remote state unless you explicitly ask.

## 🤖 Agent Support

Last checked: 2026-06-20.

### Native Or Folder-Compatible Install

| Agent / Tool | Support type | Recommended setup | Maintainer verified | Last checked | Notes |
| --- | --- | --- | --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | Native skill directory | `$HOME/.agents/skills/oh-my-gh-writing` or project `.agents/skills/oh-my-gh-writing` | Yes | 2026-06-20 | Official docs list `.agents/skills` user and repository locations |
| [Claude Code](https://code.claude.com/docs/en/skills) | Native skill directory | `~/.claude/skills/oh-my-gh-writing` or project `.claude/skills/oh-my-gh-writing` | Not yet | 2026-06-20 | Official docs use a `SKILL.md` directory as the skill entrypoint |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | Native skill directory | Manual runtime-only copy to `$HOME/.agents/skills/oh-my-gh-writing` or `.agents/skills/oh-my-gh-writing` | Not yet | 2026-06-20 | Official docs list `.agents/skills` as an alias and support `gemini skills install`, but verify install output because this repo should not install non-runtime files |
| [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | Native skill directory | Copy the runtime folder to `~/.hermes/skills/github/oh-my-gh-writing` | Not yet | 2026-06-20 | Do not use HTTP single-file install for this repo because `references/` are required |

### Host-Specific Rule Setup

These tools do not consume this full Agent Skill folder as-is. Use them by converting the router plus selected `references/*.md` files into the host's rule or instruction format.

| Tool | Supported setup | Recommended file/path | Maintainer verified | Last checked | Notes |
| --- | --- | --- | --- | --- | --- |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Repository custom instructions | `.github/copilot-instructions.md`, `.github/instructions/gh-writing.instructions.md`, or `AGENTS.md` | Not yet | 2026-06-20 | Use a compact summary; Copilot will not automatically load this skill directory |
| [Continue](https://docs.continue.dev/customize/rules) | Project rules | `.continue/rules/oh-my-gh-writing.md` | Not yet | 2026-06-20 | Split large guidance by scenario when needed |
| [Cursor](https://cursor.com/docs) | Project rules | `.cursor/rules/oh-my-gh-writing.mdc` | Not yet | 2026-06-20 | Treat as a rules adaptation, not native Agent Skill support |

### Not Listed As Supported Yet

| Tool | Status | Last checked | Notes |
| --- | --- | --- | --- |
| Antigravity CLI | Not confirmed | 2026-06-20 | Keep out of setup instructions until official docs confirm a stable skill or rules path |
| Windsurf / Devin Desktop | Not confirmed | 2026-06-20 | Current docs redirect to Devin Desktop and do not expose a stable skill/rules path for this package |

## 📂 Files

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Thin runtime router and workflow rules |
| [`INDEX.md`](INDEX.md) | Navigation for 18 artifact standards and 7 workflow packs |
| [`references/`](references) | Scenario standards, workflow packs, and quality appendices |
| [`references/readme.md`](references/readme.md) | README writing standard used by this skill |
| [`references/source-catalog.md`](references/source-catalog.md) | Public source catalog and maintenance notes |
| [`evals/`](evals) | Trigger and output-quality eval fixtures for future skill iteration |
| [`scripts/`](scripts) | Maintainer validation utilities |
| [`cases/`](cases) | Public evidence drafts, not runtime references |
| [`.github/`](.github) | Public issue forms and pull request template for repository collaboration |
| [`README_Example.md`](README_Example.md) | Skill-generated README example, not the canonical homepage |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidance |
| [`assets/`](assets) | Logo and local README assets |

## 🧪 Evaluation

This repository includes lightweight eval fixtures for skill maintenance:

- [`evals/trigger-queries.json`](evals/trigger-queries.json) checks whether the skill description should activate for realistic GitHub-writing prompts and avoid near-miss prompts.
- [`evals/evals.json`](evals/evals.json) records output-quality tasks for routing, cleanliness, evidence boundaries, and workflow-pack behavior.
- [`evals/expected/`](evals/expected) stores short clean outputs that illustrate passable artifact shape.
- [`cases/`](cases) stores synthetic public evidence drafts for routing and evidence-boundary behavior; they are not runtime references.

Run:

```bash
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

## 🧪 Example: Public Launch Readiness Audit

This is a synthetic review-draft excerpt, not a real repository outcome or validated comparison case.

Input:

```text
Please check what files this sample repository still needs before I publish the project to GitHub.

Current repository files: README.md, LICENSE, SKILL.md, references/, evals/, scripts/.
```

Output excerpt:

```markdown
## Existing

- README: present.
- License: present.

## Recommended

- CONTRIBUTING.md — explains setup, test, branch, and PR expectations before outside contributors arrive.
- Bug report Issue Form — standardizes defect reports with reproduction, expected behavior, actual behavior, and environment fields.
- Pull request template — gives contributors a consistent place for summary, testing, risk, and related issues.

## Next steps

- Confirm which recommended files to prepare.
- Draft target files only after maintainer confirmation.
```

Excerpt shortened; the full case also includes Feature request Issue Form, Validation workflow, and Changelog recommendations.

See [`cases/005-project-launch-audit/`](cases/005-project-launch-audit/) for the synthetic review-draft case. Baseline behavior has not been collected yet.

## 📚 Sources

The standards reference the [Agent Skills specification](https://agentskills.io/specification), [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/), and selected patterns from mature open-source repositories such as React, Kubernetes, TypeScript, Node.js, Tailwind CSS, Angular, and VS Code. See [`references/source-catalog.md`](references/source-catalog.md).

The source catalog is not copied into user artifacts; it records structural patterns and maintenance evidence only.

## 📄 License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
