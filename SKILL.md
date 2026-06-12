---
name: oh-my-gh-writing
description: "GitHub writing standards for AI agents. Use when drafting or revising GitHub issues, pull request descriptions, code reviews, commit messages, README/CONTRIBUTING/CHANGELOG docs, release notes, migration guides, RFCs, issue forms, or PR templates with normal/complete variants and progressive reference loading."
---

# oh-my-gh-writing

Use this skill to produce GitHub-ready writing for common collaboration workflows. Keep the runtime path narrow: classify the request, choose a detail level, load only the relevant reference file, and produce the requested Markdown or YAML.

## Workflow

1. Identify the scenario from the user's request.
2. Choose **normal** mode by default.
3. Use **complete** mode only when the user asks for a complete/formal version, the change is high-risk, the work is release/migration/design related, or breaking changes are involved.
4. Read the matching `reference/*.md` file before writing the final output.
5. Read [`reference/weapons.md`](./reference/weapons.md) only when badges, alerts, collapsible logs, Mermaid, tables, or other formatting tools are needed.
6. Read [`INDEX.md`](./INDEX.md) only for full repository navigation or maintenance work.

Do not load every reference file for a normal request. Do not expose reference-project analysis in user-facing output unless the user explicitly asks for rationale or sources.

## Scenario Routing

| User intent | Scenario | Reference |
|-------------|----------|-----------|
| Report a reproducible defect | Bug Report | `reference/bug-report.md` |
| Request a new feature or API | Feature Request | `reference/feature-request.md` |
| Improve an existing behavior | Enhancement | `reference/enhancement.md` |
| Open-ended community discussion | Discussion | `reference/discussion.md` |
| Describe a new feature PR | Feature PR | `reference/feature-pr.md` |
| Describe a bug fix PR | Bug Fix PR | `reference/bug-fix-pr.md` |
| Describe behavior-preserving cleanup | Refactor PR | `reference/refactor-pr.md` |
| Describe documentation-only changes | Documentation PR | `reference/documentation-pr.md` |
| Review code changes | Code Review | `reference/code-review.md` |
| Write a commit message | Standard Commit | `reference/standard-commit.md` |
| Create or revise a project homepage | README | `reference/readme.md` |
| Create or revise contribution rules | CONTRIBUTING | `reference/contributing.md` |
| Write version history | CHANGELOG | `reference/changelog.md` |
| Write a release announcement | Release Notes | `reference/release-notes.md` |
| Explain upgrade steps | Migration Guide | `reference/migration-guide.md` |
| Propose a design | RFC | `reference/rfc.md` |
| Create GitHub Issue Forms | Issue Form YAML | `reference/issue-form-yaml.md` |
| Create a PR template | PR Template | `reference/pr-template.md` |

## Shared Principles

1. Make the output usable first. If information is missing, write a reasonable draft and mark assumptions or TODO fields instead of blocking on nonessential questions.
2. Preserve existing repository style when editing an existing file: heading depth, terminology, date format, label names, link style, and language choice.
3. Keep one artifact focused on one job. Split unrelated bugs, features, or release notes instead of blending them into one issue or PR.
4. Put critical information in the body, not only behind links.
5. Record reproducible context: versions, platform, environment, affected commands, expected behavior, actual behavior, and tests where relevant.
6. Use concise, neutral language. Prefer precise impact and verification over persuasion.
7. Do not invent CI status, versions, compatibility, benchmarks, screenshots, or links. If evidence is unavailable, omit the claim or label it as a placeholder.

## README Guardrails

When the scenario is README, follow `reference/readme.md` and apply these extra constraints:

- Treat the README as a public entry page, not a dump of every internal file.
- For skill repositories, explain that the project is a portable writing skill, not a standalone app, README generator, or GitHub integration.
- Keep runtime files and maintainer files distinct: `SKILL.md` and `reference/` define behavior; `DOCS/` and `test/` are process and validation material.
- Use badges only when they answer a real reader question and link to evidence.
- Keep install commands copyable. If a repository owner or URL is unknown, label the placeholder clearly instead of presenting it as a ready-to-run command.
- If bilingual content is requested, provide a language switch and keep both language sections structurally aligned.

## Missing Information

Ask a short follow-up only when a required choice cannot be inferred safely, such as target package name, release version, or whether a breaking change is intended. Otherwise:

- Use `TBD` or `TODO` for specific missing values.
- State assumptions briefly.
- Prefer optional sections that disappear when no evidence exists.

## Repository Maintenance

When updating this skill repository itself:

- Keep `SKILL.md` as the concise runtime router.
- Put scenario-specific rules in the matching `reference/*.md`.
- Keep `INDEX.md` as navigation only.
- Treat `DOCS/` as design notes and `test/` as validation material.
- Update README-facing lessons in `reference/readme.md` so future README drafts do not repeat the same mistakes.
