# README — 项目首页标准

## 目录

- [适用场景](#适用场景)
- [写前检查](#写前检查)
- [询问触发](#询问触发)
- [核心原则](#核心原则)
- [标准结构](#标准结构)
- [Skill 仓库规则](#skill-仓库规则)
- [Agent 支持矩阵](#agent-支持矩阵)
- [中英双语](#中英双语)
- [双语文件策略](#双语文件策略)
- [徽章规则](#徽章规则)
- [Emoji 和视觉组件](#emoji-和视觉组件)
- [Star History](#star-history)
- [安装和快速开始](#安装和快速开始)
- [不应出现在公开 README](#不应出现在公开-readme)
- [Checklist](#checklist)
- [参考链接](#参考链接)

## 适用场景

项目首页文档，面向第一次打开仓库的人。README 应回答三个问题：这是什么、如何开始、下一步去哪里。它不是完整索引、设计过程记录或内部分析记录。

## 写前检查

写 README 前先快速审视仓库，不要直接套模板：

1. 读取现有 README、LICENSE、入口配置文件和顶层目录。
2. 判断项目类型：库、CLI、应用、文档站、模板、agent skill、GitHub 配置仓库等。
3. 找出真正的用户入口：安装命令、最小示例、主文档、规则入口或模板入口。
4. 区分公开用户材料和维护材料。内部过程记录默认不放进公开首页。
5. 保留已有风格：语言、标题层级、徽章风格、链接格式和命令写法。
6. 在开始写正文前，先确认交付方式：是给本地 markdown 草稿、只在对话里给草稿，还是在用户确认后再更新远端仓库。没有明确授权时，不要直接上传或 push。
7. 估计输出规模。预计超过 120 行、4000 个中文字符或 2500 个英文词时，先用 1 到 3 个问题收敛范围；用户明确要求“一次性直接写”时可以继续，但要说明默认取舍。

除非缺少无法推断的关键信息，不要先问一串问题。先给可用草稿，并把不确定项标为 `TODO` 或“替换为你的仓库 URL”。但如果交付方式未明确，必须先确认这一点，再继续写。

## 询问触发

README 有些选择会显著改变最终效果，不能全靠 agent 猜。触发条件和默认值如下：

| 触发条件 | 先问什么 | 默认值 |
|----------|----------|--------|
| 交付路径不明确 | 本地 markdown 草稿、对话草稿，还是看过后再更新远端 | 本地或对话草稿，不直接 push |
| 预计长 README | 读者是谁、要偏简洁还是完整、是否保留高级视觉组件 | 完整但克制，避免营销化 |
| 仓库定位不清 | 库 / CLI / 应用 / 文档站 / skill / 模板 | 先按代码和入口文件判断，不确定处标 `TODO` |
| 要加入 emoji、动图、截图、Star History、贡献图 | 是否真的需要这些视觉元素 | 默认不加 |
| 要更新旧仓库 README | 是否保留原有风格，是否更新陈旧外链、徽章和 Star History | 保留风格，只修正失效或过时内容 |

每次最多先问 3 个问题。推荐问题顺序：

1. 交付方式：写成本地文件、只给草稿，还是等你确认后再更新远端？
2. 风格：偏文档型克制，还是偏社区/产品型活泼？
3. 视觉：是否允许使用 emoji、徽章、截图或 Star History？

如果用户明确说“直接写”“别问”“按你判断”，就不要阻塞；使用默认值，并在草稿中避免不可证实和高维护成本的内容。

## 核心原则

- **入口清晰**：首屏必须出现项目名、一句话定位和最短开始路径。
- **分层披露**：README 放最短路径，INDEX 放全量导航，reference 放规则细节。
- **证据驱动**：不要虚构 CI、版本、下载量、兼容平台、截图、性能或 Star History。
- **安装可信**：不要把 Homebrew、npm、Docker、curl install、release asset、`go install` 等写成可用安装方式，除非仓库或官方包页面能证明它存在。
- **命令可复制**：能直接运行的命令不要含未解释的 `<owner>`、`<repo>`、`your-token` 等占位符；需要占位时先说明如何替换。
- **少即是准**：不要因为仓库里存在某个目录就把它放进 README。只链接读者下一步确实需要的入口。
- **引用内收**：链接是补充，不应代替关键信息。关键行为、安装方式和限制必须写在正文。
- **双语同步**：要求双语时，两种语言的结构、链接和命令保持一致；长 README 默认拆成两个文件。
- **官方核验**：涉及当前 agent、平台、API、安装方式或使用方式是否可用时，先查官方文档，再写支持结论和示例命令。
- **先确认后发布**：即便仓库里有源代码，也不把“能写出 README 草稿”和“已经允许更新远端仓库”混为一谈。第一版默认只产出草稿或本地文件，是否上传由用户在看过草稿后决定。

## 标准结构

默认输出可直接作为公开 README 草稿使用；信息不足时保留必要结构，并把缺失内容标为 `TODO`。

1. 标题区：项目名标题在前；如使用 logo 或主图标，放在标题下方并控制尺寸，README 顶部 logo 通常用 96 到 180 像素，不要大到压过标题。
2. 语言切换：长 README 用多文件链接，短 README 才用单文件锚点。
3. 徽章栏：3 到 6 个可验证徽章，必要时分组。
4. 简介：2 到 4 句说明目标读者、解决的问题和非目标。
5. Quick Start：安装或接入方式 + 最小可用示例 + 预期结果。
6. Agent 或平台支持矩阵：仅当项目确实需要跨工具安装说明时添加。
7. 功能或场景总览：只列核心能力，避免把所有内部文件逐项罗列。
8. 工作方式或架构概览：仅当它帮助用户理解如何使用项目时添加。
9. 文件定位：只列核心入口文件；本地草稿和未公开材料不放进公开入口。
10. 下一步链接：文档、示例、贡献指南、问题反馈，按项目实际存在情况添加。
11. License：链接到许可证文件。
12. 交付方式：README 草稿阶段默认不直接执行远端发布；先把内容写出来让用户确认，再决定是否上传。

不要为了显得完整而默认添加目录、Star History、贡献者图表、赞助商、长篇 FAQ 或完整目录树；只有它们对读者的下一步有帮助并且有证据时才加入。

## Skill 仓库规则

当 README 所属项目是 agent skill 时，必须避免把它写成普通软件产品：

- 明确说明它是可被 agent 加载的写作/工作流规则，不是独立应用、GitHub App、CI 工具或 README 生成器。
- 首要入口是 `SKILL.md`；场景细则在 `reference/`。
- 公开 README 只列运行所需入口，不展示本地过程材料。
- 文件定位只放 `SKILL.md`、`INDEX.md`、`reference/`、`LICENSE` 等用户确实需要的入口。
- 安装说明按目标 agent 分开写，并说明复制或保留 `reference/` 的必要性。
- 跨 agent 支持必须区分“直接安装 skill”与“改写为目标工具规则”。不要把不支持 `SKILL.md` 的工具写成可直接安装。
- 不把内部参考项目列表放进公开 README；只保留读者下一步确实需要的链接。

## Agent 支持矩阵

当 skill 仓库 README 需要说明多个 agent 的接入方式时，优先使用支持矩阵，而不是把所有命令堆在 “Other Agents” 小节。

每一行支持结论都必须来自目标 Agent 的官方文档或官方仓库说明。不要根据社区文章、旧经验、工具名称相似性或“应该兼容”来判断是否支持；如果官方文档没有确认，就写成“需要改写”或“待官方确认”。

矩阵应包含：

| 列 | 写法 |
|----|------|
| 图标 | 使用 16 到 20 像素品牌图标、favicon 或明确文本 fallback；图标要有 `alt` |
| Agent | 写清工具名，例如 Codex、Hermes Agent、Claude Code、Gemini CLI、Cursor、GitHub Copilot |
| 支持方式 | 写“直接安装 skill 文件夹”“直接安装 SKILL.md URL”“需要改写为 Project Rules”等 |
| 如何接入 | 写下一步动作，不写空泛的“参考文档” |

分组规则：

- **直接安装**：目标工具能读取 `SKILL.md`、Git skill 仓库或包含 `SKILL.md` 的 skill 文件夹。安装时要保留 `reference/`、`scripts/`、`assets/` 等支持资源。
- **需要改写**：目标工具没有原生 skill 目录，或不能按本仓库结构渐进读取引用文件。把 `SKILL.md` 的路由规则改写进它的原生入口，例如 `.cursor/rules/*.mdc`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md` 或通用 `AGENTS.md`。
- README 声称跨 agent 支持时，必须至少给一个直接安装示例和一个改写导入示例。
- 单文件 URL 安装只适合 `SKILL.md` 自包含或目标工具能继续读取 sidecar 资源的场景；如果 skill 依赖 `reference/`，要提供完整文件夹安装路径作为 fallback。
- 每个示例命令必须与官方文档中的命令入口一致。例如有些工具的本地链接命令只在交互会话里可用，不应写成终端命令。

示例矩阵：

```markdown
| Agent | 支持方式 | 如何接入 |
|-------|----------|----------|
| Hermes Agent | 直接安装 `SKILL.md` URL 或 skill 文件夹 | `hermes skills install <raw-skill-url> --name <skill-name>`；需要引用文件时安装完整文件夹 |
| Gemini CLI / Antigravity CLI | 需按当前官方文档确认 | Gemini CLI 当前支持 Agent Skills，但可用范围正在迁移；发布前确认应使用 Gemini CLI 还是 Antigravity CLI |
| Cursor | 需要改写为 Project Rules | 把入口规则写入 `.cursor/rules/<skill-name>.mdc`，并复制需要的 `reference/` |
```

## 中英双语

双语 README 可用两种组织方式：

| 方式 | 适用场景 | 写法 |
|------|----------|------|
| 多文件链接 | 默认选择；公开 README、内容超过一个屏幕、包含 Quick Start/表格/图表 | `README.md` + `README.en.md`，顶部互链 |
| 单文件锚点 | 很短的说明页或临时草稿 | 顶部 `中文 · English`，两个语言段落结构一致 |

规则：

- 语言切换放在标题区附近。
- 两种语言的 Quick Start、链接和文件定位必须同步。
- 不要一边有完整文档，另一边只有摘要。
- 不要用机器翻译腔补长篇解释；宁可简短但准确。

## 双语文件策略

公开 README 默认不要写成“上半中文、下半英文”的长单文件。这样会让首屏变重、读者滚动成本变高，也容易在后续维护时出现两种语言内容 drift。

推荐做法：

- `README.md` 放主语言。中文项目用中文，国际项目通常用英文。
- `README.en.md` 或 `README.zh-CN.md` 放另一种语言。
- 两个文件顶部互链，例如中文页写 `中文 · English -> README.en.md`，英文页写 `README.md <- 中文 · English`。
- 两个文件保持相同章节顺序、安装命令、场景表和许可证链接。
- 只有极短 README 或一次性说明页，才允许用单文件锚点双语。

## 徽章规则

徽章必须回答真实问题，并链接到证据页。先选择徽章意图，再生成 URL；不要看到可用徽章就堆到首屏。

| 类别 | 示例 | 证据页 |
|------|------|--------|
| 格式/载体 | `format-SKILL.md`、`template`、`CLI` | 核心入口文件或文档 |
| 覆盖范围 | `18 scenarios`、`docs` | 索引或场景列表 |
| 质量状态 | CI、coverage、checks | GitHub Actions 或覆盖率页面 |
| 版本/发布 | release、npm、Docker tag | Releases 或包管理页 |
| 许可 | MIT、Apache-2.0 | LICENSE |
| 社区入口 | discussions、issues、docs | Discussions、Issues、文档站 |

默认 3 到 6 个徽章；首屏最多保留读者决策需要的入口。徽章很多时，按状态、发布、文档、社区分组放到后文，不要把 README 顶部变成贴纸墙。

动态徽章只在数据源真实存在时使用，例如 release、包版本、workflow、coverage、downloads。静态徽章适合表达项目载体、场景数、文档入口或 license，但也必须链接到对应文件或页面。

视觉规则：

- 同一个 README 内保持一致的 badge 样式、label 大小写和颜色强度。
- 每个 badge 都写 `alt`，可点击时链接到证据页，而不是只展示图片。
- 不默认添加访问量、Star History、GitHub stats、贡献图、profile 卡片或动图素材；这些更适合个人主页或营销型 README，只有项目读者真的需要时才使用。
- Logo 或主图标需要兼容浅色/深色 GitHub 主题时，可使用 `#gh-light-mode-only` 和 `#gh-dark-mode-only` 分别提供图片。

`pudding0503/github-badge-collection` 可作为徽章、卡片和 GitHub Markdown 视觉素材的发现入口；使用其中任何具体素材、图片或大段示例时，应保留来源链接，并重新核验服务是否仍可用。

## Emoji 和视觉组件

README 默认不加 emoji。只有在项目风格、用户要求或现有 README 已经使用 emoji 时才加入，并保持少量、稳定、语义明确。

推荐规则：

- 文档型、库、基础设施、企业工具：默认不用 emoji，或只在小节标题中极少量使用。
- 社区项目、个人工具、学习型项目、产品型首页：可询问是否使用少量 emoji 增强导航。
- 不在每个标题前机械加 emoji；不要用 emoji 替代准确标题。
- 不使用动图、贡献图、统计卡片、profile 卡片来填充首屏。
- 截图、logo、架构图必须来自仓库、用户提供素材或明确授权的外部来源；没有素材时写 `TODO: add screenshot`，不要编造图片链接。

如果用户要求可选方案，可以给两个 README 风格方向：

| 方向 | 适用 |
|------|------|
| 文档型 | 克制标题、少徽章、无 emoji、强调安装和 API |
| 社区型 | 少量 emoji、徽章分组、截图或 Star History 作为辅助 |

## Star History

Star History 默认不加入 README。它适合展示成熟开源项目的长期采用趋势，不适合新项目、私有测试仓库、低 star 仓库、内部工具或严肃的 API 文档首屏。

使用前先确认：

- 仓库是公开 GitHub 仓库。
- 用户确实想展示增长趋势，而不是只需要当前 star 数。
- 图表不会挤占 Quick Start、安装方式和核心说明。
- 目标 README 已经有 Star History 时，优先更新现有图表，不新增重复区块。

更新方式：

1. 读取现有 README，搜索 `star-history.com`、`api.star-history.com` 或 `Star History`。
2. 如果只是仓库迁移或 owner/repo 变化，替换 URL 中的 `owner/repo`，并保留原有位置和标题风格。
3. 如果原 README 没有 Star History，先询问用户是否添加；默认不添加。
4. 生成图表时优先使用 Star History 官方导出的 README 片段；不要手写未经验证的复杂 `<picture>`。
5. 不需要用户手动打开网页才能更新已有链接；只有当需要官方导出深浅色 `<picture>`、多仓库比较、log scale、timeline mode 或访问 token 绕过速率限制时，才让用户在浏览器里导出片段或提供设置。

常见占位写法：

```markdown
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=owner/repo&type=Date)](https://star-history.com/#owner/repo&Date)
```

如果使用 Star History，应链接到 Star History 页面，而不是只嵌图片。

## 安装和快速开始

Quick Start 必须可执行或明确说明需要替换什么。

推荐写法：

```markdown
# In a local checkout of this repository
mkdir -p "$HOME/.agents/skills"
ln -sfn "$PWD" "$HOME/.agents/skills/<skill-name>"
```

如果必须使用占位符，先说明：

```markdown
# Replace REPO_URL with this repository or your fork.
REPO_URL="<your repository URL>"
git clone "$REPO_URL" project-name
```

不要把含 `<owner>`、`<repo>` 的命令直接放在“复制即可运行”的位置。

当项目是用户临时描述的假想项目，或仓库没有真实发布渠道时：

- Quick Start 优先展示本地运行、源码构建或最小用法。
- 安装章节写成 `TODO: add install command after first release`，或明确“替换为你的发布 URL”。
- 不要使用 `example.com`、不存在的 GitHub release、未验证的 Homebrew formula、未验证的 npm 包名来制造完整感。

## 不应出现在公开 README

- 内部参考项目清单或过程计划。
- 维护规则全文。
- 内部验证报告全文或每个本地验证入口的重复链接。
- 与项目类型不符的能力宣称，例如把 skill 写成 GitHub App、SaaS、CLI 或生成器。
- 无证据的“production ready”“best practice”“supports all platforms”等宣传语。
- 为了凑完整度而列出每个目录、每个历史草案或每个本地样例。

## Checklist

- [ ] 首屏有项目名、一句话定位和语言切换（如需要双语）。
- [ ] 顶部视觉顺序是标题优先；logo 或主图标在标题下方，尺寸适中。
- [ ] 超过长文阈值时已先收敛交付方式、风格和视觉组件，或已说明默认取舍。
- [ ] 长双语 README 使用独立语言文件，没有把完整中文和完整英文堆在同一个文件里。
- [ ] Quick Start 可复制，或占位符已明确解释。
- [ ] 已先确认交付方式；默认先给草稿，不直接上传远端仓库。
- [ ] README 没有暴露内部参考项目列表、维护规则或内部验证报告正文。
- [ ] 徽章都能链接到真实证据。
- [ ] Emoji、截图、Star History、贡献图等视觉组件有明确用途；默认不把它们作为填充内容。
- [ ] 跨 agent 安装说明已区分直接安装和改写导入，并有图标、支持方式和具体步骤。
- [ ] Agent、平台、API 或安装支持结论已查官方文档，示例命令没有把交互命令误写成终端命令。
- [ ] 文件定位只列用户真正需要的入口。
- [ ] 对 skill 项目，只列出读者真正需要的 `SKILL.md` 和 `reference/` 入口。
- [ ] 中英文结构和命令一致。
- [ ] License 链接存在。

## 参考链接

| 类型 | 链接 |
|------|------|
| GitHub README 指南 | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes |
| GitHub Markdown 基础语法 | https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax |
| shields.io | https://shields.io |
| Star History 使用说明 | https://www.star-history.com/blog/how-to-use-github-star-history |
| GitHub Badge Collection | https://github.com/pudding0503/github-badge-collection |
| VS Code README | https://github.com/microsoft/vscode/blob/main/README.md |
