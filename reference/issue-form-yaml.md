# Issue Form YAML — 精细标准

## 适用场景
用 YAML 定义 Issue 表单，引导贡献者规范填写。

## 精细标准（vscode, nextjs, rails）

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

## Issue Form YAML — 中等标准（github/docs, home-assistant, terraform）

### 结构
精简字段 + 必要验证

### 参考仓库写法

**github/docs**
- 4 字段：描述 + 重现 + 环境 + 其他
- 最小化但够用

**home-assistant/core**
- 多表单：Bug + Feature + 集成请求
- 含自动诊断采集

**hashicorp/terraform**
- Provider 级 Issue 表单
- Terraform 版本 + Provider 版本 + 配置

## 必含元素 Checklist
- [ ] name + description
- [ ] 必填字段验证
- [ ] labels 自动打

## 参考链接

| 仓库 | 链接 |
|------|------|
| vscode .github/ISSUE_TEMPLATE/ | https://github.com/microsoft/vscode/tree/main/.github/ISSUE_TEMPLATE |
| nextjs Issue 表单 | https://github.com/vercel/next.js/tree/canary/.github/ISSUE_TEMPLATE |
| rails Issue 表单 | https://github.com/rails/rails/tree/main/.github/ISSUE_TEMPLATE |
| github/docs Issue 表单 | https://github.com/github/docs/tree/main/.github/ISSUE_TEMPLATE |
| home-assistant Issue 表单 | https://github.com/home-assistant/core/tree/dev/.github/ISSUE_TEMPLATE |
| terraform Issue 表单 | https://github.com/hashicorp/terraform/tree/main/.github/ISSUE_TEMPLATE |
