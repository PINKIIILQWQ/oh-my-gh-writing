# Code Review — 写作标准

## 适用场景
对 Pull Request 或提交进行代码审查评论。

## 输入边界

必须先读取 diff、PR 文件、提交内容或用户贴出的代码后再给出文件/行号级结论。只有 PR URL 但无法访问内容时，不要编造 `src/foo.ts:42` 之类的位置；改为说明“需要 diff 才能逐行审查”，并提供基于已知变更主题的风险清单。

## 标准写法（torvalds/linux, golang/go, rust-lang/rust）

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


## 必含元素 Checklist
- [ ] 标注位置（文件/行号；必须来自真实 diff 或代码）
- [ ] 问题说明
- [ ] 建议修复方案
- [ ] Severity 标注
- [ ] 无法读取代码时只输出审查计划或主题风险，不输出虚构发现

## 参考链接

| 仓库 | 链接 |
|------|------|
| Linux LKML 归档 | https://lore.kernel.org/lkml/ |
| golang Gerrit Review | https://go.dev/doc/contribute#review |
| rust review 指南 | https://std-dev-guide.rust-lang.org/code-review/ |
| rails PR reviews | https://github.com/rails/rails/pulls |
| django PR reviews | https://github.com/django/django/pulls |
| kubernetes review 流程 | https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md |
