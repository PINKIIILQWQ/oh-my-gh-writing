<p align="center">
  <img src="https://img.shields.io/badge/8%20categories-18%20scenarios-blue" alt="18 scenarios">
  <img src="https://img.shields.io/badge/22%20reference%20repos-green" alt="reference repos">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="license">
  <img src="https://img.shields.io/badge/Hermes%20Skill-v1-brightgreen" alt="hermes skill">
</p>

<h1 align="center">oh-my-gh-writing</h1>
<p align="center"><em>GitHub 写作规范 —— Issue/PR/Review/Commit/文档/发布/设计/模板，每场景精细+中等 2 级标准</em></p>

---

## 简介

oh-my-gh-writing 是一个 Hermes 技能（SKILL.md），将 GitHub 上 22 个顶级开源项目（vscode、kubernetes、react、golang、linux 等）的写作实践提炼为一套可执行的规范。覆盖 8 大类 18 个使用场景，每个场景提供 **精细版** 和 **中等版** 两种复杂度标准，含仓库写法详解、必填 Checklist 和可选项。

解决了什么问题：
- 团队保持 Issue/PR/Commit 格式统一，无需来回 review 排版
- agent 输出 GitHub 内容时遵循社区实践，减少人工修正
- 新成员快速对齐项目协作规范，降低沟通成本

## 快速开始

```bash
# 1. 克隆仓库
git clone git@github.com:PINKIIILQWQ/oh-my-gh-writing.git

# 2. 加载 skill（Hermes agent）
hermes skill load oh-my-gh-writing

# 3. 直接使用
hermes run "写一份 Bug Report：Chrome 下首次加载白屏 3 秒"
```

**示例输出**
```markdown
### Bug Report：Chrome 首次加载白屏 3 秒

**版本**
- Chrome 125.0.6422.142
- Firefox 126.0
- 项目版本 v2.4.1

**复现步骤**
1. 打开 Chrome，访问 https://example.com
2. 等待页面加载
3. 前 3 秒白屏，之后正常渲染
4. Firefox 无此问题

**预期行为**
页面应在 1 秒内呈现内容

**实际行为**
首次加载白屏 3 秒，后续导航正常

**环境**
OS: macOS 14.5, Chrome 125, Node 20.12
```

## 功能

| 类别 | 场景数 | 包含内容 |
|------|--------|---------|
| Issue | 4（Bug Report / Feature Request / Enhancement / Discussion） | 模板结构、必填字段、环境格式 |
| PR | 4（Feature / Bug Fix / Refactor / Documentation） | 动机+设计+测试+Breaking 检查 |
| Review | 1（Code Review） | 位置标注、严重度分级、建议格式 |
| Commit | 1（Standard Commit） | type(scope): 格式、body/footer 规范、10 种 type 定义 |
| 文档 | 4（README / CONTRIBUTING / CHANGELOG / Migration Guide） | 结构骨架、徽章、快速开始 |
| 发布 | 2（Release Notes / RFC） | 亮点+Breaking+迁移 |
| 模板 | 2（Issue Form YAML / PR Template） | YAML 字段定义、验证规则 |

每个场景分两级复杂度：
- **精细版** — 完整字段、多参考仓库写法详解、多种变体示例
- **中等版** — 保留全部必要部分，精简可选内容

## 结构

```
oh-my-gh-writing/
├── SKILL.md                    # 入口索引 + 7 条原则 + 索引表 + 武器库
├── reference/                  # 18 个场景 × 2 级标准 + 附录
│   ├── bug-report.md           # Bug Report 写法标准
│   ├── feature-request.md      # Feature Request 写法标准
│   ├── feature-pr.md           # Feature PR 写法标准
│   ├── bug-fix-pr.md           # Bug Fix PR 写法标准
│   ├── code-review.md          # Code Review 写法标准
│   ├── standard-commit.md      # Standard Commit 写法标准
│   ├── readme.md               # README 写法标准
│   ├── contributing.md         # CONTRIBUTING 写法标准
│   ├── changelog.md            # CHANGELOG 写法标准
│   ├── release-notes.md        # Release Notes 写法标准
│   ├── migration-guide.md      # Migration Guide 写法标准
│   ├── rfc.md                  # RFC 写法标准
│   ├── issue-form-yaml.md      # Issue Form YAML 写法标准
│   ├── pr-template.md          # PR Template 写法标准
│   └── weapons.md              # 格式化武器库附录
├── DOCS/                       # 源材料与设计文档
│   ├── collection-plan.md      # 收集计划
│   ├── skill-outline.md        # v1 大纲
│   └── skill-outline-v2.md     # v2 大纲（修订版）
├── test/                       # 测试套件
│   ├── README.md               # 测试索引与流程
│   └── compare-18-scenarios.md # 18 场景双版对比（新参考仓库）
└── README.md                   # 本文件
```

## 设计原则

| 原则 | 说明 |
|------|------|
| 渐进式披露 | SKILL.md 核心 ≤4KB，细节在 `reference/`，源材料在 `DOCS/` |
| 仓库配额制 | 22 个参考仓库，每仓库出现在 ≤3 个场景 |
| 3 级参考 | 每场景 3 个精细参考 + 6 个中等参考仓库写法详解 |
| 两条复杂度轨道 | 精细版（完整字段+多变体）和 中等版（必含必要部分即可） |

## 贡献指南

欢迎提交 Issue 或 PR。详见 [CONTRIBUTING](CONTRIBUTING.md)（构建中）。

## 许可

MIT
