# Code Review — 精细标准

## 适用场景
对 Pull Request 或提交进行代码审查评论。

## 精细标准（torvalds/linux, golang/go, rust-lang/rust）

### 结构
1. **位置**（文件 + 行号）
2. **问题**（当前代码的问题）
3. **根因**（为什么这是错的）
4. **建议**（如何修改）
5. **Severity**：blocking / major / minor / nit

### 参考仓库写法

**torvalds/linux（LKML）**
- 经典校审文化：逐行 inline 评论 + 总结
- 强调"理由 > 命令"——解释为什么而不是告诉怎么改
- email-based review，每条评论带完整上下文

**golang/go（Gerrit）**
- "问题 + 原因 + 建议"三段式
- 每评论独立板块
- 代码引用精确到文件名:行号

**rust-lang/rust**
- RFC-style review：设计决策 + 代码质量
- 注重安全性和正确性

## Code Review — 中等标准（rails, django, kubernetes）

### 结构
1. **位置**（直接标注行号）
2. **问题 + 建议**（合并列出）

### 参考仓库写法

**rails/rails**
- GitHub PR inline review
- 评论焦点：正确性 + 性能 + 风格

**django/django**
- Committer review 风格：直接提建议代码
- 强调 ticket 关联

**kubernetes/kubernetes**
- SIG review 流程：规模大但每 PR 至少 2 个 reviewer
- LGTM 标签体系

## 必含元素 Checklist
- [ ] 标注位置（文件/行号）
- [ ] 问题说明
- [ ] 建议修复方案
- [ ] Severity 标注
