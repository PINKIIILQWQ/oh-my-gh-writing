---
name: oh-my-gh-writing
description: "Use when drafting or revising GitHub issues, PR descriptions, code reviews, commit messages, README, CHANGELOG, release notes, migration guides, RFCs, issue forms, or PR templates."
---

# oh-my-gh-writing

Use this skill as a GitHub writing operating system for AI agents. Keep the runtime path narrow: classify the request, load only the relevant reference file, enforce evidence boundaries, validate output cleanliness, and produce the requested Markdown or YAML.

## Workflow

1. Identify the scenario from the user's request.
2. Estimate whether the artifact is short-form or long-form. If the expected artifact is likely to exceed about 120 lines, 4,000 Chinese characters, or 2,500 English words, ask a brief scope question first unless the user explicitly asks for a one-shot draft. For README tasks, use the three-question prompt in step 3 instead of asking an extra long-form question.
3. If the task is to write or revise a README, ask the README three-question prompt in one message before drafting unless the user explicitly says to skip questions or draft immediately. Do not perform a GitHub upload or push as the first pass.
4. Even when source code is available, do not skip the README questions unless the user has already explicitly chosen the delivery mode, style/visual direction, and required supplemental content.
5. Read the matching `reference/*.md` file before writing the final output.
6. Read [`reference/weapons.md`](./reference/weapons.md) only when badges, alerts, collapsible logs, Mermaid, tables, emoji, Star History, or other formatting tools are needed.
7. Read [`reference/emoji-guide.md`](./reference/emoji-guide.md) only when emoji usage is requested, the existing repository style uses emoji, or README/PR title visual style requires emoji.
8. Read [`INDEX.md`](./INDEX.md) only for full repository navigation or maintenance work.
9. Before finalizing, apply [`reference/output-validation.md`](./reference/output-validation.md) mentally to remove wrapper text, test metadata, stray fences, unsupported facts, and scenario-routing mistakes.

Do not load every reference file for a normal writing request. Do not expose reference-project analysis in user-facing output unless the user explicitly asks for rationale or sources. Do not add internal validation metadata such as scenario id, source notes, input prompt, raw output markers, or verdict unless the user explicitly asks for a validation report.

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

Scenarios < 20: list all above. If ≥20 scenarios added in future, replace this table with a link to `INDEX.md`.

## Routing Rules

Use these rules when the prompt mixes issue, PR, and discussion language:

| Signal | Route to |
|--------|----------|
| User wants future support for a new capability and no implementation diff exists | Feature Request |
| User wants to improve an existing behavior, API, performance, or ergonomics | Enhancement |
| User wants community input and the solution is not decided | Discussion |
| User says a branch, diff, or PR implemented a new capability | Feature PR |
| User says a branch, diff, or PR fixes a bug, regression, root cause, or failing behavior | Bug Fix PR |
| User says the change reorganizes code, renames, moves files, or updates imports without behavior changes | Refactor PR |
| User says documentation changed and no runtime code changed | Documentation PR |
| User asks to review code, a PR, or a diff | Code Review |

If the user asks to turn a PR, implementation, or postmortem into a future request, route by the requested artifact, not by the source material. For example, "rewrite PR #178 as a Feature Request" is Feature Request, not Feature PR.

## Shared Principles

