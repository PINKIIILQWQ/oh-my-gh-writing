# 收集计划（简化版）

## 结构

8 大类 × 场景，每场景 2 级（精细 + 中等，中等也必须含必要部分）。
参考仓库跨场景共用，22 仓库每家 ≤ 3 次。

非必要内容（README 徽章、项目文档里的 badge、emoji、折叠块等标注工具）：
→ SKILL.md 中标记为「可选」，使用者选择复杂度后按需嵌入。

---

## 二、Issue 类 — 6 种场景

每种场景等级细分。精细=完整表单+详细步骤；中等=必要结构完整但更简洁。

| # | 场景 | 精细参考（~2 个） | 中等参考（~1-2 个） | 必要部分 |
|---|------|------------------|-------------------|---------|
| 1 | **Bug Report** | `vscode`（12字段YAML表单）、`home-assistant`（自动诊断采集） | `react`（CodeSandbox必填）、`nextjs`（复现链接核心） | 描述/重现/预期vs实际/环境 |
| 2 | **Feature Request** | `angular`（多use case+API草案） | `typescript`（含workaround）、`eslint`（代码示例） | 场景/期望/替代方案/动机 |
| 3 | **Enhancement** | `pandas`（当前vs期望对比） | `prettier`（增量改进提案） | 当前限制/改进效果/兼容性 |
| 4 | **Regression** | `nodejs`（版本范围+benchmark） | `electron`（回归模板） | 上一可用/第一坏/bisect |
| 5 | **Performance** | `golang/go`（benchmark+环境） | `vscode`（CPU/内存Profile） | 场景/基准数据/Profile |
| 6 | **Discussion** | `rails`（动机+方案选项） | — | 背景/方案对比/征求意见 |

> Security Vulnerability 合并进 Bug Report 作为特殊子类型标注说明。
> Documentation Issue 合并进 Enhancement 作为改进场景。

---

## 三、PR 类 — 6 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **Feature PR** | `kubernetes`（完整checklist+cherry-pick+breaking）、`vscode`（12项验证） | `react`（三段式）、`django`（Ticket引用） | 动机/方案/测试/breaking |
| 2 | **Bug Fix PR** | `golang/go`（测试必含、Fixes#必填） | `eslint`（rule测试引用） | 根因/方案/测试/Fixes# |
| 3 | **Refactor PR** | `react`（before/after性能对比） | `pandas`（API兼容性） | 目标/不变量/行为不变验证 |
| 4 | **Docs PR** | `home-assistant`（截图要求） | `nextjs`（预览链接+片段确认） | 原文vs改后/截图/无代码声明 |
| 5 | **Dependency Update** | `django`（安全评级） | `electron`（Changelog引用） | 范围/兼容性/breaking |
| 6 | **Backport** | `nodejs`（LTS版本） | `angular`（cherry-pick） | 源commit/目标分支/冲突 |

> Hotfix 合并进 Bug Fix 特殊子类型。Draft/WIP 作为 PR 模板页脚备注。

---

## 四、Review 类 — 4 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **Code Review Comment** | `torvalds/linux`（LKML经典）、`kubernetes`（PR评论体系） | `golang/go`（Gerrit注释） | 位置/影响/建议/severity |
| 2 | **Review Summary** | `django`（Committer review） | `typescript`（核心团队review） | 亮点/问题/阻塞/建议 |
| 3 | **Design Review** | `rust-lang/rfcs`（RFC review） | `kubernetes/enhancements`（KEP review） | 关注点/风险/备选/决策 |
| 4 | **Security Review** | `vscode`（安全checklist） | `home-assistant`（安全流程） | 威胁模型/攻击面/缓解 |

> Performance Review 合并进 Code Review Comment 作为注释类型之一。

---

## 五、Commit 类 — 4 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **Standard Commit** | `angular`（Conventional Commits）、`torvalds/linux`（detail极致） | `golang/go`（pkg:描述+body） | type(scope):/正文/footer |
| 2 | **Merge Commit** | `kubernetes`（自动squash模板） | `react`（手动squash描述） | PR引用/变更概览/冲突说明 |
| 3 | **Fixup Commit** | `torvalds/linux`（fixup风格） | — | 修正范围/原commit引用 |
| 4 | **Revert Commit** | `golang/go`（Revert+"pkg:"） | `torvalds/linux`（revert含原因） | Revert"原始"/原因/影响 |

---

