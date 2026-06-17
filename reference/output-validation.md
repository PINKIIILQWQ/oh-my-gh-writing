# Output Validation — 提交前验收

## 适用场景

所有场景在最终输出前都应经过这一层检查。它不是第 19 个用户写作场景，而是内部验收清单：判断产物能否不经解释地粘贴到 GitHub。

## 输出清洁

目标输出必须是 GitHub artifact 本身。

禁止内容：

- 对话前言，例如“下面是”“可以直接使用”“我为你写好了”。
- 测试标题，例如 `# 02 Feature Request 测试`。
- 整篇 Markdown 外层代码块，例如 ```markdown 包住完整 README 或 Issue。
- 复制污染，例如多余反引号、终端残留、无关 docker-compose 片段、半截代码块。
- 来源清单、测试元数据、来源元数据、input prompt，除非用户明确要求测试报告。
- 已勾选但没有证据的 checklist。模板、未来工作和待验证事项默认保持未勾选。

允许内容：

- YAML 多文件展示时，在对话中用 `## File: ...` 加 fenced `yaml`。
- 单个目标文件落盘时，只写文件内容，不加 Markdown 包装。
- Issue/PR 正文需要代码、日志、diff、配置时，使用局部 fenced code block。

## 事实边界

以下事实必须有来源：

| 事实类型 | 合法来源 |
|----------|----------|
| 版本号、发布日期、release URL | 用户输入、release 页面、tag、CHANGELOG |
| PR/Issue 编号、提交哈希 | diff、GitHub 页面、仓库历史、用户输入 |
| 测试结果、CI 名称、workflow 名称 | 工具输出、CI 配置、用户输入 |
| 安装命令、包名、Node/Rust/Python 版本 | package/config 文件、官方文档、用户输入 |
| 平台支持、兼容范围、迁移时间线 | 官方文档、release notes、仓库文件、用户输入 |
| 截图、GIF、Star History、徽章 | 仓库资源、用户素材、官方服务或可验证链接 |

没有证据时：

- 写 `TODO`、`TBD`、`To confirm`。
- 删除可选段落。
- 把原因写成 "Suspected cause" 或 "Needs confirmation"。
- 不把模型记忆或案例事实当作目标仓库事实。

## 场景路由验收

| 输出症状 | 判定 |
|----------|------|
| 未来能力请求被写成已实现 PR | ROUTING_FAIL |
| "从 PR 复盘重构为 Feature Request" 被写成 PR 描述 | ROUTING_FAIL |
| 没有 diff 却输出行号级 review | FORMAT_FAIL |
| PR 描述声称测试已通过但没有证据 | FACT_CHECK_REQUIRED |
| Discussion 已经替用户决定方案 | DRAFT_ONLY |
| README 整篇包在代码块里 | FORMAT_FAIL |
| YAML 文件带外层解释标题并要直接落盘 | FORMAT_FAIL |

## 验收标签

测试时给每次输出一个标签：

| 标签 | 含义 |
|------|------|
| PASS | 原样可提交到目标 GitHub 位置 |
| PASS_AFTER_CLEANUP | 内容成立，但需要清掉包装、标题、占位或格式污染 |
| DRAFT_ONLY | 可当草稿，不能直接提交 |
| ROUTING_FAIL | 场景识别错误 |
| FACT_CHECK_REQUIRED | 事实密集内容缺少来源或需要核验 |
| FORMAT_FAIL | 格式不可提交 |

## 提交前 Checklist

- [ ] 没有测试标题或测试元数据。
- [ ] 没有整篇外层 `markdown` 代码块。
- [ ] 没有对话性前言或结尾。
- [ ] 没有无关代码片段、终端残留或复制污染。
- [ ] 没有未解释、不可行动、或不适合提交位置的 `#XXXXX`、`Fixes #`、`TODO`、`TBD`。
- [ ] 没有把待验证 checklist 预先打钩；只有用户输入、仓库、diff 或工具输出证明完成的项目才勾选。
- [ ] YAML 能被解析；多文件展示和单文件落盘边界清楚。
- [ ] Markdown 表格、代码块、details 和 alert 没有破坏渲染。
- [ ] PR/Review 没有声明未实际运行的测试。
- [ ] 场景路由和用户请求一致。
- [ ] 高风险事实都有来源，或者已标为待确认。

## 维护者本地验收

维护者做本地回归时，建议使用三层文件：

```text
.local-validation/<编号>-<scenario>/
  input.md
  output.raw.md
  output.clean.md
  verdict.md
```

- `output.raw.md` 保留 agent 原始输出，用于观察污染来源。
- `output.clean.md` 只放可提交 artifact，不能有测试标题或解释。
- `verdict.md` 记录标签、来源、暴露问题和是否需要改 skill。

不要把 `output.clean.md` 当成展示报告；它必须满足“可以不经解释地粘贴到 GitHub”的标准。
