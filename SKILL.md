---
name: oh-my-gh-writing
description: "GitHub writing standards for AI agents. Use when drafting or revising GitHub issues, pull request descriptions, code reviews, commit messages, README/CONTRIBUTING/CHANGELOG docs, release notes, migration guides, RFCs, issue forms, or PR templates with concise/full-detail modes and progressive reference loading."
---

# oh-my-gh-writing

Use this skill to produce GitHub-ready writing for common collaboration workflows. Keep the runtime path narrow: classify the request, choose a detail level, load only the relevant reference file, and produce the requested Markdown or YAML.

## Workflow

1. Identify the scenario from the user's request.
2. Choose **concise** mode by default.
3. Use **full-detail** mode only when the user asks for a full-detail/formal output, the change is high-risk, the work is release/migration/design related, or breaking changes are involved.
4. If the task is to write or revise a README, confirm the delivery mode before drafting when it is not already explicit: either provide a local markdown draft for review or a chat-only draft. Do not perform a GitHub upload or push as the first pass.
5. Even when source code is available, do not skip the confirmation step above for README work unless the user has already explicitly chosen the delivery mode.
6. Read the matching `reference/*.md` file before writing the final output.
7. Read [`reference/weapons.md`](./reference/weapons.md) only when badges, alerts, collapsible logs, Mermaid, tables, or other formatting tools are needed.
8. Read [`INDEX.md`](./INDEX.md) only for full repository navigation or maintenance work.
9. When the user asks for real-world examples, case studies, or reference projects for a scenario, read the matching file in [`案例/`](./案例/) after loading the scenario reference.

Do not load every reference file for a concise request. Do not expose reference-project analysis in user-facing output unless the user explicitly asks for rationale or sources. Do not add test-gallery metadata such as `scenario`, `mode`, `case-sources`, or `input-prompt` unless the task explicitly asks for a test output gallery.

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
7. Treat user-provided facts, repository files, tool output, and verified links as the only factual source. Use `案例/` files for structure and style only; do not copy their project facts into the user's artifact.
8. Do not invent CI status, versions, compatibility, benchmarks, screenshots, links, issue numbers, PR numbers, file paths, line numbers, package-manager install commands, release URLs, deprecation dates, migration timelines, or support matrices. If evidence is unavailable, omit the claim or label it as `TODO` / `TBD`.
9. Do not mark checkboxes as completed unless the user, diff, repository, or tool output proves they are done. Use unchecked boxes or a `Verification to run` section for unknown work.
10. Do not turn hypotheses into conclusions. Use "Suspected cause", "Likely cause", or "Needs confirmation" unless the root cause is shown by code, logs, or the user's explicit statement.
11. Use fenced code blocks with language hints for multi-line code, config, diffs, YAML, JSON, logs, or templates. Do not use raw HTML `<code>` blocks to force formatting.
12. For templates and YAML, separate display wrappers from file content. In chat, use headings plus fenced blocks when multiple files are requested; when editing or generating a single target file, produce valid file content without explanatory wrappers.
13. For current tool, agent, platform, API, or installation support claims, verify availability in official documentation before writing the claim or example. Link the official source when the output includes a support matrix or install guide.
14. For README drafting, keep the first response as a draft or a clarification step; only upload or push after the user explicitly approves the content and delivery path.

## README Guardrails

When the scenario is README, follow `reference/readme.md` and apply these extra constraints:

- Treat the README as a public entry page, not a dump of every internal file.
- Before producing or editing a README from source code, confirm whether the user wants a local markdown draft, a chat-only draft, or a remote repository update. Do not assume upload is authorized because source code is available.
- For skill repositories, explain that the project is a portable writing skill, not a standalone app, README generator, or GitHub integration.
- Keep runtime files focused: `SKILL.md` and `reference/` define behavior; `案例/` is supporting material for examples and calibration, not the primary runtime source.
- Use badges only when they answer a real reader question and link to evidence.
- Keep install commands copyable. If a repository owner or URL is unknown, label the placeholder clearly instead of presenting it as a ready-to-run command.
- If bilingual README content is requested, prefer separate files for non-trivial documents, such as `README.md` plus `README.en.md`. Do not stack a full Chinese README above a full English README in the same file.
- For skill repository install docs, separate agents that can load `SKILL.md` or a skill folder directly from agents that require adaptation into native rule, instruction, or command files. Include an icon/name, support level, and exact next step for each listed agent.
- Include at least one direct-install example and one adapted-import example when the README claims cross-agent support.
- Base every agent support row and install example on current official docs. Do not infer that an agent can load this skill format merely because it supports prompts, rules, custom instructions, or another vendor's skill system.

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
- Keep local research and validation runs out of tracked repository content unless they are intentionally published.
- Keep `案例/` useful for review by linking source, raw text, rendered view, and a short structure analysis where applicable.
- Update README-facing lessons in `reference/readme.md` so future README drafts do not repeat the same mistakes.
