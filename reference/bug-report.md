# Bug Report — 写作标准

## 适用场景
提交 Bug 报告，要求可复现、环境完整的 Issue。

## 输出边界

Bug Report 只描述已经观察到的缺陷。不要把未验证原因写成结论，不要发明环境采集脚本、复现仓库、日志、截图或版本号。

## 标准结构

1. **标题**：`[Component] 简短问题描述`，用前缀标记模块
2. **描述**：一句话概述问题影响
3. **重现步骤**（编号列表，每一步精确到输入→操作→结果）
4. **预期行为**：应该发生什么
5. **实际行为**：实际发生什么（附错误信息全文）
6. **环境**：OS / 版本 / 浏览器 / Node 版本 / 包管理器
7. **日志/截图**：控制台错误、截图、录屏
8. **附加上下文**：频率、相关 Issue、已验证线索或待确认假设

## 信息不足时

- 缺少复现步骤时，写 `Steps to reproduce: TODO`，不要补想象步骤。
- 缺少环境时，列出需要用户补充的字段。
- 只有症状、没有原因时，用 `Suspected cause` 或 `Needs confirmation`。

## 禁止编造项

- 不编造复现仓库、sandbox 链接、日志、截图、版本号、平台或 root cause。
- 不声称“已确认 regression”或“已定位到某文件”，除非用户或代码证据已给出。
- 不把参考仓库的字段和标签直接当成目标仓库事实。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Issue templates | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository |
| VS Code Bug Report | https://github.com/microsoft/vscode/blob/main/.github/ISSUE_TEMPLATE/bug_report.md |
| Next.js Bug Report | https://github.com/vercel/next.js/blob/canary/.github/ISSUE_TEMPLATE/1.bug_report.yml |
| Tailwind CSS Bug Report | https://github.com/tailwindlabs/tailwindcss/blob/main/.github/ISSUE_TEMPLATE/bug-report.md |
| TypeScript Bug Report | https://github.com/microsoft/TypeScript/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml |
| Kubernetes Issue Templates | https://github.com/kubernetes/kubernetes/tree/master/.github/ISSUE_TEMPLATE |

## 必含元素 Checklist
- [ ] 可复现的最小示例
- [ ] 期望/实际对比
- [ ] 环境信息
- [ ] 错误信息全文
- [ ] 未验证原因写成“可能原因”或“待确认”，不要写成确定 root cause
