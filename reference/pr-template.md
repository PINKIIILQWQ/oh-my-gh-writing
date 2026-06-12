# PR Template — 完整写法

## 适用场景
Pull Request 的描述模板，引导贡献者写全信息。

## 输出边界

PR 模板是给未来贡献者填写的文件，默认使用空白字段、注释和未勾选 checklist。不要把具体测试状态、Issue 编号、benchmark 或项目事实写进模板，除非用户明确要求固定模板内容。

在对话中展示模板时可以用 fenced `markdown` 代码块；真正写入 `.github/PULL_REQUEST_TEMPLATE.md` 时，文件内只保留模板正文，不要包含外层标题。

## 完整写法（kubernetes, react, moby）

### 结构
```markdown
## 动机
（关联 Issue # + 背景）

## 设计
（变更的设计思路）

## 测试
（测试做了什么）

## Checklist
- [ ] 代码风格符合项目规范
- [ ] 自测通过
- [ ] 文档已更新（如需要）
- [ ] Breaking Changes 已标注

## 发布说明
（如果支持自动 Release Note，填一句话）
```

### 参考仓库写法

**kubernetes/kubernetes**
- 最完整的行业标杆 PR 模板
- 12 项 checklist（CHERRY_PICK / SIG / 文档 / 测试 / Breaking / API 变更）
- 严格 CI：lint + test + verify 全绿才合

**facebook/react**
- What / Why / How 三段式
- 测试 + 性能影响
- 简洁但完整

**moby/moby（Docker）**
- 动机 → 实现 → 测试 → 备注
- Docker 级别的产品 PR 规范

## PR Template — 简洁写法（eslint, tailwindcss, apache/spark）

### 结构
动机 → 变更 → Checklist

### 参考仓库写法

**eslint/eslint**
- 动机 + 变更 + 测试 + checklist
- 规则变更示例必含

**tailwindlabs/tailwindcss**
- 简洁 4 字段：动机 + 变更 + 影响 + 测试
- 聚焦最小化 PR

**apache/spark**
- 企业级 PR 规范：JIRA 号 + 描述 + 测试
- 组件前缀（`[SQL]` / `[CORE]`）

## 必含元素 Checklist
- [ ] 动机 / 关联 Issue
- [ ] 变更描述
- [ ] 测试说明
- [ ] Checklist
- [ ] 模板字段保持待填写状态，不预先勾选或填入虚构编号

## 参考链接

| 仓库 | 链接 |
|------|------|
| kubernetes PR 模板 | https://github.com/kubernetes/kubernetes/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| react PR 模板 | https://github.com/facebook/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| moby (Docker) PR 模板 | https://github.com/moby/moby/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| eslint PR 模板 | https://github.com/eslint/eslint/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| tailwindcss PR 模板 | https://github.com/tailwindlabs/tailwindcss/blob/next/.github/PULL_REQUEST_TEMPLATE.md |
| spark PR 模板 | https://github.com/apache/spark/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
