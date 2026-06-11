# Enhancement — 完整版

## 适用场景
对已有功能做增量改进，不是新增能力。

> 与 Feature Request 区别：Enhancement 是改进已有功能的行为/性能/API，Feature Request 是增加尚未存在的能力。

## 完整版（pandas-dev/pandas, prettier/prettier）

### 结构
1. **当前限制**：现有功能的不足
2. **改进效果**：改进后应该怎么样
3. **兼容性**：对现有 API/行为的破坏程度
4. **代码示例**：before → after 对比

### 参考仓库写法

**pandas-dev/pandas**
- Enhancement 模板：当前行为 vs 期望行为 + 兼容性
- 含 FutureWarning 过渡方案

**prettier/prettier**
- 格式规则改进提案
- 代码 before/after 示例
- 含 lint 变化说明

## Enhancement — 普通版

### 结构
当前限制 → 改进效果 → 示例

## 必含元素 Checklist
- [ ] 当前行为说明
- [ ] 改进后的行为
- [ ] 兼容性分析

## 参考链接

| 仓库 | 链接 |
|------|------|
| pandas Enhancement 搜索 | https://github.com/pandas-dev/pandas/issues?q=label%3AEnhancement |
| prettier Enhancement | https://github.com/prettier/prettier/issues?q=label%3Aenhancement |
