<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/blob/main/LICENSE"><img src="https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=License" alt="MIT"></a>
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main"><img src="https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=Updated" alt="Last Commit"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-Agent%20Skill-22AA66?style=flat" alt="Agent Skill"></a>
</p>

**oh-my-gh-writing** 是一个面向 AI Agent 的 GitHub 写作技能包。它把 Issue、PR、Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form 和 PR Template 等常见 GitHub 写作任务路由到对应标准，帮助 agent 生成结构清晰、事实边界明确、接近可提交的 Markdown 或 YAML 草稿。

它不是 README 生成器，也不是 GitHub 集成服务。它是一组可移植的 Markdown 写作规则：原生支持 Agent Skills 的工具可以直接加载；不支持 skill 格式的工具也可以把 `SKILL.md` 和对应 `reference/*.md` 改写为自己的规则、指令或知识库。

## 适用范围

根据各平台对 skill、规则文件和自定义指令的支持程度，本仓库提供两类使用方式：

**Direct（原生/近原生）**：工具可以加载包含 `SKILL.md` 的 skill 目录，并按需读取 `reference/`。这类方式最能保留场景路由和渐进加载能力。

**Adapted（适配）**：工具不能直接消费本仓库格式，但可以把核心规则改写到自定义指令、规则文件、项目知识库或文档索引中。适配后仍可使用 18 个场景标准，但自动路由和按需加载能力取决于目标工具。

| Agent / Tool | 等级 | 推荐接入方式 | 官方文档 |
|--------------|------|--------------|----------|
| Codex | Direct | 克隆到 `$HOME/.agents/skills/oh-my-gh-writing`，或作为项目 skill 放到 `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| Claude Code | Direct | 克隆或软链接到 `~/.claude/skills/oh-my-gh-writing`，或项目内 `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| Gemini CLI / Antigravity CLI | Check current docs | Gemini CLI 文档列出 `~/.gemini/skills/`、`~/.agents/skills/` 和 `gemini skills install`；同时提示部分用户正在迁移到 Antigravity CLI，使用前按当前官方说明确认 | [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/) |
| Hermes | Direct | 放入 `~/.hermes/skills/<category>/oh-my-gh-writing`；HTTP 单文件安装只适合 `SKILL.md`，本仓库建议保留 `reference/` 目录 | [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| Cursor | Adapted | 将路由摘要和需要的场景规则改写为 Cursor project rules；长 reference 可作为 Docs/知识库索引 | [Cursor Docs](https://cursor.com/docs) |
| GitHub Copilot | Adapted | 改写为 `.github/copilot-instructions.md`、`.github/instructions/*.instructions.md` 或 Copilot agent skill 结构 | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| Continue | Adapted | 改写为 `.continue/rules/*.md`；按场景拆规则比塞进单个文件更稳定 | [Continue Rules](https://docs.continue.dev/customize/rules) |
| Windsurf | Adapted | 改写为 Windsurf rules / workspace instructions，并按场景保留短入口 | [Windsurf Docs](https://docs.windsurf.com) |

表中未列出的工具只要支持读取 Markdown、自定义系统指令、项目规则或知识库，也可以用 Adapted 方式使用。最稳妥的适配方式是保留 `SKILL.md` 的路由表，再按任务只复制对应的 `reference/*.md`。

## 快速开始

Codex 用户可以直接安装到用户级 skills 目录：

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"
```

Claude Code 用户可以安装到个人 skills 目录：

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

本地开发或测试时，也可以把当前仓库软链接到目标工具的 skill 目录：

```bash
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"
```

安装后，在支持自动触发的 agent 中直接提出任务即可，例如：

```text
帮我根据这个仓库写一个 README。
把这个 bug 描述整理成 GitHub Issue。
根据当前 diff 写一个 PR description。
review 这个 PR，按 blocking / major / minor / nit 分类。
```

如果目标工具不支持 skill 目录，把 `SKILL.md` 中的路由表放入项目规则，再按场景补充对应 `reference/*.md`。不要一次性塞入所有 reference；这会降低触发精度，也会浪费上下文。

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

每个场景都有对应的标准文件，位于 `reference/`。这些文件提供结构、必含字段、事实边界、格式要求和参考来源提示。完整导航见 [`INDEX.md`](INDEX.md)。

## 目录结构

```text
oh-my-gh-writing/
├── SKILL.md                  # Agent 入口规则和场景路由
├── INDEX.md                  # 全量导航索引
├── CONTRIBUTING.md           # 贡献规则
├── LICENSE
├── assets/
│   └── oh-my-gh-writing-logo.png
└── reference/
    ├── shared-principles.md  # 通用输出质量规则
    ├── readme.md             # README 写作规则
    ├── output-validation.md  # 输出验收清单
    ├── source-catalog.md     # 参考来源目录
    ├── weapons.md            # GitHub Markdown 工具
    ├── badge-catalog.md      # Badge URL 模式
    ├── emoji-guide.md        # 常用 emoji 索引
    └── *.md                  # 18 个场景标准
```

## 贡献

欢迎贡献场景规则、参考来源、输出验收规则和小型 Markdown 工具改进。案例也有价值，但请先通过 Issue 或 Discussion 描述来源、场景、测试目标和授权/隐私边界，不要直接提交大批复制内容或本地验证输出。

贡献时请保持 `SKILL.md` 轻量，把场景细节写入对应 `reference/*.md`。详细规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 鸣谢

- [GitHub Docs](https://docs.github.com/en) — Issue/PR 模板、Markdown 语法和社区实践规范
- [Conventional Commits](https://www.conventionalcommits.org/) — Commit message 格式规范
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG 格式标准
- [shields.io](https://shields.io) — Badge 生成服务
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Code Review 实践指南
- Angular、Kubernetes、React、TypeScript、VS Code、Node.js、Tailwind CSS 等开源项目的 Issue/PR 模板和贡献指南 — 场景结构参考
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) 和 [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Emoji 与 commit intent 参考

## 许可证

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
