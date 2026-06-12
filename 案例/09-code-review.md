# Code Review — 经典案例

---


> 格式：**Markdown**（GitHub PR Review 评论）

## 精细版（详尽审查指南）

### 案例 1：google/eng-practices (20.5k⭐)

**仓库：** https://github.com/google/eng-practices
**完整指南：** https://google.github.io/eng-practices/review/

Google 官方代码审查指南，三篇核心文档：

#### The Standard of Code Review

**黄金法则：** 如果 CL 明显提升了系统的整体代码健康程度，就应批准，即使它不完美。

**关键原则：**
- 没有完美的代码——只有更好的代码
- 追求持续改进，而非完美
- 不要因小的格式问题拖延 CL 数天
- 用 `Nit:` 前缀标记可选建议
- 除非紧急情况，不应签入降低整体代码健康度的 CL

**指导顺序：**
1. **事实优于观点：** 技术事实和数据压倒个人偏好
2. **风格是绝对的：** 风格指南是最高权威
3. **软件设计有原则：** 基于底层原则，非口味
4. **一致性：** 无其他规则时，保持与当前代码库一致

#### What to Look For in a Code Review

1. **Design** — 交互合理吗？变更属于代码库吗？
2. **Functionality** — CL 做了开发者预期的吗？检查边缘情况、并发问题
3. **Complexity** — 能否被代码阅读者快速理解？
4. **Tests** — 正确、有用、合理的测试覆盖率？
5. **Naming** — 清晰的名称是否解释了代码的意图？
6. **Comments** — 解释"为什么"而非"是什么"
7. **Style** — 与风格指南一致
8. **Documentation** — 是否更新了相关文档？

#### 评论规范
- 保持礼貌和专业，解释推理过程
- 平衡指出问题和给予赞扬
- `Nit:` 前缀标记小问题

---

### 案例 2：rails/rails (56k⭐)

**仓库：** https://github.com/rails/rails
**贡献指南：** https://github.com/rails/rails/blob/main/CONTRIBUTING.md

Rails 的代码审查流程：

- 所有变更必须经审查后才能合并
- GitHub PR inline review 模式
- 检查：设计 → 功能 → 测试 → 文档
- CI 必须全绿
- `[ci skip]` 用于纯文档变更
- 至少一位 core team 成员批准

---

### 案例 3：swiftlang/swift (67.5k⭐)

**仓库：** https://github.com/swiftlang/swift
**贡献指南：** https://swift.org/contributing/

Swift 项目的代码审查理念：

**增量开发哲学：** 小的、增量的变更 > 大型变更。大变更难以审查、绕过 CI、制造合并冲突。

**Commit 消息规范：**
```
[tag] Description

Body with rationale
```
- 单行标题 + 空行 + 正文
- `[tag]` 标记区域（如 `[stdlib]`, `[SILGen]`）
- 传达动机而非机制

**审查要求：**
- 所有重要变更必须经审查后才能合并
- 小型变更可在提交后审查
- **需明确批准**——不要假设沉默即同意
- Review 他人的变更可建立善意

---

## 普通版（审查模板/指南）

### 案例 4：knonm/code-review-checklist (0.5k⭐)

**仓库：** https://github.com/knonm/code-review-checklist

14 项代码审查检查清单（每条带 bad/good 示例）：

| # | 检查项 | Bad 示例 | Good 示例 |
|---|--------|----------|-----------|
| 1 | Magic numbers | `for (i=0; i<26; i++)` | `int alphabetLength = 26;` |
| 2 | Defensive code | 不检查 null | 验证输入 |
| 3 | 过度防御 | `catch (Exception e)` | `catch (NumberFormatException e)` |
| 4 | 命名 | `mSize`, `z` | `numberOfMonths` |
| 5 | 返回类型 | `HashMap<...>` | `Map<Long, List<String>>` |
| 6 | 访问权限 | 公开方法 | 最小可见性 |
| 7 | 无用代码 | 注释掉的代码 | 清理死代码 |
| 8 | 格式 | 不一致缩进 | 一致格式化 |
| 9 | 测试覆盖 | 新代码无测试 | 有测试 |
| 10 | 圈复杂度 | 巨大函数 | 小函数 |
| 11 | DRY | 重复代码 | 复用 |
| 12 | 算法复杂度 | O(n²) | O(n log n) |
| 13 | 架构 | 违反分层 | 遵循架构 |
| 14 | SOLID | 违反单一职责 | 原则合规 |

### 案例 5：awesome-skills/code-review-skill (0.8k⭐)

**仓库：** https://github.com/awesome-skills/code-review-skill

四阶段审查框架：

```
Phase 1 — Context Gathering
    理解 PR 范围、关联 issue 和意图
Phase 2 — High-Level Review
    架构 · 性能影响 · 测试策略
Phase 3 — Line-by-Line Analysis
    逻辑 · 安全 · 可维护性 · 边界情况
Phase 4 — Summary & Decision
    结构化反馈 · 批准状态 · 行动项
```

**严重级别标签：** `blocking` · `important` · `nit` · `suggestion` · `learning` · `praise`

### 案例 6：mntnr/awesome-contributing (0.3k⭐)

**仓库：** https://github.com/mntnr/awesome-contributing

精选优秀 CONTRIBUTING.md 的策展列表，提供审查文化参考。

---

> 收集日期：2026-06-12
