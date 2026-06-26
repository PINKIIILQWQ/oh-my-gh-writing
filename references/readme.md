# README Standard

When routing to README, apply these detailed rules in addition to the top-level constraints in `SKILL.md`.

## Positioning

Treat the README as a public entry page, not a dump of every internal file. For skill repositories, explain that the project is a portable skill or rulebase, not a standalone app, README generator, or GitHub integration unless that is true.

## Required README Prompt

Before drafting a README, ask one compact message with three required choices. Each choice must provide three options, put the recommended option first, and allow the user to add supplements in the same reply.

Use this shape:

```text
Before I draft the README, please choose:

1. Delivery
   A. Local Markdown file (Recommended)
   B. Chat-only draft
   C. Remote repository update after review

2. Style & visuals
   A. Documentation-first with badges and concise tables (Recommended)
   B. Community/product style with richer visuals
   C. Minimal plain Markdown

3. Required supplements
   A. Applicability scope + install/usage + file index (Recommended)
   B. Multilingual README + language switcher
   C. Visual assets / screenshots / Star History / acknowledgements

Add any extra requirements in the same reply, such as official website, docs/demo URL, supported frameworks/products/platforms/runtimes/integrations, title emoji preference, reference projects, or files that must be included.
```

If the user already supplied an answer, do not ask again. If the user explicitly says to skip questions, draft using the recommended options and state assumptions briefly.

## Title & Logo

Title and logo default to centered. Use `<p align="center">` for the logo image and `<h1 align="center">` for the title. Do not ask separately unless the user requests a different style.

## Badge

Badge writing follows `weapons.md`. If the user requests detailed badge design or exact shields.io URL patterns, read `badge-catalog.md`.

Project-fit check before writing badges:

- Add a CI badge only if CI config exists.
- Add a package version badge only if the package is published to a registry such as npm, PyPI, crates.io, or GitHub Releases.
- Add a downloads badge only if a real data source exists.
- Do not create virtual badges for missing data. Ask or omit when uncertain.

If a shields.io dynamic badge returns error/unknown because the data source does not exist, skip it and mention the reason. Avoid duplicate badges; one badge per intent. Default to 3-6 badges in this order: CI, Version, License, Downloads, Security/Social.

## Table Formatting

Tables must have blank lines before and after them, use normal alignment rows such as `| --- | --- |`, and keep each row independent. If a table exceeds 5 columns or cells exceed about 30 words, split it into smaller tables or use lists. Avoid cramped text.

## Brand / Tool Icons

When README tables or lists mention brands, tools, frameworks, platforms, or projects, default to an official icon or stable favicon. Priority: official favicon/logo asset, simple-icons/skillicons/devicon, stable favicon aggregator, then omit. If a direct favicon returns 403, 404, HTML, or does not render on GitHub, use a stable favicon aggregator. Do not invent icons.

Icons must have `alt`. In tables, default to `width="24" height="24"`; use 18px only for especially compact tables. Do not use 14px. Brand/tool names link to official sites, docs, or repositories. Icons should link to the same official destination. Use `Icon` as the column name.

Do not store third-party brand logos in this repository's `assets/`; keep `assets/` for project-owned visuals only. If icon stability, licensing, or maintenance cost is not worth it, omit the icon column entirely.

## Section Completeness

Core explanatory sections such as Overview, Quick Start, Usage, Configuration, and Architecture need real substance, not one-line slogans. Entry sections such as License, Contributing, Links, and Acknowledgements may be short. Merge or omit sections with no real information.

GitHub recognizes README files in `.github/`, repository root, and `docs/`, in that display priority. For ordinary project homepages, prefer the repository root unless the target repository already uses another supported location. Keep README focused on getting started, usage, help, maintainers, and contribution entry points; do not turn it into a full docs site. GitHub truncates very large README files, so move long reference material into linked docs.

## Good Output Shape

```markdown
## Quick Start
<first reliable install command>

## Applicability
<who and what environments this project actually supports>
```

## Common Failure

- Putting the first runnable install command below long feature tables.
- Listing platforms or frameworks without repository evidence.
- Linking language README files that were not generated.

## Quick Start Placement

For installable tools, agent skills, CLIs, plugins, templates, SDKs, or libraries, place Quick Start immediately after the short overview and before long rationale, support, or architecture sections. Start with the shortest reliable install command, then add host-specific or manual alternatives. Do not bury the first runnable command below broad applicability or feature tables.

When a project supports both a universal installer and manual clone/symlink paths, use this order:

1. Shortest credible one-line installer when it reduces onboarding friction; disclose immediately when it installs the full repository rather than the minimal runtime.
2. A collapsible minimal runtime-only install or update path for users who need only the declared runtime files.
3. Optional target-host command variants inside a collapsible section when they would otherwise crowd the first screen.
4. One or more example prompts or usage commands.

Do not describe a package-manager install as runtime-only unless it has been tested for that repository. If the installer fetches or copies the full repository, say so plainly and provide a visible runtime-only alternative. A manual runtime-only command should copy only the declared runtime files into a fresh target directory.

For a runtime-only install or update, build and validate a staging directory before replacing the target. Preserve an existing target as a backup; do not merge files into it and then describe the result as minimal. Keep this advanced flow collapsible when a simple installer is available.

Quick Start command blocks must be easy to copy line-by-line:

- Put each standalone command or variable assignment on its own line.
- Avoid `&&`, `;`, and backslash continuations for independent commands.
- If several hosts differ only by target path, show each host's `target=...` line as its own copyable block, then show the shared install commands separately.
- Keep comments outside command blocks unless a shell comment is essential.

