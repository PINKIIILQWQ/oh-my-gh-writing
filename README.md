<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-场景索引)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** 是一套为 AI Agent 设计的 GitHub 写作规范系统。它不是一个 README 生成器或独立应用，而是一个可移植的 skill 包——Agent 加载后能按场景自动匹配 Issue、PR、Review、Commit、README、CHANGELOG、RFC 等 18 种 GitHub 文书的写作规范，保持输出质量一致、事实有边界、格式可直接提交。

---

## 场景索引

| # | 类别 | 场景 | 对应标准 |
|---|------|------|----------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` 等 |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` 等 |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` 等 |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` 等 |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` 等 |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` 等 |

完整路由规则见 [`SKILL.md`](SKILL.md)。

---

## 安装

### Claude Code（直接加载）

```bash
# 克隆仓库
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

然后在 Claude Code 中使用 `/oh-my-gh-writing` 即可调用。

### 其他 AI Agent

| Agent | 支持等级 | 操作 |
|-------|----------|------|
| Cline / Roo Code | 适配导入 | 将 `SKILL.md` 内容复制到项目自定义指令中，按需加载对应 `reference/*.md` |

> 本 skill 为 Claude Code 原生设计，其他 agent 需根据其规则系统做适配。

---

## 快速开始

```text
/oh-my-gh-writing 帮我写一个 Bug Report
/oh-my-gh-writing 为这次修改写一个 PR 描述
/oh-my-gh-writing 审查这个 PR 的变更
/oh-my-gh-writing 写一个 CHANGELOG 条目
```

Agent 会自动识别场景，加载对应 `reference/*.md` 规范，输出可直接提交到 GitHub 的 artifact。

---

## 核心原则

- **Evidence Boundaries** — 版本号、PR 编号、测试结果、安装命令等必须有来源，无来源则标 `TODO`
- **Precise Routing** — 按用户意图路由到正确场景，Feature Request 不会写成已实现的 PR
- **Output Cleanliness** — 产物可直接粘贴到 GitHub，无对话前言、无外层代码块、无测试元数据
- **One Artifact, One Job** — 不把多个 Issue 或 Release Note 混在同一份输出里
- **Usable First** — 缺信息时先写合理草稿标 TODO，不阻塞

---

## 项目结构

```
oh-my-gh-writing/
├── SKILL.md                    # Agent 运行时路由器和共享规则
├── INDEX.md                    # 仓库导航索引
├── reference/
│   ├── bug-report.md           # Bug Report 标准
│   ├── feature-request.md      # Feature Request 标准
│   ├── enhancement.md          # Enhancement 标准
│   ├── discussion.md           # Discussion 标准
│   ├── feature-pr.md           # Feature PR 标准
│   ├── bug-fix-pr.md           # Bug Fix PR 标准
│   ├── refactor-pr.md          # Refactor PR 标准
│   ├── documentation-pr.md     # Documentation PR 标准
│   ├── code-review.md          # Code Review 标准
│   ├── standard-commit.md      # Commit 信息标准
│   ├── readme.md               # README 写作标准
│   ├── contributing.md         # CONTRIBUTING 写作标准
│   ├── changelog.md            # CHANGELOG 标准
│   ├── release-notes.md        # Release Notes 标准
│   ├── migration-guide.md      # Migration Guide 标准
│   ├── rfc.md                  # RFC 标准
│   ├── issue-form-yaml.md      # Issue Form YAML 标准
│   ├── pr-template.md          # PR Template 标准
│   ├── weapons.md              # GitHub Markdown 工具（Badge / Mermaid / Alert 等）
│   ├── emoji-guide.md          # Emoji 使用指引
│   ├── output-validation.md    # 输出验收清单
│   └── source-catalog.md       # 参考来源目录
├── CONTRIBUTING.md             # 贡献指南
├── assets/                     # 项目展示资源
└── LICENSE                     # MIT
```

---

## 贡献

欢迎提交 PR 改进场景规则、参考来源或输出验收标准。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 许可

[MIT](LICENSE)
