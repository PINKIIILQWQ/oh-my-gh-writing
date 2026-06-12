# Feature PR — 完整写法

## 适用场景
提交新功能/特性的 Pull Request，需覆盖设计、实现、测试和升级。

## 完整写法（kubernetes, react, django）

### 结构
1. **动机**：为什么需要这个功能；关联 Issue # 只在已知时写
2. **设计**：变更的设计思路，含架构图/数据流
3. **实现**：改了什么文件、如何改
4. **测试**：新增测试覆盖/手动验证步骤；未知时写“Verification to run”
5. **Breaking Changes**：是否破坏兼容性，迁移路径
6. **升级说明**：用户升级需要做什么

### 参考仓库写法

**kubernetes/kubernetes**
- 12 项 checklist：CHERRY_PICK→SIG 标注→文档更新→测试→Breaking→API 变更
- 模板生成器自动填充大部分
- 示例：https://github.com/kubernetes/kubernetes/pulls

**facebook/react**
- What / Why / How 三段式
- 测试修改 + 性能影响说明
- CI 要求所有 lint + test 全绿

**django/django**
- Ticket 关联强制
- 描述 + Patch 说明 + 测试
- Django committer 审查标准

## Feature PR — 简洁写法（storybook, apollo, grafana）

### 结构
1. **动机**：关联 Issue（如已知）
2. **变更**：改了啥
3. **备注**：需注意的特殊点

### 参考仓库写法

**storybookjs/storybook**
- What / Why / How + Screenshot（可选）
- Checklist：测试→文档→Breaking

**apollographql/apollo-client**
- 关联 Issue → 描述 → 测试 → 备注

**grafana/grafana**
- 产品级 PR 模板含截图区域

## 必含元素 Checklist
- [ ] 变更描述
- [ ] 关联 Issue #（已知时）
- [ ] 测试结果或待运行验证项
- [ ] 不把未证实的测试、CI、文件路径或 Issue 编号写成事实

## 可选项
- 截图/录屏：视觉变更必填，默认开启

## 参考链接

| 仓库 | 链接 |
|------|------|
| kubernetes PR 模板 | https://github.com/kubernetes/kubernetes/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| react PR 模板 | https://github.com/facebook/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| django PR 模板 | https://github.com/django/django/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| storybook PRs | https://github.com/storybookjs/storybook/pulls |
| apollo-client PRs | https://github.com/apollographql/apollo-client/pulls |
| grafana PRs | https://github.com/grafana/grafana/pulls |
