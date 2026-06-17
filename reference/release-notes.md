# Release Notes — 写作标准

## 适用场景
发布公告，面向用户介绍本次发布。

## 输出边界

Release Notes 面向发布读者。版本号、日期、release URL、贡献者、截图、GIF、迁移命令和 Full Changelog 必须来自真实 release、tag、compare URL、仓库文件或用户输入。

## 标准结构

短发布或 patch/minor 版本：

1. **Version**：版本号和日期；未知时写 `TBD`。
2. **Highlights**：1-3 条用户最需要知道的变化。
3. **Fixes / Changes**：只列有证据的修复或改动。
4. **Upgrade notes**：如有必要，写升级注意事项。
5. **Full changelog**：有真实 release、tag 或 compare URL 时才写。

大型版本或 major release：

1. **版本标签**（`v2.0.0` + 发布日期）
2. **摘要**（1-2 句版本亮点）
3. **新特性**（每个特性含名称、影响和用法；截图/GIF 只在已有素材时加入）
4. **Breaking Changes**（影响 + 迁移步骤）
5. **升级指南**（从上一版本升级所需操作）
6. **Full Changelog 链接**：有真实 release、compare URL 或仓库范围时才写

## 信息不足时

- 缺少版本号或日期时写 `TBD`，不要猜。
- 没有真实 compare URL 时，删除 Full Changelog。
- 没有素材时不写 screenshot/GIF 段落。

## 禁止编造项

- 不编造 release URL、贡献者名单、迁移命令、内置插件列表、截图/GIF、平台支持或 benchmark。
- 不把 changelog 条目改写成未经证实的宣传语。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Releases docs | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases |
| Astro 5.0 release | https://github.com/withastro/astro/releases/tag/astro%405.0.0 |
| npm CLI v11 release | https://github.com/npm/cli/releases/tag/v11.0.0 |
| Svelte 5 release | https://github.com/sveltejs/svelte/releases/tag/svelte%405.0.0 |
| Buf v1.50 release | https://github.com/bufbuild/buf/releases/tag/v1.50.0 |
| Deno 2.0 release | https://github.com/denoland/deno/releases/tag/v2.0.0 |

## 必含元素 Checklist
- [ ] 版本号 + 日期
- [ ] Highlights 或新特性列表
- [ ] Breaking Changes / Upgrade notes（如有）
- [ ] Full Changelog 链接（已知时）
- [ ] 不虚构迁移命令、内置插件列表、release URL、截图/GIF 或贡献者名单
