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

**oh-my-gh-writing** 是一个面向 AI Agent 的 GitHub 写作技能包。它将常见的 GitHub 写作需求（Issue、PR、README、CHANGELOG 等）路由到对应的质量标准，确保每次输出都符合社区惯例——可提交、可读性强，无需人工二次润色。

整套规则以 Markdown 文件形式存放在仓库中，不依赖任何外部服务。任何支持加载本地技能的 AI Agent 都可以直接加载使用。

## 适用范围

oh-my-gh-writing 面向 AI Agent 设计。任何支持加载自定义规则、知识库或系统指令的 AI 编程工具都可以使用本技能。根据各平台对技能/规则系统的支持程度，分为两个等级：

**Direct（原生支持）**：可直接加载 `SKILL.md` 及其引用的 `reference/` 目录，自动完成场景识别和路由。配置后 Agent 会在用户提出写作需求时匹配对应的场景标准，按规范生成内容，无需手动指定场景。

**Adapted（适配使用）**：不支持直接加载 skill 格式，但可以通过项目规则文件（如 `.cursorrules`、`copilot-instructions.md`）、自定义指令或文档索引等方式引用写作标准。部分自动路由能力受限，用户需要手动指明当前写作场景。

| 图标 | Agent | 等级 | 使用方法 | 官方文档 |
|------|-------|------|---------|---------|
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude Code** | Direct | 将本仓库路径添加到 skill 列表；Agent 自动路由到对应场景 | [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code) |
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude**（Web/API） | Adapted | 将 `SKILL.md` 和对应 `reference/*.md` 内容注入到系统指令 | [Claude API 文档](https://docs.anthropic.com/en/docs) |
| <img src="https://cursor.sh/favicon.ico" width="14" height="14"> | **Cursor** | Adapted | 通过 `.cursorrules` 引用规则，或 Docs 索引 `reference/` 目录 | [Cursor 文档](https://docs.cursor.com) |
| <img src="https://github.com/favicon.ico" width="14" height="14"> | **GitHub Copilot** | Adapted | 在 `.github/copilot-instructions.md` 中引用核心规则 | [Copilot 文档](https://docs.github.com/en/copilot) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14"> | **Continue** | Adapted | 配置 docs 源指向 `reference/` 目录，通过 `@docs` 检索 | [Continue 文档](https://docs.continue.dev) |
| <img src="https://codeium.com/favicon.ico" width="14" height="14"> | **Windsurf** | Adapted | 通过 `.windsurfrules` 或 AI Rules 配置引用规则 | [Windsurf 文档](https://docs.codeium.com) |

表中未列出的 AI 工具只要支持自定义指令或规则文件加载，同样可以通过 Adapted 方式参考本技能。核心写作标准（`reference/*.md`）是纯 Markdown，不依赖特定平台格式，任何能读取 Markdown 的工具都可以使用。

## 场景

| # | 类别 | 场景 | 适用时机 |
|---|------|------|----------|
| 1 | Issue | Bug Report | 报告可复现缺陷 |
| 2 | Issue | Feature Request | 提议新功能或新 API |
| 3 | Issue | Enhancement | 改进已有能力 |
| 4 | Issue | Discussion | 开放式社区讨论 |
| 5 | PR | Feature PR | 新功能 Pull Request |
| 6 | PR | Bug Fix PR | 修复缺陷 Pull Request |
| 7 | PR | Refactor PR | 不改变行为的重构 |
| 8 | PR | Documentation PR | 文档改动 Pull Request |
| 9 | Review | Code Review | 审查代码变更 |
| 10 | Commit | Standard Commit | 写提交信息 |
| 11 | Docs | README | 项目首页文档 |
| 12 | Docs | CONTRIBUTING | 贡献指南 |
| 13 | Docs | CHANGELOG | 版本变更记录 |
| 14 | Release | Release Notes | 发布说明 |
| 15 | Release | Migration Guide | 迁移指南 |
| 16 | Design | RFC | 设计提案 |
| 17 | Templates | Issue Form YAML | GitHub Issue 表单 |
| 18 | Templates | PR Template | Pull Request 模板 |

每个场景都有对应的写作标准文件，位于 `reference/` 目录下，包含标准结构、强制字段、事实边界规则、高质量参考来源和必含元素 Checklist。Agent 在收到对应写作需求时自动加载对应标准，按规范输出内容。

## 快速开始

将本仓库作为 Skill 加载到你的 AI Agent 中：

```bash
# Claude Code — 在项目 .claude/settings.json 或 Claude 配置中关联本技能
# 或直接引用 SKILL.md 作为 Agent 系统指令的一部分
```

以 Claude Code 为例：将本仓库路径添加到 Agent 的可用技能列表中后，当用户提出 GitHub 写作需求（"写一个 Bug Report"、"帮我 review 这个 PR"），Agent 会自动匹配场景、加载对应 `reference/*.md` 标准文件，并按照规范生成可直接提交的内容。

所有场景标准和路由规则详见 [`SKILL.md`](SKILL.md)，全量索引见 [`INDEX.md`](INDEX.md)。

## 目录结构

```
oh-my-gh-writing/
├── SKILL.md                  # Agent 入口规则和场景路由
├── INDEX.md                  # 全量导航索引
├── CONTRIBUTING.md           # 贡献规则
├── LICENSE                   # MIT 许可证
├── .gitignore
├── assets/                   # 项目展示素材
│   └── oh-my-gh-writing-logo.png
├── reference/                # 场景标准文件
│   ├── shared-principles.md  # 19 条共享质量规则
│   ├── readme.md             # README 写作详细规则
│   ├── bug-report.md         # Bug Report 标准
│   ├── feature-request.md    # Feature Request 标准
│   ├── enhancement.md        # Enhancement 标准
│   ├── discussion.md         # Discussion 标准
│   ├── feature-pr.md         # Feature PR 标准
│   ├── bug-fix-pr.md         # Bug Fix PR 标准
│   ├── refactor-pr.md        # Refactor PR 标准
│   ├── documentation-pr.md   # Documentation PR 标准
│   ├── code-review.md        # Code Review 标准
│   ├── standard-commit.md    # Standard Commit 标准
│   ├── contributing.md       # CONTRIBUTING 标准
│   ├── changelog.md          # CHANGELOG 标准
│   ├── release-notes.md      # Release Notes 标准
│   ├── migration-guide.md    # Migration Guide 标准
│   ├── rfc.md                # RFC 标准
│   ├── issue-form-yaml.md    # Issue Form YAML 标准
│   ├── pr-template.md        # PR Template 标准
│   ├── weapons.md            # GitHub Markdown 工具参考
│   ├── emoji-guide.md        # Emoji 使用指南
│   ├── output-validation.md  # 输出验收清单
│   └── source-catalog.md     # 参考来源目录
└── README.*.md               # 多语言 README
```

## 贡献

欢迎贡献！无论是指出场景规则的缺漏、改进参考来源质量、补充 Markdown 工具参考，还是提交使用案例，都可以让这个项目变得更好。

- 先通过 Issue 或 Discussion 讨论你的想法
- Fork 仓库后提交 PR
- 场景规则写入对应的 `reference/*.md`，不要堆在路由层
- 保持 `SKILL.md` 轻量，专注于路由职责
- 避免在公开仓库中包含本地验证输出或大量未整理的案例

详细规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 鸣谢

- [GitHub Docs](https://docs.github.com/en) — Issue/PR 模板、Markdown 语法和社区实践规范
- [Conventional Commits](https://www.conventionalcommits.org/) — Commit message 格式规范
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG 格式标准
- [shields.io](https://shields.io) — Badge 生成服务
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Code Review 实践指南
- Angular、Kubernetes、React、TypeScript、VS Code、Node.js、Tailwind CSS 等开源项目的 Issue/PR 模板和贡献指南 — 场景标准的结构参考
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Emoji 速查表
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Commit 意图 emoji 指南

## 许可证

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
