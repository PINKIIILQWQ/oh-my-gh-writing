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

**oh-my-gh-writing** 是一个面向 AI Agent 的 GitHub 写作技能包。它把 Issue、PR、Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form 和 PR Template 等常见 GitHub 写作任务路由到对应标准，帮助 agent 生成结构清晰、事实边界明确、接近可提交的 Markdown 或 YAML 草稿。

它不是 README 生成器，也不是 GitHub 集成服务。它是一组可移植的 Markdown 写作规则：原生支持 Agent Skills 的工具可以直接加载；不支持 skill 格式的工具也可以把 `SKILL.md` 和对应 `reference/*.md` 改写为自己的规则、指令或知识库。

## 为什么用 oh-my-gh-writing？

GitHub 写作最难的不是把 Markdown 写满，而是判断当前场景该写什么、哪些事实必须核验、哪些内容不能编造，以及最终产物能否直接贴进 Issue、PR、Review 或 README。oh-my-gh-writing 把这些判断整理成一套可被 agent 按需读取的 GitHub 写作规则系统，让输出更接近真实开源项目的协作标准。

- **覆盖 18 个 GitHub 写作场景**：Issue、PR、Code Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form、PR Template 等。
- **先路由，再写作**：区分 Feature Request、Enhancement、Discussion、Feature PR、Bug Fix PR、Refactor PR，减少“把 issue 写成 PR”的常见错误。
- **按需读取 reference**：`SKILL.md` 只做轻量入口，具体规则按场景加载，避免把所有模板一次性塞进上下文。
- **内置事实边界**：版本号、命令、CI、兼容性、release 信息、issue/PR 编号等不能确认时不编造，改用 TODO / TBD / 待确认。
- **输出更接近可提交 artifact**：强调去掉对话前言、外层代码块、测试标题、复制残留和无关内容，让结果更像真实 GitHub artifact。
- **参考真实开源项目**：规则吸收了 GitHub Docs、Conventional Commits、Keep a Changelog，以及 React、Kubernetes、TypeScript、Node.js、Tailwind CSS 等成熟项目的写作习惯。

## 适用范围

根据各平台对 skill、规则文件和自定义指令的支持程度，本仓库可以有几种使用方式：

**作为 skill 使用**：工具可以加载包含 `SKILL.md` 的目录，并按需读取 `reference/`。这类方式最能保留场景路由和渐进加载能力。

**作为规则使用**：工具不能直接消费本仓库格式时，可以把 `SKILL.md` 的路由表和对应 `reference/*.md` 放进自定义指令、项目规则或知识库中。此时仍可复用 18 个场景标准，但触发和按需加载能力取决于目标工具。

| 图标 | Agent / Tool | 推荐接入方式 | 注意事项 / 文档 |
|------|--------------|--------------|---------------|
| <img src="https://openai.com/favicon.ico" width="14" height="14" alt="OpenAI"> | Codex | 克隆到 `$HOME/.agents/skills/oh-my-gh-writing`，或作为项目 skill 放到 `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <img src="https://claude.ai/favicon.ico" width="14" height="14" alt="Claude"> | Claude Code | 克隆或软链接到 `~/.claude/skills/oh-my-gh-writing`，或项目内 `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <img src="https://geminicli.com/favicon.ico" width="14" height="14" alt="Gemini CLI"> | Gemini CLI / Antigravity CLI | Gemini CLI 文档列出 `~/.gemini/skills/`、`~/.agents/skills/` 和 `gemini skills install` | 部分用户正在迁移到 Antigravity CLI，使用前按 [当前官方说明](https://geminicli.com/docs/cli/skills/) 确认 |
| <img src="https://hermes-agent.nousresearch.com/favicon.ico" width="14" height="14" alt="Hermes"> | Hermes | 放入 `~/.hermes/skills/<category>/oh-my-gh-writing` | HTTP 单文件安装只适合 `SKILL.md`；本仓库建议保留 `reference/` 目录。见 [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <img src="https://cursor.com/favicon.ico" width="14" height="14" alt="Cursor"> | Cursor | 将路由摘要和需要的场景规则改写为项目规则；长 reference 可作为知识库索引 | 具体规则格式按 [Cursor Docs](https://cursor.com/docs) 当前版本确认 |
| <img src="https://github.com/favicon.ico" width="14" height="14" alt="GitHub"> | GitHub Copilot | 改写为 `.github/copilot-instructions.md`、`.github/instructions/*.instructions.md` 或 Copilot agent skill 结构 | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14" alt="Continue"> | Continue | 改写为 `.continue/rules/*.md`；按场景拆规则比塞进单个文件更稳定 | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <img src="https://docs.windsurf.com/favicon.ico" width="14" height="14" alt="Windsurf"> | Windsurf / Devin Desktop | 当前文档提到 memories and rules 可用于自定义行为 | 具体规则文件路径和接入方式需按 [Windsurf / Devin Docs](https://docs.windsurf.com) 当前版本确认 |

表中未列出的工具只要支持读取 Markdown、自定义系统指令、项目规则或知识库，也可以使用本技能的规则。最稳妥的方式是保留 `SKILL.md` 的路由表，再按任务只复制对应的 `reference/*.md`。

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
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
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
    ├── *.md                  # 18 个场景标准
    ├── readme.md             # README 写作规则
    ├── shared-principles.md  # 通用输出质量规则
    ├── output-validation.md  # 输出验收清单
    ├── source-catalog.md     # 参考来源目录
    ├── weapons.md            # GitHub Markdown 工具
    ├── emoji-guide.md        # 常用 emoji 场景索引
    └── badge-catalog.md      # badge 模式目录
```

## 贡献

欢迎贡献场景规则、参考来源、输出验收规则和小型 Markdown 工具改进。案例也有价值，但请先通过 Issue 或 Discussion 描述来源、场景、测试目标和授权/隐私边界，不要直接提交大批复制内容或本地验证输出。

贡献时请保持 `SKILL.md` 轻量，把场景细节写入对应 `reference/*.md`。详细规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 参考来源

本项目的场景规则参考了 [GitHub Docs](https://docs.github.com/en)、[Conventional Commits](https://www.conventionalcommits.org/)、[Keep a Changelog](https://keepachangelog.com/)、[Google Engineering Practices](https://google.github.io/eng-practices/review/)，以及 Angular、Kubernetes、React、TypeScript、VS Code、Node.js、Tailwind CSS 等成熟开源项目的 Issue/PR 模板和贡献指南。完整来源见 [`reference/source-catalog.md`](reference/source-catalog.md)。

## 许可证

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
