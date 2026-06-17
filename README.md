<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
    <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
  </picture>
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue" alt="License"></a>
  <a href="#-场景索引"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad" alt="Scenarios"></a>
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Agent%20Skills-Open%20Standard-8A2BE2" alt="Agent Skills"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Format-Agent%20Skills-22AA66" alt="Format"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs Welcome"></a>
</p>

<p align="center">
  <b>为 AI Agent 设计的 GitHub 写作规范系统 — 18 场景 · 证据边界 · 输出清洁</b><br>
  <sub>一款可移植的 Agent Skill，AI 加载后自动匹配 Issue、PR、Review、Commit、README 等 GitHub 文书的写作规范</sub>
</p>

---

## 概述

**oh-my-gh-writing** 不是 README 生成器或独立应用，而是一套为 AI Agent 设计的 GitHub 写作规范系统。基于 [Agent Skills](https://agentskills.io) 开放标准，Agent 加载后按场景自动匹配 18 种文书规范，保持输出质量一致、事实有边界、格式可直接提交。

---

## 场景索引

| # | 类别 | 场景 | 对应标准 |
|---|------|------|----------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` 等 |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` 等 |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` 等 |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` 等 |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` 等 |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` 等 |

完整路由规则见 [`SKILL.md`](SKILL.md)。

---

## Agent 支持

本 skill 遵循 [Agent Skills](https://agentskills.io) 开放标准，以下 Agent 可直接加载 `SKILL.md` 或需适配导入。

### 直接加载（原生支持 Agent Skills）

支持 `SKILL.md` 目录结构，直接放入指定路径即可。

| Agent | 安装方法 | 适配范围 | 文档 |
|-------|---------|----------|------|
| <img src="https://code.claude.com/favicon.ico" width="16" height="16"> **Claude Code** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing` → 然后使用 `/oh-my-gh-writing` | 完整支持 18 场景。Agent 按需加载 `SKILL.md` 和对应 `reference/*.md` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| <img src="https://cursor.com/favicon.ico" width="16" height="16"> **Cursor** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.cursor/skills/oh-my-gh-writing` | 完整支持 Agent Skills 标准 | [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills) |
| <img src="https://roocode.com/favicon.ico" width="16" height="16"> **Roo Code** | `gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.roo/skills/oh-my-gh-writing` | 支持 Agent Skills 格式加载 | [docs.roocode.com/features/skills](https://docs.roocode.com/features/skills) |
| <img src="https://code.visualstudio.com/favicon.ico" width="16" height="16"> **VS Code** | 通过 GitHub Copilot Agent Skills 功能配置 | 支持 Agent Skills 标准 | [code.visualstudio.com/docs/copilot/customization/agent-skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| <img src="https://github.com/favicon.ico" width="16" height="16"> **GitHub Copilot** | 在 GitHub 仓库设置中配置 Agent Skills | 支持 Agent Skills 格式 | [docs.github.com/en/copilot/concepts/agents/about-agent-skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| <img src="https://geminicli.com/favicon.ico" width="16" height="16"> **Gemini CLI** | 配置到 Gemini CLI skills 目录 | 支持 Agent Skills 开放标准 | [geminicli.com/docs/cli/skills](https://geminicli.com/docs/cli/skills/) |
| <img src="https://developers.openai.com/favicon.ico" width="16" height="16"> **OpenAI Codex** | 配置到 Codex skills 目录 | 支持 Agent Skills 格式 | [developers.openai.com/codex/skills](https://developers.openai.com/codex/skills/) |
| <img src="https://opencode.ai/favicon.ico" width="16" height="16"> **OpenCode** | 配置到 skills 目录 | 支持 Agent Skills 开放标准 | [opencode.ai/docs/skills](https://opencode.ai/docs/skills/) |
| <img src="https://block.github.io/goose/favicon.ico" width="16" height="16"> **Goose** | 配置到 Goose skills 目录 | 支持 Agent Skills | [block.github.io/goose/docs/guides/context-engineering/using-skills](https://block.github.io/goose/docs/guides/context-engineering/using-skills/) |
| <img src="https://docs.openhands.dev/favicon.ico" width="16" height="16"> **OpenHands** | 配置到 skills 目录 | 支持 Agent Skills 标准 | [docs.openhands.dev/overview/skills](https://docs.openhands.dev/overview/skills) |
| <img src="https://www.jetbrains.com/favicon.ico" width="16" height="16"> **Junie (JetBrains)** | 配置到 Junie skills 目录 | 支持 Agent Skills | [junie.jetbrains.com/docs/agent-skills](https://junie.jetbrains.com/docs/agent-skills.html) |
| <img src="https://ampcode.com/favicon.ico" width="16" height="16"> **Amp** | 配置到 Amp skills 目录 | 支持 Agent Skills | [ampcode.com/manual#agent-skills](https://ampcode.com/manual#agent-skills) |
| <img src="https://www.letta.com/favicon.ico" width="16" height="16"> **Letta** | 配置到 Letta skills 目录 | 支持 Agent Skills | [docs.letta.com/letta-code/skills](https://docs.letta.com/letta-code/skills/) |
| <img src="https://factory.ai/favicon.ico" width="16" height="16"> **Factory** | 配置到 Factory skills 目录 | 支持 Agent Skills | [docs.factory.ai/cli/configuration/skills](https://docs.factory.ai/cli/configuration/skills) |
| <img src="https://www.tabnine.com/favicon.ico" width="16" height="16"> **Tabnine** | 配置到 Tabnine skills 目录 | 支持 Agent Skills | [docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills) |
| <img src="https://www.trae.ai/favicon.ico" width="16" height="16"> **TRAE** | 配置到 TRAE skills 目录 | 支持 Agent Skills | [trae.ai/blog/trae_tutorial_0115](https://www.trae.ai/blog/trae_tutorial_0115) |
| <img src="https://autohand.ai/favicon.ico" width="16" height="16"> **Autohand Code CLI** | 配置到 autohand skills 目录 | 支持 Agent Skills | [autohand.ai/docs/working-with-autohand-code/agent-skills](https://autohand.ai/docs/working-with-autohand-code/agent-skills.html) |
| <img src="https://www.qodo.ai/favicon.ico" width="16" height="16"> **Qodo** | 配置到 Qodo skills 目录 | 支持 Agent Skills | [qodo.ai/blog/how-i-use-qodos-agent-skills](https://www.qodo.ai/blog/how-i-use-qodos-agent-skills-to-auto-fix-issues-in-pull-requests/) |
| <img src="https://github.com/mistralai/mistral-vibe/raw/main/assets/logo.svg" width="16" height="16"> **Mistral Vibe** | 配置到 mistral-vibe skills 目录 | 支持 Agent Skills | [github.com/mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) |
| <img src="https://commandcode.ai/favicon.ico" width="16" height="16"> **Command Code** | 配置到 Command Code skills 目录 | 支持 Agent Skills | [commandcode.ai/docs/skills](https://commandcode.ai/docs/skills) |

### 适配导入（需复制规则）

不支持 `SKILL.md` 格式，需将规则内容复制到其自有规则体系中。

| Agent | 安装方法 | 适配范围 | 文档 |
|-------|---------|----------|------|
| <img src="https://docs.cline.bot/favicon.ico" width="16" height="16"> **Cline** | 将 `SKILL.md` 内容写入 `.clinerules` 文件，并将 `reference/*.md` 内容作为项目背景指令 | 覆盖 18 场景的规则文本内容，但无自动路由能力。需要手动指定场景 | [docs.cline.bot](https://docs.cline.bot/improving-your-prompting/custom-instructions) |
| <img src="https://codeium.com/favicon.ico" width="16" height="16"> **Windsurf** | 将 `SKILL.md` 规则写入 `.windsurfrules` 文件 | 覆盖核心原则和输出验收标准，但无场景自动路由 | [codeium.com/windsurf](https://codeium.com/windsurf) |
| <img src="https://aider.chat/favicon.ico" width="16" height="16"> **Aider** | 将核心规则写入 `.aider.conf.yml` 或 `CONVENTIONS.md` | 覆盖事实边界和输出清洁规则 | [aider.chat/docs/usage/conventions](https://aider.chat/docs/usage/conventions.html) |
| <img src="https://continue.dev/favicon.ico" width="16" height="16"> **Continue** | 将规则内容写入 `.continuerc.json` 或项目级配置 | 覆盖文档规范的核心规则 | [docs.continue.dev/customize](https://docs.continue.dev/customize) |

---

## 快速开始

```text
/oh-my-gh-writing 帮我写一个 Bug Report
/oh-my-gh-writing 为这次修改写一个 PR 描述
/oh-my-gh-writing 审查这个 PR 的变更
/oh-my-gh-writing 写一个 CHANGELOG 条目
```

在适配导入的 Agent 中使用时，指定场景后 Agent 会应用对应规范产出 GitHub artifact。

---

## 核心原则

- **证据边界** — 版本号、PR 编号、测试结果、安装命令等必须有来源，无来源则标 `TODO`
- **精确路由** — 按用户意图路由到正确场景，Feature Request 不会写成已实现的 PR
- **输出清洁** — 产物可直接粘贴到 GitHub，无对话前言、无外层代码块、无测试元数据
- **一个 artifact 一件事** — 不把多个 Issue 或 Release Note 混在同一份输出里
- **可用优先** — 缺信息时先写合理草稿标 TODO，不阻塞

---

## 项目结构

```
oh-my-gh-writing/
├── SKILL.md                    # Agent 运行时路由器和共享规则
├── INDEX.md                    # 仓库导航索引
├── reference/                  # 18 场景标准 + 工具参考
│   ├── bug-report.md
│   ├── feature-request.md
│   ├── enhancement.md
│   ├── discussion.md
│   ├── feature-pr.md
│   ├── bug-fix-pr.md
│   ├── refactor-pr.md
│   ├── documentation-pr.md
│   ├── code-review.md
│   ├── standard-commit.md
│   ├── readme.md
│   ├── contributing.md
│   ├── changelog.md
│   ├── release-notes.md
│   ├── migration-guide.md
│   ├── rfc.md
│   ├── issue-form-yaml.md
│   ├── pr-template.md
│   ├── weapons.md              # GitHub Markdown 工具集
│   ├── emoji-guide.md          # Emoji 使用指引
│   ├── output-validation.md    # 输出验收清单
│   └── source-catalog.md       # 参考来源目录
├── CONTRIBUTING.md             # 贡献指南
├── assets/                     # 项目展示资源
├── LICENSE                     # MIT
├── README.en.md                # English
├── README.ja.md                # 日本語
├── README.ko.md                # 한국어
├── README.es.md                # Español
├── README.fr.md                # Français
├── README.de.md                # Deutsch
└── README.pt.md                # Português
```

---

## 多语言 README

此 README 提供 8 种语言版本：

| 文件 | 语言 |
|------|------|
| [`README.md`](README.md) | 简体中文 |
| [`README.en.md`](README.en.md) | English |
| [`README.ja.md`](README.ja.md) | 日本語 |
| [`README.ko.md`](README.ko.md) | 한국어 |
| [`README.es.md`](README.es.md) | Español |
| [`README.fr.md`](README.fr.md) | Français |
| [`README.de.md`](README.de.md) | Deutsch |
| [`README.pt.md`](README.pt.md) | Português |

需要更多语言？在 README 任务中告知 Agent "最多语言" 即可。

---

## 贡献

欢迎提交 PR 改进场景规则、参考来源或输出验收标准。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 许可

[MIT](LICENSE)
