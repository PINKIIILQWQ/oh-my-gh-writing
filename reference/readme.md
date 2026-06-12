# README — 项目首页标准

## 目录

- [适用场景](#适用场景)
- [写前检查](#写前检查)
- [核心原则](#核心原则)
- [完整版结构](#完整版结构)
- [普通版结构](#普通版结构)
- [Skill 仓库规则](#skill-仓库规则)
- [中英双语](#中英双语)
- [徽章规则](#徽章规则)
- [安装和快速开始](#安装和快速开始)
- [不应出现在公开 README](#不应出现在公开-readme)
- [Checklist](#checklist)
- [参考链接](#参考链接)

## 适用场景

项目首页文档，面向第一次打开仓库的人。README 应回答三个问题：这是什么、如何开始、下一步去哪里。它不是完整索引、设计过程记录、测试报告或参考项目分析。

## 写前检查

写 README 前先快速审视仓库，不要直接套模板：

1. 读取现有 README、LICENSE、入口配置文件和顶层目录。
2. 判断项目类型：库、CLI、应用、文档站、模板、agent skill、GitHub 配置仓库等。
3. 找出真正的用户入口：安装命令、最小示例、主文档、规则入口或模板入口。
4. 区分公开用户材料和维护材料。内部设计、测试记录、采集计划默认不放进公开首页。
5. 保留已有风格：语言、标题层级、徽章风格、链接格式和命令写法。

除非缺少无法推断的关键信息，不要先问一串问题。先给可用草稿，并把不确定项标为 `TODO` 或“替换为你的仓库 URL”。

## 核心原则

- **入口清晰**：首屏必须出现项目名、一句话定位和最短开始路径。
- **分层披露**：README 放最短路径，INDEX 或 docs 放全量导航，reference 放规则细节，test 放验证材料。
- **证据驱动**：不要虚构 CI、版本、下载量、兼容平台、截图、性能或 Star History。
- **命令可复制**：能直接运行的命令不要含未解释的 `<owner>`、`<repo>`、`your-token` 等占位符；需要占位时先说明如何替换。
- **少即是准**：不要因为仓库里存在某个目录就把它放进 README。只链接读者下一步确实需要的入口。
- **引用内收**：链接是补充，不应代替关键信息。关键行为、安装方式和限制必须写在正文。
- **双语同步**：要求双语时，两种语言的结构、链接和命令保持一致。

## 完整版结构

适合公开项目、复杂项目、正式发布项目或用户要求“完整版”的场景。

1. 标题区：logo 或项目名 + 一句话定位。
2. 语言切换：单文件锚点或多文件链接。
3. 徽章栏：3 到 6 个可验证徽章，必要时分组。
4. 简介：2 到 4 句说明目标读者、解决的问题和非目标。
5. Quick Start：安装或接入方式 + 最小可用示例 + 预期结果。
6. 功能或场景总览：只列核心能力，避免把所有内部文件逐项罗列。
7. 工作方式或架构概览：仅当它帮助用户理解如何使用项目时添加。
8. 文件定位：只列核心入口文件；内部材料放到 INDEX 或 docs 中。
9. 下一步链接：文档、示例、贡献指南、问题反馈，按项目实际存在情况添加。
10. License：链接到许可证文件。

## 普通版结构

适合中小型项目、内部工具、模板仓库或信息不足时的默认输出。

1. 标题 + 一句话定位。
2. Quick Start。
3. 核心用法或场景。
4. 关键文件或文档入口。
5. License。

普通版不默认添加目录、Star History、贡献者图表、赞助商、长篇 FAQ 或完整目录树。

## Skill 仓库规则

当 README 所属项目是 agent skill 时，必须避免把它写成普通软件产品：

- 明确说明它是可被 agent 加载的写作/工作流规则，不是独立应用、GitHub App、CI 工具或 README 生成器。
- 首要入口是 `SKILL.md`；场景细则在 `reference/`。
- `DOCS/` 是设计过程或维护材料，`test/` 是验证材料。公开 README 不默认强展示这两个目录。
- 文件定位只放 `SKILL.md`、`INDEX.md`、`reference/`、`LICENSE` 等用户确实需要的入口。
- 安装说明按目标 agent 分开写，并说明复制 `reference/` 的必要性。
- 不把参考项目列表放进公开 README；参考项目可留在 `reference/*.md` 或内部分析文档里。

## 中英双语

双语 README 可用两种模式：

| 模式 | 适用场景 | 写法 |
|------|----------|------|
| 单文件锚点 | 内容较短、希望维护一个文件 | 顶部 `中文 · English`，两个语言段落结构一致 |
| 多文件链接 | 内容较长、社区以英文为主 | `README.md` + `README.zh-CN.md` 或相反 |

规则：

- 语言切换放在标题区附近。
- 两种语言的 Quick Start、链接和文件定位必须同步。
- 不要一边有完整文档，另一边只有摘要。
- 不要用机器翻译腔补长篇解释；宁可简短但准确。

## 徽章规则

徽章必须回答真实问题，并链接到证据页。

| 类别 | 示例 | 证据页 |
|------|------|--------|
| 格式/载体 | `format-SKILL.md`、`template`、`CLI` | 核心入口文件或文档 |
| 覆盖范围 | `18 scenarios`、`docs` | 索引或场景列表 |
| 质量状态 | CI、coverage、tests | GitHub Actions 或测试报告 |
| 版本/发布 | release、npm、Docker tag | Releases 或包管理页 |
| 许可 | MIT、Apache-2.0 | LICENSE |

默认 3 到 6 个徽章。没有 CI 就不要放 CI；没有发布版本就不要放 release；没有真实统计价值时不要放 Star History。

## 安装和快速开始

Quick Start 必须可执行或明确说明需要替换什么。

推荐写法：

```markdown
# In a local checkout of this repository
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD" "${CODEX_HOME:-$HOME/.codex}/skills/<skill-name>"
```

如果必须使用占位符，先说明：

```markdown
# Replace <repo-url> with this repository or your fork.
git clone <repo-url> <project-name>
```

不要把含 `<owner>`、`<repo>` 的命令直接放在“复制即可运行”的位置。

## 不应出现在公开 README

- 内部参考项目清单或采集计划。
- 维护规则全文。
- 测试报告全文或每个测试入口的重复链接。
- 与项目类型不符的能力宣称，例如把 skill 写成 GitHub App、SaaS、CLI 或生成器。
- 无证据的“production ready”“best practice”“supports all platforms”等宣传语。
- 为了凑完整度而列出每个目录、每个历史草案或每个测试样例。

## Checklist

- [ ] 首屏有项目名、一句话定位和语言切换（如需要双语）。
- [ ] Quick Start 可复制，或占位符已明确解释。
- [ ] README 没有暴露内部参考项目列表、维护规则或测试报告正文。
- [ ] 徽章都能链接到真实证据。
- [ ] 文件定位只列用户真正需要的入口。
- [ ] 对 skill 项目，清楚区分 `SKILL.md`、`reference/`、`DOCS/` 和 `test/`。
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