1. Make the output usable first. If information is missing, write a reasonable draft and mark assumptions or TODO fields instead of blocking on nonessential questions.
2. Preserve existing repository style when editing an existing file: heading depth, terminology, date format, label names, link style, and language choice.
3. Keep one artifact focused on one job. Split unrelated bugs, features, or release notes instead of blending them into one issue or PR.
4. Put critical information in the body, not only behind links.
5. Record reproducible context: versions, platform, environment, affected commands, expected behavior, actual behavior, and tests where relevant.
6. Use clear, neutral language. Prefer precise impact and verification over persuasion.
7. Treat user-provided facts, repository files, tool output, and verified links as the only factual source. Do not copy project facts from unrelated reference material into the user's artifact.
8. Do not invent CI status, versions, compatibility, benchmarks, screenshots, links, issue numbers, PR numbers, file paths, line numbers, package-manager install commands, release URLs, deprecation dates, migration timelines, or support matrices. If evidence is unavailable, omit the claim or label it as `TODO` / `TBD`.
9. Do not mark checkboxes as completed unless the user, diff, repository, or tool output proves they are done. Use unchecked boxes, "N/A", or a `Verification to run` section for unknown work. Templates and future-work checklists should stay unchecked by default.
10. Do not turn hypotheses into conclusions. Use "Suspected cause", "Likely cause", or "Needs confirmation" unless the root cause is shown by code, logs, or the user's explicit statement.
11. Use fenced code blocks with language hints for multi-line code, config, diffs, YAML, JSON, logs, or templates. Do not use raw HTML `<code>` blocks to force formatting.
12. For templates and YAML, separate display wrappers from file content. In chat, use headings plus fenced blocks when multiple files are requested; when editing or generating a single target file, produce valid file content without explanatory wrappers.
13. For current tool, agent, platform, API, or installation support claims, verify availability in official documentation before writing the claim or example. Link the official source when the output includes a support matrix or install guide.
14. For README drafting, keep the first response as a draft or a clarification step; only upload or push after the user explicitly approves the content and delivery path.
15. Use follow-up questions as a scope-control tool, not as a questionnaire. Ask at most three questions before drafting; choose defaults for low-risk style choices and state them briefly.
16. Output only the target GitHub artifact unless the user explicitly asks for explanation. Do not add conversational prefaces, test titles, outer `markdown` fences, source lists, or "you can copy this" wrappers to artifact content.
17. Fact-heavy scenarios require evidence. Versions, release dates, PR/issue numbers, CI workflow names, package-manager commands, platform support, dependency versions, migration timelines, screenshots, and links must come from user input, repository files, diffs, tool output, or official sources. Unknown facts become `TODO`, `TBD`, or "To confirm".
18. Never claim a test, check, benchmark, build, or review passed unless it was actually run or provided. For unknown verification, write "Verification to run" or leave checklist boxes unchecked.
19. **优先遵循目标仓库已有格式。** 写入或修改文件前，先检查目标仓库是否已有同类文件（README、CONTRIBUTING、CHANGELOG 等）。如果有，以其格式、风格、结构为准，本 skill 的 reference 仅作补充。如果没有，再使用本 skill 的参考规则。

## Reference Source Policy

Reference links in `reference/*.md` are evidence for structure and field design, not facts to copy into the user's artifact. For normal writing tasks, read the selected scenario rules and treat the links as maintenance context, not runtime material to quote or summarize. The fuller source inventory lives in [`reference/source-catalog.md`](./reference/source-catalog.md) and is for audits, maintenance, and release credibility checks.

- Keep each scenario to about 5-6 high-quality references.
- Prefer official specifications, official platform docs, current template files, contribution guides, single high-quality release pages, RFC templates, or migration guides.
- Avoid using search pages, PR lists, issue lists, discussion lists, repository homepages, or release indexes as primary evidence.
- A 100k+ star repository may be reused across 2-3 scenarios when it has genuinely strong artifacts for each scenario.
- If a reference link breaks or becomes too generic, remove or replace it before relying on that scenario reference.
- Keep scenario rules independent from reference-project facts. Never transfer project-specific versions, commands, test status, labels, file paths, or issue numbers from a reference project into the user's target artifact.

## README Guardrails

When the scenario is README, follow `reference/readme.md` and apply these extra constraints:

