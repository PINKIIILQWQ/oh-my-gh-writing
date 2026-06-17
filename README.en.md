<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  🌐 <a href="README.md">中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a>
</p>

<p align="center">
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/blob/main/LICENSE"><img src="https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=License" alt="MIT"></a>
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main"><img src="https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=Updated" alt="Last Commit"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-Agent%20Skill-22AA66?style=flat" alt="Agent Skill"></a>
</p>

**oh-my-gh-writing** is a GitHub writing skill pack for AI agents. It routes common GitHub writing needs — Issues, PRs, READMEs, CHANGELOGs, and more — to the appropriate quality standard, ensuring every output follows community conventions: submission-ready and readable without manual polishing.

The entire rule set is stored as Markdown files in this repository with no external dependencies. Any AI agent that supports loading local skills can use it directly.

## Scenarios

| # | Category | Scenario | When to use |
|---|----------|----------|-------------|
| 1 | Issue | Bug Report | Report a reproducible defect |
| 2 | Issue | Feature Request | Propose a new feature or API |
| 3 | Issue | Enhancement | Improve existing behavior |
| 4 | Issue | Discussion | Open-ended community discussion |
| 5 | PR | Feature PR | Pull Request for a new feature |
| 6 | PR | Bug Fix PR | Pull Request for a bug fix |
| 7 | PR | Refactor PR | Behavior-preserving refactoring |
| 8 | PR | Documentation PR | Documentation-only changes |
| 9 | Review | Code Review | Review code changes |
| 10 | Commit | Standard Commit | Write commit messages |
| 11 | Docs | README | Project homepage documentation |
| 12 | Docs | CONTRIBUTING | Contribution guidelines |
| 13 | Docs | CHANGELOG | Version changelog |
| 14 | Release | Release Notes | Release announcement |
| 15 | Release | Migration Guide | Upgrade guidance |
| 16 | Design | RFC | Design proposal |
| 17 | Templates | Issue Form YAML | GitHub Issue forms |
| 18 | Templates | PR Template | Pull Request template |

Each scenario has a corresponding writing standard file in `reference/`, with standard structure, required fields, evidence boundary rules, high-quality reference sources, and a required-element checklist. When the agent receives a matching writing request, it automatically loads the standard and produces compliant output.

## Quick Start

Load this repository as a Skill in your AI agent:

```bash
# Claude Code — configure in .claude/settings.json or Claude config
# Or reference SKILL.md directly as part of your agent's system instructions
```

In Claude Code, once this repository is added to the agent's available skills, when you make a GitHub writing request ("write a Bug Report", "review this PR"), the agent automatically matches the scenario, loads the corresponding `reference/*.md` standard file, and generates submission-ready content following the specification.

See [`SKILL.md`](SKILL.md) for all scenario rules and routing. Full index at [`INDEX.md`](INDEX.md).

## Project Structure

```
oh-my-gh-writing/
├── SKILL.md                  # Agent entry & scenario routing
├── INDEX.md                  # Full navigation index
├── CONTRIBUTING.md           # Contribution rules
├── LICENSE                   # MIT License
├── .gitignore
├── assets/                   # Project assets
│   └── oh-my-gh-writing-logo.png
├── reference/                # Scenario standard files
│   ├── shared-principles.md  # 19 shared quality rules
│   ├── readme.md             # README writing rules
│   ├── bug-report.md         # Bug Report standard
│   ├── feature-request.md    # Feature Request standard
│   ├── enhancement.md        # Enhancement standard
│   ├── discussion.md         # Discussion standard
│   ├── feature-pr.md         # Feature PR standard
│   ├── bug-fix-pr.md         # Bug Fix PR standard
│   ├── refactor-pr.md        # Refactor PR standard
│   ├── documentation-pr.md   # Documentation PR standard
│   ├── code-review.md        # Code Review standard
│   ├── standard-commit.md    # Standard Commit standard
│   ├── contributing.md       # CONTRIBUTING standard
│   ├── changelog.md          # CHANGELOG standard
│   ├── release-notes.md      # Release Notes standard
│   ├── migration-guide.md    # Migration Guide standard
│   ├── rfc.md                # RFC standard
│   ├── issue-form-yaml.md    # Issue Form YAML standard
│   ├── pr-template.md        # PR Template standard
│   ├── weapons.md            # GitHub Markdown tools reference
│   ├── emoji-guide.md        # Emoji usage guide
│   ├── output-validation.md  # Output validation checklist
│   └── source-catalog.md     # Reference source catalog
└── README.*.md               # Multi-language READMEs
```

## Contributing

Contributions are welcome — whether fixing scenario rules, improving reference source quality, adding Markdown tool references, or submitting use cases.

- Open an Issue or Discussion to discuss your ideas first
- Fork the repository and submit a PR
- Put scenario rules in the matching `reference/*.md`, not in the routing layer
- Keep `SKILL.md` lightweight and focused on routing
- Avoid including local validation output or large unorganized case collections in the public repo

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed rules.

## Acknowledgements

- [GitHub Docs](https://docs.github.com/en) — Issue/PR templates, Markdown syntax, and community practices
- [Conventional Commits](https://www.conventionalcommits.org/) — Commit message format specification
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG format standard
- [shields.io](https://shields.io) — Badge generation service
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Code Review guide
- Open-source project templates and contribution guides from Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS — structural references for scenario standards
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Emoji lookup reference
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Commit intent emoji guide

## License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
