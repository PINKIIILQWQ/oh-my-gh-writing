# README 写作标准 — 详细规则

当场景路由为 README 时，除 `SKILL.md` 的顶层约束外，应用以下详细规则。

## 定位

Treat the README as a public entry page, not a dump of every internal file. For skill repositories, explain that the project is a portable skill, not a standalone app, README generator, or GitHub integration.

## Title & Logo

**Title & logo default to centered.** Use `<p align="center">` for the logo image and `<h1 align="center">` for the title. Do not ask — center by default.

## Badge

Badge 写法遵循 [`weapons.md`](./weapons.md)。如果用户要求精细 badge 设计或需要查找具体 shields.io URL 模式，再读取 [`badge-catalog.md`](./badge-catalog.md)。

**项目适配检查：** 写 badge 前先判断项目类型（库/CLI 工具/应用/插件/文档等），只写确实有的东西：
- 有 CI 配置文件 → 才写 CI badge
- 有发到包注册表（npm/PyPI/crates.io）→ 才写 version badge
- 有下载量数据 → 才写 downloads badge
- 没有的东西不写虚拟 badge。不确定时问用户，不猜测

如果 shields.io 动态 badge 因数据源不存在返回 error/unknown，跳过并告知用户。不重复 badge，同一意图只用一个。默认 3–6 个，推荐顺序：CI → Version → License → Downloads → Security/Social。

## Table Formatting

表格前后必须有空行；用 `| --- | --- |` 对齐线；每行保持独立，不要把多行内容塞入一个单元格。超过 5 列或单元格内容超 30 字时，拆分为多个子表或用列表代替。不得出现文字堆积粘连。

## Brand / Tool Icons

当 README 表格或列表中出现品牌、工具、框架、平台或项目名称时，默认使用对应官方图标或稳定 favicon。优先级：官方站点 favicon / 官方 logo asset → simple-icons / skillicons / devicon → 省略图标。找不到稳定来源时不要自造图标。图标必须有 `alt`，尺寸保持 14-18px，表格列名可用 `Icon` / `图标`。

## Section Completeness

Overview、Quick Start、Usage、Configuration、Architecture 等核心解释区应有实质内容，不能只有一句空泛口号。License、Contributing、Links、Acknowledgements 等入口型小节可以很短；如果某节没有真实信息，合并或省略。

## Scenario Index

If scenarios < 20, list all rows in a complete table. If ≥20 scenarios, replace with a link: "See all scenarios in [INDEX.md](../INDEX.md)". Do not enumerate 20+ items inline.

## Multi-language

**默认：** English + 用户对话所用语言。如果用户用英文，只默认 English。

询问语言时标注默认值。中文对话示例：`目标语言（默认：English + 简体中文）`。英文对话示例：`Target language (default: English)`。

如用户要求多语言但未指定语言，在 README three-question prompt 的补充问题中询问具体语言列表。不要默认输出大语言集合。

只有当对应 README 文件会同步生成或已经存在时，才添加语言切换链接。不得链接不存在的 `README.*.md`。

如果用户明确要求多语言，可建议这些候选：English、简体中文、Español、हिन्दी、العربية、Français、Português、日本語、한국어。最终输出语言以用户确认或已有文件为准。

## Acknowledgements

仅当仓库文件、依赖、用户输入、现有 README 或来源目录证明存在真实使用、参考、派生、借鉴或资源来源时，添加 "Acknowledgements" / "Thanks"。每个被参考的项目必须说明关系，例如 "结构参考自 X"、"badge 模式参考 Y"、"图标来自 Z"。不得写笼统感谢，不声明不存在的从属、授权或背书关系。

## Contributing in README

如果仓库存在 `CONTRIBUTING.md`，或项目明确面向外部贡献者，README 应包含一个简短 Contributing 入口，并链接到完整规则。不要为私有、一次性、内部或没有外部贡献流程的项目强行生成贡献流程。

## Form / Template Priority

如果目标仓库已有 `.github/` 目录下的 ISSUE_TEMPLATE、PULL_REQUEST_TEMPLATE、bug_report.yml、feature_request.yml 等表单文件，直接使用该仓库自带的模板，不需要自行生成。具体流程：
1. 搜索目标仓库的 `.github/` 目录，获取模板文件
2. 读取模板内容，解析所有字段及其 `validations.required` 状态
3. **必填项（required: true）** 如果用户描述中已覆盖，直接填入；如果未覆盖，**询问用户**，不猜测
4. **可选项（无 required 或 required: false）** 跳过，不填、不问、不留 TODO。用户没提就当不需要
5. 按模板结构输出完整的 artifact，去掉对话性包装
6. 如果仓库没有模板，再使用本 skill 的场景标准文件

## Agent / Platform Support Table

当 README 包含支持表时：

- 对于此项目，支持表的覆盖类型不一定是 Agent，取决于实际需求确认。选择最合适的纵列（框架、平台、技术栈、工具）。本 skill 以 Agent 为例
- 查阅最新官方文档后写支持声明，链接每个条目的官方文档
- 表必须包含：图标、名称、推荐接入方式、注意事项或官方文档链接
- 不要硬分平台等级。直接说明是作为 skill 目录使用、作为项目规则使用、作为自定义指令使用，还是需要按当前文档确认
- 每个条目写明使用范围：本规则覆盖什么、有什么限制
- 对品牌/工具默认使用图标；没有稳定图标来源时省略，不要编造
- 所有支持声明基于当前官方文档，不推断

## README Three-Question Prompt

在起草 README 前（除非用户明确说跳过），一次性问三个问题：

1. **Delivery:** local markdown file, chat-only draft, or remote repository update after review?
2. **Style & visuals:** documentation-first, community/product style, title/heading emoji, badges, screenshots, or Star History?
3. **Required supplements:** languages, official website, docs/demo URL, screenshot assets, reference projects or acknowledgements, file index, or any other must-include content?
