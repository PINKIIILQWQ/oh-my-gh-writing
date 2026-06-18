# Shared Principles

These principles apply to all GitHub artifacts produced by this skill. They are referenced from `SKILL.md` and only loaded when needed.

## Output Quality

1. **Usable first.** If information is missing, write a reasonable draft and mark assumptions or TODO fields instead of blocking on nonessential questions.
2. **Preserve existing style.** When editing an existing file, match its heading depth, terminology, date format, label names, link style, and language choice.
3. **One artifact, one job.** Split unrelated bugs, features, or release notes instead of blending them into one issue or PR.
4. **Put critical information in the body**, not only behind links.
5. **Record reproducible context:** versions, platform, environment, affected commands, expected behavior, actual behavior, and tests where relevant.

## Language & Evidence

6. **Clear, neutral language.** Prefer precise impact and verification over persuasion.
7. **Match the artifact language.** Use the user's requested language or the target repository's primary language. Do not let the language of this skill's instructions leak into the artifact.
8. **Only user-provided facts, repository files, tool output, and verified links are factual sources.** Do not copy project facts from unrelated reference material into the user's artifact.
9. **Do not invent** CI status, versions, compatibility, benchmarks, screenshots, links, issue numbers, PR numbers, file paths, line numbers, package-manager install commands, release URLs, deprecation dates, migration timelines, or support matrices. If evidence is unavailable, omit the claim or label it as `TODO` / `TBD`.
10. **Do not mark checkboxes as completed** unless the user, diff, repository, or tool output proves they are done. Templates and future-work checklists stay unchecked by default.
11. **Do not turn hypotheses into conclusions.** Use "Suspected cause", "Likely cause", or "Needs confirmation" unless the root cause is shown by code, logs, or the user's explicit statement.

## Formatting

12. **Use fenced code blocks with language hints** for multi-line code, config, diffs, YAML, JSON, logs, or templates. Do not use raw HTML `<code>` blocks.
13. **For templates and YAML,** separate display wrappers from file content. In chat, use headings plus fenced blocks when multiple files are requested. For a single target file, produce valid file content without explanatory wrappers.
14. **Current tool, agent, platform, API, or installation support claims** must be verified in official documentation before writing. Link the official source when the output includes a support matrix or install guide.

## Drafting

15. **For README drafting,** keep the first response as a draft or a clarification step; only upload or push after the user explicitly approves the content and delivery path.
16. **Use follow-up questions as a scope-control tool, not a questionnaire.** Ask at most three questions before drafting; choose defaults for low-risk style choices.
17. **Output only the target GitHub artifact** unless the user explicitly asks for explanation. No conversational prefaces, test titles, outer `markdown` fences, source lists, or "you can copy this" wrappers.
18. **Fact-heavy scenarios require evidence.** Versions, release dates, PR/issue numbers, CI workflow names, package-manager commands, platform support, dependency versions, migration timelines, screenshots, and links must come from user input, repository files, diffs, tool output, or official sources. Unknown facts become `TODO`, `TBD`, or "To confirm".
19. **Never claim a test, check, benchmark, build, or review passed** unless it was actually run or provided.
20. **Prefer the target repository's existing format.** Before writing or editing a file, check whether the target repository already has the same artifact type, such as README, CONTRIBUTING, or CHANGELOG. If it exists, match that format, style, and structure; use this skill's references only as supplements.
