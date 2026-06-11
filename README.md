<p align="center">
  <a href="#english">English</a> · <a href="#chinese">简体中文</a>
</p>

<p align="center">
  <img src="./assets/oh-my-gh-writing-logo.png" width="320" alt="oh-my-gh-writing logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/8%20categories-40%2B%20scenarios-blue" alt="40+ scenarios">
  <img src="https://img.shields.io/badge/22%20reference%20repos-green" alt="reference repos">
  <img src="https://img.shields.io/badge/14%20agent%20frameworks-orange" alt="agent support">
  <img src="https://img.shields.io/badge/17%20design%20principles-8A2BE2" alt="design principles">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="license">
</p>

---

<a id="english"></a>
<h1 align="center">oh-my-gh-writing</h1>
<p align="center"><em>GitHub Writing Standards — Issue · PR · Review · Commit · Docs · Release · Design · Templates — delivered as a portable SKILL.md for Hermes Agent, compatible with 14 agent frameworks</em></p>

---

## Index

- [What is this?](#what-is-this)
- [Quick Start](#quick-start)
- [Features](#features)
- [Project Structure](#project-structure)
- [Design Principles](#design-principles)
- [Agent Compatibility](#agent-compatibility)
- [Contributing](#contributing)
- [License & Acknowledgments](#license--acknowledgments)

---

## What is this?

**oh-my-gh-writing** distills the writing practices of 22 top open-source projects into a single, executable specification. Each reference repo appears in **≤3 scenarios** (see [repo quota table](#design-principles)). Every brand, protocol, and license links to its source.

**What problems does it solve?**

- Teams maintain consistent Issue/PR/Commit formatting without manual review cycles
- AI agents produce GitHub content following real community practices, reducing post-generation edits
- New contributors onboard faster with explicit templates and checklists for every common scenario

**Two complexity levels per scenario:**

| Level | Content | Best for |
|-------|---------|----------|
| **Complete** | Full field set, multi-repo detailed examples, variant outputs | RFCs, high-stakes PRs, formal design docs |
| **Normal** | All required fields, stripped optional sections, 2-minute learn curve | Daily bug reports, routine PRs, quick commits |

## Quick Start

**Option 1 — Hermes Agent (native)**

```bash
git clone git@github.com:PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing
hermes skill install ./SKILL.md
hermes run "oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。"
```

**Option 2 — Copy to any agent rules directory**

```bash
# Claude Code / Cursor / Windsurf / Cline / Aider / Codex CLI
cp SKILL.md ./CLAUDE.md && cp -r reference/ ./reference/
# See full compatibility matrix below
```

**After loading the skill**, a Bug Report request produces structured output with reproduction steps, environment, severity label — following the practices of [VS Code](https://github.com/microsoft/vscode), [React](https://github.com/facebook/react), and [Home Assistant](https://github.com/home-assistant/core).

## Features

| Category | Scenarios | Reference repos (partial) |
|----------|-----------|---------------------------|
| **Issue** | Bug Report, Feature Request, Enhancement, Regression, Performance, Documentation, Security, Discussion | VS Code · React · Home Assistant · TypeScript · Go · ESLint |
| **PR** | Feature, Bug Fix, Hotfix, Refactor, Documentation, Dependency, Backport, Draft | Kubernetes · Vue · Django · Tailwind · React · Prettier |
| **Review** | Code Review, Review Summary, Design Review, Performance Review, Security Review | Linux · Rust · Go · MDN · Home Assistant |
| **Commit** | Standard, Fixup, Revert, Automated | Angular · Vue · Go · Django |
| **Docs** | README · CONTRIBUTING · CHANGELOG · Migration · Security Policy · Code of Conduct · API Reference · FAQ · Architecture · Troubleshooting | Next.js · Tailwind · axios · Pandas · Home Assistant |
| **Release** | Release Notes, Changelog Entry, Version Bump, Migration Guide | Kubernetes · Next.js · React · Go |
| **Design** | RFC, Decision Record, Proposal | Rust · React · Kubernetes |
| **Templates** | Issue Form YAML, PR Template, Commit Template | VS Code · Angular · TypeScript · Kubernetes |

Each scenario provides **Complete** and **Normal** complexity levels.

## Project Structure

```
oh-my-gh-writing/
├── SKILL.md                  # Entry index + 17 principles + index + weapons
├── reference/                # Scenario standards, 40+ files
│   ├── bug-report.md         # Each scenario: Complete + Normal versions
│   ├── feature-pr.md
│   ├── code-review.md
│   ├── readme.md             # README layout patterns (17 repos analyzed)
│   ├── weapons.md            # Formatting Weapons appendix (alerts, badges, mermaid, kbd, etc.)
│   └── ...
├── reference/tool-analysis.md  # 5 writing-tool deep-dive (PR-Agent, Release Drafter, etc.)
├── DOCS/                     # Source materials & design docs
│   ├── collection-plan.md    # Collection plan (3-tier samples)
│   ├── skill-outline.md      # v1 outline
│   └── skill-outline-v2.md   # v2 outline (revised, 17 principles)
├── assets/
│   └── oh-my-gh-writing-logo.png
└── README.md                 # This file
```

## Design Principles

oh-my-gh-writing is governed by **17 principles** across two tiers:

### 7 Core Principles (writing craft)

| # | Principle | Description |
|---|-----------|-------------|
| 1 | **One Topic per Unit** | One commit/PR/Issue = one logical change |
| 2 | **Required Fields Mandatory** | Each doc type has non-optional fields |
| 3 | **Reader-Driven** | Write for your audience: maintainer? user? contributor? agent? |
| 4 | **Precision over Length** | Exact code/log/screenshot > verbose description |
| 5 | **Link, Don't Paraphrase** | Reference the source; don't rephrase it |
| 6 | **Searchability** | Titles and keywords let you find this in 3 months |
| 7 | **Atomicity** | One commit = one change, one PR = one feature/fix |

### 10 Principles from Tool Analysis

Derived from studying [PR-Agent](https://github.com/The-PR-Agent/pr-agent), [Release Drafter](https://github.com/release-drafter/release-drafter), [Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator), [README Generator](https://github.com/kefranabg/readme-md-generator), and [Profile README Generator](https://github.com/rahuldkjain/github-profile-readme-generator). Full analysis in [`reference/tool-analysis.md`](reference/tool-analysis.md).

| # | Principle | Origin |
|---|-----------|--------|
| 8 | **Schema-first** — Define output structure before filling content | [PR-Agent](https://github.com/The-PR-Agent/pr-agent) Pydantic schema |
| 9 | **Section-based Output** — Each section independently toggleable | [Profile README Gen](https://github.com/rahuldkjain/github-profile-readme-generator) modular assembly |
| 10 | **Template Variables > Hardcoding** — Version, date, author injected via vars | [Release Drafter](https://github.com/release-drafter/release-drafter) `$CHANGES` |
| 11 | **Label as Taxonomy** — GitHub labels drive document classification | [Changelog Gen](https://github.com/github-changelog-generator/github-changelog-generator) label→section |
| 12 | **Two Complexity Tracks** — Complete + Normal per scenario | [README Gen](https://github.com/kefranabg/readme-md-generator) HTML-rich vs plain md |
| 13 | **Escape User Input** — Sanitize PR titles/author names to protect markdown | [Release Drafter](https://github.com/release-drafter/release-drafter) `change-title-escapes` |
| 14 | **Source Transparency** — Auto-generated docs declare their origin tool | [README Gen](https://github.com/kefranabg/readme-md-generator) footer + Changelog Gen credit |
| 15 | **Read Metadata as Defaults** — package.json/git config populate initial values | [README Gen](https://github.com/kefranabg/readme-md-generator) auto-read strategy |
| 16 | **Category Aggregation** — Multiple entries grouped into one section | [Release Drafter](https://github.com/release-drafter/release-drafter) category system |
| 17 | **Conditional Rendering** — No data → no section | [README Gen](https://github.com/kefranabg/readme-md-generator) EJS conditional branches |

## Agent Compatibility

oh-my-gh-writing ships as [`SKILL.md`](https://hermes-agent.nousresearch.com/docs) (Hermes native). The content is consumable by any agent framework accepting markdown instruction files:

| Platform | File | Adaptation |
|----------|------|------------|
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs) | `SKILL.md` | None |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) | `CLAUDE.md` | Strip frontmatter |
| [Cursor](https://docs.cursor.com/context/rules-for-ai) | `.cursorrules` | Strip frontmatter |
| [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) | `.github/copilot-instructions.md` | Strip frontmatter, flatten sections |
| [Cline](https://github.com/cline/cline) | `.clinerules` | Strip frontmatter |
| [Roo Code](https://github.com/RooVetGit/Roo-Cline) | `.roorules` | Strip frontmatter |
| [Windsurf](https://codeium.com/windsurf) | `.windsurfrules` | Strip frontmatter, simplify |
| [Continue](https://docs.continue.dev/customize/how-continue-works) | `.continuerc.json` | Convert to JSON |
| [Aider](https://aider.chat/docs/usage/conventions.html) | `CONVENTIONS.md` | Strip frontmatter |
| [Augment Code](https://www.augmentcode.com/) | `.augment/` dir | Split into rule files |
| [OpenCode](https://github.com/opencode-ai/opencode) | `.opencode/rules/` | Split into per-rule files |
| [Codex CLI](https://github.com/openai/codex) | `RULES.md` | Strip frontmatter |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | `.cody/` dir | Adapt format |
| [Zed AI](https://zed.dev/) | `.zed/` settings | Extract rules |

**Legend**: ✅ Native · ⚠️ Minor adaptation · ❌ Format mismatch (content extractable)

## Contributing

Issues and PRs welcome at [github.com/PINKIIILQWQ/oh-my-gh-writing](https://github.com/PINKIIILQWQ/oh-my-gh-writing).

Before contributing, review the [17 design principles](#design-principles) that govern all scenarios.

## License & Acknowledgments

- **License**: [MIT](https://opensource.org/licenses/MIT)
- **Agent frameworks**: [Hermes Agent](https://hermes-agent.nousresearch.com) · [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) · [Cursor](https://docs.cursor.com/context/rules-for-ai) · [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) · [Cline](https://github.com/cline/cline) · [Windsurf](https://codeium.com/windsurf) · [Aider](https://aider.chat) · [Codex CLI](https://github.com/openai/codex)
- **Tools**: [shields.io](https://shields.io) (badge generator) · [Star History](https://star-history.com)
- **Writing tools studied**: [PR-Agent](https://github.com/The-PR-Agent/pr-agent) · [Release Drafter](https://github.com/release-drafter/release-drafter) · [Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator) · [README Generator](https://github.com/kefranabg/readme-md-generator) · [Profile README Generator](https://github.com/rahuldkjain/github-profile-readme-generator)

> **请问还有什么需要额外注意的地方吗？** — After generating the first draft, confirm with the user: need Star History? multi-language variants? specific badge style? any features or community links to highlight?

---

<a id="chinese"></a>
<h1 align="center">oh-my-gh-writing</h1>
<p align="center"><em>GitHub 写作规范 —— Issue/PR/Review/Commit/文档/发布/设计/模板 —— 每场景完整+普通 2 级标准，以可移植 SKILL.md 分发，兼容 14 种 agent 框架</em></p>

---

## 目录

- [这是什么？](#这是什么)
- [快速开始](#快速开始)
- [功能](#功能)
- [项目结构](#项目结构)
- [设计原则](#设计原则)
- [Agent 兼容性](#agent-兼容性)
- [贡献指南](#贡献指南)
- [许可与致谢](#许可与致谢)

---

## 这是什么？

**oh-my-gh-writing** 将 22 个顶级开源项目的写作实践提炼为一套可执行规范。每个参考仓库出现在 **≤3 个场景**（见[设计原则](#设计原则)），提及的品牌、协议、许可均附带源地址链接。

**解决了什么问题？**

- 团队保持 Issue/PR/Commit 格式统一，无需反复 review 排版
- AI agent 产出 GitHub 内容时遵循真实社区实践，减少人工修正
- 新贡献者通过显式模板和 checklist 快速对齐协作规范

**每场景双复杂度等级：**

| 等级 | 内容 | 适用场景 |
|------|------|----------|
| **完整版** | 全字段 + 多仓库详尽示例 + 变体输出 | RFC、高优先级 PR、正式设计文档 |
| **普通版** | 全部必要字段，精简可选部分，2 分钟学会 | 日常 Bug Report、常规 PR、快速提交 |

## 快速开始

**方式 1 —— Hermes Agent（原生）**

```bash
git clone git@github.com:PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing
hermes skill install ./SKILL.md
hermes run "oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。"
```

**方式 2 —— 复制到任意 agent 规则目录**

```bash
# Claude Code / Cursor / Windsurf / Cline / Aider / Codex CLI
cp SKILL.md ./CLAUDE.md && cp -r reference/ ./reference/
```

## 功能

| 类别 | 场景数 | 参考仓库（部分） |
|------|--------|------------------|
| **Issue** | 8 种 | VS Code · React · Home Assistant · TypeScript · Go · ESLint |
| **PR** | 8 种 | Kubernetes · Vue · Django · Tailwind · React · Prettier |
| **Review** | 5 种 | Linux · Rust · Go · MDN · Home Assistant |
| **Commit** | 4 种 | Angular · Vue · Go · Django |
| **文档** | 10 种 | Next.js · Tailwind · axios · Pandas · Home Assistant |
| **发布** | 4 种 | Kubernetes · Next.js · React · Go |
| **设计** | 3 种 | Rust · React · Kubernetes |
| **模板** | 3 种 | VS Code · Angular · TypeScript · Kubernetes |

每场景提供 **完整版**（全字段）和 **普通版**（必要字段）双等级。

## 项目结构

```
oh-my-gh-writing/
├── SKILL.md                  # 入口索引 + 17 条原则 + 索引表 + 武器库
├── reference/                # 场景标准（40+ 文件）
│   ├── bug-report.md         # 每场景：完整版 + 普通版
│   ├── feature-pr.md
│   ├── code-review.md
│   ├── readme.md             # README 布局模式（17 仓库分析）
│   ├── weapons.md            # 格式化武器库附录
│   ├── tool-analysis.md      # 5 款写作工具深度分析
│   └── ...
├── DOCS/                     # 源材料与设计文档
├── assets/                   # 项目图标
└── README.md                 # 本文件
```

## 设计原则

oh-my-gh-writing 由 **17 条原则** 指导（7 条核心 + 10 条工具分析）。

### 7 条核心原则

1. **一条一主题** — 一个 commit/PR/Issue 只做一件事
2. **必要部分必填** — 每类文档有不可省略的必填字段
3. **读者驱动** — 写之前想清楚读者是谁
4. **精确大于长度** — 精确的代码/log/截图 > 冗长描述
5. **引用优先** — 引用源地址 > 复述内容
6. **可搜索性** — 标题和关键词让三个月后的你搜得到
7. **保持原子** — 一条 commit = 一个逻辑变更

### 10 条工具分析原则

源自 [PR-Agent](https://github.com/The-PR-Agent/pr-agent)、[Release Drafter](https://github.com/release-drafter/release-drafter)、[Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator)、[README Generator](https://github.com/kefranabg/readme-md-generator)、[Profile README Generator](https://github.com/rahuldkjain/github-profile-readme-generator)。详见 [`reference/tool-analysis.md`](reference/tool-analysis.md)。

| # | 原则 | 来源 |
|---|------|------|
| 8 | **Schema-first** — 先定义结构再填充内容 | PR-Agent Pydantic schema |
| 9 | **Section 化产出** — 每部分独立可配 | Profile README Gen 模块化拼接 |
| 10 | **变量替换 > 硬编码** — 动态值通过模板注入 | Release Drafter `$CHANGES` |
| 11 | **Label 即分类** — label 直接对应文档分类 | Changelog Gen label→section |
| 12 | **两种复杂度** — 完整版与普通版 | README Gen HTML-rich vs 纯 md |
| 13 | **逃逸用户输入** — 防止特殊字符破坏 markdown | Release Drafter escapes |
| 14 | **来源透明** — 自动生成文档标注工具来源 | README Gen footer + Changelog Gen credit |
| 15 | **元数据做默认值** — 读取 package.json 等自动填充 | README Gen 自动读取策略 |
| 16 | **Category 聚合** — 多条变更为一类合并展示 | Release Drafter category 体系 |
| 17 | **条件渲染** — 无数据则无 section | README Gen EJS 条件分支 |

## Agent 兼容性

oh-my-gh-writing 以 [`SKILL.md`](https://hermes-agent.nousresearch.com/docs)（Hermes 原生）分发，兼容 14 个 agent 平台。详见[英文版 Agent 兼容性表格](#agent-compatibility)。

## 贡献指南

欢迎提交 Issue 或 PR： [github.com/PINKIIILQWQ/oh-my-gh-writing](https://github.com/PINKIIILQWQ/oh-my-gh-writing)

贡献前请先阅读[17 条设计原则](#设计原则)。

## 许可与致谢

- **许可**：[MIT](https://opensource.org/licenses/MIT)
- **Agent 框架**：[Hermes Agent](https://hermes-agent.nousresearch.com) · [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) · [Cursor](https://docs.cursor.com/context/rules-for-ai) · [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) · [Cline](https://github.com/cline/cline) · [Windsurf](https://codeium.com/windsurf) · [Aider](https://aider.chat) · [Codex CLI](https://github.com/openai/codex)
- **工具**：[shields.io](https://shields.io)（徽章生成器）· [Star History](https://star-history.com)
- **写作工具分析**：[PR-Agent](https://github.com/The-PR-Agent/pr-agent) · [Release Drafter](https://github.com/release-drafter/release-drafter) · [Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator) · [README Generator](https://github.com/kefranabg/readme-md-generator) · [Profile README Generator](https://github.com/rahuldkjain/github-profile-readme-generator)

> **请问还有什么需要额外注意的地方吗？** — 初稿产出后向使用者确认：是否需要补充 Star History？是否需要多语言变体？是否要特定风格的徽章？是否有需要强调的特定功能或社区链接？
