<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">✨ oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Skill-v0.1.0-2563eb?style=flat" alt="Skill v0.1.0"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 artifact standards"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 workflow packs"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · 简体中文
</p>

> 英文 README 是 canonical 版本；本文档是同步维护的简体中文译本。

**oh-my-gh-writing** 是一个面向 AI Agent 的 GitHub 写作 Skill。它帮助 agent 起草更干净的 GitHub Issue、PR 描述、Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form、PR Template，以及多文件 workflow pack。

核心思路很简单：先判断请求属于哪类 GitHub 写作任务，再只加载对应标准，明确事实边界，最后输出更少需要清理的 GitHub artifact 或本地草稿包。

## 🚀 快速开始

只安装 runtime skill 文件。下面的 Codex 路径已经由维护者验证：

```bash
target="$HOME/.agents/skills/oh-my-gh-writing"
tmp="$(mktemp -d)"
repo="$tmp/oh-my-gh-writing"
git clone --depth 1 https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$repo"
rm -rf "$target"
mkdir -p "$target"
cp -R "$repo/SKILL.md" "$repo/INDEX.md" "$repo/references" "$target/"
rm -rf "$tmp"
```

其他有文档依据但维护者暂未实测的 host，可以使用同一段命令，只替换 `target`：

| Host | Target path | 状态 |
| --- | --- | --- |
| Claude Code | `$HOME/.claude/skills/oh-my-gh-writing` | 有官方文档依据，维护者暂未实测 |
| Gemini CLI | `$HOME/.agents/skills/oh-my-gh-writing` | 有官方文档依据，维护者暂未实测 |
| Hermes | `$HOME/.hermes/skills/github/oh-my-gh-writing` | 有官方文档依据，维护者暂未实测 |

如果要参与仓库开发或运行维护验证，单独 clone 完整仓库：

