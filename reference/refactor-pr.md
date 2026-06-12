# Refactor PR — 完整写法

## 适用场景
重构代码，不新增功能，不修 bug，只改进内部结构。

## 完整写法（facebook/react, pandas-dev/pandas）

### 结构
1. **重构目标**：为什么要重构（可维护性/性能/安全性）
2. **不变量说明**：重构后行为不变的部分
3. **before-after 对比**：重构前后代码对比
4. **测试覆盖**：保证行为不变的测试（回归保护）；未知时列出待运行验证

### 参考仓库写法

**facebook/react**
- 重构 PR 含 before/after 性能对比
- 内部架构变更说明

**pandas-dev/pandas**
- 重构含 API 兼容性说明
- 测试覆盖确保行为不变

## Refactor PR — 简洁写法

### 结构
目标 → 变更 → 测试 → 备注

## 必含元素 Checklist
- [ ] 重构动机
- [ ] before-after 对比
- [ ] 测试覆盖或待运行验证项
- [ ] 行为不变声明
- [ ] 不虚构文件数量、测试数量、测试通过状态或导入路径

## 参考链接

| 仓库 | 链接 |
|------|------|
| react 重构 PRs | https://github.com/facebook/react/pulls?q=label%3Arefactor |
| pandas 重构 PRs | https://github.com/pandas-dev/pandas/pulls?q=label%3Arefactor |
