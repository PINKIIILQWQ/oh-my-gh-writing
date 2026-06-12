# RFC — 经典案例

---

## 精细版（完整 RFC 模板）

### 案例 1：python/peps (PEP) — PEP 1（PEP 模板）

**来源：** https://github.com/python/peps

Python 的 PEP（Python Enhancement Proposal）是最成熟的语言设计 RFC 体系之一：

**PEP 头部元数据：**
```
PEP: <数字>
Title: <标题>
Author: <姓名 <email>>
Sponsor: <姓名 <email>>
Discussions-To: <Discourse URL>
Status: Draft | Active | Accepted | Provisional | Deferred | Rejected | Withdrawn | Final | Superseded
Type: Standards Track | Informational | Process
Content-Type: text/x-rst
Created: <YYYY-MM-DD>
Python-Version: <版本号>
Post-History: <YYYY-MM-DD>, <YYYY-MM-DD>
Replaces: <PEP 数字>
```

**标准模板结构：**
```
Abstract
  [简短摘要]

Motivation
  [为什么要做]

Rationale
  [设计决策解释]

Specification
  [详细规范]

Backwards Compatibility
  [向后兼容分析]

Security Implications
  [安全影响]

How to Teach This
  [如何教学]

Reference Implementation
  [参考实现链接]

Rejected Ideas
  [被拒绝的方案]

Open Issues
  [待解决问题]

Footnotes
  [脚注]

Copyright
  [版权声明]
```

**特点：** 最全面的 RFC 模板系统，含 10+ 必选章节 + 标准化元数据头 + 明确的 Status 流转（Draft → Accepted → Final）。

---

### 案例 2：tc39/proposals (ECMAScript)

**来源：** https://github.com/tc39/proposals

TC39 的提案流程分为 5 个 Stage：

**Stage 0 (Strawperson)：** 任何想法
**Stage 1 (Proposal)：** 问题描述 + 解决方案 + API 示例 + 潜在挑战
**Stage 2 (Draft)：** 正式规范文本
**Stage 3 (Candidate)：** 实现 + 规范反馈
**Stage 4 (Finished)：** 两个实现 + Test262 测试 + 学术审阅

**提案模板：**
```markdown
# <proposal-name>

## Status
Champion(s): @user1, @user2
Stage: 1

## Motivation
[问题描述]

## Proposed Solution
[方案 + 代码示例]

## Examples
[使用示例]

## API
[详细 API 签名]

## Comparison with existing features
[与已有方案的对比]

## Q&A
[常见问题]
```

**特点：** Stage 驱动的渐进式设计 + 必须由 champion 推动 + 每个 Stage 有明确的完成标准。

---

### 案例 3：opencontainers/runtime-spec (OCI)

**来源：** https://github.com/opencontainers/runtime-spec

OCI 规范的 RFC 风格提案：

**结构：**
```
## Overview
[问题描述和新能力概述]

## Use Cases
[具体用例]

## Specification Changes
[规范修改细节，含逐行 diff]

## Backwards Compatibility
[向后兼容分析]

## Security Considerations
[安全考虑]

## Implementation
[参考实现]
```

**特点：** 容器运行时规范的标准化提案流程，强调安全影响分析和向后兼容。

---

## 普通版（精简 RFC）

### 案例 4：graphql/graphql-spec

GraphQL 规范提案使用 GitHub Issues + RFC PR 模式：

```
## Problem Statement
[问题描述]

## Proposed Change
[变更内容]

## Impact
[对现有实现的影响]

## Alternatives
[备选方案]
```

---

### 案例 5：open-telemetry/opentelemetry-specification

OpenTelemetry 规范提案模板：

```
## Objective
[目标]

## Motivation
[动机]

## Design Details
[设计方案]

## Trade-offs and Limitations
[权衡和限制]

## Prior Art and Alternatives
[已有方案和备选]

## Migration Plan
[迁移计划]
```

---

### 案例 6：json-api/json-api

JSON:API 规范的提案模板：

```
## Description
[功能描述]

## Request / Response Changes
[请求/响应变更说明]

## Example
[完整示例]

## Backwards Compatibility
[向后兼容分析]
```

---

> 收集日期：2026-06-12
