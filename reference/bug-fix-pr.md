# Bug Fix PR — 写作标准

## 适用场景
修复 Bug 的 Pull Request，重点在根因分析和测试。

## 输出边界

Bug Fix PR 只描述已经修复的缺陷。根因必须来自代码、日志、测试或用户明确说明；没有证据时写待确认假设。

## 标准结构

1. **根因**：Bug 的根本原因，含代码位置；只有在代码、日志或用户说明支持时写成确定结论
2. **方案**：你是怎么修的
3. **测试**：新增测试或回归验证；未知时写待运行验证
4. **Fixes #**：关联 Issue 号，仅在用户或仓库上下文已提供时写

## 信息不足时

- 缺少 Issue 编号时，不写 `Fixes #` 占位。
- 缺少测试输出时，写 `Verification to run`。
- 根因不确定时，用 `Suspected cause`。

## 禁止编造项

- 不编造文件路径、行号、测试通过状态、CI 名称、Issue 编号或 regression 范围。
- 不把参考项目的测试命令写进目标项目。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR template docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository |
| Kubernetes PR Template | https://github.com/kubernetes/kubernetes/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| React PR Template | https://github.com/react/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Node.js CONTRIBUTING | https://github.com/nodejs/node/blob/main/CONTRIBUTING.md |
| Electron CONTRIBUTING | https://github.com/electron/electron/blob/main/CONTRIBUTING.md |
| Helm CONTRIBUTING | https://github.com/helm/helm/blob/main/CONTRIBUTING.md |

## 必含元素 Checklist
- [ ] 根因说明或待确认假设
- [ ] 测试覆盖或待运行验证项
- [ ] Fixes # 关联（已知时）
- [ ] 不虚构 Issue 编号、文件路径、测试通过状态或代码 diff
