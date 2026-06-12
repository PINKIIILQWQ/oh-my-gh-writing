# Documentation PR — 写作标准

## 适用场景
纯文档变更，无代码改动。

## 标准写法（home-assistant/core, vercel/nextjs）

### 结构
1. **原文位置**：改了哪个文档的哪个部分
2. **原文 vs 改后**：只有在原文可见时引用；否则描述变更主题
3. **截图预览**（文档 UI 类，已有时提供）
4. **无代码改动声明**

### 参考仓库写法

**home-assistant/core**
- 文档 PR 含截图要求
- 配置变更说明

**vercel/nextjs**
- 文档 PR 含预览链接
- 片段确认机制


## 必含元素 Checklist
- [ ] 修改位置（已知文件/章节；不要编造行号）
- [ ] 原文 vs 新内容（原文可见时）
- [ ] 无代码改动声明
- [ ] 不虚构预览链接、截图、原文片段或文档路径

## 参考链接

| 仓库 | 链接 |
|------|------|
| home-assistant 文档 PRs | https://github.com/home-assistant/core/pulls?q=label%3Adocumentation |
| nextjs 文档 PRs | https://github.com/vercel/next.js/pulls?q=label%3Adocs |
