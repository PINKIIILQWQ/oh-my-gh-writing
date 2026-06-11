<p align="center">
  <a href="#english">English</a> · <a href="#chinese">简体中文</a>
</p>

<p align="center">
  <img src="./assets/oh-my-gh-writing-logo.png" width="320" alt="oh-my-gh-writing logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/8%20categories-18%20scenarios-blue" alt="18 scenarios">
  <img src="https://img.shields.io/badge/22%20reference%20repos-green" alt="reference repos">
  <img src="https://img.shields.io/badge/agent%20support-14%20frameworks-orange" alt="agent support">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="license">
  <img src="https://img.shields.io/badge/Hermes%20Skill-v1.0.0-brightgreen" alt="hermes skill">
</p>

---

<a id="english"></a>
<h1 align="center">oh-my-gh-writing</h1>
<p align="center"><em>GitHub Writing Standards — Issue · PR · Review · Commit · Docs · Release · Design · Templates — 2 levels (Complete / Normal) per scenario from 22 reference repos, delivered as a portable SKILL.md</em></p>

---

## Index

- [What is this?](#what-is-this)
- [Product Scope](#product-scope)
- [Quick Start](#quick-start)
- [Features](#features)
- [Use Cases](#use-cases)
- [Agent Compatibility](#agent-compatibility)
- [Project Structure](#project-structure)
- [Design Principles](#design-principles)
- [Contributing](#contributing)
- [Star History](#star-history)
- [License & Acknowledgments](#license--acknowledgments)

---

## What is this?

**oh-my-gh-writing** distills the writing practices of 22 top open-source projects — [VS Code](https://github.com/microsoft/vscode), [Kubernetes](https://github.com/kubernetes/kubernetes), [React](https://github.com/facebook/react), [Go](https://github.com/golang/go), [Next.js](https://github.com/vercel/next.js), [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss), [Electron](https://github.com/electron/electron), [Django](https://github.com/django/django), [Angular](https://github.com/angular/angular), [Rust](https://github.com/rust-lang/rust), [Linux](https://github.com/torvalds/linux), [Node.js](https://github.com/nodejs/node), [Deno](https://github.com/denoland/deno), [Supabase](https://github.com/supabase/supabase), [Pandas](https://github.com/pandas-dev/pandas), [Prettier](https://github.com/prettier/prettier), [Lodash](https://github.com/lodash/lodash), [Redux](https://github.com/reduxjs/redux), [Immer](https://github.com/immerjs/immer), [TypeScript](https://github.com/microsoft/TypeScript), [Rails](https://github.com/rails/rails), [ESLint](https://github.com/eslint/eslint) — into a single, executable specification.

Each reference is capped at **≤3 scenarios** (see [Design Principles](#design-principles)), and every brand, protocol, and license mentioned links to its source.

**What problems does it solve?**

- Teams maintain consistent Issue/PR/Commit formatting without manual review cycles
- AI agents produce GitHub content following real community practices, reducing post-generation edits
- New contributors onboard faster with explicit templates and checklists for every common scenario

## Product Scope

| Dimension | Details |
|-----------|---------|
| **Format** | [`SKILL.md`](https://hermes-agent.nousresearch.com/docs) (Hermes Agent native) — YAML frontmatter + markdown body, progressive disclosure |
| **Carrier** | File-based — copy `SKILL.md` + `reference/` directory into any agent's rules directory or load via supported framework |
| **Dependencies** | None — pure markdown, no build step, no runtime |
| **Supported frameworks** | 14 platforms (see [Agent Compatibility](#agent-compatibility)) |
| **Reference repos** | 22 open-source projects, each ≤3 scenarios |
| **Coverage** | 8 categories — Issue (4) / PR (4) / Review (1) / Commit (1) / Docs (4) / Release (2) / Design (1) / Templates (2) |
| **Complexity levels** | 2 per scenario — **Complete** (full fields, multi-repo examples, variants) and **Normal** (all essential parts, stripped optional) |

## Quick Start

**Option 1 — Hermes Agent (native)**

```bash
# Clone the repository
git clone git@github.com:PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing

# Install the skill
hermes skill install ./SKILL.md

# Use it
hermes run "oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。"
```

**Option 2 — Copy to any agent rules directory**

```bash
# Claude Code
cp SKILL.md ./CLAUDE.md
cp reference/ ./reference/ -r

# Cursor
cp SKILL.md ./.cursorrules

# Windsurf
cp SKILL.md ./.windsurfrules
```

**Expected behavior**

After loading the skill, when you ask for a Bug Report, you get:

```
### Bug Report: Chrome 首次加载白屏 3 秒

**Version**
- Chrome 125.0.6422.142
- Firefox 126.0
- Project version v2.4.1

**Reproduction Steps**
1. Open Chrome, visit https://example.com
2. Wait for page to load
3. White screen for 3 seconds, then normal rendering
4. Firefox has no such issue

**Expected Behavior**
Page should render content within 1 second

**Actual Behavior**
First load shows white screen for 3 seconds; subsequent navigations work normally

**Environment**
OS: macOS 14.5, Chrome 125, Node 20.12
```

## Features

| Category | Scenarios | Includes |
|----------|-----------|----------|
| **Issue** | Bug Report, Feature Request, Enhancement, Discussion | Template structure, required fields, environment format, reproduction requirements |
| **PR** | Feature PR, Bug Fix PR, Refactor PR, Documentation PR | Motivation + design + tests + breaking check + upgrade guide |
| **Review** | Code Review | Location annotation, severity grading, suggestion format |
| **Commit** | Standard Commit | `type(scope): subject` format, body/footer rules, 11 type definitions per [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (Angular convention) |
| **Docs** | README, CONTRIBUTING, CHANGELOG, Migration Guide | Structure skeleton, badges, quickstart, bilingual default |
| **Release** | Release Notes, Migration Guide | Highlights + breaking changes + migration path + full changelog link |
| **Design** | RFC | Motivation + design + compatibility + alternatives + open questions |
| **Templates** | Issue Form YAML, PR Template | YAML field definitions, validation rules, example forms from 6 top-tier projects |

Each scenario provides two complexity levels:
- **Complete** — full field set, multi-repo detailed examples, variant outputs
- **Normal** — all required fields, necessary context, learnable in 2 minutes

## Use Cases

> Use `/oh-my-gh-writing` as the invocation prefix.

- **`/oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。`** — Generates a bilingual README with badges, quickstart, feature table, and all referenced brands hyperlinked
- **`/oh-my-gh-writing 开一个 Bug Report Issue：Node 20 下内存泄漏。`** — Produces a structured bug report with reproduction steps, environment auto, and severity label
- **`/oh-my-gh-writing Review 这个 PR #42 的代码。`** — Outputs a line-by-line review with severity grades following Linux LKML conventions
- **`/oh-my-gh-writing 写一行符合 Conventional Commits 的 commit message。`** — Returns `<type>(<scope>): <subject>` with body explaining the change rationale

Generate a README that follows the best practices of [Next.js](https://github.com/vercel/next.js), [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss), and [VS Code](https://github.com/microsoft/vscode).

## Agent Compatibility

oh-my-gh-writing ships as a [`SKILL.md`](https://hermes-agent.nousresearch.com/docs) (Hermes native), but its content is consumable by any agent framework that accepts markdown instruction files. Below is the compatibility matrix:

| Platform | Instruction File | YAML Frontmatter | Direct Use | Adaptation Needed | Notes |
|----------|----------------|:---:|:---:|:---:|-------|
| **[Hermes Agent](https://hermes-agent.nousresearch.com/docs)** | `SKILL.md` | ✅ | ✅ | None | Native format, load via `hermes skill load` |
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)** (Anthropic) | `CLAUDE.md` | ❌ | ⚠️ | Strip frontmatter, keep body | Highest compatibility; 70% of scenarios work as-is |
| **[Cursor](https://docs.cursor.com/context/rules-for-ai)** (Anysphere) | `.cursorrules` | ❌ | ⚠️ | Strip frontmatter | Configures AI behavior per-project |
| **[GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)** | `.github/copilot-instructions.md` | ❌ | ⚠️ | Strip frontmatter, flatten sections | Supports Issue/PR/Commit instructions natively |
| **[Cline](https://github.com/cline/cline)** | `.clinerules` | ❌ | ⚠️ | Strip frontmatter | VS Code extension, markdown rules |
| **[Roo Code](https://github.com/RooVetGit/Roo-Cline)** | `.roorules` | ❌ | ⚠️ | Strip frontmatter | Fork of Cline, same format |
| **[Windsurf](https://codeium.com/windsurf)** (Codeium) | `.windsurfrules` | ❌ | ⚠️ | Strip frontmatter, simplify | Cascade AI rules engine |
| **[Continue](https://docs.continue.dev/customize/how-continue-works)** | `.continuerc.json` / `.continuerc.yaml` | ❌ | ❌ | Convert to JSON/YAML | Config-based, less flexible for prose rules |
| **[Aider](https://aider.chat/docs/usage/conventions.html)** (Paul Gauthier) | `CONVENTIONS.md` | ❌ | ⚠️ | Strip frontmatter | Code conventions, best for commit/docs rules |
| **[Augment Code](https://www.augmentcode.com/)** | `.augment/` dir | ❌ | ⚠️ | Split into separate rule files | Directory-based rules |
| **[OpenCode](https://github.com/opencode-ai/opencode)** | `.opencode/rules/` | ❌ | ⚠️ | Split into per-rule files | Multi-file rules directory |
| **[Codex CLI](https://github.com/openai/codex)** (OpenAI) | `RULES.md` | ❌ | ⚠️ | Strip frontmatter | OpenAI's agent CLI |
| **[Sourcegraph Cody](https://sourcegraph.com/cody)** | `.cody/` dir | ❌ | ⚠️ | Adapt format | AI coding assistant context files |
| **[Zed AI](https://zed.dev/)** | `.zed/` settings | ❌ | ❌ | Extract rules | JSON-based settings, partial support |

**Legend**: ✅ Native | ⚠️ Needs minor adaptation | ❌ Format mismatch (but content can be extracted)

For non-Hermes platforms, copy `SKILL.md` to the appropriate file/directory and strip the YAML frontmatter (lines between `---` delimiters).

## Project Structure

```
oh-my-gh-writing/
├── assets/
│   └── oh-my-gh-writing-logo.png    # Project logo
├── SKILL.md                          # Entry index + 7 principles + index table + weapons (fits in 4KB core)
├── reference/                        # 18 scenarios × 2 complexity levels + appendix
│   ├── bug-report.md                 # Bug Report writing standard
│   ├── feature-request.md            # Feature Request writing standard
│   ├── feature-pr.md                 # Feature PR writing standard
│   ├── bug-fix-pr.md                 # Bug Fix PR writing standard
│   ├── code-review.md                # Code Review writing standard
│   ├── standard-commit.md            # Standard Commit writing standard
│   ├── readme.md                     # README writing standard
│   ├── contributing.md               # CONTRIBUTING writing standard
│   ├── changelog.md                  # CHANGELOG writing standard
│   ├── release-notes.md              # Release Notes writing standard
│   ├── migration-guide.md            # Migration Guide writing standard
│   ├── rfc.md                        # RFC writing standard
│   ├── issue-form-yaml.md            # Issue Form YAML writing standard
│   ├── pr-template.md                # PR Template writing standard
│   └── weapons.md                    # Formatting Weapons appendix (alerts, badges, mermaid, etc.)
├── DOCS/                             # Source materials & design documents
│   ├── collection-plan.md            # Collection plan
│   ├── skill-outline.md              # v1 outline
│   └── skill-outline-v2.md           # v2 outline (revised)
├── test/                             # Test suite
│   ├── README.md                     # Test index & workflow
│   └── compare-18-scenarios.md       # 18-scenario comparison with new reference repos
└── README.md                         # This file
```

## Design Principles

| # | Principle | Description |
|---|-----------|-------------|
| 1 | **Progressive Disclosure** | `SKILL.md` core ≤4KB; details in `reference/`; source materials in `DOCS/` |
| 2 | **Repo Quota System** | 22 reference repos, each appearing in **≤3 scenarios** — prevents over-reliance on any single project |
| 3 | **2 Complexity Tracks** | **Complete** (full fields + multi-repo examples + variants) and **Normal** (all essential parts only) |
| 4 | **Bilingual by Default** | All content available in both English and Chinese; README anchors `[English](#english)` / `[简体中文](#chinese)` at top |
| 5 | **Hyperlink Every Reference** | Every brand ([MIT](https://opensource.org/licenses/MIT)), protocol ([Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)), vendor ([OpenAI](https://openai.com)), and tool ([shields.io](https://shields.io)) must link to its source |
| 6 | **No Prompt Leakage** | Scenario descriptions must never contain system prompts, "you are" instructions, or role-play directives |
| 7 | **Auditable Origins** | Every scenario's reference section includes direct links to the source repo's actual template/config files, not just the README |

## Contributing

GitHub Issues and PRs are welcome. See the [source repository](https://github.com/PINKIIILQWQ/oh-my-gh-writing).

**Before contributing**: review the [7 Writing Principles](https://github.com/PINKIIILQWQ/oh-my-gh-writing/blob/main/SKILL.md#7-%E6%9D%A1%E5%86%99%E4%BD%9C%E9%80%9A%E7%94%A8%E5%8E%9F%E5%88%99) that govern all scenarios.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=PINKIIILQWQ/oh-my-gh-writing&type=Date)](https://star-history.com/#PINKIIILQWQ/oh-my-gh-writing&Date)

> **Is there anything else that needs attention?** — After generating the first draft, confirm with the user: do you need Star History? multi-language variants? specific badge style? any specific features or community links to highlight?

## License & Acknowledgments

- **License**: [MIT](https://opensource.org/licenses/MIT)
- **Reference repos**: [VS Code](https://github.com/microsoft/vscode) · [Kubernetes](https://github.com/kubernetes/kubernetes) · [React](https://github.com/facebook/react) · [Go](https://github.com/golang/go) · [Next.js](https://github.com/vercel/next.js) · [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) · [Electron](https://github.com/electron/electron) · [Django](https://github.com/django/django) · [Angular](https://github.com/angular/angular) · [Rust](https://github.com/rust-lang/rust) · [Linux](https://github.com/torvalds/linux) · [Node.js](https://github.com/nodejs/node) · [Deno](https://github.com/denoland/deno) · [Supabase](https://github.com/supabase/supabase) · [Pandas](https://github.com/pandas-dev/pandas) · [Prettier](https://github.com/prettier/prettier) · [Lodash](https://github.com/lodash/lodash) · [Redux](https://github.com/reduxjs/redux) · [Immer](https://github.com/immerjs/immer) · [TypeScript](https://github.com/microsoft/TypeScript) · [Rails](https://github.com/rails/rails) · [ESLint](https://github.com/eslint/eslint)
- **Agent frameworks**: [Hermes Agent](https://hermes-agent.nousresearch.com) · [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) · [Cursor](https://docs.cursor.com/context/rules-for-ai) · [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) · [Cline](https://github.com/cline/cline) · [Windsurf](https://codeium.com/windsurf) · [Aider](https://aider.chat) · [Codex CLI](https://github.com/openai/codex)
- **Tools**: [shields.io](https://shields.io) (badge generator) · [Star History](https://star-history.com)

---

<a id="chinese"></a>
<h1 align="center">oh-my-gh-writing</h1>
<p align="center"><em>GitHub 写作规范 —— Issue/PR/Review/Commit/文档/发布/设计/模板 —— 每场景完整+普通 2 级标准，覆盖 22 个参考仓库，以可移植 SKILL.md 分发</em></p>

---

## 目录

- [这是什么？](#这是什么)
- [产品适用范围](#产品适用范围)
- [快速开始](#快速开始)
- [功能](#功能)
- [使用案例](#使用案例)
- [Agent 兼容性](#agent-兼容性)
- [项目结构](#项目结构)
- [设计原则](#设计原则)
- [贡献指南](#贡献指南)
- [Star 历史](#star-历史)
- [许可与致谢](#许可与致谢)

---

## 这是什么？

**oh-my-gh-writing** 将 22 个顶级开源项目的写作实践提炼为一套可执行规范。参考仓库包括 [VS Code](https://github.com/microsoft/vscode)、[Kubernetes](https://github.com/kubernetes/kubernetes)、[React](https://github.com/facebook/react)、[Go](https://github.com/golang/go)、[Next.js](https://github.com/vercel/next.js)、[Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)、[Electron](https://github.com/electron/electron)、[Django](https://github.com/django/django)、[Angular](https://github.com/angular/angular)、[Rust](https://github.com/rust-lang/rust)、[Linux](https://github.com/torvalds/linux)、[Node.js](https://github.com/nodejs/node)、[Deno](https://github.com/denoland/deno)、[Supabase](https://github.com/supabase/supabase)、[Pandas](https://github.com/pandas-dev/pandas)、[Prettier](https://github.com/prettier/prettier)、[Lodash](https://github.com/lodash/lodash)、[Redux](https://github.com/reduxjs/redux)、[Immer](https://github.com/immerjs/immer)、[TypeScript](https://github.com/microsoft/TypeScript)、[Rails](https://github.com/rails/rails)、[ESLint](https://github.com/eslint/eslint)。

每仓库出现在 **≤3 个场景**（见[设计原则](#设计原则)），提及的品牌、协议、许可均附带源地址链接。

**解决了什么问题？**

- 团队保持 Issue/PR/Commit 格式统一，无需反复 review 排版
- AI agent 产出 GitHub 内容时遵循真实社区实践，减少人工修正
- 新贡献者通过显式模板和 checklist 快速对齐协作规范

## 产品适用范围

| 维度 | 详情 |
|------|------|
| **格式** | [`SKILL.md`](https://hermes-agent.nousresearch.com/docs)（Hermes Agent 原生）—— YAML frontmatter + markdown 正文，渐进式披露 |
| **载体** | 纯文件 —— 将 `SKILL.md` + `reference/` 目录复制到任意 agent 的规则目录即可 |
| **依赖** | 无 —— 纯 markdown，无需构建步骤、无需运行时 |
| **支持的框架** | 14 个平台（见 [Agent 兼容性](#agent-兼容性)） |
| **参考仓库** | 22 个开源项目，每仓库 ≤3 场景 |
| **覆盖范围** | 8 大类 —— Issue(4) / PR(4) / Review(1) / Commit(1) / 文档(4) / 发布(2) / 设计(1) / 模板(2) |
| **复杂度等级** | 每场景 2 级 —— **完整版**（全字段+多仓库详解+变体）和 **普通版**（全部必要部分，精简可选） |

## 快速开始

**方式 1 —— Hermes Agent（原生）**

```bash
# 克隆仓库
git clone git@github.com:PINKIIILQWQ/oh-my-gh-writing.git
cd oh-my-gh-writing

# 安装 skill
hermes skill install ./SKILL.md

# 使用
hermes run "oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。"
```

**方式 2 —— 复制到任意 agent 规则目录**

```bash
# Claude Code
cp SKILL.md ./CLAUDE.md
cp reference/ ./reference/ -r

# Cursor
cp SKILL.md ./.cursorrules

# Windsurf
cp SKILL.md ./.windsurfrules
```

**预期效果**

加载 skill 后，当你要求写 Bug Report 时：

```
### Bug Report：Chrome 首次加载白屏 3 秒

**版本**
- Chrome 125.0.6422.142
- Firefox 126.0
- 项目版本 v2.4.1

**复现步骤**
1. 打开 Chrome，访问 https://example.com
2. 等待页面加载
3. 前 3 秒白屏，之后正常渲染
4. Firefox 无此问题

**预期行为**
页面应在 1 秒内呈现内容

**实际行为**
首次加载白屏 3 秒，后续导航正常

**环境**
OS: macOS 14.5, Chrome 125, Node 20.12
```

## 功能

| 类别 | 场景数 | 包含内容 |
|------|--------|---------|
| **Issue** | Bug Report、Feature Request、Enhancement、Discussion（4） | 模板结构、必填字段、环境格式、重现要求 |
| **PR** | Feature PR、Bug Fix PR、Refactor PR、Documentation PR（4） | 动机+设计+测试+Breaking 检查+升级指南 |
| **Review** | Code Review（1） | 位置标注、严重度分级、建议格式 |
| **Commit** | Standard Commit（1） | `type(scope): subject` 格式、body/footer 规范、11 种 type 定义 |
| **文档** | README、CONTRIBUTING、CHANGELOG、Migration Guide（4） | 结构骨架、徽章、快速开始、中英双语默认 |
| **发布** | Release Notes、Migration Guide（2） | 亮点+Breaking+迁移路径+完整 changelog 链接 |
| **设计** | RFC（1） | 动机+设计+兼容性+备选+开放问题 |
| **模板** | Issue Form YAML、PR Template（2） | YAML 字段定义、验证规则、6 个顶级项目实例 |

每场景分两级复杂度：
- **完整版** —— 全字段、多仓库详细写法示例、变体输出
- **普通版** —— 全部必要字段、2 分钟可学会

## 使用案例

> 使用 `/oh-my-gh-writing` 作为调用前缀。

- **`/oh-my-gh-writing 帮我把刚刚的仓库重写更细致的 README 文档。`** —— 生成双语 README，含徽章、快速开始、功能表和所有品牌超链接
- **`/oh-my-gh-writing 开一个 Bug Report Issue：Node 20 下内存泄漏。`** —— 生成结构化 bug 报告，含重现步骤、环境自动采集、严重度标签
- **`/oh-my-gh-writing Review 这个 PR #42 的代码。`** —— 按行输出 review 评论，带严重度分级，遵循 Linux LKML 审阅规范
- **`/oh-my-gh-writing 写一行符合 Conventional Commits 的 commit message。`** —— 返回 `<type>(<scope>): <subject>` 格式 commit，body 解释改动原因

生成一份遵循 [Next.js](https://github.com/vercel/next.js)、[Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)、[VS Code](https://github.com/microsoft/vscode) 最佳实践的 README。

## Agent 兼容性

oh-my-gh-writing 以 [`SKILL.md`](https://hermes-agent.nousresearch.com/docs)（Hermes 原生格式）分发，但内容可在任何支持 markdown 指令文件的 agent 框架中使用：

| 平台 | 指令文件 | YAML Frontmatter | 直接使用 | 需适配 | 说明 |
|------|---------|:---:|:---:|:---:|------|
| **[Hermes Agent](https://hermes-agent.nousresearch.com/docs)** | `SKILL.md` | ✅ | ✅ | 无 | 原生支持，`hermes skill load` 直接加载 |
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)** (Anthropic) | `CLAUDE.md` | ❌ | ⚠️ | 去掉 frontmatter，保留正文 | 兼容性最高；70% 场景即开即用 |
| **[Cursor](https://docs.cursor.com/context/rules-for-ai)** (Anysphere) | `.cursorrules` | ❌ | ⚠️ | 去掉 frontmatter | 按项目配置 AI 行为 |
| **[GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)** | `.github/copilot-instructions.md` | ❌ | ⚠️ | 去掉 frontmatter，扁平化章节 | 原生支持 Issue/PR/Commit 指令 |
| **[Cline](https://github.com/cline/cline)** | `.clinerules` | ❌ | ⚠️ | 去掉 frontmatter | VS Code 扩展，markdown 规则 |
| **[Roo Code](https://github.com/RooVetGit/Roo-Cline)** | `.roorules` | ❌ | ⚠️ | 去掉 frontmatter | Cline 分支，相同格式 |
| **[Windsurf](https://codeium.com/windsurf)** (Codeium) | `.windsurfrules` | ❌ | ⚠️ | 去掉 frontmatter，简化 | Cascade AI 规则引擎 |
| **[Continue](https://docs.continue.dev/customize/how-continue-works)** | `.continuerc.json` / `.continuerc.yaml` | ❌ | ❌ | 转为 JSON/YAML | 基于配置，不适合长篇幅规则 |
| **[Aider](https://aider.chat/docs/usage/conventions.html)** (Paul Gauthier) | `CONVENTIONS.md` | ❌ | ⚠️ | 去掉 frontmatter | 代码规范，最适合 commit/文档规则 |
| **[Augment Code](https://www.augmentcode.com/)** | `.augment/` 目录 | ❌ | ⚠️ | 拆分为独立规则文件 | 目录式规则 |
| **[OpenCode](https://github.com/opencode-ai/opencode)** | `.opencode/rules/` | ❌ | ⚠️ | 拆分为单规则文件 | 多文件规则目录 |
| **[Codex CLI](https://github.com/openai/codex)** (OpenAI) | `RULES.md` | ❌ | ⚠️ | 去掉 frontmatter | OpenAI 的 agent CLI |
| **[Sourcegraph Cody](https://sourcegraph.com/cody)** | `.cody/` 目录 | ❌ | ⚠️ | 适配格式 | AI 编程助手上下文文件 |
| **[Zed AI](https://zed.dev/)** | `.zed/` 配置 | ❌ | ❌ | 提取规则 | JSON 配置，部分支持 |

**图例**：✅ 原生 | ⚠️ 需小幅适配 | ❌ 格式不匹配（但内容可提取）

非 Hermes 平台：将 `SKILL.md` 复制到对应文件/目录，并去掉 YAML frontmatter（`---` 分隔符之间的内容）。

## 项目结构

```
oh-my-gh-writing/
├── assets/
│   └── oh-my-gh-writing-logo.png    # 项目图标
├── SKILL.md                          # 入口索引 + 7 条原则 + 索引表 + 武器库（核心 ≤4KB）
├── reference/                        # 18 场景 × 2 级标准 + 附录
│   ├── bug-report.md                 # Bug Report 写法标准
│   ├── feature-request.md            # Feature Request 写法标准
│   ├── feature-pr.md                 # Feature PR 写法标准
│   ├── bug-fix-pr.md                 # Bug Fix PR 写法标准
│   ├── code-review.md                # Code Review 写法标准
│   ├── standard-commit.md            # Standard Commit 写法标准
│   ├── readme.md                     # README 写法标准
│   ├── contributing.md               # CONTRIBUTING 写法标准
│   ├── changelog.md                  # CHANGELOG 写法标准
│   ├── release-notes.md              # Release Notes 写法标准
│   ├── migration-guide.md            # Migration Guide 写法标准
│   ├── rfc.md                        # RFC 写法标准
│   ├── issue-form-yaml.md            # Issue Form YAML 写法标准
│   ├── pr-template.md                # PR Template 写法标准
│   └── weapons.md                    # 格式化武器库附录（alerts、badges、mermaid 等）
├── DOCS/                             # 源材料与设计文档
│   ├── collection-plan.md            # 收集计划
│   ├── skill-outline.md              # v1 大纲
│   └── skill-outline-v2.md           # v2 大纲（修订版）
├── test/                             # 测试套件
│   ├── README.md                     # 测试索引与流程
│   └── compare-18-scenarios.md       # 18 场景双版对比（新参考仓库）
└── README.md                         # 本文件
```

## 设计原则

| # | 原则 | 说明 |
|---|------|------|
| 1 | **渐进式披露** | `SKILL.md` 核心 ≤4KB；细节在 `reference/`；源材料在 `DOCS/` |
| 2 | **仓库配额制** | 22 个参考仓库，每仓库出现在 **≤3 个场景** —— 避免过度依赖单个项目 |
| 3 | **两条复杂度轨道** | **完整版**（全字段+多仓库详解+变体）和 **普通版**（全部必要部分，精简可选） |
| 4 | **中英双语默认** | 所有内容中英文双语可用；README 顶部提供 `[English](#english)` / `[简体中文](#chinese)` 锚点切换 |
| 5 | **所有引用含超链接** | 每个品牌（[MIT](https://opensource.org/licenses/MIT)）、协议（[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)）、厂商（[OpenAI](https://openai.com)）、工具（[shields.io](https://shields.io)）必须链接到源地址 |
| 6 | **无提示词泄漏** | 场景描述中不得包含系统提示词、"你是"指令或角色扮演指令 |
| 7 | **来源可追溯** | 每个场景的参考部分包含指向源仓库实际模板/配置文件的直接链接，而非仅 README |

## 贡献指南

欢迎提交 Issue 或 PR。详见[源仓库](https://github.com/PINKIIILQWQ/oh-my-gh-writing)。

**贡献前**：请先阅读适用于所有场景的[7 条写作通用原则](https://github.com/PINKIIILQWQ/oh-my-gh-writing/blob/main/SKILL.md#7-%E6%9D%A1%E5%86%99%E4%BD%9C%E9%80%9A%E7%94%A8%E5%8E%9F%E5%88%99)。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=PINKIIILQWQ/oh-my-gh-writing&type=Date)](https://star-history.com/#PINKIIILQWQ/oh-my-gh-writing&Date)

> **请问还有什么需要额外注意的地方吗？** —— 初稿产出后向使用者确认：是否需要补充 Star History？是否需要多语言变体？是否要特定风格的徽章？是否有需要强调的特定功能或社区链接？

## 许可与致谢

- **许可**：[MIT](https://opensource.org/licenses/MIT)
- **参考仓库**：[VS Code](https://github.com/microsoft/vscode) · [Kubernetes](https://github.com/kubernetes/kubernetes) · [React](https://github.com/facebook/react) · [Go](https://github.com/golang/go) · [Next.js](https://github.com/vercel/next.js) · [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) · [Electron](https://github.com/electron/electron) · [Django](https://github.com/django/django) · [Angular](https://github.com/angular/angular) · [Rust](https://github.com/rust-lang/rust) · [Linux](https://github.com/torvalds/linux) · [Node.js](https://github.com/nodejs/node) · [Deno](https://github.com/denoland/deno) · [Supabase](https://github.com/supabase/supabase) · [Pandas](https://github.com/pandas-dev/pandas) · [Prettier](https://github.com/prettier/prettier) · [Lodash](https://github.com/lodash/lodash) · [Redux](https://github.com/reduxjs/redux) · [Immer](https://github.com/immerjs/immer) · [TypeScript](https://github.com/microsoft/TypeScript) · [Rails](https://github.com/rails/rails) · [ESLint](https://github.com/eslint/eslint)
- **Agent 框架**：[Hermes Agent](https://hermes-agent.nousresearch.com) · [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) · [Cursor](https://docs.cursor.com/context/rules-for-ai) · [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) · [Cline](https://github.com/cline/cline) · [Windsurf](https://codeium.com/windsurf) · [Aider](https://aider.chat) · [Codex CLI](https://github.com/openai/codex)
- **工具**：[shields.io](https://shields.io)（徽章生成器）· [Star History](https://star-history.com)
