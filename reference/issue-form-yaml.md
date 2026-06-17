# Issue Form YAML — 写作标准

## 适用场景
用 YAML 定义 Issue 表单，引导贡献者规范填写。

## 输出边界

输出必须覆盖用户请求的全部表单类型。用户要求 Bug Report 和 Feature Request 时，两种表单都要给出。不要添加带假 URL 的 `contact_links`；只有真实文档、讨论区或安全政策链接已知时才写。

在对话中展示多个 YAML 文件时，用 `## File: ...` 标题加 fenced `yaml` 代码块。真正写入 `.github/ISSUE_TEMPLATE/*.yml` 时，文件内只保留有效 YAML，不要包含 Markdown 标题或说明。

## 标准结构

```yaml
name: Bug Report
description: 提交 Bug 报告
labels: [bug]
body:
  - type: markdown
    attributes:
      value: "## Bug Report"
  - type: textarea
    id: description
    attributes:
      label: 描述
      placeholder: 清楚描述问题
    validations:
      required: true
  - type: dropdown
    id: version
    attributes:
      label: 版本
      options:
        - TODO: add supported versions
    validations:
      required: true
```

## 信息不足时

- 不知道版本列表时，用文本输入或 `TODO`，不要写假版本。
- 不知道文档/安全/讨论链接时，不写 `contact_links`。
- 多个表单必须分别输出文件名和内容。

## 禁止编造项

- 不编造 label、project、assignee、外链、版本号或环境字段。
- 不把 Markdown 展示标题写进实际 YAML 文件。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Issue forms docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository |
| VS Code Issue Templates | https://github.com/microsoft/vscode/tree/main/.github/ISSUE_TEMPLATE |
| Next.js Issue Templates | https://github.com/vercel/next.js/tree/canary/.github/ISSUE_TEMPLATE |
| TypeScript Issue Templates | https://github.com/microsoft/TypeScript/tree/main/.github/ISSUE_TEMPLATE |
| Kubernetes Issue Templates | https://github.com/kubernetes/kubernetes/tree/master/.github/ISSUE_TEMPLATE |
| Home Assistant Issue Templates | https://github.com/home-assistant/core/tree/dev/.github/ISSUE_TEMPLATE |

## 必含元素 Checklist
- [ ] name + description
- [ ] 必填字段验证
- [ ] labels 自动打
- [ ] 请求的每一种表单类型都有对应 YAML
- [ ] 不包含未验证的外链或 Markdown 包装（当输出目标是实际 YAML 文件时）
