# Feature Request — 完整写法

## 适用场景
请求新功能或能力增强，需要阐明使用场景和期望行为。

## 完整写法（angular, typescript, rails）

### 结构
1. **动机**：当前缺失的能力或痛点
2. **Use Case**（列出 2-3 个典型场景，含具体输入→输出）
3. **期望 API**：伪代码或接口签名，标明这是提案草案
4. **替代方案**：当前 workaround，为什么不够
5. **兼容性**：对现有 API 的影响；未知版本或支持范围用 `TBD`

### 参考仓库写法

**angular**
- Feature 模板：动机→Use Case→期望行为→备选→兼容性
- 每个 Use Case 详细描述用户操作流程
- API 草案常用 TypeScript 类型签名

**rails**
- Rails 的 feature discussion 格式：动机→实施想法→备选
- 开放式的社区讨论风格，但结构完整
- 示例：https://github.com/rails/rails/issues

**microsoft/typescript**
- 建议模板：`Search Terms` → `Suggestion` → `Use Cases` → `Examples` → `Checklist`
- 用 `Playground Link` 跑示例
- 最规范的 TS 社区 feature request

## Feature Request — 简洁写法（svelte, nuxt, babel）

### 结构
1. **问题**（当前你碰到的限制）
2. **期望**（你希望的行为）
3. **备选**（现有 workaround）

### 参考仓库写法

**svelte/svelte**
- 极简式：3-5 句话覆盖问题→期望→为什么
- 附 REPL 链接
- 不要求完整 API 草案

**nuxt/nuxt**
- 问题→建议→workaround
- 偏实用，快速聚焦

**babel/babel**
- 插件式 feature request
- 配置样例 + 期望转换结果

## 必含元素 Checklist
- [ ] 使用场景描述
- [ ] 期望行为/API
- [ ] 替代方案
- [ ] API、版本和兼容性没有被写成已确认事实，除非用户或资料已提供证据

## 参考链接

| 仓库 | 链接 |
|------|------|
| angular Feature Request 表单 | https://github.com/angular/angular/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml |
| TypeScript Suggestion 模板 | https://github.com/microsoft/TypeScript/blob/main/.github/ISSUE_TEMPLATE/suggestion.yml |
| rails Feature Issue 列表 | https://github.com/rails/rails/issues?q=label%3Afeature |
| svelte Feature 讨论 | https://github.com/sveltejs/svelte/discussions |
| nuxt Feature Request | https://github.com/nuxt/nuxt/issues/new/choose |
| babel Feature 讨论 | https://github.com/babel/babel/issues?q=label%3A%22Feature+Request%22 |
