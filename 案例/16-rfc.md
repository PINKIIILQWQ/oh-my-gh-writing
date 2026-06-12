# RFC — 经典案例

---

## 精细版（完整 RFC 模板）

### 案例 1：python/peps (4k⭐)

PEP（Python Enhancement Proposal）是最成熟的 RFC 体系之一。

**元数据头：**
```
PEP: <number>
Title: <title>
Author: <name <email>>
Status: Draft | Active | Accepted | Rejected | Final | Superseded
Type: Standards Track | Informational | Process
Created: <YYYY-MM-DD>
Python-Version: <version>
```

**标准模板结构（10+ 必选章节）：**
```
Abstract           — 简短摘要
Motivation         — 为什么要做
Rationale          — 设计决策解释
Specification      — 详细规范
Backwards Compatibility — 向后兼容
Security Implications    — 安全影响
How to Teach This       — 教学建议
Reference Implementation — 参考实现
Rejected Ideas           — 被拒绝方案
Open Issues             — 待解决问题
```

---

### 案例 2：tc39/proposals (19k⭐)

TC39 提案流程——5-Stage 渐进式设计：

| Stage | 名称 | 完成标准 |
|-------|------|----------|
| 0 | Strawperson | 任何想法 |
| 1 | Proposal | 问题 + API 示例 + 挑战分析 |
| 2 | Draft | 正式规范文本 |
| 3 | Candidate | 实现 + 规范反馈 |
| 4 | Finished | 2 个实现 + Test262 + 审阅 |

**提案模板：**
```markdown
# <proposal-name>
## Status
Champion(s): @user
Stage: 1

## Motivation
## Proposed Solution
## Examples
## API
## Comparison with existing features
## Q&A
```

---

### 案例 3：kubernetes/enhancements (3k⭐)

KEP（Kubernetes Enhancement Proposal）是最工程化的 RFC 体系：

```
KEP Template:
1. Summary
2. Motivation (User Stories + Goals/Non-Goals)
3. Design Details
4. Test Plan
5. Graduation Criteria (Alpha → Beta → Stable)
6. Production Readiness Review
```

**特点：** 5k-10k 词的书级文档；Provisional → Implementable → Implemented → Rejected 状态流转。

---

## 普通版（精简 RFC）

### 案例 4：graphql/graphql-spec (14k⭐)

GraphQL 规范提案模板：

```markdown
## Problem Statement
## Proposed Change
## Impact
## Alternatives
```

### 案例 5：opencontainers/runtime-spec (3k⭐)

OCI 运行时规范提案：

```markdown
## Overview
## Use Cases
## Specification Changes
## Backwards Compatibility
## Security Considerations
```

### 案例 6：json-api/json-api (7k⭐)

JSON:API 扩展提案：

```markdown
## Description
## Request / Response Changes
## Example
## Backwards Compatibility
```

---

> 收集日期：2026-06-12
