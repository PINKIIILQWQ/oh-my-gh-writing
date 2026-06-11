# GitHub Writing Standards — SKILL.md 目录

> 渐进式：核心内容在本文件（~15KB），详细规格放在 `reference/` 子文件。
> 本文件是 目录 + 一级定义。每个条目标注参考仓库（最多 3 个，仓库不跨场景重复）。

---

## 一、格式化武器库（基础）

> 所有文档类型通用。作为附录放在 reference/ 中，需要时查。

| 工具 | 示例 | 说明 |
|------|------|------|
| Alert | `> [!WARNING] 文本` | 彩色提示框 |
| Kbd | `<kbd>⌘S</kbd>` | 按键样式 |
| Collapse | `<details><summary>标题</summary>内容</details>` | 可折叠块 |
| Task | `- [x] 已完成` | 清单 |
| Badge | `![](https://img.shields.io/badge/...)` | 徽章 |
| Mermaid | `` ```mermaid `` | 流程图 |
| Math | `$E=mc^2$` | 公式 |
| Table | `\| 列1 \| 列2 \|` | 表格 |
| Footnote | `正文[^1]` / `[^1]: 注释` | 脚注 |
| Emoji | `:rocket:` | 图标 |
| HTML | `<sup>®</sup>` | 自定义排版 |
| Frontmatter | `---\ntype: bug-report\n---` | 元数据 |
| Template Var | `{{ env }}` / `${{ github.ref }}` | 动态值占位 |
| Custom Alert | `> [!SKILL] 技能说明` | 自定义提醒框 |

---

## 二、Issue 类 — 7 种场景

### 场景 1：Bug Report（用户报 bug）

**必要部分**：描述 / 重现步骤 / 预期 vs 实际 / 环境信息

- **详细版** — 表单 12+ 字段，分类细致，含 log 自动采集
  - `microsoft/vscode` — `.github/ISSUE_TEMPLATE/bug_report.yml`（最规范的 YAML 表单）
  - `home-assistant/core` — 自动采集诊断信息脚本，多平台调试模板
- **适中版** — 结构完整，强调 CodeSandbox 重现
  - `facebook/react` — bug report 模板 + CodeSandbox 必填
  - `electron/electron` — 多平台环境描述表单
- **精简版** — 必要部分齐全但极简（描述+步骤+环境）
  - `vercel/next.js` — 核心是复现链接，3 段话
  - `tailwindlabs/tailwindcss` — 字段少但每个都必须

### 场景 2：Feature Request（功能请求）

**必要部分**：使用场景 / 期望行为 / 替代方案

- **详细版** — 多个 use case，对比表格，API 草案
  - `angular/angular` — feature request 模板含使用场景 + 设计思路
  - `npm/cli` — 详细的 RFE 模板，含实现思路
- **适中版** — 一个主要场景 + 行为描述
  - `eslint/eslint` — rule 请求模板，含代码示例
  - `microsoft/typescript` — Suggestion 模板，含现有 workaround

### 场景 3：Enhancement（改进已有功能）

**必要部分**：当前限制 / 改进效果 / 兼容性

- `pandas-dev/pandas` — Enhancement 模板含当前行为+期望行为
- `prettier/prettier` — 格式化规则改进模板

### 场景 4：Regression Report（回归 bug）

**必要部分**：上一个可用版本 / 第一个坏版本 / bisect 结果

- `nodejs/node` — regression 模板含版本范围 + 基准测试
- `electron/electron` — 版本升级回归模板

### 场景 5：Performance Issue（性能问题）

**必要部分**：场景描述 / 基准数据 / Profile / 环境

- `golang/go` — 性能 issue 模板含 benchmark 数据
- `microsoft/vscode` — Performance issue 表单含 CPU/内存 Profile

### 场景 6：Documentation Issue（文档问题）

**必要部分**：问题原文位置 / 建议修正 / 截图

- `MicrosoftDocs/azure-docs` — 文档 bug 模板含原文链接+建议
- `home-assistant/core` — Docs issue 模板含平台+版本

### 场景 7：Discussion / RFC（讨论）

**必要部分**：背景 / 方案对比 / 征求意见

- `reactjs/rfcs` — 纯 RFC 仓库，格式最严格
- `rails/rails` — Discussion 模板含动机+方案选项
- `kubernetes/enhancements` — KEP (Kubernetes Enhancement Proposal) 模板

---

## 三、PR 类 — 6 种场景

### 场景 1：Feature PR（新功能）

**必要部分**：动机 / 实现方案 / 测试 / 破坏性变更

- **详细版** — 完整 checklist，SIG 标签，release note
  - `kubernetes/kubernetes` — 最完整的 PR 模板：cherry-pick/Breaking Change/release note
  - `microsoft/vscode` — PR checklist 详尽，含 12 项验证
- **适中版** — 结构完整，动机+改动+测试
  - `facebook/react` — PR 模板标准三段式
  - `django/django` — 含 Ticket 引用 + 兼容性说明
- **精简版** — 核心三要素
  - `vercel/next.js` — PR 模板极简
  - `tailwindlabs/tailwindcss` — 2-3 段解决

### 场景 2：Bug Fix PR（修 bug）

**必要部分**：根因 / 修复方案 / 测试覆盖

- `golang/go` — 修复 PR 必须含测试，Fixes # 引用必填
- `electron/electron` — 修复 PR 含 Checklist + 手动测试项
- `eslint/eslint` — 修复 PR 模板含 rule 测试引用

### 场景 3：Refactor PR（重构）

**必要部分**：重构目标 / 不变量说明 / 行为不变验证

- `facebook/react` — 重构 PR 通常含 before/after 性能对比
- `prettier/prettier` — 重构 PR 含快照变更说明
- `pandas-dev/pandas` — 重构 PR 含 API 兼容性说明

### 场景 4：Documentation PR（纯文档变更）

**必要部分**：原文 vs 改后 / 截图预览 / 无代码改动声明

- `home-assistant/core` — 文档 PR 模板含截图要求
- `vercel/nextjs` — 文档 PR 含预览链接 + 片段确认

### 场景 5：Dependency Update PR（依赖升级）

**必要部分**：变更范围 / 兼容性 / Breaking Change

- `electron/electron` — 依赖升级 PR 含 Changelog 引用
- `kubernetes/kubernetes` — 依赖升级 PR 含 go.sum/ vendor 校验

### 场景 6：Backport PR（向后移植）

**必要部分**：源 commit / 目标分支 / 冲突说明

- `kubernetes/kubernetes` — cherry-pick 模板最完整
- `nodejs/node` — Backport PR 含 LTS 版本说明

---

## 四、Review 类 — 4 种场景

### 场景 1：Code Review Comment（单行/函数级）

**必要部分**：问题位置 / 影响分析 / 建议方案 / severity

- `torvalds/linux` — LKML 邮件存档，最经典的 review 风格
- `golang/go` — Gerrit 上的 review 注释模式
- `kubernetes/kubernetes` — GitHub PR review comment 体系

### 场景 2：Review Summary（PR 总体评价）

**必要部分**：亮点 / 问题 / 阻塞项 / 建议

- `kubernetes/kubernetes` — SIG Reviewers 的 review 总结
- `django/django` — Committer review 总结模板
- `facebook/react` — 核心团队 review 模式

### 场景 3：Design Review（架构/设计审查）

**必要部分**：关注点 / 风险 / 替代方案 / 决策

- `rust-lang/rfcs` — RFC review 最正式
- `angular/angular` — 设计 review 含性能/安全/兼容性考量

### 场景 4：Security Review（安全审计）

**必要部分**：威胁模型 / 攻击面 / 缓解措施

- `microsoft/vscode` — 安全 review 检查清单
- `home-assistant/core` — Security review 流程

---

## 五、Commit 类 — 3 种场景

### 场景 1：Standard Commit（常规提交）

**必要部分**：`type(scope): 描述` / 正文 / body

- `angular/angular` — Conventional Commits 发源地，git-log 最规范
- `golang/go` — Go 的 commit 风格：`pkg: 描述` + 详细 body
- `torvalds/linux` — 经典描述式 commit style（不严格 type 但 detail 极致）

### 场景 2：Merge / Squash Commit（合并提交）

**必要部分**：PR 标题引用 / 变更概要 / 冲突说明

- `kubernetes/kubernetes` — 自动生成的 squash commit 消息模板
- `facebook/react` — 手动 squash 的合并描述风格

### 场景 3：Fixup / Revert（修正或回退）

**必要部分**：回退原因 / 影响 / 原始 commit 引用

- `torvalds/linux` — revert commit 经典：说明了回退原因和分析
- `golang/go` — revert commit 风格：`Revert "pkg: "` + 原因

---

## 六、项目文档类 — 6 种场景

### 场景 1：CONTRIBUTING.md（贡献指南）

**必要部分**：工作流 / 编码规范 / PR 流程 / 开发环境

- `home-assistant/core` — 最详尽的 CONTRIBUTING（含开发环境搭建步骤）
- `nodejs/node` — 贡献指南含协作流程+代码风格
- `microsoft/vscode` — 贡献指南含扩展开发说明

### 场景 2：CHANGELOG.md（变更日志）

**必要部分**：按版本 / 按类型（Added/Changed/Fixed/Removed） / 版本日期

- `keepachangelog/keepachangelog` — 官方规范
- `electron/electron` — 最完整的 changelog，每个版本含 Breaking/Features/Fixes
- `npm/cli` — Changelog 含 Release Notes 混合风格

### 场景 3：README.md（项目主页）

**必要部分**：项目简介 / 快速开始 / 一句话示例 / 徽标

- `microsoft/vscode` — README 含截图+功能亮点+下载按钮
- `facebook/react` — README 家族最标准：简介+文档链接+快速开始+Example
- `vercel/nextjs` — README 含 logo+快速链接+功能表格

### 场景 4：SECURITY.md（安全披露）

**必要部分**：报告渠道 / 私钥 / 响应时间 / 赏金

- `electron/electron` — 安全性披露策略模板
- `kubernetes/kubernetes` — 安全披露含 PGP 密钥

### 场景 5：CODE_OF_CONDUCT.md（行为准则）

**必要部分**：准则 / 报告途径 / 执行范围

- 多数项目直接用 `Contributor Covenant` 标准模板

### 场景 6：CODEOWNERS（代码负责人）

**必要部分**：`@team` / `* @default` 模式

- `microsoft/vscode` — CODEOWNERS 文件最细致（分模块分目录）
- `kubernetes/kubernetes` — SIG 级别 CODEOWNERS 分配

---

## 七、发布变更类 — 4 种场景

### 场景 1：Release Notes（发布公告）

**必要部分**：版本号 / 日期 / 新特性 / Breaking Change / 升级指南

- `kubernetes/kubernetes` — CHANGELOG + Release Notes 最完整
- `angular/angular` — 发版公告含升级链接+破坏性变更对照表
- `npm/cli` — 详细的 Release blog 风格

### 场景 2：Migration Guide（迁移指南）

**必要部分**：旧 API vs 新 API 对照 / 迁移步骤 / 回滚方案

- `angular/angular` — `guide/upgrade` 文档体系
- `electron/electron` — Breaking Change 迁移指南

### 场景 3：Deprecation Notice（废弃声明）

**必要部分**：废弃 API / 替代方案 / 移除时间线

- `pandas-dev/pandas` — FutureWarning 体系最佳
- `django/django` — deprecation timeline 文档

### 场景 4：Changelog Fragment（towncrier 式）

**必要部分**：单功能条目 / 类型分类 / 自动合并

- `pip(pypa/pip)` — towncrier fragment 例子
- `twisted/twisted` — towncrier 规范的创始者之一

---

## 八、设计与决策类 — 3 种场景

### 场景 1：ADR（Architecture Decision Record）

**必要部分**：上下文 / 方案对比 / 决策 / 后果

- `home-assistant/core` — ADR 目录最规范
- `angular/angular` — 设计文档 ADR 体系

### 场景 2：RFC（大功能设计文档）

**必要部分**：动机 / 详细设计 / 兼容性 / 替代方案

- `reactjs/rfcs` — RFC 模板最严格：摘要+动机+设计+缺点+备选
- `rust-lang/rfcs` — RFC 体系最完整
- `kubernetes/enhancements` — KEP 模板含所有阶段

### 场景 3：Proposal（改进提案）

**必要部分**：问题陈述 / 解决方案 / 收益评估

- `facebook/react` — 讨论中的 Feature proposal 模式
- `nodejs/node` — Proposal 模板含挑战+替代方案

---

## 九、模板类 — 3 种场景

### 场景 1：Issue Form YAML（结构化表单）

**必要部分**：type / fields / validations / labels

- `microsoft/vscode` — `.github/ISSUE_TEMPLATE/` 多个 YAML 表单
- `rails/rails` — Issue forms 含复选框+验证规则
- `tailwindlabs/tailwindcss` — 最精简的 YAML 表单

### 场景 2：PR Template（PR 描述模板）

**必要部分**: PR 描述框架 / checklist / 测试要求

- `kubernetes/kubernetes` — `.github/PULL_REQUEST_TEMPLATE.md` 最完整
- `facebook/react` — PR template 适中型
- `prettier/prettier` — PR template 精简型

### 场景 3：Discussion Template（讨论分类模板）

**必要部分**: 分类标签 / 提问引导

- `home-assistant/core` — Discussion 分类 + 模板
- `nodejs/node` — 讨论模板含 agenda

---

## 附录：仓库使用统计

> 每个仓库最多在 3 个场景中出现，以下为实际分配（52 个场景，19 个仓库）

| 仓库 | 出现次数 | 场景 |
|------|---------|------|
| microsoft/vscode | 3 | Bug Report / Feature PR / CODEOWNERS |
| home-assistant/core | 3 | Bug Report / Documentation PR / CONTRIBUTING |
| kubernetes/kubernetes | 3 | Discussion/RFC / Feature PR / Backport PR |
| facebook/react | 3 | Bug Report / Refactor PR / Merge Commit |
| golang/go | 3 | Performance Issue / Bug Fix PR / Standard Commit |
| electron/electron | 3 | Bug Report / Dependency Update PR / CHANGELOG |
| vercel/nextjs | 2 | Bug Report / Documentation PR |
| tailwindlabs/tailwindcss | 2 | Bug Report / Issue Form YAML |
| angular/angular | 3 | Feature Request / Standard Commit / Migration Guide |
| django/django | 2 | Feature PR / Deprecation Notice |
| nodejs/node | 2 | Regression Report / Proposal |
| torvalds/linux | 2 | Code Review Comment / Fixup/Revert |
| eslint/eslint | 2 | Feature Request / Bug Fix PR |
| pandas-dev/pandas | 2 | Enhancement / ADR |
| kubernetes/enhancements | 1 | RFC |
| reactjs/rfcs | 1 | RFC |
| rails/rails | 1 | Issue Form YAML |
| prettier/prettier | 1 | Enhancement |
| mcr.microsoft/devcontainers | — | (未使用) |

---

## SKILL.md 文件结构（最终产物）

```
oh-my-gh-writing/
├── SKILL.md                    ← 核心文件（~15KB，定义所有标准）
├── reference/
│   ├── 01-issue-examples.md    ← 各类 Issue 完整示例
│   ├── 02-pr-examples.md       ← 各类 PR 完整示例
│   ├── 03-review-examples.md   ← Review Comment 示例
│   ├── 04-commit-examples.md   ← Commit Message 示例
│   ├── 05-rewriting-cheatsheet.md ← 格式化武器库完整表
│   ├── 06-agent-prompts.md     ← 用于 agent 的 prompt 模板
│   └── 07-repo-index.md        ← 所有参考仓库的链接和关键文件路径
├── DOCS/
│   ├── collection-plan.md      ← 收集计划（本文件）
│   └── skill-outline.md        ← 本文件（目录结构）
└── .gitignore
```

> **渐进式阅读**：
> 1. 读 `SKILL.md` — 了解所有标准定义（核心）
> 2. 需要示例时查 `reference/01-*.md`
> 3. 需要格式化语法时查 `reference/05-rewriting-cheatsheet.md`
> 4. 需要 agent 直接使用时查 `reference/06-agent-prompts.md`
