# Bug Fix PR — 精细标准

## 适用场景
修复 Bug 的 Pull Request，重点在根因分析和测试。

## 精细标准（lodash, redux, immer）

### 结构
1. **根因**：Bug 的根本原因，含代码位置
2. **方案**：你是怎么修的
3. **测试**：新增测试（回归测试保护）
4. **Fixes #**：关联 Issue 号

### 参考仓库写法

**lodash/lodash**
- 极简 fix：15 行代码改动用 30+ 行测试覆盖
- 根因分析 + before/after 对比
- perf 影响说明

**reduxjs/redux**
- 根因 → 方案 → 测试 → Fixes #
- 含 breaking 声明

**immerjs/immer**
- fix 模板聚焦最小化变更
- 测试即文档：修改对应的测试用例说明行为变化

## Bug Fix PR — 中等标准（neovim, terraform, helm）

### 结构
1. **方案**（含 Fixes #）
2. **测试**

### 参考仓库写法

**neovim/neovim**
- 简洁：方案 + Fixes # + 测试结果
- 测试通过截图

**hashicorp/terraform**
- 核心：根因说明 + Fixes # + 测试
- provider 级别的 fix 规范

**helm/helm**
- 方案 → Fixes # → 备注
- 含升级兼容性

## 必含元素 Checklist
- [ ] Fixes # 关联
- [ ] 根因说明
- [ ] 测试覆盖
