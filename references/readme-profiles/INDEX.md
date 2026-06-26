# README Profiles Index

Use this index after `references/readme.md` when drafting or revising a README for a known project type.

Read one primary profile by default. Read a second profile only for a genuine hybrid project where it changes Quick Start, applicability, or required evidence.

## Profile Selection

| Project signal | Profile |
| --- | --- |
| `SKILL.md`, prompt pack, rulebase, agent instructions, knowledge-base rules | `agent-skill-rulebase.md` |
| CLI entry point, executable package, developer workflow command | `cli-dev-tool.md` |
| Library, package, SDK, API client, framework integration | `library-sdk.md` |
| GitHub Action, reusable workflow, CI template | `github-action-ci.md` |
| MCP server, plugin, editor/agent extension | `mcp-plugin-extension.md` |
| Web app, SaaS, hosted service, dashboard | `web-app-saas.md` |
| Documentation set, template repo, starter, boilerplate, public rule collection | `docs-template-repo.md` |
| Dataset, model, benchmark, ML/data processing project | `data-model-project.md` |
| Component library, design tokens, UI kit, design system | `design-system-ui-kit.md` |

## Fallback Rule

If the repository type is ambiguous, write the README from `references/readme.md` only and include a `TBD` or `To confirm` note for applicability. Do not invent a project category to make a profile fit.

## Shared Constraints

- The selected profile refines README shape; it does not override evidence boundaries.
- Existing target README structure wins when the user asks to revise an existing README, unless it is clearly broken or misleading.
- Profile-specific badges, install paths, platform support, screenshots, and demos require repository evidence or user input.
