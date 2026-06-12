# README — 经典案例

---

## 精细版（经典高星 README）

### 案例 1：ohmyzsh/ohmyzsh (188k⭐)

**来源：** https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/README.md

```markdown
# Oh My Zsh

Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.

Sounds boring. Let's try again.

**Oh My Zsh will not make you a 10x developer...but you may feel like one.**

Once installed, your terminal shell will become the talk of the town _or your money back!_
Strangers will come up to you in cafés and ask you, _"that is amazing! are you some sort of genius?"_

Finally, you'll begin to get the sort of attention that you have always felt you deserved.
```

**结构：**
1. 标题 + 一句话定位（两段风格：正经 vs 幽默）
2. 徽章栏（CI + OpenSSF Best Practices）
3. OS 兼容性表格（Android ✓, LCARS 🛸, OS/2 Warp ❌ — 幽默风格）
4. 前提条件（Zsh, curl/wget, git）
5. 安装指南（多种方式表格：curl/wget/fish/git）
6. 升级方式
7. 卸载方式
8. 项目社区资源

**特点：** 强烈的人格化开头 + 信息密度极高的表格格式 + 趣味道具元素（🛸）。

---

### 案例 2：nvm-sh/nvm (94k⭐)

**来源：** https://raw.githubusercontent.com/nvm-sh/nvm/master/README.md

```markdown
# Node Version Manager
[![Tests](https://github.com/nvm-sh/nvm/actions/workflows/tests-fast.yml/badge.svg)]
[![nvm version](https://img.shields.io/badge/version-v0.40.5-yellow.svg)]
[![CII Best Practices](https://bestpractices.dev/projects/684/badge)]
```

**结构：**
1. 标题 + 3 个徽章
2. 完整目录（含嵌套子目录）
3. Intro + About（项目背景）
4. 安装脚本（Install & Update Script + 校验方式）
5. 使用指南（16 个子节：LTS、离线安装、默认包、io.js、版本列表、颜色设置、nvmrc 等）
6. 运行测试
7. 环境变量
8. Bash 自动补全
9. 兼容性问题
10. 卸载指南
11. Docker 开发环境
12. 排错（macOS / WSL）
13. 维护者列表

**特点：** 最完整的使用文档式 README，一个文件既是首页又是完整用户手册。

---

### 案例 3：jlevy/the-art-of-command-line (160k⭐)

**来源：** https://raw.githubusercontent.com/jlevy/the-art-of-command-line/master/README.md

```markdown
# The Art of Command Line

Fluency on the command line is a skill often neglected or considered arcane,
but it improves your flexibility and productivity as an engineer in both obvious
and subtle ways. This is a selection of notes and tips on using the command-line
that we've found useful when working on Linux.

This work is the result of [many authors and translators](AUTHORS.md).
```

**结构：** 目录导航 → 简介 → 15 个知识点章节（Basics / Everyday use / Processing files / System debugging / One-liners / Obscure / macOS / Windows / More resources）

**特点：** 知识集合类 README 的典范——扁平章节、深度内容、多语言支持（中/英/日/法等）。

---

## 普通版（规范 README）

### 案例 4：nektos/act (70k⭐)

```markdown
# Overview

> "Think globally, `act` locally"

Run your [GitHub Actions](https://developer.github.com/actions/) locally!

**Fast Feedback** - Rather than having to commit/push every time...
**Local Task Runner** - Use GitHub Actions to replace your `Makefile`!
```

**结构：** 一句话定位 → 工作原理 → 用户指南链接 → 支持 → 贡献 → 从源码构建。

---

### 案例 5：hasura/graphql-engine (31k⭐)

```markdown
# Hasura GraphQL Engine

The Hasura engine supercharges building modern applications by providing access
to data via a single, composable, secure API endpoint.
```

**结构：** 品牌标题 → V3/V2 区分 → 克隆说明 → 支持和排错 → 行为准则 → 安全 → 贡献 → License。

**特点：** 产品级 README，版本分支清晰。

---

### 案例 6：dapr/dapr (28k⭐)

```markdown
# Dapr - APIs for Building Secure and Reliable Microservices

Dapr is a set of integrated APIs with built-in best practices and patterns
to build distributed applications. We are a CNCF graduated project.
```

**结构：** 项目定位 → Goals → 工作原理 → 为什么 Dapr → 功能列表 → 后续链接。

**特点：** CNCF 项目的标准化 README 风格，强调治理和社区成熟度。

---

> 收集日期：2026-06-12