## 六、项目文档类 — 6 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **README.md** | `vscode`（截图+下载）、`react`（文档家族标准） | `nextjs`（功能表格+快速链接） | 简介/快速开始/示例/徽标 ← 可选 |
| 2 | **CONTRIBUTING.md** | `home-assistant`（最详尽） | `nodejs`（协作流程+代码风格） | 工作流/编码规范/PR流程/开发环境 |
| 3 | **CHANGELOG.md** | `electron`（Breaking/Features/Fixes） | `npm/cli`（混合风格） | 版本/日期/按类型分类 |
| 4 | **SECURITY.md** | `kubernetes`（含PGP密钥） | `electron`（披露策略） | 渠道/私钥/响应时间 |
| 5 | **CODEOWNERS** | `vscode`（分模块细致） | `kubernetes`（SIG级别） | @team / * @default |
| 6 | **ARCHITECTURE.md** | `angular`（架构guide） | `home-assistant`（架构文档） | 模块/通信/数据流 |

> ROADMAP/SUPPORT/FAQ 合并为 ARCHITECTURE 下的子变体做标准结构说明。
> 徽章使用标注为「可选」——使用者决定用哪种复杂度。

---

## 七、发布变更类 — 3 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **Release Notes** | `kubernetes`（最完整） | `npm/cli`（blog风格） | 版本/日期/新特性/breaking/升级 |
| 2 | **Migration Guide** | `angular`（升级文档） | `electron`（breaking迁移） | 旧vs新/步骤/回滚 |
| 3 | **Deprecation Notice** | `pandas`（FutureWarning体系） | `django`（timeline文档） | 废弃API/替代/移除时间线 |

> Changelog Fragment 合并进 Release Notes 的自动化子流程说明。

---

## 八、设计与决策类 — 2 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **RFC** | `reactjs/rfcs`（最严格） | `rust-lang/rfcs`（最完整） | 动机/设计/兼容性/备选 |
| 2 | **ADR** | `home-assistant`（ADR目录最规范） | — | 上下文/方案对比/决策/后果 |

> Proposal 合并进 RFC 作为精简子类型。

---

## 九、模板类 — 2 种场景

| # | 场景 | 精细参考 | 中等参考 | 必要部分 |
|---|------|---------|---------|---------|
| 1 | **Issue Form YAML** | `vscode`（多YAML表单） | `rails`（复选框+验证） | type/fields/validations/labels |
| 2 | **PR Template** | `kubernetes`（最完整） | `react`（适中checklist） | 框架/checklist/测试要求 |

---

## 仓库配额表（22 仓库 × 3 上限）

| 仓库 | 使用次数 | 场景 |
|------|---------|------|
| microsoft/vscode | 3 | Bug Report · Feature PR · Security Review |
| kubernetes/kubernetes | 2 | Feature PR · Code Review Comment |
| home-assistant/core | 3 | Bug Report · ADR · ARCHITECTURE |
| facebook/react | 3 | Bug Report · Feature PR · Refactor PR |
| golang/go | 3 | Performance · Bug Fix PR · Revert Commit |
| electron/electron | 3 | Regression · Docs PR (Dependency) · CHANGELOG |
| tailwindlabs/tailwindcss | 1 | Bug Report（精简） |
| vercel/nextjs | 3 | Bug Report · Docs PR · README.md |
| microsoft/typescript | 2 | Feature Request · Review Summary |
| angular/angular | 3 | Feature Request · Backport PR · Migration Guide |
| django/django | 3 | Feature PR · Dependency · Deprecation Notice |
| nodejs/node | 3 | Regression · Backport PR · CONTRIBUTING |
| torvalds/linux | 3 | Code Review Comment · Standard Commit · Fixup Commit |
| eslint/eslint | 1 | Bug Fix PR |
| pandas-dev/pandas | 2 | Enhancement · Deprecation Notice |
| rails/rails | 1 | Discussion |
| prettier/prettier | 1 | Enhancement |
| reactjs/rfcs | 1 | RFC |
| rust-lang/rfcs | 1 | Design Review |
| kubernetes/enhancements | 1 | Design Review |
| npm/cli | 2 | Feature Request · Release Notes |
| MicrosoftDocs/azure-docs | 1 | Bug Report（文档） |

**合计**：22 仓库 × ≤3，48 次引用分布在 32 个场景。✅

---

## 非必要内容说明（使用者决定）

在 SKILL.md 中标注为「可选」，附预设选项：

| 文档类型 | 可选内容 | 预设选项 |
|---------|---------|---------|
| README.md | 徽章栏（构建状态/覆盖/版本/许可） | 「全部」/「仅 top 3」/「无」 |
| README.md | GIF 演示 | 「有」/「无」（仅截图） |
| README.md | 目录 TOC | 「有」/「无」 |
| README.md | 贡献者表格 | 「有」/「无」 |
| CONTRIBUTING.md | 开发环境搭建步骤 | 「详细 docker+脚本」/「仅文字」/「无」 |
| PR 描述 | 截图/录屏 | 「必填」/「建议」/「可选」 |
| Bug Report | 环境自动采集脚本 | 「有」/「无」（手动填写） |
| CHANGELOG.md | 版本比较链接 | 「有」/「无」 |
| 任意 | emoji/alert/kbd 等格式化武器 | 「完全启用」/「仅基础 markdown」 |