```bash
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

从这些提示词开始：

```text
/oh-my-gh-writing 帮我根据这个仓库写一个 README。
/oh-my-gh-writing 根据当前 diff 写一个 PR description。
/oh-my-gh-writing 根据这些已合并 PR 摘要准备 v1.2.0 的完整发布材料：修复登录重定向、增加 CSV 导出、更新文档。不要发布任何东西。
```

如果你使用兼容 Agent Skills 的包管理工具，请确认安装后的 skill 目录里同时包含 `SKILL.md` 和 `references/`。本仓库有意不把 `evals/`、`cases/`、`scripts/` 放进 runtime 安装。

## 🧪 调用示例

| Prompt | 路由到 | 预期产物形态 |
| --- | --- | --- |
| `/oh-my-gh-writing 我要发布一个新的开源项目，需要准备哪些 GitHub 材料？` | Project Launch audit | 发布准备度审查：已有文件、建议补充文件、可选文件和下一步。不创建文件，也不生成 `.github-writing/` 草稿。 |
| `/oh-my-gh-writing 请为这个新开源项目起草 public launch package，但不要发布任何东西。` | Project Launch workflow pack | 本地 `.github-writing/project-launch/TBD/` 草稿，包含 README、CONTRIBUTING、Issue Form、PR Template 和 `package-manifest.md` |
| `/oh-my-gh-writing 根据这些已合并 PR 摘要准备 v1.2.0 发布材料：修复登录重定向、增加 CSV 导出、更新文档。不要发布。` | Version Release workflow pack | 本地 `.github-writing/version-release/v1.2.0/` 发布草稿、manifest 和确认项 |
| `/oh-my-gh-writing 帮这个仓库建立接收外部贡献的流程。` | Contribution Setup workflow pack | CONTRIBUTING、Issue Form、PR Template、README 贡献入口和本地 manifest |
| `/oh-my-gh-writing 根据这个 diff 写一个 bug-fix PR。测试还没跑。` | Bug Fix PR | PR 正文，包含摘要、已有 root-cause 证据、未运行测试说明和风险提示 |
| `/oh-my-gh-writing 创建一个 bug report Issue Form YAML。labels 和 assignees 都未确认。` | Issue Form YAML | YAML 文件内容，不编造 labels、assignees、projects 或 contact links |

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
| Skill 目录 | Codex、Claude Code、目录兼容的 skill host | 路由、按需读取、输出验收最完整 | 需要本地文件读取能力 |
| 项目规则 | Cursor、Continue、GitHub Copilot | 在项目内复用选定标准 | 需要按工具格式手动适配 |
| 知识库 | 可检索 Markdown 的 agent 或团队规范库 | 结构标准、来源说明、质量规则 | 路由依赖宿主工具能力 |

## 🧭 覆盖内容

| 类型 | 内容 |
| --- | --- |
| 18 个 artifact 标准 | Bug Report、Feature Request、Enhancement、Discussion、Feature PR、Bug Fix PR、Refactor PR、Documentation PR、Code Review、Standard Commit、README、CONTRIBUTING、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form YAML、PR Template |
| 7 个 workflow pack | Version Release、Project Launch、Contribution Setup、Bug Fix Workflow、Proposal to Implementation、Breaking Change Package、Docs Overhaul |
| 质量附录 | shared principles、output validation、badge patterns、emoji guide、GitHub Markdown tools、source catalog |

Workflow pack 只做编排：能安全判断时会推断最合适的材料包，无法安全判断时才询问，并把所选方案记录到 `package-manifest.md`。默认输出到本地 `.github-writing/...` 草稿目录，不默认发布 release、推 tag、开 PR 或修改远端状态。

## 🤖 Agent 支持

最后检查：2026-06-20。

### 原生或目录兼容安装

| Agent / Tool | 支持类型 | 推荐接入方式 | 维护者已验证 | 最后检查 | 说明 |
| --- | --- | --- | --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | 原生 skill 目录 | `$HOME/.agents/skills/oh-my-gh-writing` 或项目 `.agents/skills/oh-my-gh-writing` | 是 | 2026-06-20 | 官方文档列出 `.agents/skills` 用户和仓库位置 |
| [Claude Code](https://code.claude.com/docs/en/skills) | 原生 skill 目录 | `~/.claude/skills/oh-my-gh-writing` 或项目 `.claude/skills/oh-my-gh-writing` | 暂未 | 2026-06-20 | 官方文档使用包含 `SKILL.md` 的目录作为 skill 入口 |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | 原生 skill 目录 | 手动 runtime-only 复制到 `$HOME/.agents/skills/oh-my-gh-writing` 或 `.agents/skills/oh-my-gh-writing` | 暂未 | 2026-06-20 | 官方文档列出 `.agents/skills` alias，并支持 `gemini skills install`，但本仓库不应安装非 runtime 文件，需验证安装结果 |
| [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | 原生 skill 目录 | 把 runtime 目录复制到 `~/.hermes/skills/github/oh-my-gh-writing` | 暂未 | 2026-06-20 | 本仓库依赖 `references/`，不要使用 HTTP 单文件安装 |

### 宿主工具规则 / 指令设置

这些工具不能直接消费完整 Agent Skill 目录。使用时需要把 router 和选定的 `references/*.md` 改写为该工具的规则或指令格式。

| 工具 | 支持方式 | 推荐文件 / 路径 | 维护者已验证 | 最后检查 | 说明 |
| --- | --- | --- | --- | --- | --- |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 仓库 custom instructions | `.github/copilot-instructions.md`、`.github/instructions/gh-writing.instructions.md` 或 `AGENTS.md` | 暂未 | 2026-06-20 | 用压缩版规则；Copilot 不会自动加载本 skill 目录 |
| [Continue](https://docs.continue.dev/customize/rules) | 项目 rules | `.continue/rules/oh-my-gh-writing.md` | 暂未 | 2026-06-20 | 内容较长时按场景拆分 |
| [Cursor](https://cursor.com/docs) | 项目 rules | `.cursor/rules/oh-my-gh-writing.mdc` | 暂未 | 2026-06-20 | 这是规则适配，不是原生 Agent Skill 支持 |

### 暂不列为已支持

| 工具 | 状态 | 最后检查 | 说明 |
| --- | --- | --- | --- |
| Antigravity CLI | 未确认 | 2026-06-20 | 等官方文档确认稳定 skill 或 rules 路径后再写安装方式 |
| Windsurf / Devin Desktop | 未确认 | 2026-06-20 | 当前文档跳转到 Devin Desktop，未看到适合本包的稳定 skill/rules 路径 |

## 📂 文件

| 路径 | 作用 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | 轻量运行时路由和工作流规则 |
| [`INDEX.md`](INDEX.md) | 18 个 artifact 标准和 7 个 workflow pack 的导航 |
| [`references/`](references) | 场景标准、workflow pack 和质量附录 |
| [`references/readme.md`](references/readme.md) | README 写作标准 |
| [`references/source-catalog.md`](references/source-catalog.md) | 公开参考来源和维护说明 |
| [`evals/`](evals) | 用于后续 skill 迭代的触发和输出质量 eval fixtures |
| [`scripts/`](scripts) | 维护者验证工具 |
| [`cases/`](cases) | 公开 evidence drafts，不是 runtime references |
| [`.github/`](.github) | 公开 Issue Forms 和 Pull Request Template |
| [`README_Example.md`](README_Example.md) | 由 skill 生成的 README 示例，不是 canonical 首页 |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | 贡献说明 |
| [`assets/`](assets) | Logo 和 README 本地资产 |

## 🧪 评估

本仓库包含轻量 eval fixtures，便于后续维护：

- [`evals/trigger-queries.json`](evals/trigger-queries.json) 用来检查 skill description 是否会在真实 GitHub 写作请求中触发，并避开相近但不该触发的请求。
- [`evals/evals.json`](evals/evals.json) 记录输出质量任务，覆盖路由、输出清洁、事实边界和 workflow pack 行为。
- [`evals/expected/`](evals/expected) 保存短小 clean outputs，用来展示合格 artifact 的形态。
- [`cases/`](cases) 保存 synthetic public evidence drafts，用来观察路由和事实边界表现；它们不是 runtime references。

运行：

```bash
python3 scripts/validate-evals.py
python3 scripts/validate-cases.py
```

## 🧪 示例：项目公开发布前的文件审查

这是一个 synthetic review-draft excerpt，不是真实仓库结果，也不是 validated comparison case。

输入：

```text
Please check what files this sample repository still needs before I publish the project to GitHub.

Current repository files: README.md, LICENSE, SKILL.md, references/, evals/, scripts/.
```

输出片段：

```markdown
## Existing

- README: present.
- License: present.

## Recommended

- CONTRIBUTING.md — explains setup, test, branch, and PR expectations before outside contributors arrive.
- Bug report Issue Form — standardizes defect reports with reproduction, expected behavior, actual behavior, and environment fields.
- Pull request template — gives contributors a consistent place for summary, testing, risk, and related issues.

## Next steps

- Confirm which recommended files to prepare.
- Draft target files only after maintainer confirmation.
```

首页片段是缩短版；完整 case 还包含 Feature request Issue Form、Validation workflow 和 Changelog 建议。

完整 synthetic review-draft case 见 [`cases/005-project-launch-audit/`](cases/005-project-launch-audit/)。Baseline behavior 还没有收集。

## 📚 参考来源

本项目标准参考 [Agent Skills specification](https://agentskills.io/specification)、[GitHub Docs](https://docs.github.com/en)、[Conventional Commits](https://www.conventionalcommits.org/)、[Keep a Changelog](https://keepachangelog.com/)、[Google Engineering Practices](https://google.github.io/eng-practices/review/)，以及 React、Kubernetes、TypeScript、Node.js、Tailwind CSS、Angular、VS Code 等成熟开源项目的写作模式。完整来源见 [`references/source-catalog.md`](references/source-catalog.md)。

source catalog 不会被复制到用户产物中；它只记录结构模式和维护依据。

## 📄 许可证

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
