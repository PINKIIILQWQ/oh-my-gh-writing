# 六款专项仓库写法分析

## 概述

对 6 款 GitHub 写作类工具/资料仓库进行格式、排版、写法与设计思路分析。目标：提取可复用的**写作模式与设计哲学**，融入 SKILL.md。

---

## 1. rahuldkjain/github-profile-readme-generator
⭐ 24.1k | <https://github.com/rahuldkjain/github-profile-readme-generator>

### 设计哲学

- **内容与呈现分离**：用户只填表单（内容层），工具自动加 HTML 包装（呈现层）。用户不写 markdown，只做选择题
- **模块化产出**：Profile README 由独立 section 拼接而成（social → skills → stats → support → about），每个 section 可独立开关
- **less is more**：工具说明页明确写道 "too much content, too many images/gifs distracts visitors"——徽章和统计图足够，不要过度堆砌
- **外部服务集成**：不自己算数据，把统计交给 github-readme-stats、streak-stats、trophy 等外部服务，通过图片 URL 传参定制

### 格式特征

- **HTML 包裹**：用 `<p align="center">`、`<h3 align="left">` 控制对齐，用 `<a>` 给图片包链接
- **徽章即入口**：每个 badge 用 `<a href="https://example.com">` 包裹，点击 badge 跳转对应页面（license→LICENSE 文件，stars→stargazers 页面）
- **图标回退链**：skillicons.dev → simpleicons.org → devicon → raw.githubusercontent.com，三层 fallback
- **一行式配置**：badge 颜色、风格、标签文字全由 URL query 参数控制（`?color=green&style=flat`）

### 可提取原则

- **用户只做选择题**：写作工具应优先提供选项而非空白输入框
- **外部数据远程拉取**：动态数据（统计、趋势）通过 URL 嵌入而非本地生成
- **Section 化产出**：写作者应先分解文档的模块结构，再逐一填充
- **Badge 作为导航元素**：徽章不仅是装饰，更是交互入口

---

## 2. The-PR-Agent/pr-agent (原 Codium-ai)
⭐ 11.5k | <https://github.com/The-PR-Agent/pr-agent>

### 设计哲学

- **Schema 即模板**：用 Pydantic 模型定义 PR 描述的字段结构（PRType、FileDescription），迫使 LLM 输出结构化数据后再渲染为 markdown
- **系统提示即规范**：系统提示中明确规定了 markdown 格式规则（代码用反引号、bullet 用 `-`、block scalar 用 `|`），把格式问题前移到生成阶段
- **尊重现有文件风格**：changelog 更新时，要求 "Follow the file's existing format and style conventions like dates, section titles"——不破坏已有格式
- **精简原则**：changelog 输出 "minimal, no more than 3-4 short lines"、"be general, avoid specific details"

### 格式特征

- **YAML → Markdown 管道**：AI 先生成 YAML 结构体，再渲染成 markdown。既确保机器可读，又有好的展示效果
- **语义化文件分类**：每个文件变更打语义标签（bug fix、tests、enhancement、documentation、refactor），便于阅读者快速定位关注的文件
- **变更摘要+标题**：每个文件两个字段：一行标题（5-10 words）+ 1-4 条 bullet points
- **可自定义标签体系**：支持 `enable_custom_labels`，让仓库所有者定义自己的分类

### 可提取原则

- **Schema-first 写作**：定义输出结构体先于写内容。强类型约束保证格式一致
- **语义标签分级**：PR/Issue 文件应标注变更类型，便于快速扫描
- **尊重既有格式**：更新已有文档时，检测并沿用其格式约定
- **LLM 提示包含格式规则**：在 prompt 中就规定好 markdown 语法，不需要后处理修复

---

## 3. kefranabg/readme-md-generator
⭐ 10k+ | <https://github.com/kefranabg/readme-md-generator>

### 设计哲学

- **智能默认值**：读取 package.json（name, version, description, author, license, repository）+ git config 作为默认值。用户只需确认/修改，不必从头填写
- **两种模式**：HTML-rich（带 `<h1 align="center">`、居中徽章栏） vs 纯 markdown（扁平结构）。用户根据平台选择
- **条件渲染**：每个 Section 只在有数据时才出现。没有 tests 就不出现 "Run tests" 章节
- **模板引擎驱动**：用 EJS 模板 + 用户回答数据渲染最终 markdown。生成与数据完全解耦

