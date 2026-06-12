---
name: oh-my-gh-writing
description: "GitHub Writing Standards — Issue/PR/Review/Commit/Docs/Release/Design/Templates, 2 levels per scenario (Complete/Normal), bilingual by default, progressive disclosure."
version: 1.0.0
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Writing, Issues, Pull-Requests, Code-Review, Documentation]
    related_skills: [github-code-review, github-issues, github-pr-workflow]
---

# oh-my-gh-writing

GitHub 写作规范技能。覆盖 8 大类 18 场景，每场景分完整/普通 2 级，使用渐进式披露组织索引、场景标准和格式工具。

---

## 渐进式使用路径

1. 先用本文件判断用户请求属于哪个场景，以及默认使用普通版还是完整版
2. 再读取对应 `reference/*.md` 获取完整字段、参考写法和 checklist
3. 需要全量导航、场景目录或维护入口时，再查看 [`INDEX.md`](./INDEX.md)

不要把所有细节一次性灌给用户。默认先给可用草稿；只有用户要求“完整版”“详细说明”“正式发布”“高风险变更”时，再展开完整结构。

---

## 索引

| 类别 | 场景 | 完整参考 | 普通参考 | 参考文件 |
|------|------|---------|---------|---------|
| Issue | Bug Report | vscode, nextjs, tailwindcss | golang, electron, eslint | `reference/bug-report.md` |
| Issue | Feature Request | angular, typescript, rails | svelte, nuxt, babel | `reference/feature-request.md` |
| Issue | Enhancement | pandas, prettier | — | `reference/enhancement.md` |
| Issue | Discussion | rails, eslint | — | `reference/discussion.md` |
| PR | Feature PR | kubernetes, react, django | storybook, apollo, grafana | `reference/feature-pr.md` |
| PR | Bug Fix PR | lodash, redux, immer | neovim, terraform, helm | `reference/bug-fix-pr.md` |
| PR | Refactor PR | react, pandas | — | `reference/refactor-pr.md` |
| PR | Documentation PR | home-assistant, nextjs | — | `reference/documentation-pr.md` |
| Review | Code Review | linux, golang, rust | rails, django, kubernetes | `reference/code-review.md` |
| Commit | Standard Commit | angular, linux, nodejs | react, golang, gitea | `reference/standard-commit.md` |
| 文档 | README | vscode, nextjs, tailwindcss | deno, supabase, github/docs | `reference/readme.md` |
| 文档 | CONTRIBUTING | home-assistant, nodejs, angular | electron, django, github/docs | `reference/contributing.md` |
| 文档 | CHANGELOG | electron, npm, pandas | eslint, graphql, prisma | `reference/changelog.md` |
| 发布 | Release Notes | astro, npm, svelte | buf, bun, deno | `reference/release-notes.md` |
| 发布 | Migration Guide | fluentui, pandas, gitlab | reactjs/rfcs, react-spectrum, hugo | `reference/migration-guide.md` |
| 设计 | RFC | reactjs/rfcs, rust-lang/rfcs, kubernetes/enhancements | prometheus, rust, nixpkgs | `reference/rfc.md` |
| 模板 | Issue Form YAML | vscode, nextjs, rails | github/docs, home-assistant, terraform | `reference/issue-form-yaml.md` |
| 模板 | PR Template | kubernetes, react, moby | eslint, tailwindcss, spark | `reference/pr-template.md` |

---

## 7 条写作通用原则

所有场景共用，写在最前：

1. **可复现优先** — 任何描述必须能让他人独立重现。Bug 报告必须有复现步骤，PR 必须有测试
2. **标题即摘要** — 标题应独立概括内容。Issue/PR 标题要让读者不点开也能判断是否相关
3. **结构优先于措辞** — 先搭骨架（环境/步骤/预期/实际），再填充细节。骨架不全则信息丢失
4. **环境必记录** — 版本、平台、上下文必须显式写出。默认"最新版"不可接受
5. **链接不是引用** — 关键信息写在正文，链接作补充。不得"详见链接"代替描述
6. **一个变更一件事** — 单 Issue 报告一个 bug，单 PR 做一件事。混入无关变更应拆分
7. **礼貌但准确** — 措辞礼貌，信息精确。"你错了"→"这里的行为与文档描述不一致"

---

## 场景标准（摘要）

### Bug Report

**完整版（vscode/nextjs/tailwindcss）**
YAML 表单式：描述→重现步骤→预期行为→实际行为→环境（OS/版本/浏览器）→日志/截图→附加上下文。vscode 的 12 字段表单是标杆，每字段必填。