- Treat the README as a public entry page, not a dump of every internal file.
- Before producing or editing a README from source code, confirm whether the user wants a local markdown draft, a chat-only draft, or a remote repository update. Do not assume upload is authorized because source code is available.
- **Title & logo default to centered.** Use `<p align="center">` for the logo image and `<h1 align="center">` for the title. Do not ask — center by default.
- **Badge rules:**
  - Badge 写法遵循 [`reference/weapons.md`](./reference/weapons.md)，包含完整的摆放惯例、优先级顺序和 200+ URL 模式。
  - 如果 shields.io 动态 badge 因数据源不存在返回 error/unknown，跳过该 badge 并告知用户。不重复 badge，同一意图只用一个。
  - 默认 3–6 个，按优先级：CI → Version → License → Downloads → Security/Social。
- **Scenario index in README:** If scenarios < 20, list all rows in a complete table. If ≥20 scenarios, replace with a link: "See all scenarios in [INDEX.md](INDEX.md)". Do not enumerate 20+ items inline.
- For README work, ask exactly three concise questions in one message before drafting unless the user explicitly says to skip questions or draft immediately:
  1. Delivery: local markdown file, chat-only draft, or remote repository update after review?
  2. Style and visuals: documentation-first, community/product style, title/heading emoji, badges, screenshots, or Star History?
  3. Required supplements: languages, official website, docs/demo URL, screenshot assets, reference projects or acknowledgements, file index, or any other must-include content?
- **Multi-language README:**
  - Default to English plus the language used in the user conversation. If the user uses English, do not list a second default language.
  - If the user signals "最多语言", "多语言", "尽量多语言", "3个及以上语言版本", "as many languages as possible", "all languages", or explicitly names 3+ languages, produce the full set: **zh-CN** (README.md), **en** (README.en.md), **ja** (README.ja.md), **ko** (README.ko.md), **es** (README.es.md), **fr** (README.fr.md), **de** (README.de.md), **pt** (README.pt.md). Include the same badges, centered logo, and project structure in each. Use separate files per language — do not stack multiple languages in one file.
  - If the user asks for multilingual output without specifying which languages, ask which languages to include as part of the README three-question prompt. Do not default to a large set.
- For skill repositories, explain that the project is a portable writing skill, not a standalone app, README generator, or GitHub integration.
- Keep runtime files focused: `SKILL.md` and `reference/` define behavior. Local research, examples, and validation outputs are not public runtime inputs unless the repository intentionally publishes them.
- Keep install commands copyable. If a repository owner or URL is unknown, label the placeholder clearly instead of presenting it as a ready-to-run command.
- **Agent & platform support table:**
  - 对于此项目，支持表横跨的通用的不一定是 Agent（可能取决于实际需求确认），覆盖的类型选择最合适的纵列（如框架、平台、技术栈、工具），本 skill 以 Agent 为例。
  - Research the latest official docs before writing support claims. Link each agent's docs.
  - The table must include: icon, agent name, support level, exact method, official docs link.
  - 主流 agent **尽可能多写**，不超过 20。分为三类：
    1. **Direct** — 原生支持 Agent Skills（`SKILL.md` 格式）
    2. **Adapted** — 不支持原生 SKILL.md，但有自有规则体系可适配导入
    3. **Not supported** — 主流 agent 但不支持规则定制，标注为"暂不支持"
  - For each agent, write a clear **adaptation scope**: what the skill covers and any limitations.
  - Include at least one direct-install example and one adapted-import example.
  - Base every agent support row and install example on current official docs. Do not infer that an agent can load this skill format merely because it supports prompts, rules, custom instructions, or another vendor's skill system.

## Missing Information

Ask a short follow-up only when a required choice cannot be inferred safely, such as target package name, release version, whether a breaking change is intended, or a long-form scope/style choice that would change the artifact structure. Otherwise:

- Use `TBD` or `TODO` for specific missing values.
- State assumptions briefly.
- Prefer optional sections that disappear when no evidence exists.

## Repository Maintenance

When updating this skill repository itself:

- Keep `SKILL.md` as the focused runtime router.
- Put scenario-specific rules in the matching `reference/*.md`.
- Keep `INDEX.md` as navigation only.
- Keep local research and validation runs out of tracked repository content unless they are intentionally published.
- Update README-facing lessons in `reference/readme.md` so future README drafts do not repeat the same mistakes.
