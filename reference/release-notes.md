# Release Notes — 完整版

## 适用场景
版本发布公告，面向用户介绍新版本。

## 完整版（astro, npm/cli, svelte）

### 结构
1. **版本标签**（`v2.0.0` + 发布日期）
2. **摘要**（1-2 句版本亮点）
3. **新特性**（每个特性含：名称 / 截图或 GIF / 用法示例 / 链接到文档）
4. **Breaking Changes**（影响 + 迁移步骤）
5. **升级指南**（从上一版本升级所需操作）
6. **Full Changelog 链接**

### 参考仓库写法

**withastro/astro**
- 每版 release 配 GIF 演示 + Code Block 示例
- 结构：Highlights → Breaking → 迁移 → 致谢
- 社区感强（Contributor 致谢列表）

**npm/cli**
- Blog 风格 release：叙述式介绍 + 变更列表 + 升级说明
- 适合读者逐段阅读

**svelte/svelte**
- 公告式 release：版本亮点 → 新特性详情 → Breaking → 迁移
- 配代码对比（before/after）

## Release Notes — 普通版（buf, bun, deno）

### 结构
版本 + 主要变更列表 + 链接

### 参考仓库写法

**bufbuild/buf**
- 列表式 release：Breaking → Features → Fixes
- 简洁，每条带 PR

**oven-sh/bun**
- bullet list release：每条变更一句话 + PR 链接
- 重点突出 perf 改进

**denoland/deno**
- 功能列表 + 稳定性说明
- 含内置工具更新记录

## 必含元素 Checklist
- [ ] 版本号 + 日期
- [ ] 新特性列表
- [ ] Breaking Changes（如有）
- [ ] Full Changelog 链接

## 参考链接

| 仓库 | 链接 |
|------|------|
| astro Release | https://github.com/withastro/astro/releases |
| npm Release | https://github.com/npm/cli/releases |
| svelte Release | https://github.com/sveltejs/svelte/releases |
| buf Release | https://github.com/bufbuild/buf/releases |
| bun Release | https://github.com/oven-sh/bun/releases |
| deno Release | https://github.com/denoland/deno/releases |
