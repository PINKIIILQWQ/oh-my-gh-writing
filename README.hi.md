<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · हिन्दी · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** AI Agents के लिए GitHub लेखन skill pack है। यह Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms और PR Templates जैसे GitHub लेखन कार्यों को सही scenario standard तक route करता है, ताकि agent साफ संरचना और स्पष्ट evidence boundary वाले Markdown या YAML drafts बना सके।

यह README generator या GitHub integration service नहीं है। यह portable Markdown rulebase है: जिन tools में Agent Skills support है वे इसे सीधे load कर सकते हैं; बाकी tools `SKILL.md` और आवश्यक `reference/*.md` files को rules, custom instructions या knowledge base में बदल सकते हैं।

## oh-my-gh-writing क्यों?

GitHub पर अच्छा लिखना सिर्फ Markdown भरना नहीं है। मुश्किल हिस्सा यह है कि सही scenario पहचाना जाए, कौन-से facts verify करने हैं, क्या invent नहीं करना है, और final artifact Issue, PR, Review या README में साफ तरीके से paste किया जा सकता है या नहीं।

- **18 GitHub writing scenarios**: Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template आदि।
- **पहले routing, फिर writing**: Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR और Refactor PR को अलग रखता है।
- **Progressive reference loading**: `SKILL.md` हल्का रहता है; detailed standards जरूरत पर ही load होते हैं।
- **Evidence boundaries**: versions, commands, CI, compatibility, releases और issue/PR numbers guess नहीं किए जाते।
- **Clean artifacts**: chat preface, outer Markdown fences, test titles, copy residue और unrelated snippets हटाने पर जोर।
- **Real open-source references**: GitHub Docs, Conventional Commits, Keep a Changelog, React, Kubernetes, TypeScript, Node.js और Tailwind CSS जैसे projects से सीख।

## उपयोग के तरीके

**Skill के रूप में**: repository को ऐसे location में रखें जहां agent `SKILL.md` वाली folder load कर सके और `reference/` को जरूरत पर पढ़ सके।

**Rules के रूप में**: अगर tool यह format सीधे नहीं पढ़ सकता, तो `SKILL.md` की routing table और relevant `reference/*.md` files को project rules, custom instructions या knowledge base में adapt करें।

| Icon | Agent / Tool | Recommended setup | Notes / Docs |
|------|--------------|-------------------|--------------|
| <img src="https://openai.com/favicon.ico" width="14" height="14" alt="OpenAI"> | Codex | `$HOME/.agents/skills/oh-my-gh-writing` या `.agents/skills/oh-my-gh-writing` में clone करें | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <img src="https://claude.ai/favicon.ico" width="14" height="14" alt="Claude"> | Claude Code | `~/.claude/skills/oh-my-gh-writing` या `.claude/skills/oh-my-gh-writing` में clone/symlink करें | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <img src="https://geminicli.com/favicon.ico" width="14" height="14" alt="Gemini CLI"> | Gemini CLI / Antigravity CLI | docs में `~/.gemini/skills/`, `~/.agents/skills/` और `gemini skills install` listed हैं | इस्तेमाल से पहले [official docs](https://geminicli.com/docs/cli/skills/) देखें |
| <img src="https://hermes-agent.nousresearch.com/favicon.ico" width="14" height="14" alt="Hermes"> | Hermes | `~/.hermes/skills/<category>/oh-my-gh-writing` में रखें | single-file HTTP install सिर्फ `SKILL.md` के लिए ठीक है; `reference/` रखें. [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <img src="https://cursor.com/favicon.ico" width="14" height="14" alt="Cursor"> | Cursor | router और जरूरी scenario rules को project rules या knowledge base में adapt करें | [Cursor Docs](https://cursor.com/docs) देखें |
| <img src="https://github.com/favicon.ico" width="14" height="14" alt="GitHub"> | GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` या Copilot agent skill structure में adapt करें | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14" alt="Continue"> | Continue | `.continue/rules/*.md` में adapt करें; scenario-based rules ज्यादा stable हैं | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <img src="https://docs.windsurf.com/favicon.ico" width="14" height="14" alt="Windsurf"> | Windsurf / Devin Desktop | current docs customization के लिए memories और rules mention करते हैं | [Windsurf / Devin Docs](https://docs.windsurf.com) में current method confirm करें |

## Quick Start

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

Local development:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

Example requests:

```text
इस repository के लिए README लिखो।
इस bug report को GitHub Issue में बदलो।
current diff से PR description लिखो।
इस PR को review करो और findings को blocking / major / minor / nit में बांटो।
```

## Scenarios

| # | Category | Scenario | Use when |
|---|----------|----------|----------|
| 1 | Issue | Bug Report | reproducible defect report करना |
| 2 | Issue | Feature Request | नई feature या API propose करना |
| 3 | Issue | Enhancement | existing behavior improve करना |
| 4 | Issue | Discussion | open-ended community discussion शुरू करना |
| 5 | PR | Feature PR | new feature PR describe करना |
| 6 | PR | Bug Fix PR | bug fix PR describe करना |
| 7 | PR | Refactor PR | behavior-preserving cleanup describe करना |
| 8 | PR | Documentation PR | documentation-only changes describe करना |
| 9 | Review | Code Review | code changes review करना |
| 10 | Commit | Standard Commit | commit messages लिखना |
| 11 | Docs | README | project homepage बनाना या सुधारना |
| 12 | Docs | CONTRIBUTING | contribution guidelines बनाना |
| 13 | Docs | CHANGELOG | version history लिखना |
| 14 | Release | Release Notes | release announcement लिखना |
| 15 | Release | Migration Guide | upgrade steps समझाना |
| 16 | Design | RFC | design proposal लिखना |
| 17 | Templates | Issue Form YAML | GitHub Issue Forms बनाना |
| 18 | Templates | PR Template | Pull Request templates बनाना |

हर scenario का standard file `reference/` में है। पूरी navigation [`INDEX.md`](INDEX.md) में है।

## Repository Structure

```text
oh-my-gh-writing/
├── README.md
├── README.*.md
├── SKILL.md
├── INDEX.md
├── CONTRIBUTING.md
├── LICENSE
├── assets/
│   └── oh-my-gh-writing-logo.png
└── reference/
    ├── *.md
    ├── readme.md
    ├── shared-principles.md
    ├── output-validation.md
    ├── source-catalog.md
    ├── weapons.md
    ├── emoji-guide.md
    └── badge-catalog.md
```

## Contributing

Scenario rules, reference sources, output validation और छोटे Markdown helpers में contributions welcome हैं। Examples या test cases के लिए पहले Issue या Discussion में source, scenario, test goal और licensing/privacy boundary बताएं।

`SKILL.md` को lightweight रखें और scenario details matching `reference/*.md` में डालें। देखें [`CONTRIBUTING.md`](CONTRIBUTING.md)।

## Sources

Rules [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/) और Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS जैसे mature projects से reference लेते हैं। देखें [`reference/source-catalog.md`](reference/source-catalog.md)।

## License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
