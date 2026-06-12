# Issue Form YAML — 写作标准

## 适用场景
用 YAML 定义 Issue 表单，引导贡献者规范填写。

## 输出边界

输出必须覆盖用户请求的全部表单类型。用户要求 Bug Report 和 Feature Request 时，两种表单都要给出。不要添加带假 URL 的 `contact_links`；只有真实文档、讨论区或安全政策链接已知时才写。

在对话中展示多个 YAML 文件时，用 `## File: ...` 标题加 fenced `yaml` 代码块。真正写入 `.github/ISSUE_TEMPLATE/*.yml` 时，文件内只保留有效 YAML，不要包含 Markdown 标题或说明。

## 标准写法（vscode, nextjs, rails）

### 结构
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
      options: [v1.x, v2.x, v3.x]
    validations:
      required: true
```

### 参考仓库写法

**microsoft/vscode**
- 10+ 个 YAML 表单：Bug / Feature / Performance / Regression 等
- 二级下拉 + 环境采集 + 自动 labels
- 最完整的 YAML Issue Form 实践

**vercel/nextjs**
- 3 种表单：Bug / Feature / 其他
- CodeSandbox 链接必填验证
- 环境字段 `required: true`

**rails/rails**
- 复选框 + 验证 + 关联版 type
- 风格简洁但完整


## 必含元素 Checklist
- [ ] name + description
- [ ] 必填字段验证
- [ ] labels 自动打
- [ ] 请求的每一种表单类型都有对应 YAML
- [ ] 不包含未验证的外链或 Markdown 包装（当输出目标是实际 YAML 文件时）

## 参考链接

| 仓库 | 链接 |
|------|------|
| vscode .github/ISSUE_TEMPLATE/ | https://github.com/microsoft/vscode/tree/main/.github/ISSUE_TEMPLATE |
| nextjs Issue 表单 | https://github.com/vercel/next.js/tree/canary/.github/ISSUE_TEMPLATE |
| rails Issue 表单 | https://github.com/rails/rails/tree/main/.github/ISSUE_TEMPLATE |
| github/docs Issue 表单 | https://github.com/github/docs/tree/main/.github/ISSUE_TEMPLATE |
| home-assistant Issue 表单 | https://github.com/home-assistant/core/tree/dev/.github/ISSUE_TEMPLATE |
| terraform Issue 表单 | https://github.com/hashicorp/terraform/tree/main/.github/ISSUE_TEMPLATE |
