<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <img src="./assets/oh-my-gh-writing-logo.png" width="160" alt="oh-my-gh-writing logo">
</p>

<p align="center">
  GitHub writing standards for AI agents, packaged as one portable skill.
</p>

<p align="center">
  <a href="./SKILL.md"><img src="https://img.shields.io/badge/format-SKILL.md-2f80ed" alt="SKILL.md"></a>
  <a href="./INDEX.md"><img src="https://img.shields.io/badge/scenarios-18-00a676" alt="18 scenarios"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="MIT license"></a>
</p>

<p align="center">
  <a href="./README.md">中文</a> · English
</p>

---

`oh-my-gh-writing` is a GitHub writing operating system for AI agents. It covers 18 common collaboration scenarios, including issues, pull requests, reviews, commits, README files, changelogs, release notes, RFCs, and GitHub templates, while helping agents route the scenario, respect evidence boundaries, and produce GitHub-ready artifacts.

It is not a README generator or a GitHub App. The project works as a portable writing standard: `SKILL.md` routes the request, `reference/` defines the scenario standards, and the agent produces ready-to-use Markdown or YAML.

## Quick Start

### Local Codex Install

Install it into your Codex user skills directory with one command:

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"
```

If you already have a local checkout, run this from the repository root:

```bash
mkdir -p "$HOME/.agents/skills"
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"
```

You can also hand this prompt to an agent:

```text
Install https://github.com/PINKIIILQWQ/oh-my-gh-writing.git as a Codex skill named oh-my-gh-writing. If the target agent does not support SKILL.md skills, adapt SKILL.md and reference/ into that agent's native rule format.
```

After restarting Codex, use prompts like:

```text
Use oh-my-gh-writing to write a bug report: the first page load is blank for 3 seconds in Chrome, but works in Firefox.

Use oh-my-gh-writing to write a feature PR: OAuth2 login has been implemented.

Use oh-my-gh-writing to write a README for a Rust CLI tool.
```

### Agent Support Matrix

Support levels are checked against each agent's official documentation; each agent name links to the relevant docs. When adding or revising a use case, verify availability from official docs before writing the support claim.

| Icon | Agent | Support | How to connect it |
|------|-------|---------|-------------------|
| <img src="https://icons.duckduckgo.com/ip3/openai.com.ico" width="18" alt="Codex"> | [Codex](https://developers.openai.com/codex/skills) | Direct skill folder install | Put this repository at `$HOME/.agents/skills/oh-my-gh-writing` or repo-local `.agents/skills/oh-my-gh-writing`, keeping both `SKILL.md` and `reference/` |
| <img src="https://icons.duckduckgo.com/ip3/hermes-agent.nousresearch.com.ico" width="18" alt="Hermes Agent"> | [Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | Direct `SKILL.md` URL or skill folder install | Use `hermes skills install`; when full scenario rules are needed, make sure `reference/` is available inside the skill directory |
| <img src="https://icons.duckduckgo.com/ip3/claude.ai.ico" width="18" alt="Claude Code"> | [Claude Code](https://code.claude.com/docs/en/skills) | Direct skill folder install | Link this repository to `~/.claude/skills/oh-my-gh-writing` or project-local `.claude/skills/oh-my-gh-writing` |
| <img src="https://icons.duckduckgo.com/ip3/gemini.google.com.ico" width="18" alt="Gemini CLI"> | [Gemini CLI / Antigravity CLI](https://geminicli.com/docs/cli/skills/) | Verify against current official docs | Gemini CLI currently supports Agent Skills and `gemini skills install`, but availability is migrating; confirm whether Gemini CLI or Antigravity CLI is the right path before release |
| <img src="https://icons.duckduckgo.com/ip3/cursor.com.ico" width="18" alt="Cursor"> | [Cursor](https://cursor.com/docs/rules) | Adapt into Project Rules | Rewrite the `SKILL.md` workflow and the needed `reference/*.md` summaries into `.cursor/rules/oh-my-gh-writing.mdc` |
| <img src="https://icons.duckduckgo.com/ip3/github.com.ico" width="18" alt="GitHub Copilot"> | [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Adapt into custom instructions | Put the core rules in `.github/copilot-instructions.md`; split scenario-specific rules into `.github/instructions/*.instructions.md` when needed |

### Example: Direct Hermes Agent Install

Hermes CLI can install from a remote `SKILL.md` URL. This installs the entry file only; prefer a full folder install when the scenario reference files are needed.

```bash
hermes skills install \
  https://raw.githubusercontent.com/PINKIIILQWQ/oh-my-gh-writing/main/SKILL.md \
  --name oh-my-gh-writing
```

If your Hermes setup downloads only the single `SKILL.md` and cannot read this repository's `reference/`, install the whole folder instead:

```bash
mkdir -p "$HOME/.hermes/skills"
ln -sfn "$PWD" "$HOME/.hermes/skills/oh-my-gh-writing"
```

### Example: Adapt for Cursor

Cursor does not load this repository as a `SKILL.md` skill folder directly. The easiest path is to ask an agent to convert it inside the target project:

```text
Read oh-my-gh-writing's SKILL.md and reference/, then adapt them into Cursor Project Rules:
1. Create .cursor/rules/oh-my-gh-writing.mdc
2. Preserve scenario routing, evidence boundaries, and README guardrails
3. Reference or inline the relevant reference/*.md summaries when needed
4. Do not treat local research or validation material as runtime rules
```

If you do it manually, the minimum rule file is `.cursor/rules/oh-my-gh-writing.mdc`, derived from `SKILL.md`'s Workflow, Scenario Routing, and Shared Principles.

## Scenario Coverage

See the full index in [`INDEX.md`](./INDEX.md).

| Category | Count | Includes |
|----------|-------|----------|
| Issue | 4 | Bug Report, Feature Request, Enhancement, Discussion |
| PR | 4 | Feature PR, Bug Fix PR, Refactor PR, Documentation PR |
| Review / Commit | 2 | Code Review, Standard Commit |
| Docs | 3 | README, CONTRIBUTING, CHANGELOG |
| Release / Design | 3 | Release Notes, Migration Guide, RFC |
| Templates | 2 | Issue Form YAML, PR Template |

## How It Works

```mermaid
flowchart LR
  A["User request"] --> B["Detect scenario"]
  B --> C["Read scenario standard"]
  C --> D["Apply field order and checklist"]
  D --> E["Produce Markdown or YAML"]
```

Default behavior:

- Produce a GitHub-ready draft by default
- Produce a usable draft when information is missing, then mark the gaps clearly
- Preserve existing heading levels, date formats, labels, and link style when updating documents
- Prefer badge navigation, copyable commands, conditional sections, and compact structure for README work

## File Map

| File | Purpose |
|------|---------|
| [`SKILL.md`](./SKILL.md) | Skill entry: scenario routing and shared principles |
| [`INDEX.md`](./INDEX.md) | Full index for all 18 scenarios and their standards |
| [`reference/`](./reference) | Standardized writing rules, field order, checklists, and output validation |
| [`assets/`](./assets) | README logo and project presentation assets |
| [`LICENSE`](./LICENSE) | MIT license |

Final output hygiene and evidence checks live in [`reference/output-validation.md`](./reference/output-validation.md).

## Acknowledgements

README badge and GitHub visual-entry rules were informed by [pudding0503/github-badge-collection](https://github.com/pudding0503/github-badge-collection). This repository uses it as a structural reference and source link, without copying its badge catalog or asset files.

## License

[MIT](./LICENSE). The logo in `assets/` is part of this repository and is distributed under the same MIT license unless otherwise noted.
