# PR Template — 写作标准

## 适用场景
Pull Request 的描述模板，引导贡献者写全信息。

## 输出边界

PR 模板是给未来贡献者填写的文件，默认使用空白字段、注释和未勾选 checklist。不要把具体测试状态、Issue 编号、benchmark 或项目事实写进模板，除非用户明确要求固定模板内容。

在对话中展示模板时可以用 fenced `markdown` 代码块；真正写入 `.github/PULL_REQUEST_TEMPLATE.md` 时，文件内只保留模板正文，不要包含外层标题。

## 标准结构

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

## 信息不足时

- 模板不知道项目命令时，不写具体 `npm test` / `go test` / CI 名称。
- 不知道 label 或 Issue 格式时，保留通用 `Related issue`。
- 不知道 release note 机制时，提供空白区块或注释，不写固定自动化规则。

## 禁止编造项

- 不预先勾选 checklist。
- 不写项目不存在的测试命令、发布流程、label、cherry-pick 流程或自动 release note 格式。
- 不把参考模板里的组织字段复制到目标项目。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR template docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository |
| Kubernetes PR Template | https://github.com/kubernetes/kubernetes/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| React PR Template | https://github.com/facebook/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Moby PR Template | https://github.com/moby/moby/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| ESLint PR Template | https://github.com/eslint/eslint/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Tailwind CSS PR Template | https://github.com/tailwindlabs/tailwindcss/blob/main/.github/PULL_REQUEST_TEMPLATE.md |

## 必含元素 Checklist
- [ ] 动机 / 关联 Issue
- [ ] 变更描述
- [ ] 测试说明
- [ ] Checklist
- [ ] 模板字段保持待填写状态，不预先勾选或填入虚构编号
