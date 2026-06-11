# Refactor PR — 精细标准

## 适用场景
重构代码，不新增功能，不修 bug，只改进内部结构。

## 精细标准（facebook/react, pandas-dev/pandas）

### 结构
1. **重构目标**：为什么要重构（可维护性/性能/安全性）
2. **不变量说明**：重构后行为不变的部分
3. **before-after 对比**：重构前后代码对比
4. **测试覆盖**：保证行为不变的测试（回归保护）

### 参考仓库写法

**facebook/react**
- 重构 PR 含 before/after 性能对比
- 内部架构变更说明

**pandas-dev/pandas**
- 重构含 API 兼容性说明
- 测试覆盖确保行为不变

## Refactor PR — 中等标准

### 结构
目标 → 变更 → 测试 → 备注

## 必含元素 Checklist
- [ ] 重构动机
- [ ] before-after 对比
- [ ] 测试覆盖
- [ ] 行为不变声明
