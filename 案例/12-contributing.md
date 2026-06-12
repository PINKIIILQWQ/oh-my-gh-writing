# CONTRIBUTING — 经典案例

---


> 格式：**Markdown**（GitHub CONTRIBUTING）

## 精细版（完整贡献指南，含真实内容）

### 案例 1：psf/black (39k⭐)

**仓库：** https://github.com/psf/black
**完整内容：** https://raw.githubusercontent.com/psf/black/main/CONTRIBUTING.md

```markdown
# Contributing to _Black_

Welcome future contributor! We're happy to see you willing to make the project better.

If you aren't familiar with _Black_, or are looking for documentation on something
specific, the [user documentation](https://black.readthedocs.io/en/latest/) is the
best place to look.

For getting started on contributing, please read the [contributing documentation](
https://black.readthedocs.org/en/latest/contributing/) for all you need to know.

Thank you, and we look forward to your contributions!
```

**特点：** 极简但友好——将详细内容放在 ReadTheDocs 上，CONTRIBUTING.md 本身只提供入口链接。这是"仓库轻+文档站重"模式的典型。

---

### 案例 2：redis/redis (68k⭐)

**仓库：** https://github.com/redis/redis
**完整内容：** https://raw.githubusercontent.com/redis/redis/unstable/CONTRIBUTING.md

```markdown
By contributing code to the Redis project in any form you agree to the Redis
Software Grant and Contributor License Agreement attached below.

# REDIS SOFTWARE GRANT AND CONTRIBUTOR LICENSE AGREEMENT

To specify the intellectual property license granted in any Contribution,
Redis Ltd. requires a Software Grant and Contributor License Agreement.

By making any Contribution, You accept and agree to the following terms:

1. **Definitions**
    1.1. "**You**" (or "**Your**") means the copyright owner or legal entity
         authorized by the copyright owner.
    1.2. "**Contribution**" means the code, documentation, or any original work.

2. **Grant of Copyright License**. You grant to Redis and to recipients a
   perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable
   copyright license.

3. **Grant of Patent License**. You grant a perpetual, worldwide, non-exclusive,
   no-charge, royalty-free, irrevocable patent license.

4. **Representations and Warranties**. You represent that You are legally
   entitled to grant the above licenses.

5. **Disclaimer**. You provide Your Contribution on an "AS IS" BASIS.

# IMPORTANT: HOW TO USE REDIS GITHUB ISSUES

GitHub issues SHOULD ONLY BE USED to report bugs and for DETAILED feature
requests. Everything else should be asked on Discord.

PLEASE DO NOT POST GENERAL QUESTIONS that are not about bugs or suspected
bugs in the GitHub issues system.

# How to provide a patch for a new feature
1. If it is a major feature, start by posting in the mailing list and
   creating an issue at Github with the description.
2. If in step 1 you get an acknowledgment from the project leaders, use
   the following procedure to submit a patch:
   a. Fork the repository
   b. Create a topic branch
   c. Make changes and commit
   d. Push to your fork
   e. Open a pull request
```

**特点：** 将完整 CLA 法律文档嵌入 CONTRIBUTING.md + 明确的 issue 使用规范 + Patch 提交步骤。

---

### 案例 3：pytorch/pytorch (86k⭐)

**仓库：** https://github.com/pytorch/pytorch
**完整内容：** https://raw.githubusercontent.com/pytorch/pytorch/main/CONTRIBUTING.md

```
Thank you for your interest in contributing to PyTorch!

If you're a new contributor, please first take a read through our
Contributing Guide, specifically the Submitting a Change section.

The rest of this document covers some of the more technical aspects.

[Table of Contents]
- Developing PyTorch
  - Tips and Debugging
- Nightly Checkout & Pull
- Codebase structure
- AI-Assisted Development
- Spin (Building, Linting, Regenerating)
- Unit testing
  - Python Unit Testing
  - Better local unit tests with pytest
  - Local linting
  - C++ Unit Testing
  - Run Specific CI Jobs
- Merging your Change
- Writing documentation
- Profiling with py-spy
- Managing multiple build trees
- C++ development tips
- CUDA development tips
- Windows development tips
- Pre-commit tidy/linting hook
- Building PyTorch with ASAN
- CI failure tips
```

**特点：** 最系统的贡献指南之一。含 AI-Assisted Development 章节 + `spin` 工具封装构建/测试/lint + 平台相关技巧（CUDA/Windows/ASAN）。

---

## 简洁写法（简洁贡献指南）

### 案例 4：apache/echarts (62k⭐)

**仓库：** https://github.com/apache/echarts
**完整内容：** https://raw.githubusercontent.com/apache/echarts/master/CONTRIBUTING.md

```markdown
# Contributing

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

## What can you do for the ECharts community?
- Help others with the issues
- Make pull requests to fix bugs or implement new features
- Improve or translate the documents
- Discuss in the [mailing list](https://echarts.apache.org/en/maillist.html)

## Issues
We have already prepared issue templates for bug reports and feature requests.

## Release Milestone Discussion
We will start the discussion about bugs and features of each release in
the mailing list.

## Pull Requests
Wiki: How to make a pull request
```

### 案例 5：jupyter/notebook (13k⭐)

**仓库：** https://github.com/jupyter/notebook
**完整内容：** https://raw.githubusercontent.com/jupyter/notebook/main/CONTRIBUTING.md

```markdown
# Contributing to Jupyter Notebook

## Setting up a development environment
# create a new environment
mamba create -n notebook -c conda-forge python nodejs -y
mamba activate notebook
pip install -e ".[dev,docs,test]"
jlpm
jlpm build

## Running Tests
jlpm run build:test
jlpm run test

## Code Styling
All non-python source code is formatted using prettier and Python
source code is formatted using black.

## Documentation
```

### 案例 6：python/mypy (19k⭐)

**仓库：** https://github.com/python/mypy
**完整内容：** https://raw.githubusercontent.com/python/mypy/master/CONTRIBUTING.md

包含：
- Code of Conduct（Python Community Code of Conduct）
- Fork → Clone → Virtual env → Install → Test 完整 4 步法
- LLM-assisted contributions 政策声明（持中立态度，但建议新手不使用）
- first time contributors 指引 → good first issue

---

### 附加参考

**godotengine/godot (95k⭐)** — https://github.com/godotengine/godot — C++/GDScript/文档三套贡献标准。
**astropy/astropy (4k⭐)** — https://github.com/astropy/astropy — 含 affiliated package 政策。
**microsoft/playwright (70k⭐)** — https://github.com/microsoft/playwright — 跨浏览器测试框架的贡献指南典范。
**ruby/ruby (22k⭐)** — https://github.com/ruby/ruby — 邮件列表驱动的经典贡献流程。

---

> 收集日期：2026-06-12