**普通版（golang/go/electron/eslint）**
自然语言式但结构完整：问题概述→复现→期望 vs 实际→环境。golang 的 Bug Report 模板最精炼，5 段覆盖全部必要信息。

  > 可选：环境自动采集脚本（默认开启）
  > 可选：截图粘贴区（默认建议）

### Feature Request

**完整版（angular/typescript/rails）**
动机→Use Case（多场景）→期望 API→替代方案→兼容性。angular 的 feature 模板会要求写多 use case + 伪代码 API 草案。

**普通版（svelte/nuxt/babel）**
问题→期望→备选。svelte 的 feature 请求最简洁：一句话问题 + 你希望的写法 + 现在的 workaround。

### Enhancement

**完整版（pandas, prettier）**
当前限制→改进效果（含 before/after 代码对比）→兼容性分析。pandas 的 enhancement 模板最系统——当前行为 vs 期望行为 + FutureWarning 过渡方案。

**普通版**
当前限制 → 改进效果 → 示例。省略兼容性分析，但含 before/after。

### Discussion

**完整版（rails, eslint）**
背景→动机→方案对比（表格形式各方案优缺点）→征求意见。rails 的 Discussion 模板是标杆，结构完整但保持开放式风格。

**普通版**
背景 → 问题列表 → 讨论。省略方案对比表格。

### Feature PR

**完整版（kubernetes/react/django）**
动机→设计→实现→测试→Breaking Changes→升级说明。kubernetes PR 模板含 12 项 checklist，从 CHERRY_PICK 到 SIG 标注全覆盖。

**普通版（storybook/apollo/grafana）**
动机→变更→测试→备注。storybook PR 模板三段式：What/Why/How，加上 screenshot checklist。

  > 可选：截图/录屏（默认必填，视觉变更）

### Bug Fix PR

**完整版（lodash/redux/immer）**
根因→方案→测试→Fixes #。lodash 的 fix PR 是标杆：15 行代码改动的 fix 配 30 行测试 + 根因分析 + perf 对比。

**普通版（neovim/terraform/helm）**
方案→Fixes #→测试。neovim 的 fix PR 模板突出测试引用。

### Refactor PR

**完整版（react, pandas）**
重构目标→不变量说明→before-after 代码对比→测试覆盖。react 的重构 PR 标杆：性能对比 + 内部架构变更说明。pandas 侧重 API 兼容性证明。

**普通版**
目标 → 变更 → 测试 → 备注。省略 before-after 性能对比。

### Documentation PR

**完整版（home-assistant, nextjs）**
原文位置→原文 vs 改后→截图预览（UI 类）→无代码改动声明。home-assistant 的文档 PR 强制截图验证。

**普通版**
原文 → 改后 → 截图（可选）。省略无代码改动声明。

### Code Review

**完整版（torvalds/linux/golang/rust）**
位置→影响→建议→Severity。Linux LKML 是最老牌的 review 文化，golang 的 Gerrit review 强调"问题 + 原因 + 建议"三段式。

**普通版（rails/django/kubernetes）**
问题→建议。rails 的 code review 在 PR 评论中直接标注行号 + 建议。

### Standard Commit

**完整版（angular/linux/nodejs）**
`<type>(<scope>): <subject>` → body（why）→ footer（Breaking/Refs）。angular 的 Conventional Commits 是事实标准，linux 的 commit 以 detail 极深入著称。

**普通版（react/golang/gitea）**
`pkg: message` → body。Go 风格的 `pkg: description` 最简洁。

### README

**完整版（vscode/nextjs/tailwindcss）**
标题→语义化徽章栏→简介→快速开始→示例→功能→文档链接→贡献→许可。vscode 的 README 含截图 + 下载 + 功能表格；徽章参考 github-badge-collection 的分类、链接和数量控制思路。

**普通版（deno/supabase/github/docs）**
标题→简介→快速开始→示例→链接。supabase 的 README 干净聚焦：产品 + 快速开始 + 社区。

  > 可选：徽章（默认 top 3：格式/构建+版本+许可；每个徽章都应可点击到证据页）
  > 可选：TOC（默认自动生成）
  > 可选：贡献者表（默认无）

### CONTRIBUTING

**完整版（home-assistant/nodejs/angular）**
工作流→分支策略→Commit 规范→代码风格→PR 流程→测试→本地开发环境。home-assistant 的 CONTRIBUTING 是公认最详尽。

**普通版（electron/django/github/docs）**
PR 流程→代码风格→开发环境。electron 的 contributing 聚焦核心流程。

### CHANGELOG

**完整版（electron/npm/pandas）**
按版本号归类：Breaking→Features→Fixes→Performance→Deprecation→Dependency。electron 是 Keep a Changelog 最佳实践代表。

