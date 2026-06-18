<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">✨ oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Pre--release-2563eb?style=flat" alt="Pre-release"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 artifact standards"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 workflow packs"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · 简体中文
</p>

**oh-my-gh-writing** 是一个面向 AI Agent 的 GitHub 写作 Skill。它帮助 agent 起草更干净的 GitHub Issue、PR 描述、Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form、PR Template，以及多文件 workflow pack。

核心思路很简单：先判断请求属于哪类 GitHub 写作任务，再只加载对应标准，明确事实边界，最后输出更少需要清理的 GitHub artifact 或本地草稿包。

## 🚀 快速开始

推荐手动安装：

```bash
# Codex / Gemini 类 skill 路径
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

如果目标 host 支持开放 [Agent Skills](https://agentskills.io) `skills` CLI：

```bash
npx skills add PINKIIILQWQ/oh-my-gh-writing -g
npx skills add PINKIIILQWQ/oh-my-gh-writing -g -a codex
npx skills add PINKIIILQWQ/oh-my-gh-writing -g -a claude-code
```

`-g` 表示安装到当前用户全局目录；如果目标工具支持项目级 skill，可以去掉 `-g` 做项目内安装。

示例提示词：

```text
帮我根据这个仓库写一个 README。
把这个 bug 描述整理成 GitHub Issue。
根据当前 diff 写一个 PR description。
准备 v1.2.0 的完整发布材料。
让这个仓库具备接收外部贡献的流程。
```

## ✨ 为什么用 oh-my-gh-writing？

- **不只是模板，而是 workflow pack**：发版准备、项目首发、贡献流程、Bug 修复链路、从提案到实现、破坏性变更沟通、文档重写都被当作多文件 GitHub 写作任务处理。
- **先路由，再写作**：区分 Feature Request、Enhancement、Discussion、Feature PR、Bug Fix PR、Refactor PR、Documentation PR，减少把 Issue 写成 PR、把讨论写成需求的情况。
- **默认保护事实边界**：版本号、命令、CI 名称、兼容性、issue/PR 编号、release 信息必须来自用户输入、仓库文件、diff 或官方来源。
- **渐进读取 reference**：`SKILL.md` 保持轻量，具体规则放在 `references/*.md`，按场景读取，避免一次性塞满上下文。
- **输出更干净**：明确避免对话前言、外层 Markdown 代码块、旧测试标题、复制残留、未实际完成却打勾的 checklist 和编造事实。
- **参考真实 GitHub 实践**：规则参考 GitHub Docs、Conventional Commits、Keep a Changelog、Google Engineering Practices 和成熟开源项目的写作模式。

## 🛡️ 它能避免什么？

- PR 描述声称测试已通过，但没有证据。
- Bug Report 编造 root cause 或受影响版本。
- README 宣称不支持或未确认的平台、安装方式。
- Release Notes 编造迁移命令、日期、贡献者或 compare link。
- Issue Form 从无关项目复制 labels、SIG、版本列表或 required checkbox。

## 🎯 适用范围

本项目是一个可移植的 Markdown rulebase，适用于 AI Agent 和支持自定义规则的编码工具。最理想的使用方式是让工具读取 `SKILL.md` 和本地 `references/*.md`；如果工具不支持 Skill 目录，也可以把相关标准改写为项目规则、自定义指令或知识库。

| 使用方式 | 适用对象 | 保留能力 | 限制 |
| --- | --- | --- | --- |
| Skill 目录 | Codex、Claude Code、Gemini 类 skill host | 路由、按需读取、输出验收最完整 | 需要本地文件读取能力 |
| 项目规则 | Cursor、Continue、Copilot、Windsurf / Devin 类规则系统 | 在项目内复用选定标准 | 需要按工具格式手动适配 |
| 知识库 | 可检索 Markdown 的 agent 或团队规范库 | 结构标准、来源说明、质量规则 | 路由依赖宿主工具能力 |

## 🧭 覆盖内容

| 类型 | 内容 |
| --- | --- |
| 18 个 artifact 标准 | Bug Report、Feature Request、Enhancement、Discussion、Feature PR、Bug Fix PR、Refactor PR、Documentation PR、Code Review、Standard Commit、README、CONTRIBUTING、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form YAML、PR Template |
| 7 个 workflow pack | Version Release、Project Launch、Contribution Setup、Bug Fix Workflow、Proposal to Implementation、Breaking Change Package、Docs Overhaul |
| 质量附录 | shared principles、output validation、badge patterns、emoji guide、GitHub Markdown tools、source catalog |

Workflow pack 只做编排：先询问你需要哪种材料包，再按需读取单项 artifact 标准。默认输出到本地 `.github-writing/...` 草稿目录，不默认发布 release、推 tag、开 PR 或修改远端状态。

## 🤖 Agent 支持

| Agent / Tool | 推荐接入方式 | 说明 |
| --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | 克隆到 `$HOME/.agents/skills/oh-my-gh-writing` 或项目 `.agents/skills/oh-my-gh-writing` | 原生 Agent Skills 模型 |
| [Claude Code](https://code.claude.com/docs/en/skills) | 克隆或软链接到 `~/.claude/skills/oh-my-gh-writing` | 使用 `SKILL.md` frontmatter |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | 按当前文档确认 skill 路径和安装命令 | Gemini / Antigravity 可用范围正在变化，使用前核对官方文档 |
| [Antigravity](https://antigravity.google/) | 按当前文档确认 rules 或 skill 支持 | 以最新官方说明为准 |
| [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | 将完整目录放入 Hermes skills 目录 | HTTP 单文件安装只覆盖 `SKILL.md`，不包含 `references/` |
| [Cursor](https://cursor.com/docs) | 将路由和选定 reference 改写为项目规则 | 只放当前任务相关的场景规则 |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 改写为 Copilot repository instructions 或 agent skill 文件 | 默认不能直接加载完整 skill 目录 |
| [Continue](https://docs.continue.dev/customize/rules) | 改写为 `.continue/rules/*.md` | 按场景拆分比一个大规则更稳 |
| [Windsurf / Devin Desktop](https://docs.windsurf.com) | 按当前 memories / rules 文档确认 | 路径和支持细节需使用前核对 |

## 📂 文件

| 路径 | 作用 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | 轻量运行时路由和工作流规则 |
| [`INDEX.md`](INDEX.md) | 18 个 artifact 标准和 7 个 workflow pack 的导航 |
| [`references/`](references) | 场景标准、workflow pack 和质量附录 |
| [`references/readme.md`](references/readme.md) | README 写作标准 |
| [`references/source-catalog.md`](references/source-catalog.md) | 公开参考来源和维护说明 |
| [`evals/`](evals) | 用于后续 skill 迭代的触发和输出质量 eval fixtures |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | 贡献说明 |
| [`assets/`](assets) | Logo 和 README 本地资产 |

## 🧪 评估

本仓库包含轻量 eval fixtures，便于后续维护：

- [`evals/trigger-queries.json`](evals/trigger-queries.json) 用来检查 skill description 是否会在真实 GitHub 写作请求中触发，并避开相近但不该触发的请求。
- [`evals/evals.json`](evals/evals.json) 记录输出质量任务，覆盖路由、输出清洁、事实边界和 workflow pack 行为。
- [`evals/expected/`](evals/expected) 保存短小 clean outputs，用来展示合格 artifact 的形态。

## 📚 参考来源

本项目标准参考 [Agent Skills specification](https://agentskills.io/specification)、[GitHub Docs](https://docs.github.com/en)、[Conventional Commits](https://www.conventionalcommits.org/)、[Keep a Changelog](https://keepachangelog.com/)、[Google Engineering Practices](https://google.github.io/eng-practices/review/)，以及 React、Kubernetes、TypeScript、Node.js、Tailwind CSS、Angular、VS Code 等成熟开源项目的写作模式。完整来源见 [`references/source-catalog.md`](references/source-catalog.md)。

## 📄 许可证

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
