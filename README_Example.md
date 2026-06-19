<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="128">
</p>

<h1 align="center">oh-my-gh-writing</h1>

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
- **Maintainer-friendly evals:** includes lightweight routing and output-quality fixtures plus a no-dependency validation script.

## 🚀 Quick Start

Use the package from a local skill directory or repository checkout.

1. Keep the package structure intact:

```text
SKILL.md
INDEX.md
references/
evals/
scripts/
```

2. Ask your agent to use the skill for a GitHub writing task:

```text
Use oh-my-gh-writing to draft a feature PR description from this diff.
```

3. For a broader package, ask for a workflow pack:

```text
Use oh-my-gh-writing to prepare full v1.2.0 release materials.
```

4. Validate eval fixtures after changing routing, standards, or expected outputs:

```bash
python3 scripts/validate-evals.py
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
| `CONTRIBUTING.md` | Contribution principles, source requirements, case feedback rules, and validation expectations. |
| `cases/` | Sanitized public evidence cases, not runtime references. |
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
```

## 🤝 Contributing

Contributions should keep the runtime path narrow, evidence-based, and easy for agents to load.

Good contribution areas include scenario rule fixes, source quality updates, README or install wording fixes, output hygiene improvements, GitHub Markdown utilities, and case reports that show where the skill works well or fails.

See `CONTRIBUTING.md` for the full contribution process.

## 📄 License

MIT License. See `LICENSE` for details.
