# README — 项目首页标准

## 目录

- [适用场景](#适用场景)
- [写前检查](#写前检查)
- [核心原则](#核心原则)
- [标准结构](#标准结构)
- [Skill 仓库规则](#skill-仓库规则)
- [Agent 支持矩阵](#agent-支持矩阵)
- [中英双语](#中英双语)
- [双语文件策略](#双语文件策略)
- [徽章规则](#徽章规则)
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

除非缺少无法推断的关键信息，不要先问一串问题。先给可用草稿，并把不确定项标为 `TODO` 或“替换为你的仓库 URL”。但如果交付方式未明确，必须先确认这一点，再继续写。

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
| Gemini CLI | 直接安装 skill 仓库或本地文件夹 | `gemini skills install <repo-url>`；本地链接在会话内使用 `/skills link <path>` |
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

徽章必须回答真实问题，并链接到证据页。

| 类别 | 示例 | 证据页 |
|------|------|--------|
| 格式/载体 | `format-SKILL.md`、`template`、`CLI` | 核心入口文件或文档 |
| 覆盖范围 | `18 scenarios`、`docs` | 索引或场景列表 |
| 质量状态 | CI、coverage、checks | GitHub Actions 或覆盖率页面 |
| 版本/发布 | release、npm、Docker tag | Releases 或包管理页 |
| 许可 | MIT、Apache-2.0 | LICENSE |

默认 3 到 6 个徽章。没有 CI 就不要放 CI；没有发布版本就不要放 release；没有真实统计价值时不要放 Star History。

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
# Replace <repo-url> with this repository or your fork.
git clone <repo-url> <project-name>
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
- [ ] 长双语 README 使用独立语言文件，没有把完整中文和完整英文堆在同一个文件里。
- [ ] Quick Start 可复制，或占位符已明确解释。
- [ ] 已先确认交付方式；默认先给草稿，不直接上传远端仓库。
- [ ] README 没有暴露内部参考项目列表、维护规则或内部验证报告正文。
- [ ] 徽章都能链接到真实证据。
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
| shields.io | https://shields.io |
| vscode README | https://github.com/microsoft/vscode |
| nextjs README | https://github.com/vercel/next.js |
| tailwindcss README | https://github.com/tailwindlabs/tailwindcss |
| deno README | https://github.com/denoland/deno |
| supabase README | https://github.com/supabase/supabase |
