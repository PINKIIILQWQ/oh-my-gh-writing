---
name: oh-my-gh-writing
description: "Use when drafting or revising GitHub issues, PR descriptions, code reviews, commit messages, README, CHANGELOG, release notes, migration guides, RFCs, issue forms, or PR templates."
---

# oh-my-gh-writing

GitHub writing skill for AI agents. Routes requests to the right scenario, loads the matching standard, enforces evidence boundaries, and produces submission-ready artifacts.

## Workflow

1. Identify the scenario from the user's request (see scenario routing below)
2. Estimate artifact length. If >120 lines / 4,000 CJK chars / 2,500 words, ask a brief scope question. For README, use the three-question prompt instead
3. Read the matching `reference/*.md` before writing
4. Read [`reference/weapons.md`](./reference/weapons.md) when badges, alerts, Mermaid, collapsible blocks, emoji, or tables are needed
5. Read [`reference/emoji-guide.md`](./reference/emoji-guide.md) when emoji is requested or the repo already uses emoji
6. Read [`reference/shared-principles.md`](./reference/shared-principles.md) for detailed output quality rules
7. Read [`reference/readme.md`](./reference/readme.md) when the scenario is README (badge rules, multi-language, acknowledgements, support table, table formatting, etc.)
8. Before finalizing, apply [`reference/output-validation.md`](./reference/output-validation.md) mentally — remove wrapper text, stray fences, unsupported facts, and routing mistakes

Progressive disclosure: load only the files needed for the current task. Do not preload everything.

## Quick Start

以下是三种典型用法，用户说出类似指令即可触发对应场景：

| 用户指令 | 匹配场景 | Agent 行为 |
|---------|---------|-----------|
| `帮我写个 Bug Report，描述 Vite 构建时 Module not found 的问题` | Bug Report | 加载 `reference/bug-report.md` → 输出复现步骤、环境、期望/实际对比。仓库有 Issue 模板时自动读取字段 |
| `review 这个 PR：https://github.com/owner/repo/pull/123` | Code Review | 加载 `reference/code-review.md` → 读 diff → 按文件/行号输出发现，标注 blocking/major/minor/nit |
| `给这个项目写个 README` | README | 加载 `reference/readme.md` → 先问三个问题（交付方式、风格、补充内容）→ 按标准结构输出 |

每个场景的具体标准文件见下方表格。

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
| [`reference/shared-principles.md`](./reference/shared-principles.md) | Any artifact — 19 output quality rules (usable first, evidence boundaries, formatting, drafting) |
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
