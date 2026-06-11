# README — 完整版

## 适用场景
项目首页文档，开源或闭源项目的入口页面，面向新用户快速了解项目价值、安装上手、贡献方式。

## 完整版（vscode, nextjs, tailwindcss）

### 核心原则
- **中英双语默认可切换**：README 以英文为主（GitHub 默认语言），在文档开头提供中文版跳转链接；或通过 README-zh.md 并行维护
- **仓库内容全面罗列**：每项重要功能、每个目录、每个配置项都应被覆盖或通过链接可达
- **审视代码后输出大纲**：写 README 前，先审查项目源码结构（目录树、配置文件、入口文件），然后输出一份目录大纲，内容较少时全部列出
- **嵌入式引用**：所有提及的品牌、协议、技术栈必须附带超链接 —— [MIT](https://opensource.org/licenses/MIT)、[Next.js](https://nextjs.org)、[OpenAI](https://openai.com)、[shields.io](https://shields.io)

### 结构

1. **标题 + 副标题**（项目名 + 一行概括）
2. **徽章栏**（构建状态 / 最新版本 / 许可 / 测试覆盖 / 下载量 / 平台 / Star History 徽章）
3. **简介**（2-5 句说明项目解决了什么问题，与同类项目的核心差异，面向用户画像）
4. **Star History 区**（询问使用者是否需要 star history 图表，若需要嵌入 `![Star History](https://api.star-history.com/svg?repos=owner/repo&type=Date)`）
5. **目录**（TOC，自动生成锚点链接，场景较多时必含）
6. **功能列表**（Feature 表格或列表，每项含 emoji 图标 + 说明 + 可选 GIF/截图）
7. **快速开始**（安装命令 → 最小可运行示例 → 预期输出，确保可复制粘贴执行）
8. **使用案例**（若场景过多则用超链接指向 docs/examples 目录；场景少则逐项列出）
9. **文档导航**（API 文档 / 教程 / Wiki / 讨论区 / Discord / Stack Overflow 标签）
10. **贡献指南**（指向 CONTRIBUTING.md，含 PR 流程、开发环境搭建、commit 规范）
11. **许可与致谢**（许可协议链接 + 依赖项目 + 赞助商）

### 参考仓库写法

**microsoft/vscode**
- README 首页 Hero 截图 + 下载按钮突出，10+ 徽章
- [功能表格列出全部核心特性](https://github.com/microsoft/vscode#features)
- 文档家族导航完整（Docs / API / Extensions / 论坛）
- 底部许可 + 隐私声明 + 商标声明
- 多语言说明（Translate this README）
- 地址：https://github.com/microsoft/vscode

**vercel/nextjs**
- 标题下方极简单行描述
- [快速开始 3 步构建](https://github.com/vercel/next.js#quick-start) — 完全可复制
- 文档链接全覆盖（Learn / API / Examples / Deploy）
- 底部显示 Star History + [贡献者统计](https://github.com/vercel/next.js/graphs/contributors)
- 地址：https://github.com/vercel/next.js

**tailwindlabs/tailwindcss**
- [Live Play CDN 链接](https://play.tailwindcss.com) 直接可试，无需安装
- 功能列表 + 截图 + 简洁导航
- 无多余装饰，干净聚焦
- 地址：https://github.com/tailwindlabs/tailwindcss

### 使用案例

- **开源框架**：Next.js/React 等 —— 突出快速开始 + 文档分层 + 社区链接
- **CLI 工具**：curl/jq 等 —— 突出安装命令 + 核心用法示例 + man page
- **UI 组件库**：shadcn/ui 等 —— 突出安装 + 截图 + 可交互 Playground
- **数据项目**：pandas/TensorFlow 等 —— 突出 Quickstart + API 文档 + 教程
- 使用案例较多时，以表格形式列出场景名 → 说明 → 链接到 examples/

### 审视代码输出大纲

写 README 前，按以下步骤审视项目：

1. 检查根目录 `ls -la`，列出全部文件和目录
2. 阅读 `package.json` / `Cargo.toml` / `pyproject.toml` 等入口配置文件，提取项目名、版本、依赖、scripts
3. 检查 `src/` 或 `lib/` 目录结构，了解模块划分
4. 检查示例代码目录 `examples/` / `demo/`
5. 检查配置文件 `.env.example` / `config.yml`
6. 输出大纲（内容较少时全文输出）：

```
## 大纲
1. 项目名 + 描述（来自 package.json）
2. 功能列表（根据 src/ 目录推断）
3. 安装方式（npm/pip/cargo/brew）
4. 快速开始（读取 examples/ 目录）
5. 配置说明（读取 .env.example）
6. 文档与链接
7. 许可（读取 LICENSE 文件）
```

### 默认中英双语切换

在 README 顶部添加：

```markdown
<p align="center">
  <a href="./README-zh.md">简体中文</a> · <a href="./README.md">English</a>
</p>
```

或使用 `<h1>` 下方双语描述。要求中英文 README 同步更新，避免内容 drift。

### 产品适用范围

README 应说明项目运行的载体和兼容环境。对于 agent skill 类项目：

```markdown
## Product Scope

| Dimension | Details |
|-----------|---------|
| **Format** | SKILL.md (YAML frontmatter + markdown) |
| **Carrier** | File-based — copy into agent's rules directory |
| **Dependencies** | None |
| **Supported agents** | [Hermes Agent](https://hermes-agent.nousresearch.com/docs), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Cursor](https://docs.cursor.com/context/rules-for-ai), [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot), etc. |
| **License** | [MIT](https://opensource.org/licenses/MIT) |
```

### 必含元素 Checklist

- [ ] 标题 + 一行描述
- [ ] 徽章栏（构建 + 版本 + 许可，至少 3 个）
- [ ] 快速开始（安装 + 最小可运行示例）
- [ ] 功能列表（2-10 项，每项含说明）
- [ ] 文档导航链接
- [ ] 许可协议（含超链接）
- [ ] Star History（询问使用者是否需要）
- [ ] 目录/锚点导航（场景 ≥5 时必含）
- [ ] 所有技术栈/协议提及附带超链接
- [ ] 产品适用范围说明（格式、载体、支持的 agent 框架、许可）

### 可选项

- 徽章：默认 top 3（构建 + 版本 + 许可），可根据项目类型扩展（npm 下载量、Docker pulls、Coveralls）
- TOC：默认自动生成，手动维护时用 `<!-- START doctoc -->` 标记
- 贡献者表：默认不包含，若项目活跃且用户要求则加
- GIF/截图演示：若产品有 UI 则默认含，否则可略
- 多语言说明：中英双语为默认配置
- Star History 图表：询问使用者是否需要
- 赞助商/资金信息：如项目有 Open Collective / GitHub Sponsors 则询情添加

### 参考链接

| 仓库 | 链接 |
|------|------|
| vscode README | https://github.com/microsoft/vscode |
| nextjs README | https://github.com/vercel/next.js |
| tailwindcss README | https://github.com/tailwindlabs/tailwindcss |
| deno README | https://github.com/denoland/deno |
| supabase README | https://github.com/supabase/supabase |
| github/docs README | https://github.com/github/docs |
| Star History | https://api.star-history.com/svg?repos= |
| shields.io 徽章 | https://shields.io |

> **请问还有什么需要额外注意的地方吗？** — 在 README 初稿产出后向使用者确认：是否需要补充 Star History？是否需要多语言版本？是否要特定风格的徽章？是否有需要强调的特定功能或社区链接？

---

# README — 普通版

## 适用场景
中小型项目或内部工具，需要清晰但不过度复杂的首页文档。

## 结构
标题 → 简介 → 快速开始 → 功能 → 文档链接 → 许可

### 参考仓库写法

**denoland/deno**
- https://github.com/denoland/deno
- 极简标题 + 安装命令 `curl -fsSL https://deno.land/install.sh | sh`
- 快速开始含完整示例（hello world + HTTP 服务器）
- 无徽章栏，干净聚焦

**supabase/supabase**
- https://github.com/supabase/supabase
- Hero 区域 + 快速开始
- 产品导向，文档链接分层（Client / CLI / API）
- 底部含 GitHub 统计

**github/docs**
- https://github.com/github/docs
- 标题 + 描述 + 快速开始 + 配置
- 开发者友善，精简但完整

### 必含元素 Checklist
- [ ] 标题 + 一行描述
- [ ] 快速开始（安装 + 最小示例）
- [ ] 文档链接
- [ ] 许可信息

### 参考链接

| 仓库 | 链接 |
|------|------|
| deno README | https://github.com/denoland/deno |
| supabase README | https://github.com/supabase/supabase |
| github/docs README | https://github.com/github/docs |
