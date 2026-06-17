# Refactor PR — 写作标准

## 适用场景
重构代码，不新增功能，不修 bug，只改进内部结构。

## 输出边界

Refactor PR 必须保持外部行为不变。只在 diff、测试或用户输入支持时声明性能、安全或架构收益。

## 标准结构

1. **重构目标**：为什么要重构（可维护性/性能/安全性）
2. **不变量说明**：重构后行为不变的部分
3. **before-after 对比**：重构前后代码对比
4. **测试覆盖**：保证行为不变的测试（回归保护）；未知时列出待运行验证

## 信息不足时

- 缺少 diff 时，不写文件数量、模块名或导入路径。
- 测试未运行时，列出待验证项。
- 行为是否不变不确定时，写 `Behavior impact: To confirm`。

## 禁止编造项

- 不编造性能收益、文件数量、测试数量、测试通过状态、导入路径或行为不变结论。
- 不把 bug fix 或 feature PR 误写成 refactor。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR template docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository |
| React PR Template | https://github.com/facebook/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Moby PR Template | https://github.com/moby/moby/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| Google Engineering Review Guide | https://google.github.io/eng-practices/review/ |
| Kubernetes Review Ownership | https://github.com/kubernetes/community/blob/main/contributors/guide/owners.md |
| Rust CONTRIBUTING | https://github.com/rust-lang/rust/blob/main/CONTRIBUTING.md |

## 必含元素 Checklist
- [ ] 重构动机
- [ ] before-after 对比
- [ ] 测试覆盖或待运行验证项
- [ ] 行为不变声明
- [ ] 不虚构文件数量、测试数量、测试通过状态或导入路径
