> This is a skill-generated README example used for public review. It is not the canonical project homepage. See [`README.md`](README.md) for maintained documentation.
>
> 这是由 skill 生成的 README 示例，不是本项目 canonical 首页；正式文档请看 [`README.md`](README.md)。

<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="128">
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
  A portable GitHub writing skill for AI agents.
</p>

## ✨ Overview

`oh-my-gh-writing` helps AI agents draft and revise GitHub-facing artifacts with clear routing, evidence boundaries, and clean artifact formatting. It is a skill package and rulebase, not a standalone app or GitHub integration.

Use it when you need GitHub issues, pull request descriptions, code reviews, commit messages, repository docs, release materials, templates, or coordinated multi-file writing packages.

## 🎯 Why Use It

- **GitHub-specific routing:** separates issues, PRs, reviews, commits, docs, templates, release notes, migration guides, RFCs, and workflow packs.
- **Evidence-bounded writing:** avoids invented CI results, versions, issue numbers, labels, compatibility claims, release URLs, and test status.
- **Output cleanliness:** guards against chat prefaces, outer Markdown fences, test metadata, and half-open code blocks.
- **Progressive loading:** keeps `SKILL.md` small and loads only the relevant `references/*.md` standard for the task.
- **Composite workflow support:** creates coordinated local draft packages with manifests, assumptions, TODOs, and maintainer-confirmation notes.
- **Reviewable evidence:** includes lightweight routing fixtures and public case drafts for maintainers to inspect.

## 🚀 Quick Start

Install only the runtime skill files into your local skill directory:

```bash
# Codex-style hosts:
target="$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code:
# target="$HOME/.claude/skills/oh-my-gh-writing"

tmp="$(mktemp -d)"
git clone --depth 1 https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$tmp/oh-my-gh-writing"

rm -rf "$target"
mkdir -p "$target"
cp -R "$tmp/oh-my-gh-writing/SKILL.md" \
  "$tmp/oh-my-gh-writing/INDEX.md" \
  "$tmp/oh-my-gh-writing/references" \
  "$target/"

rm -rf "$tmp"
```

Then ask your agent to use the skill for a GitHub writing task:

```text
/oh-my-gh-writing Write a feature PR description from this diff.
```

For a broader package, ask for a workflow pack:

```text
/oh-my-gh-writing Prepare full v1.2.0 release materials from these merged PR summaries: fix login redirect, add CSV export, update docs. Do not publish anything.
```

For repository development, clone the full repository separately and validate eval fixtures:

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

## 🧭 Applicability

This project applies to:

- AI agents or local workflows that can load a skill directory and read Markdown reference files.
- GitHub repository writing artifacts, including issues, PR descriptions, reviews, commits, docs, release materials, and templates.
- Maintainers who want reusable standards for evidence-bounded GitHub writing.
- Local draft packages for release, launch, contribution setup, bug-fix, proposal, breaking-change, and docs-overhaul workflows.

This project does **not** apply to:

- Generic prose, UI copy, marketing copy, or product strategy.
- Code implementation tasks.
- Publishing releases, pushing tags, opening PRs, or modifying remote GitHub state unless explicitly requested.

## 📂 File Map

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Thin runtime router, trigger boundary, workflow rules, and reference index. |
| `INDEX.md` | Human-readable navigation for artifact standards, workflow packs, and maintenance entry points. |
| `references/` | Scenario standards, composite workflow packs, shared principles, output validation, Markdown tools, emoji guidance, badges, and source catalog. |
| `evals/` | Trigger queries, structured eval fixtures, schema, and expected clean outputs. |
| `scripts/validate-evals.py` | Local no-dependency validation for eval fixture structure and containment checks. |
| `scripts/validate-cases.py` | Local no-dependency validation for public case evidence structure. |
| `CONTRIBUTING.md` | Contribution principles, source requirements, case feedback rules, and validation expectations. |
| `cases/` | Sanitized public evidence cases, not runtime references. |
| `.github/` | Public issue forms and pull request template for repository collaboration. |
| `assets/` | Project-owned visual assets. |
| `LICENSE` | MIT license. |

## 🧩 Artifact Standards

| Category | Artifacts |
| --- | --- |
| Issues | Bug Report, Feature Request, Enhancement, Discussion |
| Pull Requests | Feature PR, Bug Fix PR, Refactor PR, Documentation PR |
| Review and Commit | Code Review, Standard Commit |
| Docs | README, CONTRIBUTING, CHANGELOG |
| Release and Design | Release Notes, Migration Guide, RFC |
| Templates | Issue Form YAML, PR Template |

## 📦 Workflow Packs

| Pack | Use When |
| --- | --- |
| Version Release | Preparing release or version-update materials. |
| Project Launch | Preparing a repository for first public launch. |
| Contribution Setup | Making a project ready for outside contributors. |
| Bug Fix Workflow | Handling a bug from report or triage through fix PR. |
| Proposal to Implementation | Turning an idea into discussion, design, issue, and implementation materials. |
| Breaking Change Package | Communicating and shipping a breaking change. |
| Docs Overhaul | Planning or documenting a broad documentation refresh. |

Composite packs default to local draft output under `.github-writing/<pack-name>/<version-or-date>/` and include a `package-manifest.md`.

## 🧪 Validation And Evals

The package includes lightweight eval coverage for trigger boundaries, scenario routing, evidence handling, output cleanliness, workflow-pack behavior, and Markdown/YAML expectations.

Run:

```bash
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

## 🤝 Contributing

Contributions should keep the runtime path narrow, evidence-based, and easy for agents to load.

Good contribution areas include scenario rule fixes, source quality updates, README or install wording fixes, output hygiene improvements, GitHub Markdown utilities, and case reports that show where the skill works well or fails.

See `CONTRIBUTING.md` for the full contribution process.

## 📄 License

MIT License. See `LICENSE` for details.
