# Documentation PR — 写作标准

## 适用场景
纯文档变更，无代码改动。

## 输出边界

Documentation PR 只描述文档变更。没有代码改动证据时不要声明运行时行为变化；没有预览链接或截图时不要编造。

## 标准结构

1. **原文位置**：改了哪个文档的哪个部分
2. **原文 vs 改后**：只有在原文可见时引用；否则描述变更主题
3. **截图预览**（文档 UI 类，已有时提供）
4. **无代码改动声明**

## 信息不足时

- 不知道具体文件时，写 `Docs location: TODO`。
- 没有预览系统时，删除 preview 段落。
- 原文不可见时，不引用“原文”，只写变更主题。

## 禁止编造项

- 不编造文档路径、行号、预览链接、截图、原文片段或部署状态。
- 不把文档 PR 写成代码 PR；如有代码变更，改走对应 PR 场景。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR template docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository |
| Kubernetes Website PR Template | https://github.com/kubernetes/website/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| VS Code Docs CONTRIBUTING | https://github.com/microsoft/vscode-docs/blob/main/CONTRIBUTING.md |
| MDN Content CONTRIBUTING | https://github.com/mdn/content/blob/main/CONTRIBUTING.md |
| Django writing docs | https://github.com/django/django/blob/main/docs/internals/contributing/writing-documentation.txt |
| Angular docs contribution rules | https://github.com/angular/angular/blob/main/CONTRIBUTING.md#documentation |

## 必含元素 Checklist
- [ ] 修改位置（已知文件/章节；不要编造行号）
- [ ] 原文 vs 新内容（原文可见时）
- [ ] 无代码改动声明
- [ ] 不虚构预览链接、截图、原文片段或文档路径
