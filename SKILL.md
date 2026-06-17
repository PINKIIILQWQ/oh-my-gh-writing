---
name: oh-my-gh-writing
description: "Use when drafting or revising GitHub issues, PR descriptions, code reviews, commit messages, README, CHANGELOG, release notes, migration guides, RFCs, issue forms, or PR templates."
---

# oh-my-gh-writing

GitHub writing skill for AI agents. Routes requests to the right scenario, loads the matching standard, enforces evidence boundaries, and produces near-submission-ready GitHub drafts.

## Workflow

1. Identify the scenario from the user's request (see scenario routing below)
2. Ask a brief scope question when the user requests an exhaustive, all-in-one, or clearly oversized artifact. For README, use the three-question prompt instead
3. **Critical:** explicitly open and read the matching `reference/*.md` before writing user-facing output. Do not infer or guess the reference contents from memory
4. Read [`reference/weapons.md`](./reference/weapons.md) when badges, alerts, Mermaid, collapsible blocks, emoji, or tables are needed
5. Read [`reference/badge-catalog.md`](./reference/badge-catalog.md) only when the user asks for detailed badge design or exact shields.io URL patterns
6. Read [`reference/emoji-guide.md`](./reference/emoji-guide.md) when emoji is requested or the repo already uses emoji
7. Read [`reference/shared-principles.md`](./reference/shared-principles.md) when the request is fact-heavy, high-risk, cross-scenario, or output quality rules need clarification
8. Read [`reference/readme.md`](./reference/readme.md) when the scenario is README (badge rules, multi-language, acknowledgements, support table, table formatting, etc.)
9. Before finalizing, use [`reference/output-validation.md`](./reference/output-validation.md) as a silent revision checklist. If the draft fails a check, revise it before delivering. Do not output validation notes unless the user asks

If local file reading is unavailable, ask the user to provide the relevant `reference/*.md` content or state that references are unavailable and produce only a conservative draft from the scenario routing and shared principles. Do not pretend to have read files you cannot access.

Progressive disclosure: load only the files needed for the current task. Do not preload everything. When several references are truly needed and the platform supports it, read them in one batch instead of serial tool calls.

Language fidelity: match the user's requested language or the target repository's primary language. The language of this skill's instructions or reference files must not leak into the final GitHub artifact.

## Quick Start

Typical requests and expected routing:

| User request | Scenario | Agent behavior |
|--------------|----------|----------------|
| `Write a Bug Report for a Vite "Module not found" build failure` | Bug Report | Read `reference/bug-report.md`, then output reproduction steps, environment, expected/actual behavior. Read target repository issue templates only when the user asks to submit to or fill that repository's template |
| `Review this PR: https://github.com/owner/repo/pull/123` | Code Review | Read `reference/code-review.md`, inspect the diff, then report findings by file/line with blocking/major/minor/nit severity |
| `Write a README for this project` | README | Read `reference/readme.md`, ask the three README questions first, then draft using the README standard |

Each scenario's standard file is listed below.

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

Scenarios < 20: list all above. If ≥20 in future, replace with link to `INDEX.md`.

## Routing Rules

Use these when the prompt mixes issue, PR, and discussion language:

| Signal | Route to |
|--------|----------|
| User wants future support for a new capability, no diff exists | Feature Request |
| User wants to improve existing behavior | Enhancement |
| User wants community input, solution undecided | Discussion |
| User says a branch/diff/PR implements a new capability | Feature PR |
| User says a diff/PR fixes a bug or regression | Bug Fix PR |
| User says the change reorganizes code without behavior change | Refactor PR |
| User says only documentation changed | Documentation PR |
| User asks to review code, a PR, or a diff | Code Review |

If the user asks to turn a PR or postmortem into a future request, route by the requested artifact, not the source material.

## Reference Index

| File | When to load |
|------|-------------|
| [`reference/shared-principles.md`](./reference/shared-principles.md) | Fact-heavy, high-risk, cross-scenario, or quality-sensitive requests |
| [`reference/readme.md`](./reference/readme.md) | README scenario — badge rules, multi-language, table formatting, section completeness, acknowledgements, contributing, form priority, support table, 3-question prompt |
| [`reference/bug-report.md`](./reference/bug-report.md) | Bug Report scenario |
| [`reference/feature-request.md`](./reference/feature-request.md) | Feature Request scenario |
| [`reference/enhancement.md`](./reference/enhancement.md) | Enhancement scenario |
| [`reference/discussion.md`](./reference/discussion.md) | Discussion scenario |
| [`reference/feature-pr.md`](./reference/feature-pr.md) | Feature PR scenario |
| [`reference/bug-fix-pr.md`](./reference/bug-fix-pr.md) | Bug Fix PR scenario |
| [`reference/refactor-pr.md`](./reference/refactor-pr.md) | Refactor PR scenario |
| [`reference/documentation-pr.md`](./reference/documentation-pr.md) | Documentation PR scenario |
| [`reference/code-review.md`](./reference/code-review.md) | Code Review scenario |
| [`reference/standard-commit.md`](./reference/standard-commit.md) | Standard Commit scenario |
| [`reference/contributing.md`](./reference/contributing.md) | CONTRIBUTING scenario |
| [`reference/changelog.md`](./reference/changelog.md) | CHANGELOG scenario |
| [`reference/release-notes.md`](./reference/release-notes.md) | Release Notes scenario |
| [`reference/migration-guide.md`](./reference/migration-guide.md) | Migration Guide scenario |
| [`reference/rfc.md`](./reference/rfc.md) | RFC scenario |
| [`reference/issue-form-yaml.md`](./reference/issue-form-yaml.md) | Issue Form YAML scenario |
| [`reference/pr-template.md`](./reference/pr-template.md) | PR Template scenario |
| [`reference/weapons.md`](./reference/weapons.md) | When badges, alerts, Mermaid, tables, or other Markdown tools are needed |
| [`reference/badge-catalog.md`](./reference/badge-catalog.md) | Detailed shields.io URL patterns; load only for exact badge design |
| [`reference/emoji-guide.md`](./reference/emoji-guide.md) | When emoji is requested or repo uses them |
| [`reference/output-validation.md`](./reference/output-validation.md) | Final validation before delivering any artifact |
| [`reference/source-catalog.md`](./reference/source-catalog.md) | Auditing or checking reference source quality |

## Missing Information

Ask a short follow-up only when a required choice cannot be inferred safely (target package name, release version, breaking change intent, or scope choice that changes artifact structure). Otherwise use `TBD` or `TODO`, state assumptions briefly, and let optional sections disappear when no evidence exists.

## Repository Maintenance

- Keep `SKILL.md` as the thin runtime router.
- Put scenario-specific rules in the matching `reference/*.md`.
- Keep `INDEX.md` as navigation only.
- Update README-facing lessons in `reference/readme.md` when README mistakes are discovered.
- Keep local research and validation outputs out of tracked content.