## Public Examples And Cases

Keep public examples near the main example/prompt section, not as a detached duplicate gallery near the bottom of the README. A short featured case excerpt can follow the example prompt table, and other cases can be listed after it.

When showing a public case excerpt:

- Mark whether it is synthetic, review-draft, sanitized, or validated.
- State whether baseline behavior has been collected.
- Keep the excerpt short and link to the full `cases/<id>/` directory.
- Say when the excerpt is shortened or paraphrased.
- Do not imply a real repository outcome unless the source and attribution prove it.

Do not treat `cases/` as runtime material. It is public evidence and maintenance material only; `SKILL.md` must not ask agents to load cases automatically while drafting user artifacts.

## Project Applicability Scope

Every README must state project applicability scope. It answers which users, environments, frameworks, platforms, products, runtimes, integrations, or artifact types the project applies to. It is not a feature list, marketing pitch, usage scenario list, or example gallery.

Small projects can include one paragraph or 3-5 bullets in Overview or Usage. Tools, frameworks, AI products, plugins, templates, SDKs, and platforms should use a dedicated `Applicability`, `Supported Targets`, or `Compatibility` section or table.

Do not confuse built-in features with applicability scope. For example, this project has 18 GitHub artifact standards and workflow packs as product capabilities; its applicability scope is the agent products, rule hosts, knowledge bases, and GitHub writing workflows that can use it.

Scope claims must be evidence-based: repository files, user input, config, dependencies, existing docs, or official sources. Unknown scope becomes `TBD`, `To confirm`, or omitted. Do not write "theoretically usable" as "supported".

Useful scope terms:

- **Libraries / frameworks:** language, runtime, framework versions, package manager, modules/plugins, target developers.
- **CLI / developer tools:** operating systems, shells, runtime, package manager, config files, local/CI workflows.
- **Web apps / SaaS:** browsers, deployment targets, user roles, auth providers, data sources, admin/user workflows.
- **APIs / SDKs:** protocol, auth method, client languages, server runtime, API version, environments, rate limits.
- **Agent skills / prompt packs / AI products:** agent products, host apps, load paths, native skill support, adapted rules/custom instructions, unsupported direct loading.
- **MCP servers / plugins / extensions:** host clients, transport, permissions, auth, local/remote boundary, supported commands.
- **GitHub Actions / CI templates:** events, runners, permissions, required secrets, target repository types.
- **Data / model projects:** input formats, output formats, tasks, model/runtime requirements, hardware, dataset/license boundaries.
- **Mobile / desktop apps:** OS versions, architectures, device types, distribution channels.
- **Infrastructure / DevOps:** cloud providers, Kubernetes/Terraform/Helm versions, regions/environments, required permissions.
- **Design systems / UI kits:** UI frameworks, styling stack, component libraries, design tools, theming modes.
- **Docs / templates / rulebases:** target artifact types, audience, required host format, conversion/adaptation paths.

## Scenario Index

If scenarios or standards are under 20, a complete table is acceptable. If 20 or more items exist, use grouped tables or link to `INDEX.md`; do not force a single crowded table.

## Multi-language

Default languages: English plus the language used in the user conversation. If the user uses English, default to English only.

For this skill repository's public documentation, maintain only `README.md` as the English default homepage and `README.zh-CN.md` as the Simplified Chinese secondary page unless the maintainer explicitly requests additional languages.

When asking about languages, include the default value. Example for a Chinese conversation: `Target languages (default: English + Simplified Chinese)`. Example for English: `Target language (default: English)`.

If the user asks for multilingual output but does not specify languages, include language choice in the required README prompt. Do not default to a large language set.

Add language switch links only when those README files will be generated or already exist. Do not link nonexistent `README.*.md` files.

If the user wants multilingual output, suggested candidates are English, Simplified Chinese, Spanish, Hindi, Arabic, French, Portuguese, Japanese, and Korean. Final languages follow user confirmation or existing files.

## Acknowledgements

Add Acknowledgements or Thanks only when repository files, dependencies, user input, existing README, or source catalog evidence shows real usage, reference, derivation, inspiration, or resource origin. Each referenced project must state the relationship, such as "structure inspired by X", "badge pattern follows Y", or "icons from Z". Do not write vague thanks or imply endorsement, dependency, or license relationship that does not exist.

## Contributing in README

If the repository has `CONTRIBUTING.md` or is intended for external contributors, include a short Contributing entry and link to the full rules. Do not force an external contribution process into private, one-off, internal, or no-contribution projects.

When a public repository is being prepared for launch, mention only community files that exist or are being drafted: contribution guide, issue forms, PR template, code of conduct, support resources, security policy, citation file, funding links, or CODEOWNERS. Do not imply those files exist before they do.

## Target Repository Templates

For a README tied to a known target repository, read `target-repository.md` before drafting. Inspect the current README, nearby documentation, and contribution or release docs only when they are relevant to the requested update. Preserve demonstrated project conventions without copying unsupported claims or unrelated policy.

## Agent / Platform Support Table

When a README includes a support table:

- The table axis should match the project, such as frameworks, platforms, tech stacks, tools, or agents.
- Verify current official docs before writing support claims, and link each row to official docs.
- Include name, recommended setup, and notes or official docs. Add an icon column only when icon sources are stable and worth maintaining.
- Do not force platform tiers. Say whether the project is used as a skill directory, project rule, custom instruction, knowledge base, or "check current docs".
- Each row should state what is covered and what is limited.
- Omit icons when no stable source exists. Do not invent support claims.