### 格式特征

- **徽章栏优先级**：npm version > project version > prerequisites > documentation > maintenance > license > twitter
- **固定产出结构**：Banner → Badges → Description → Prerequisites → Install → Usage → Tests → Author → Contributing → License → Footer
- **EJS 条件分支**：`<% if (installCommand) { %>` —— 控制内容的有无
- **自声明 footer**：`_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_`——透明标注工具来源
- **无 HTML 版本降级**：`default-no-html.md` 仅用 markdown 语法（#、-、`code`）实现同样的信息结构

### 可提取原则

- **读取项目元数据作为默认值**：减小重复输入，增加准确度
- **Section 条件显示**：没有就不写，减少无效信息
- **提供 HTML/纯 md 模板选项**：让用户根据发布平台选择渲染风格
- **工具来源标注**：generator 在文档末尾声明生成工具，体现透明和责任

---

## 4. github-changelog-generator/github-changelog-generator
⭐ 7.5k | <https://github.com/github-changelog-generator/github-changelog-generator>

### 设计哲学

- **标签驱动分类**：GitHub issue/PR 的 label 决定 changelog 中的 section 归属。用户通过 label 管理分类，工具自动编排
- **完全自动化**：用户只需管理 git tag 和 label，生成器全自动产出 changelog。"Since you don't have to fill your CHANGELOG.md manually now: just run the script, relax and take a cup of coffee"
- **三层层级结构**：Entry（发版）→ Section（分类）→ Issue/PR Item。层次清晰，可各自独立配置
- **控制反转**：用户通过 GitHub 数据（tags、labels、milestones）间接控制输出，不需要直接编辑 changelog 文件

### 格式特征

- **时间线排序**：按 tag 时间倒序排列，最近在上
- **Section 前缀**：每个分类有 `prefix` 属性，控制 section 标题的文本格式
- **排除标签机制**：`exclude_labels` 标签 → 该 issue/PR 完全不出现在 changelog 中
- **Milestone 分组**：支持按 milestone 归属放入对应的 tag 条目下
- **自声明 credit line**：在 changelog 末尾自动追加生成工具的 credit
- **标签筛选策略**：
  - `add_pr_wo_labels` — 是否包含无标签的 PR
  - `add_issues_wo_labels` — 是否包含无标签的 issue
  - `exclude_labels` — 完全排除某些标签

### 可提取原则

- **Label 即分类策略**：文档分类应和 label 体系一一对应。写作者通过 label 管理内容，工具负责排版
- **排除机制**：部分内容不应出现在特定文档中，应提供标签级排除控制
- **三个层级**：Release → Category → Item。任何结构化文档都可以用这个框架
- **自声明来源**：自动生成的文档应标注来源工具

---

## 5. release-drafter/release-drafter
⭐ 3.9k | <https://github.com/release-drafter/release-drafter>

### 设计哲学

- **模板变量替换**：使用 `$CHANGES`、`$RESOLVED_VERSION`、`$TITLE`、`$AUTHOR`、`$NUMBER` 等模板变量，在运行时替换为实际值。最成熟的模板模式
- **持续累积 vs 一次性生成**：每个 PR merge 时自动更新 release draft，而非发版时才生成。降低发布门槛
- **类别聚合**：定义 categories，每个 category 匹配一组 label。多个 PR 自动聚合到同一 section
- **语义版本自动推断**：通过 label 推断下一个版本号（feature→minor, fix→patch）。减少版本号手动决策

### 格式特征

- **Category 类型体系**：
  - `changelog`（默认）：正常显示
  - `pre-include`：提前包含到前面的 category
  - `pre-exclude`：从前面的 category 中排除
  - `version-resolver`：仅用于版本推断，不显示内容
- **Change template**：每条变更的格式可配置（`- $TITLE @$AUTHOR (#$NUMBER)`）
- **Escapes 安全机制**：`change-title-escapes: '\\<*_&'` —— 防止 PR 标题中特殊字符破坏 markdown
- **Collapse 折叠**：pr 超过一定数量后折叠显示
- **name-template + tag-template**：发布名称和标签名可独立模板化
- **配置继承**：`_extends` 从其他文件/仓库继承配置
- **分类互斥**：`exclusive: true` 让一个 PR 只属于一个类别（避免重复）

