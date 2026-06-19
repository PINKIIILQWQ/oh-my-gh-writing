# oh-my-gh-writing Index

This file is repository navigation. `README.md` explains what the project is and how to start; this index maps the runtime standards and maintenance entry points.

Agents should start with `SKILL.md`, then load the matching `references/*.md`. Before final output, apply `references/output-validation.md` for cleanliness and evidence-boundary checks.

## Reading Path

| Level | Entry | Audience | Detail |
|-------|-------|----------|--------|
| 0 | `README.md` | First-time repository visitors | Positioning, install path, shortest route |
| 1 | `INDEX.md` | People looking for a scenario or document | Full navigation and directory map |
| 2 | `SKILL.md` | Agents and skill users | Runtime routing, workflow, reference index |
| 3 | `references/shared-principles.md` | Cross-scenario quality work | Output quality and evidence boundaries |
| 4 | `references/` | Maintainers editing standards | Per-scenario rules, workflow packs, checklists |
| 5 | `references/source-catalog.md` / `CONTRIBUTING.md` | Maintainers and contributors | Source quality, contribution, and case feedback rules |

## 18 Artifact Standards

| # | Category | Scenario | Use when | Standard |
|---|----------|----------|----------|----------|
| 1 | Issue | Bug Report | Reporting a reproducible defect | `references/bug-report.md` |
| 2 | Issue | Feature Request | Proposing a new capability or API | `references/feature-request.md` |
| 3 | Issue | Enhancement | Improving existing behavior | `references/enhancement.md` |
| 4 | Issue | Discussion | Opening community discussion | `references/discussion.md` |
| 5 | PR | Feature PR | Describing a new feature pull request | `references/feature-pr.md` |
| 6 | PR | Bug Fix PR | Describing a defect-fixing pull request | `references/bug-fix-pr.md` |
| 7 | PR | Refactor PR | Describing behavior-preserving cleanup | `references/refactor-pr.md` |
| 8 | PR | Documentation PR | Describing documentation-only changes | `references/documentation-pr.md` |
| 9 | Review | Code Review | Reviewing code changes | `references/code-review.md` |
| 10 | Commit | Standard Commit | Writing commit messages | `references/standard-commit.md` |
| 11 | Docs | README | Creating or revising a project homepage | `references/readme.md` |
| 12 | Docs | CONTRIBUTING | Creating contribution guidelines | `references/contributing.md` |
| 13 | Docs | CHANGELOG | Writing version history | `references/changelog.md` |
| 14 | Release | Release Notes | Writing release announcements | `references/release-notes.md` |
| 15 | Release | Migration Guide | Explaining upgrade steps | `references/migration-guide.md` |
| 16 | Design | RFC | Proposing a design | `references/rfc.md` |
| 17 | Templates | Issue Form YAML | Creating GitHub Issue Forms | `references/issue-form-yaml.md` |
| 18 | Templates | PR Template | Creating Pull Request templates | `references/pr-template.md` |

## 7 Workflow Packs

| # | Category | Pack | Use when | Orchestrator |
|---|----------|------|----------|--------------|
| 19 | Composite | Version Release | Preparing release or version-update materials | `references/version-release.md` |
| 20 | Composite | Project Launch | Preparing a repository for first public launch | `references/project-launch.md` |
| 21 | Composite | Contribution Setup | Making a project ready for outside contributors | `references/contribution-setup.md` |
| 22 | Composite | Bug Fix Workflow | Handling a bug from report or triage through fix PR | `references/bug-fix-workflow.md` |
| 23 | Composite | Proposal to Implementation | Turning an idea into discussion, design, issue, and implementation materials | `references/proposal-to-implementation.md` |
| 24 | Composite | Breaking Change Package | Communicating and shipping a breaking change | `references/breaking-change-package.md` |
| 25 | Composite | Docs Overhaul | Planning or documenting a broad documentation refresh | `references/docs-overhaul.md` |

## Directory Index

| Directory | Purpose | Entry |
|-----------|---------|-------|
| `references/` | Artifact standards, workflow packs, validation, Markdown tools, and source catalog | `references/readme.md` |
| `CONTRIBUTING.md` | Contribution rules, source requirements, and case feedback process | `CONTRIBUTING.md` |
| `assets/` | README and project display assets | `assets/oh-my-gh-writing-logo.png` |
| `evals/` | Trigger and output-quality eval fixtures for skill iteration | `evals/evals.json` |
| `scripts/` | Maintainer validation utilities | `scripts/validate-evals.py` |
| `cases/` | Sanitized public evidence cases, not runtime references | `cases/README.md` |

## Reference File Index

| Type | Files |
|------|-------|
| Issue | `bug-report.md`, `feature-request.md`, `enhancement.md`, `discussion.md` |
| PR | `feature-pr.md`, `bug-fix-pr.md`, `refactor-pr.md`, `documentation-pr.md` |
| Review / Commit | `code-review.md`, `standard-commit.md` |
| Docs | `readme.md`, `contributing.md`, `changelog.md` |
| Release / Design | `release-notes.md`, `migration-guide.md`, `rfc.md` |
| Templates | `issue-form-yaml.md`, `pr-template.md` |
| Composite workflow packs | `version-release.md`, `project-launch.md`, `contribution-setup.md`, `bug-fix-workflow.md`, `proposal-to-implementation.md`, `breaking-change-package.md`, `docs-overhaul.md` |
| Appendix | `shared-principles.md`, `weapons.md`, `badge-catalog.md`, `emoji-guide.md`, `output-validation.md`, `source-catalog.md` |

## Maintenance Rules

- When adding a scenario or workflow pack, update `SKILL.md`, `INDEX.md`, public README files, and the matching `references/*.md`.
- Keep `SKILL.md` thin; put details in references.
- Keep runtime files in English by default.
- Keep README focused on the shortest public path, not every internal detail.
- Ensure deep details have an upper-level entry point.
- Keep local research, collected cases, and validation outputs out of public runtime indexes.
- Keep output validation rules in `references/output-validation.md`; do not mix test titles, raw sources, or verdict metadata into submit-ready artifacts.
- Keep source references in `references/source-catalog.md`; ordinary writing requests do not need to read the full catalog.
