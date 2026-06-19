---
name: oh-my-gh-writing
description: "Draft and revise GitHub-facing writing artifacts: issues, PR descriptions, code reviews, commit messages, README/CONTRIBUTING/CHANGELOG docs, release notes, migration guides, RFCs, issue forms, PR templates, and local multi-file release/launch/contribution workflow packs. Use only for GitHub repository artifacts; do not use for generic prose, UI copy, marketing, or code implementation."
---

# oh-my-gh-writing

GitHub writing skill for AI agents. Route the request, load the matching standard, keep evidence boundaries explicit, and produce near-submission-ready GitHub drafts.

## Trigger Boundary

Use this skill for GitHub-facing writing artifacts and local GitHub writing draft packages. Do not use it for general copywriting, UI text, code implementation, product strategy, or broad documentation work unless the requested output is a GitHub artifact or GitHub repository file.

## Workflow

1. Identify whether the user wants a single artifact or a multi-artifact workflow pack.
2. If the user explicitly names a single artifact, route to that artifact even if the topic is broad.
3. If the user asks for a broad workflow, launch, setup, release package, or end-to-end material set, route to the matching composite workflow pack.
4. If the user asks to inspect, check, review readiness, or recommend what files are needed, treat it as audit-only: output a gap analysis and next-file recommendations only. Do not create target files, do not create `.github-writing/`, and do not write `.github/` or root repository files unless the user explicitly asks to draft, create, write, apply, or update files.
5. For README requests, use the three-question prompt in `references/readme.md`.
6. For composite workflow packs, follow the pack's Decision Rule. Ask the package-selection question only when the package shape cannot be inferred safely; otherwise use the recommended default and record it in `package-manifest.md`.
7. Explicitly open and read the matching `references/*.md` before writing user-facing output. Do not infer or guess reference contents from memory.
8. Read only the single-artifact references selected by a composite pack. Do not preload every reference.
9. Read `references/weapons.md` when badges, alerts, Mermaid, collapsible blocks, emoji, or complex tables are needed.
10. Read `references/badge-catalog.md` only when the user asks for detailed badge design or exact shields.io URL patterns.
11. Read `references/emoji-guide.md` when emoji is requested or the target repository already uses emoji.
12. Read `references/shared-principles.md` when the request is fact-heavy, high-risk, cross-scenario, or when output quality rules need clarification.
13. Before finalizing, use `references/output-validation.md` as a silent revision checklist. If the draft fails a check, revise it before delivering. Keep validation silent for small clean artifacts; add brief post-output submission notes only when the artifact is complex, high-risk, or has obvious blockers.

If local file reading is unavailable, ask the user to provide the relevant `references/*.md` content or state that references are unavailable and produce only a conservative draft from the visible routing rules and shared principles. Do not pretend to have read files you cannot access.

Progressive disclosure: load only files needed for the current task. When several references are truly needed and the platform supports batched reads, read them in one batch instead of serial tool calls.

Language fidelity: match the user's requested language or the target repository's primary language. The language of this skill's instructions must not leak into the final GitHub artifact.

## Scenario Routing

See `INDEX.md` for the complete list of 18 single-artifact standards and 7 composite workflow packs.

Use these top-level routing rules:

| Signal | Route to |
|--------|----------|
| The user asks for one explicit artifact, such as "write release notes" or "create a PR template" | The matching single-artifact reference |
| The user asks for a release package, version update materials, major release prep, or software update bundle | `references/version-release.md` |
| The user wants to publish or open-source a repository for the first time | `references/project-launch.md` |
| The user wants a project ready for outside contributors | `references/contribution-setup.md` |
| The user wants to handle a bug from report or triage through a fix PR | `references/bug-fix-workflow.md` |
| The user wants to turn an idea into discussion, design, issue, and implementation materials | `references/proposal-to-implementation.md` |
| The user wants a breaking-change communication package | `references/breaking-change-package.md` |
| The user wants a broad documentation refresh or docs overhaul | `references/docs-overhaul.md` |

When the prompt mixes issue, PR, and discussion language:

| Signal | Route to |
|--------|----------|
| Future capability request with no implemented diff | Feature Request |
| Improvement to existing behavior | Enhancement |
| Community input with undecided solution | Discussion |
| Branch, diff, or PR implements a new capability | Feature PR |
| Branch, diff, or PR fixes a bug or regression | Bug Fix PR |
| Change reorganizes code without behavior change | Refactor PR |
| Only documentation changed | Documentation PR |
| User asks to review code, a PR, or a diff | Code Review |

If the user asks to turn a PR, postmortem, or discussion into a different artifact, route by the requested artifact, not the source material.

## Composite Workflow Defaults

Composite workflow packs are orchestrators, not templates. They select which existing single-artifact standards to load.

- Audit-only prompts produce recommendations, not package files.
- Ask one package-selection question only when the pack's Decision Rule cannot safely choose a default.
- When a default is chosen without asking, record the selected option and assumptions in `package-manifest.md`.
- Include optional supplements in the same message.
- Default output location is local draft files under `.github-writing/<pack-name>/<version-or-date>/`.
- If no version or date is known, use `.github-writing/<pack-name>/TBD/`.
- Include `package-manifest.md` in every composite package, listing generated files, assumptions, `TODO` / `TBD` fields, files safe to write, and files requiring maintainer confirmation.
- If file writing is unavailable, display the package as multi-file chat output using `## File: ...` headings and fenced blocks. Do not claim files were written.
- Do not publish, create GitHub releases, push tags, open PRs, or modify remote state unless the user explicitly asks.

## Reference Index

Load `INDEX.md` for full navigation. Common reference groups:

| Group | References |
|-------|------------|
| Issues | `bug-report.md`, `feature-request.md`, `enhancement.md`, `discussion.md` |
| Pull requests | `feature-pr.md`, `bug-fix-pr.md`, `refactor-pr.md`, `documentation-pr.md` |
| Review and commit | `code-review.md`, `standard-commit.md` |
| Docs | `readme.md`, `contributing.md`, `changelog.md` |
| Release and design | `release-notes.md`, `migration-guide.md`, `rfc.md` |
| Templates | `issue-form-yaml.md`, `pr-template.md` |
| Composite packs | `version-release.md`, `project-launch.md`, `contribution-setup.md`, `bug-fix-workflow.md`, `proposal-to-implementation.md`, `breaking-change-package.md`, `docs-overhaul.md` |
| Appendices | `shared-principles.md`, `weapons.md`, `badge-catalog.md`, `emoji-guide.md`, `output-validation.md`, `source-catalog.md` |

## Missing Information

Ask a short follow-up only when a required choice cannot be inferred safely, such as target package name, release version, breaking-change intent, output package shape, or a scope choice that changes artifact structure. Otherwise use `TBD` or `TODO`, state assumptions briefly, and remove optional sections when no evidence exists.

## Repository Maintenance

- Keep `SKILL.md` as the thin runtime router.
- Put scenario-specific and composite-pack rules in the matching `references/*.md`.
- Keep `INDEX.md` as navigation only.
- Keep runtime instructions in English by default.
- Update README-facing lessons in `references/readme.md` when README mistakes are discovered.
- Keep local research and validation outputs out of tracked runtime content.
