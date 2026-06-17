# README 写作标准 — 详细规则

当场景路由为 README 时，除 `SKILL.md` 的顶层约束外，应用以下详细规则。

## 定位

Treat the README as a public entry page, not a dump of every internal file. For skill repositories, explain that the project is a portable skill, not a standalone app, README generator, or GitHub integration.

## Title & Logo

**Title & logo default to centered.** Use `<p align="center">` for the logo image and `<h1 align="center">` for the title. Do not ask — center by default.

## Badge

Badge 写法遵循 [`weapons.md`](./weapons.md)，包含完整摆放惯例、优先级顺序和 200+ URL 模式。

**项目适配检查：** 写 badge 前先判断项目类型（库/CLI 工具/应用/插件/文档等），只写确实有的东西：
- 有 CI 配置文件 → 才写 CI badge
- 有发到包注册表（npm/PyPI/crates.io）→ 才写 version badge
- 有下载量数据 → 才写 downloads badge
- 没有的东西不写虚拟 badge。不确定时问用户，不猜测

如果 shields.io 动态 badge 因数据源不存在返回 error/unknown，跳过并告知用户。不重复 badge，同一意图只用一个。默认 3–6 个，推荐顺序：CI → Version → License → Downloads → Security/Social。

## Table Formatting

表格前后必须有空行；用 `| --- | --- |` 对齐线；每行保持独立，不要把多行内容塞入一个单元格。超过 5 列或单元格内容超 30 字时，拆分为多个子表或用列表代替。不得出现文字堆积粘连。

## Section Completeness

README 每一节至少要有 2–3 句实质内容。不得以单句或孤立列表结束一节。某节太薄时合并到相邻节或补充上下文。Overview 不能只有一句话，Quick Start 不能只有一条命令。

## Scenario Index

If scenarios < 20, list all rows in a complete table. If ≥20 scenarios, replace with a link: "See all scenarios in [INDEX.md](../INDEX.md)". Do not enumerate 20+ items inline.

## Multi-language

**默认：** English + 用户对话所用语言。如果用户用英文，不列第二种。

**"最多语言"模式：** 当用户说"最多语言"、"多语言"、"尽量多语言"、"3个及以上语言版本"、"as many languages as possible"、"all languages"，或明确要求 3 种以上语言时，输出完整 8 种：**zh-CN**（README.md）、**en**（README.en.md）、**ja**（README.ja.md）、**ko**（README.ko.md）、**es**（README.es.md）、**fr**（README.fr.md）、**de**（README.de.md）、**pt**（README.pt.md）。每个文件包含相同 badge、居中 logo 和项目结构。使用独立文件，不堆叠在同一文件中。

**语言切换区必须居中**，放在 title/badge 下方、正文之前，用 `<p align="center">`。格式：`🌐 [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) …`。README.md（中文）中中文排首位，其他语言版本中该语言排首位。每个语言版本必须包含指向所有其他版本的链接。

如用户要求多语言但未指定语言，在三个问题中询问。不默认输出大集合。

## Acknowledgements

默认在 README 底部包含 "Acknowledgements" 或 "Thanks" 小节，列出本项目使用或参考的关键项目、工具、资源。每个被参考的项目必须明确标注来源（"部分设计参考自 X"、"基于 Y 的开发模式"、"图标来自 Z"），不得笼统写 "Thanks to all open source projects"。如果用户明确说不想要，再跳过。不声明不存在的从属或背书关系。

## Contributing in README

README 中必须包含一个 "Contributing" 节，写入精简版的贡献规则（怎么提 issue、PR 流程、代码风格要求），不能只放一个链接到 CONTRIBUTING.md。该节需要自包含、可直接阅读，同时在末尾加上 "详细规则见 [CONTRIBUTING.md](../CONTRIBUTING.md)"。

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
- 表必须包含：icon、名称、支持等级、具体方法、官方文档链接
- 主流条目尽可能多写，不超过 20 个。分三类：
  1. **Direct** — 原生支持（直接加载格式）
  2. **Adapted** — 需要适配导入自有规则体系
  3. **Not supported** — 主流但不支持规则定制，标注"暂不支持"
- 每个条目写明适配范围：本 skill 覆盖什么、有什么限制
- 至少包含一个 direct 示例和一个 adapted 示例
- 所有支持声明基于当前官方文档，不推断

## README Three-Question Prompt

在起草 README 前（除非用户明确说跳过），一次性问三个问题：

1. **Delivery:** local markdown file, chat-only draft, or remote repository update after review?
2. **Style & visuals:** documentation-first, community/product style, title/heading emoji, badges, screenshots, or Star History?
3. **Required supplements:** languages, official website, docs/demo URL, screenshot assets, reference projects or acknowledgements, file index, or any other must-include content?
