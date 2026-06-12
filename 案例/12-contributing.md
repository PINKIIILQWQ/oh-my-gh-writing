# CONTRIBUTING — 经典案例

---

## 精细版（完整贡献指南）

### 案例 1：psf/black (39k⭐)

**来源：** https://raw.githubusercontent.com/psf/black/main/CONTRIBUTING.md

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

**特点：** 极简但友好——将详细内容放在 ReadTheDocs 上，CONTRIBUTING.md 本身只提供入口连接。这是"CONTRIBUTING.md 轻+文档站重"模式的典型。

---

### 案例 2：redis/redis (68k⭐)

**来源：** https://raw.githubusercontent.com/redis/redis/unstable/CONTRIBUTING.md

Redis 的 CONTRIBUTING.md 聚焦两大核心内容：

**1. 贡献者许可协议（CLA）：** 完整复制了 Redis Software Grant and Contributor License Agreement（含 6 条法律条款：版权许可、专利许可、陈述与保证、免责声明等）。

**2. Issue 使用规范：** 明确 GitHub Issues 只用于 Bug 报告和详细功能请求——其他问题请去 Discord。

**3. Patch 提交流程：** 
- 重大功能先发邮件列表讨论
- 获得项目领导认可后再编码
- Fork → Branch → Commit → PR 标准化流程

**特点：** 法律文档（CLA）直接嵌入 CONTRIBUTING.md 而非仅链接，减少摩擦。

---

### 案例 3：pytorch/pytorch (86k⭐)

**来源：** https://raw.githubusercontent.com/pytorch/pytorch/main/CONTRIBUTING.md

最系统的贡献指南之一，完整目录：

```
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
- Building with ASAN
- CI failure tips
```

**特点：** 
- 大型项目贡献指南的行业标杆
- 含 AI-Assisted Development 章节（AI 工具使用指南）
- `Spin` 工具封装构建/测试/lint 流程
- 平台相关开发技巧（CUDA / Windows / ASAN）

---

## 普通版（贡献指南）

### 案例 4：apache/echarts (62k⭐)

**来源：** https://raw.githubusercontent.com/apache/echarts/master/CONTRIBUTING.md

```markdown
# Contributing

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

## What can you do for the ECharts community?
- Help others with issues
- Make pull requests
- Improve or translate documents
- Discuss in the mailing list
```

**特点：** Apache 项目风格——多层面贡献可能性（不仅仅是代码），Issue → PR → Debug 流程清晰。

---

### 案例 5：jupyter/notebook (13k⭐)

**来源：** https://raw.githubusercontent.com/jupyter/notebook/main/CONTRIBUTING.md

```markdown
# Contributing to Jupyter Notebook

## Setting up a development environment
## Running Tests
## Code Styling
## Documentation
```

**特点：** Jupyter 标准化格式——开发环境搭建（mamba + jlpm）→ 测试 → 代码风格（prettier + black）→ 文档。

---

### 案例 6：python/mypy (19k⭐)

**来源：** https://raw.githubusercontent.com/python/mypy/master/CONTRIBUTING.md

```markdown
# Contributing to Mypy

## Code of Conduct
## Getting started with development
  - Fork → Clone → Virtual env → Install → Test
## LLM-assisted contributions
## First time contributors
```

**特点：** LLM 辅助贡献政策声明（对 LLM 持中立态度，但建议新手不使用）+ 详细本地开发 4 步法。

---

> 收集日期：2026-06-12
