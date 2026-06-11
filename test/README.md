# oh-my-gh-writing — 测试套件

## 测试索引

| # | 场景 | 测试提示词 | 预期产出 | 状态 |
|---|------|-----------|---------|------|
| 1 | Bug Report | `写一份 Bug Report：Chrome 下首次加载页面白屏 3 秒，Firefox 正常` | 完整模板含重现/环境/日志 | — |
| 2 | Feature Request | `写一份 Feature Request：给 CLI 工具加 --json 输出模式` | 动机→Use Case→期望 API→备选 | — |
| 3 | Enhancement | `写一份 Enhancement：改进搜索功能的模糊匹配精度` | 当前限制→改进→兼容性 | — |
| 4 | Discussion | `写一份 Discussion：是否应该放弃 IE11 支持` | 背景→方案对比→征求 | — |
| 5 | Feature PR | `写一份 Feature PR：实现了 OAuth2 登录功能` | 动机→设计→测试→Breaking | — |
| 6 | Bug Fix PR | `写一份 Bug Fix PR：修复了内存泄漏，Fixes #4421` | 根因→方案→测试 | — |
| 7 | Refactor PR | `写一份 Refactor PR：把路由层从 Express 换到 Hono` | 目标→before-after→测试 | — |
| 8 | Documentation PR | `改 README 的快速开始部分，加上 Docker 安装方式` | 原文→改后→无代码改动 | — |
| 9 | Code Review | `审查这个 PR：把 forEach 改成了 for...of` | 位置→问题→建议→Severity | — |
| 10 | Standard Commit | `写一条 commit message：修复了登录页的 CSRF 漏洞` | type(scope): + body + footer | — |
| 11 | README | `写一个 Rust CLI 工具的 README` | 标题+徽章+快速开始+文档 | — |
| 12 | CONTRIBUTING | `写一个开源库的 CONTRIBUTING.md` | 工作流+规范+PR流程 | — |
| 13 | CHANGELOG | `写 v2.0.0 的 CHANGELOG 条目` | 版本+日期+类型分类 | — |
| 14 | Release Notes | `写 v3.0.0 的 Release Notes，含 Breaking Changes` | 亮点+GIF+迁移+Changelog 链接 | — |
| 15 | Migration Guide | `写从 webpack v4 到 v5 的迁移指南` | 步骤+旧新对比+回滚 | — |
| 16 | RFC | `写一份 RFC：引入 Plugin 系统` | 动机→设计→兼容→备选 | — |
| 17 | Issue Form YAML | `写 Bug Report 的 YAML Issue Form` | YAML 字段+验证+labels | — |
| 18 | PR Template | `写项目的 PR Template.md` | 动机+设计+Checklist | — |

## 测试方法

1. **选一个场景**（如 Bug Report）
2. **看对应提示词**（`test/README.md` 第 2 列）
3. **运行 skill**：告诉 agent 你要写什么，用提示词做输入
4. **对照参考文件**检查产出：

```
SKILL.md                           → 入口索引 + 原则 + 武器库
reference/<场景名>.md              → 完整/普通 2 级写法标准 + 仓库示例 + 参考链接
```

5. **自检 checklist**（在每场景 reference 文件底部）

## 测试流程

```
1. 普通复杂度运行（默认）
   → 检查是否包含全部必要部分
   → 检查结构是否完整

2. 完整复杂度运行（要求"完整版"）
   → 检查是否包含额外字段
   → 检查参考仓库做法是否体现

3. 边缘情况
   → 信息不足时是否提问（复现步骤/环境等）
   → 极端场景是否仍保持结构
```

## 参考仓库摘要

完整参考链接见各场景 `reference/*.md` 底部「参考链接」章节。
