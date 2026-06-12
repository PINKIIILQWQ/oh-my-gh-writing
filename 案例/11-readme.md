# README — 经典案例

---

## 精细版（经典高星 README，含完整内容）

### 案例 1：ohmyzsh/ohmyzsh (188k⭐)

**仓库：** https://github.com/ohmyzsh/ohmyzsh
**完整内容：** https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/README.md

Oh My Zsh 的 README 以强烈的个性化和高信息密度著称：

```
# Oh My Zsh

Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.

Sounds boring. Let's try again.

**Oh My Zsh will not make you a 10x developer...but you may feel like one.**

Once installed, your terminal shell will become the talk of the town _or your money back!_
Strangers will come up to you in cafés and ask you, _"that is amazing! are you some sort of genius?"_

Finally, you'll begin to get the sort of attention that you have always felt you deserved.
...or maybe you'll use the time that you're saving to start flossing more often. 😬
```

**结构分析：**
- 顶部：幽默两段式标题（正经 → 调侃）
- 徽章栏：CI + OpenSSF Best Practices
- OS 兼容性表格（Android ✅, FreeBSD ✅, LCARS 🛸, Linux ✅, macOS ✅, OS/2 Warp ❌, Windows WSL2 ✅）
- 前提条件（Zsh v4.3.9+, curl/wget, git v2.4.11+）
- 安装指南（多方式表格：curl/wget/fish/git）
- 升级方法
- 卸载方式
- Docker / Manual / 社区资源

**关键特点：** 人格化开头创造品牌差异、高密度表格减少滚动、趣味元素（🛸）降低严肃感。

---

### 案例 2：nvm-sh/nvm (94k⭐)

**仓库：** https://github.com/nvm-sh/nvm
**完整内容：** https://raw.githubusercontent.com/nvm-sh/nvm/master/README.md

```markdown
# Node Version Manager [![Tests]][3] [![nvm version]][4] [![CII Best Practices]][5]

## Table of Contents
- [Intro](#intro)
- [About](#about)
- [Installing and Updating](#installing-and-updating)
  - [Install & Update Script](#install--update-script)
  - [Verify Installation](#verify-installation)
  - [Important Notes](#important-notes)
  - [Git Install](#git-install)
  - [Manual Install](#manual-install)
  - [Manual Upgrade](#manual-upgrade)
- [Usage](#usage)
  - [Long-term Support](#long-term-support)
  - [Migrating Global Packages While Installing](#migrating-global-packages-while-installing)
  - [Offline Install](#offline-install)
  - [Default Global Packages From File While Installing](#default-global-packages-from-file-while-installing)
  - [io.js](#iojs)
  - [System Version of Node](#system-version-of-node)
  - [Listing Versions](#listing-versions)
  - [Setting Custom Colors](#setting-custom-colors)
  - [Restoring PATH](#restoring-path)
  - [Set default node version](#set-default-node-version)
  - [Use a mirror of node binaries](#use-a-mirror-of-node-binaries)
  - [.nvmrc](#nvmrc)
  - [Deeper Shell Integration](#deeper-shell-integration)
- [Running Tests](#running-tests)
- [Environment variables](#environment-variables)
- [Bash Completion](#bash-completion)
- [Compatibility Issues](#compatibility-issues)
- [Installing nvm on Alpine Linux](#installing-nvm-on-alpine-linux)
- [Uninstalling / Removal](#uninstalling--removal)
- [Docker For Development Environment](#docker-for-development-environment)
- [Problems](#problems)
- [macOS Troubleshooting](#macos-troubleshooting)
- [WSL Troubleshooting](#wsl-troubleshooting)
- [Maintainers](#maintainers)
```

**结构分析：** 一个文件 = 首页 + 完整用户手册。16 节使用指南覆盖所有使用场景。完整目录减少滚动成本。

---

### 案例 3：jlevy/the-art-of-command-line (160k⭐)

**仓库：** https://github.com/jlevy/the-art-of-command-line
**完整内容：** https://raw.githubusercontent.com/jlevy/the-art-of-command-line/master/README.md

```markdown
# The Art of Command Line

- [Meta](#meta)
- [Basics](#basics)
- [Everyday use](#everyday-use)
- [Processing files and data](#processing-files-and-data)
- [System debugging](#system-debugging)
- [One-liners](#one-liners)
- [Obscure but useful](#obscure-but-useful)
- [macOS only](#macos-only)
- [Windows only](#windows-only)
- [More resources](#more-resources)

Fluency on the command line is a skill often neglected or considered arcane,
but it improves your flexibility and productivity as an engineer in both obvious
and subtle ways. This is a selection of notes and tips on using the command-line
that we've found useful when working on Linux. This work is the result of
[many authors and translators](AUTHORS.md).
```

**特点：** 知识集合类 README 的典范。15 个知识点章节 + 多语言支持。

---

## 普通版（规范 README 示例）

### 案例 4：nektos/act (70k⭐)

**仓库：** https://github.com/nektos/act
**完整内容：** https://raw.githubusercontent.com/nektos/act/master/README.md

```markdown
# Overview [![push]][actions] [![Go Report Card]][goreport]

> "Think globally, `act` locally"

Run your [GitHub Actions](https://developer.github.com/actions/) locally! Why?

- **Fast Feedback** - Rather than having to commit/push every time you want
  to test out the changes you are making to your `.github/workflows/` files,
  you can use `act` to run the actions locally.
- **Local Task Runner** - Use the GitHub Actions defined in your
  `.github/workflows/` to replace your `Makefile`!
```

**结构：** 一句话定位 → How It Works → 文档链接 → Support → Contributing → 从源码构建。

### 案例 5：hasura/graphql-engine (31k⭐)

**仓库：** https://github.com/hasura/graphql-engine
**完整内容：** https://raw.githubusercontent.com/hasura/graphql-engine/master/README.md

```markdown
# Hasura GraphQL Engine

The Hasura engine supercharges building modern applications by providing access
to data via a single, composable, secure API endpoint.

## Hasura V3
## Hasura V2
## Cloning repository
## Support & Troubleshooting
## Code of Conduct
## Security
## Contributing
## Licenses
```

### 案例 6：dapr/dapr (28k⭐)

**仓库：** https://github.com/dapr/dapr
**完整内容：** https://raw.githubusercontent.com/dapr/dapr/master/README.md

```markdown
# Dapr - APIs for Building Secure and Reliable Microservices

Dapr is a set of integrated APIs with built-in best practices and patterns
to build distributed applications.

We are a Cloud Native Computing Foundation (CNCF) graduated project.

## Goals
## How it works
## Why Dapr?
## Features
- Event-driven Pub-Sub system
- Input and output bindings
- State management
- Service-to-service discovery
- Virtual actors
- Secret management
- Observability support
```

---

> 收集日期：2026-06-12
