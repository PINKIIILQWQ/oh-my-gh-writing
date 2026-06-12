# 效果测试 — oh-my-gh-writing 18 场景输出画廊

> 验证 oh-my-gh-writing skill 在 18 个场景下的实际输出效果。
> 每个场景使用固定测试输入 prompt，生成一个标准输出。

---

## 使用方法

```bash
# 查看某个场景的测试输入 prompt
cat 效果测试/prompts/01-bug-report.md

# 查看对应输出
cat 效果测试/outputs/01/output.md
```

## 测试结构

```
效果测试/
├── README.md                  ← 本索引文件
├── prompts/                   ← 18 个测试输入 prompt
│   ├── 01-bug-report.md
│   ├── 02-feature-request.md
│   └── ...
└── outputs/                   ← 18 个场景的标准输出
    ├── 01/
    │   └── output.md
    ├── 02/
    └── ...
```

## 场景索引

| # | 场景 | 测试输入 | 输出 | 格式 |
|---|------|----------|------|------|
| 1 | Bug Report | [prompt](./prompts/01-bug-report.md) | [output](./outputs/01/output.md) | Markdown |
| 2 | Feature Request | [prompt](./prompts/02-feature-request.md) | [output](./outputs/02/output.md) | Markdown |
| 3 | Enhancement | [prompt](./prompts/03-enhancement.md) | [output](./outputs/03/output.md) | Markdown |
| 4 | Discussion | [prompt](./prompts/04-discussion.md) | [output](./outputs/04/output.md) | Markdown |
| 5 | Feature PR | [prompt](./prompts/05-feature-pr.md) | [output](./outputs/05/output.md) | Markdown |
| 6 | Bug Fix PR | [prompt](./prompts/06-bug-fix-pr.md) | [output](./outputs/06/output.md) | Markdown |
| 7 | Refactor PR | [prompt](./prompts/07-refactor-pr.md) | [output](./outputs/07/output.md) | Markdown |
| 8 | Documentation PR | [prompt](./prompts/08-documentation-pr.md) | [output](./outputs/08/output.md) | Markdown |
| 9 | Code Review | [prompt](./prompts/09-code-review.md) | [output](./outputs/09/output.md) | Markdown |
| 10 | Standard Commit | [prompt](./prompts/10-standard-commit.md) | [output](./outputs/10/output.md) | Plain text |
| 11 | README | [prompt](./prompts/11-readme.md) | [output](./outputs/11/output.md) | Markdown |
| 12 | CONTRIBUTING | [prompt](./prompts/12-contributing.md) | [output](./outputs/12/output.md) | Markdown |
| 13 | CHANGELOG | [prompt](./prompts/13-changelog.md) | [output](./outputs/13/output.md) | Markdown |
| 14 | Release Notes | [prompt](./prompts/14-release-notes.md) | [output](./outputs/14/output.md) | Markdown |
| 15 | Migration Guide | [prompt](./prompts/15-migration-guide.md) | [output](./outputs/15/output.md) | Markdown |
| 16 | RFC | [prompt](./prompts/16-rfc.md) | [output](./outputs/16/output.md) | Markdown |
| 17 | Issue Form YAML | [prompt](./prompts/17-issue-form-yaml.md) | [output](./outputs/17/output.md) | YAML / Markdown wrapper |
| 18 | PR Template | [prompt](./prompts/18-pr-template.md) | [output](./outputs/18/output.md) | Markdown |

## 推荐测试流程

### 冒烟测试

每次改 `SKILL.md` 或共享原则后，优先测 6 个最容易暴露问题的场景：

1. `01-bug-report`
2. `05-feature-pr`
3. `09-code-review`
4. `11-readme`
5. `14-release-notes`
6. `17-issue-form-yaml`

把对应 prompt 逐个交给已安装 oh-my-gh-writing 的 agent，要求它直接使用 skill 生成输出，然后覆盖对应 `outputs/<编号>/output.md`。

### 全量回归

改动 `reference/` 任一场景标准后，跑 18 个场景全量回归。每个场景只生成一个输出，不再做多版本对比。

推荐给测试 agent 的任务：

```text
请直接使用 oh-my-gh-writing skill 做回归测试。

要求：
1. 读取当前仓库的 SKILL.md 和对应 reference/*.md。
2. 逐个读取 效果测试/prompts/ 下的 18 个 prompt。
3. 每个 prompt 只生成一个标准输出。
4. 把输出写入 效果测试/outputs/<编号>/output.md。
5. 不要添加测试元数据，输出文件只保留可直接复制到 GitHub 的正文。
6. 不要虚构 issue 编号、文件行号、测试通过状态、安装命令、release URL 或迁移时间线。
7. 完成后运行 git diff --check，并提交变更。
```

### 人工检查

每轮测试至少人工抽查 6 个冒烟场景，重点看：

- 是否读了对应场景标准，而不是泛泛套模板
- 是否没有虚构证据、链接、编号、行号或测试结果
- YAML / Markdown / commit message 是否能直接复制到目标位置
- README、Release Notes、Migration Guide 是否没有编造安装方式、发布时间线或外链
- Code Review 在没有真实 diff 时是否拒绝编造行级问题

## 参考

- [SKILL.md](../SKILL.md) — 场景路由和共享原则
- [案例/](../案例) — 18 场景真实仓库案例
- [reference/](../reference) — 每场景标准写法
