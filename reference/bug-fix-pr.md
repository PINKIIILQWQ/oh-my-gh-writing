# Bug Fix PR — 完整写法

## 适用场景
修复 Bug 的 Pull Request，重点在根因分析和测试。

## 完整写法（lodash, redux, immer）

### 结构
1. **根因**：Bug 的根本原因，含代码位置；只有在代码、日志或用户说明支持时写成确定结论
2. **方案**：你是怎么修的
3. **测试**：新增测试或回归验证；未知时写待运行验证
4. **Fixes #**：关联 Issue 号，仅在用户或仓库上下文已提供时写

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

## Bug Fix PR — 简洁写法（neovim, terraform, helm）

### 结构
1. **方案**（含 Fixes #，如已知）
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
- [ ] 根因说明或待确认假设
- [ ] 测试覆盖或待运行验证项
- [ ] Fixes # 关联（已知时）
- [ ] 不虚构 Issue 编号、文件路径、测试通过状态或代码 diff

## 参考链接

| 仓库 | 链接 |
|------|------|
| lodash 修复 PRs | https://github.com/lodash/lodash/pulls |
| redux 修复 PRs | https://github.com/reduxjs/redux/pulls?q=label%3Abug |
| immer 修复 PRs | https://github.com/immerjs/immer/pulls |
| neovim 修复 PRs | https://github.com/neovim/neovim/pulls |
| terraform 修复 PRs | https://github.com/hashicorp/terraform/pulls |
| helm 修复 PRs | https://github.com/helm/helm/pulls |
