# RFC — 完整写法

## 适用场景
提出重大功能或设计变更，需要社区讨论和决策。

## 完整写法（reactjs/rfcs, rust-lang/rfcs, kubernetes/enhancements）

### 结构
1. **摘要**（1-2 句提案核心）
2. **动机**：什么问题、为什么需要解决
3. **设计**：详细方案（含 API 签名 / 数据流 / 架构图）
4. **兼容性**：对现有系统的向后兼容分析
5. **备选方案**：考虑过但不选的方案及理由
6. **开放问题**：尚未决定的点、需要讨论的问题
7. **实施路径**：分阶段实施的计划

### 参考仓库写法

**reactjs/rfcs**
- 最严格的 RFC 模板
- 必含：Prior Art + Unresolved Questions + Implementation Timeline
- 讨论流程：RFC PR → Review → 决策 → Merge/Reject

**rust-lang/rfcs**
- 最全面的 RFC 体系，从语言设计到库变更
- 含：Summary → Motivation → Guide-level Explanation → Reference-level Explanation → Drawbacks → Alternatives → Unresolved Questions

**kubernetes/enhancements（KEP）**
- 书级文档：5000-10000 词的 KEP
- 含：生产风险评估 + 测试计划 + 毕业标准
- 迭代审查制（Provisional → Implementable → Implemented）

## RFC — 简洁写法（prometheus, rust-lang/rust, nixpkgs）

### 结构
问题 → 方案 → 讨论

### 参考仓库写法

**prometheus/prometheus**
- 设计文档风格：问题 → 方案 → 讨论
- 含兼容性分析

**rust-lang/rust**
- 轻量 RFC（内部变更）
- 聚焦实现细节 + 测试

**nixos/nixpkgs**
- 社区提案格式：动机 → 设计 → 替代方案
- 含 breaking 影响

## 必含元素 Checklist
- [ ] 动机说明
- [ ] 设计方案
- [ ] 兼容性分析
- [ ] 备选方案

## 参考链接

| 仓库 | 链接 |
|------|------|
| reactjs/rfcs | https://github.com/reactjs/rfcs |
| rust-lang/rfcs | https://github.com/rust-lang/rfcs |
| kubernetes/enhancements (KEP) | https://github.com/kubernetes/enhancements |
| prometheus 提案 | https://github.com/prometheus/prometheus/issues?q=label%3Aproposal |
| rust RFC 追踪 | https://github.com/rust-lang/rust/issues?q=label%3AI-rfc |
| nixpkgs RFC | https://github.com/NixOS/nixpkgs/issues |
