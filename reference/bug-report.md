# Bug Report — 精细标准

## 适用场景
提交 Bug 报告，要求可复现、环境完整的 Issue。

## 精细标准（vscode, nextjs, tailwindcss）

### 结构
1. **标题**：`[Component] 简短问题描述`，用前缀标记模块
2. **描述**：一句话概述问题影响
3. **重现步骤**（编号列表，每一步精确到输入→操作→结果）
4. **预期行为**：应该发生什么
5. **实际行为**：实际发生什么（附错误信息全文）
6. **环境**：OS / 版本 / 浏览器 / Node 版本 / 包管理器
7. **日志/截图**：控制台错误、截图、录屏
8. **附加上下文**：频率、相关 Issue、可能的原因

### 参考仓库写法

**vscode**（YAML Issue Form 量产型）
- 12 字段表单：Bug 类型→扩展名→VS Code 版本→OS→重现步骤→日志等
- 自动采集 `Help → About` 的环境信息
- 示例：https://github.com/microsoft/vscode/issues/new

**nextjs**（复现链接驱动）
- 核心字段：复现链接（CodeSandbox/StackBlitz 必填）→描述→环境
- 强制 CodeSandbox 模板，减少"I can't reproduce"
- 示例：https://github.com/vercel/nextjs/issues

**tailwindcss**（精确最小复现）
- 倾向极小化示例（单一配置 + 单一组件）
- 要求贴 Play CDN 链接
- 不要求大段日志，聚焦配置等价

## Bug Report — 中等标准（golang, electron, eslint）

### 结构
1. **问题概述**（正文第一句）
2. **复现**（简单步骤或代码片段）
3. **期望 vs 实际**（各 1-2 句）
4. **环境**（版本 + OS）

### 参考仓库写法

**golang/go**
- 标题格式：`pkg: description` → `net/http: timeout on keep-alive connections`
- 正文：复现程序（可粘贴运行的完整代码）→ 期望 → 实际 → 环境
- 环境自动填 `go version` 输出
- 最简洁的 5 段式结构，无废话

**electron**
- 环境精细（OS/electron/chrome/node 版本全部自动填）
- 复现步骤 + 实际/期望 + 附截图
- 示例：https://github.com/electron/electron/issues

**eslint**
- 单一规则 Bug 最规范
- 标题：`规则名: 问题描述`
- 正文：代码示例 → 期望报错/不报错 → 实际 → 配置

## 必含元素 Checklist
- [ ] 可复现的最小示例
- [ ] 期望/实际对比
- [ ] 环境信息
- [ ] 错误信息全文

## 可选项
- 环境自动采集脚本：默认开启
- 截图粘贴区：默认建议

## 参考链接

| 仓库 | 链接 |
|------|------|
| vscode Bug Report YAML 表单 | https://github.com/microsoft/vscode/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml |
| nextjs Bug Report YAML 表单 | https://github.com/vercel/next.js/blob/canary/.github/ISSUE_TEMPLATE/1.bug.yml |
| tailwindcss Bug Report 表单 | https://github.com/tailwindlabs/tailwindcss/blob/next/.github/ISSUE_TEMPLATE/bug-report.yml |
| golang/go Issue 分类页 | https://github.com/golang/go/issues/new/choose |
| electron Bug Report | https://github.com/electron/electron/issues/new/choose |
| eslint Bug Report | https://github.com/eslint/eslint/issues/new/choose |