**普通版（eslint/graphql/prisma）**
混合风格：版本号 + 日期 + 按类型分类，但合并次要变更。prisma 的 changelog 简洁但覆盖齐全。

### Release Notes

**完整版（astro/npm/svelte）**
版本→新特性→Breaking→升级指南→Full Changelog 链接。astro 的 release notes 含 GIF 演示。

**普通版（buf/bun/deno）**
版本→主要变更列表。bun 的 release 以 bullet list 为主。

### Migration Guide

**完整版（fluentui/pandas/gitlab）**
旧 API→新 API→迁移步骤（含代码 diff）→回滚方案→废弃时间线。pandas 的迁移文档最系统。

**普通版（reactjs/rfcs/react-spectrum/hugo）**
旧 vs 新对比→迁移步骤。省略回滚和时间线。

### RFC

**完整版（reactjs/rfcs/rust-lang/rfcs/kubernetes/enhancements）**
动机→设计→兼容性→备选方案→开放问题。reactjs/rfcs 的模板最严格，含 Prior Art + 实施路径。

**普通版（prometheus/rust/nixpkgs）**
问题→方案→讨论。省略兼容性分析等章节。

### Issue Form YAML

**完整版（vscode/nextjs/rails）**
`name`→`description`→`type`→`fields`（textarea/input/dropdown/checkbox）→`validations`→`labels`。vscode 定义 10+ YAML 表单涵盖各种 Issue 类型。

**普通版（github/docs/home-assistant/terraform）**
精简字段 + 必要验证。github/docs 的 form 只有 4 字段但够用。

### PR Template

**完整版（kubernetes/react/moby）**
动机→设计→测试→Checklist→发布说明。kubernetes 的 PR 模板是最完整的行业标杆。

**普通版（eslint/tailwindcss/spark）**
动机→变更→Checklist。tailwindcss 的 PR 模板聚焦核心。

---

## 格式化武器库（附录）

可在任意场景按需启用。默认仅基础 markdown，需要时调用 `reference/weapons.md`。

| 武器 | 写法 | 适用场景 |
|------|------|---------|
| Alert | `> [!NOTE]` / `> [!WARNING]` / `> [!TIP]` / `> [!IMPORTANT]` | 突出注意事项 |
| KBD | `<kbd>Ctrl+C</kbd>` | 快捷键说明 |
| Collapse | `<details><summary>展开</summary>内容</details>` | 折叠长日志 |
| Badges | `![label](https://img.shields.io/...svg)` | README 状态栏；先分类，后生成，数量受控 |
| Mermaid | ```` ```mermaid ```` | 流程图/时序图 |
| 任务列表 | `- [x] 完成` / `- [ ] 待办` | Checklist |
| 表格 | `\| col1 \| col2 \|` | 对比/参数 |
| 代码块 | ```` ```language ```` | 代码示例 |
| EMOJI | `:rocket:` / `:bug:` | 标题/摘要装饰 |

## 产品适用范围

| 维度 | 详情 |
|------|------|
| **格式** | [`SKILL.md`](https://hermes-agent.nousresearch.com/docs)（YAML frontmatter + markdown） |
| **载体** | 纯文件，无需构建步骤、无需运行时 |
| **依赖** | 无 |
| **支持的框架** | 原生 Hermes Agent；兼容 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)（CLAUDE.md）/ [Cursor](https://docs.cursor.com/context/rules-for-ai)（.cursorrules）/ [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)（copilot-instructions.md）/ [Cline](https://github.com/cline/cline)（.clinerules）/ [Windsurf](https://codeium.com/windsurf)（.windsurfrules）/ [Aider](https://aider.chat)（CONVENTIONS.md）/ [Codex CLI](https://github.com/openai/codex)（RULES.md）等 14 个平台 |
| **参考仓库** | 22 个场景参考仓库 + 6 个专项工具/资料仓库 |
| **覆盖范围** | 8 大类 18 场景 |
| **复杂度等级** | 完整版（全字段+多仓库详解+变体）/ 普通版（全部必要部分） |
| **许可** | [MIT](https://opensource.org/licenses/MIT) |

## 使用者流程

1. 告诉我要写什么（"写个 bug report" / "开个 feature PR"）
2. 我默认用普通复杂度（含全部必要部分），如需更完整可告知
3. 我会按场景问该问的可选项（README 徽章/PR 截图等）
4. 产出含：模板 + 参考仓库写法示例 + 检查清单

> **请问还有什么需要额外注意的地方吗？** — 初稿产出后向使用者确认：是否需要补充 Star History？是否需要多语言版本？是否需要特定风格的徽章？是否有需要强调的特定功能或社区链接？

详细每场景完整写法标准 → `reference/` 目录。