### 可提取原则

- **模板变量 > 硬编码**：任何动态值（版本号、日期、贡献者）都应通过模板变量注入，而非硬编码占位符
- **Category 聚合模式**：多个条目 → 按规则分类 → 合并输出。适用于发版笔记、周报、总结
- **特殊值逃逸**：用户输入的内容（PR title、author name）需要逃逸 markdown 特殊字符
- **发版可折叠**：条目数较多时应支持折叠/展开
- **配置继承**：允许一个配置引用另一个，减少重复

---

## 6. pudding0503/github-badge-collection
<https://github.com/pudding0503/github-badge-collection>

### 设计哲学

- **Badge 是信息入口**：徽章不只是装饰，应让读者一眼看到版本、构建、下载、许可、社区、文档等状态
- **分类优先于堆叠**：先按用途分组，再决定展示数量。README 顶部只放最关键的 3-8 个，其余可放到徽章附录或参考链接
- **复制友好**：徽章样式应能直接复制，减少用户理解 URL 参数、颜色、logo、style 的成本
- **展示密度可控**：徽章多时用分组、换行或表格，避免首屏被图标挤满

### 格式特征

- **按用途分类**：status/version/license/download/social/docs/platform 等类别比“看到什么放什么”更稳定
- **静态与动态分离**：静态徽章用于能力声明，动态徽章用于 build、version、downloads、stars 等变化数据
- **可点击徽章**：徽章应包链接，跳转到 release、license、actions、docs、issue、discussion 等真实页面
- **样式统一**：同一个 README 内 style、logo 风格、颜色饱和度应统一，避免像贴纸墙

### 可提取原则

- **Badge 有语义**：每个徽章都必须回答“它帮读者判断什么”
- **Badge 有去处**：能点击的徽章优先链接到对应证据页
- **Badge 有上限**：首屏徽章只保留状态、版本、许可、文档、场景数等关键入口
- **Badge 先分类后生成**：先选类别，再生成 shields URL，避免无意义堆叠

---

## 横向对比

| 维度 | Profile README | PR-Agent | README Generator | Changelog Gen | Release Drafter | Badge Collection |
|------|---------------|----------|-----------------|--------------|-----------------|------------------|
| **输入方式** | 填写表单 | 读取代码 diff | 读取 env + CLI 问答 | 抓取 GitHub API | 监听 webhook | 选择徽章类别 |
| **模板引擎** | 字符串拼接 | Pydantic schema | EJS 模板 | Ruby 字符串插值 | 变量替换 | URL 参数组合 |
| **自定义程度** | 勾选 section | 自定义 label | 自定义模板文件 | 自定义 prefix/section | Category+template 双重可配 | style/logo/color 可配 |
| **输出控制** | 开关 section | YAML 渲染为 md | 有无 HTML 两个版本 | label→section 映射 | 模板变量+类型系统 | 类别分组+展示上限 |
| **自动度** | 半自动（填表单） | 全自动（AI） | 半自动（CLI 问答） | 全自动（定时运行） | 全自动（每 PR 触发） | 手动选择+复制 |
| **格式预防** | 无 | Prompt 内规定 | 模板固定 | 模板固定 | escapes 逃逸 | 统一 style 和分类 |
| **来源标注** | 无 | 无 | 自动 footer | 自动 credit line | 无（用户可配） | 徽章链接到证据页 |

### 通用设计原则（纳入 SKILL.md）

1. **Schema-first** — 先定义文档结构，再填充内容
2. **Section 化产出** — 每部分独立可配，有条件才显示
3. **变量替换 > 硬编码** — 版本号、日期、作者、链接都应模板化
4. **Label 即分类** — GitHub label 直接对应文档分类
5. **两种复杂度选择** — 完整版与精简版，用户按场景选择
6. **逃逸用户输入** — 防止 PR title、issue 引用破坏 markdown
7. **来源透明** — 自动生成的文档声明由什么工具生成
8. **读取元数据作为默认值** — 减少重复输入
9. **Category 聚合** — 多条变更为一类合并展示
10. **条件渲染** — 无数据则不出现对应 section
11. **Badge 语义化** — 徽章先分类、再生成、可点击、数量受控
