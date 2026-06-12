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

### 证据分层

不同场景需要的上下文不一样。测试时不要把所有场景都当成“短 prompt 生成”：

| 场景 | 测试上下文要求 |
|------|----------------|
| 01-04 Issue / Discussion | 读取对应 `reference/*.md` 和固定 prompt；可参考 `案例/` 的结构，不需要额外找仓库事实 |
| 05-08 PR Description | 有真实 diff 时必须读 diff；没有 diff 时只能基于 prompt 写 PR 草稿，不能虚构文件路径、测试结果或 Issue 编号 |
| 09 Code Review | 必须读取真实 PR diff 或用户贴出的代码；没有代码时不要输出行级发现 |
| 10 Standard Commit | 固定 prompt 足够；只写用户给出的事实 |
| 11 README | 必须读取目标真实仓库，再读 2-3 个同类真实仓库 README 作为结构参考 |
| 12 CONTRIBUTING | 必须读取目标仓库的包管理、测试、CI、`.github/` 或现有贡献文档；再参考 1-2 个同类仓库 |
| 13 CHANGELOG | 优先读取真实 tag/release/commit/PR/changelog；没有证据时不要补 issue 编号或文档链接 |
| 14 Release Notes | 必须读取真实 release/tag/compare/changelog，或明确把缺失项标为 `TODO` |
| 15 Migration Guide | 必须读取旧/新 API 文档或真实迁移指南案例，迁移时间线没有证据就写待确认 |
| 16 RFC | 必须读取 prior art、相关 issue/proposal 或案例；推测设计必须标为草案 |
| 17 Issue Form YAML | 必须读取目标仓库 `.github/ISSUE_TEMPLATE/` 或同类仓库表单 |
| 18 PR Template | 必须读取目标仓库 `.github/`、CI/test 命令或同类仓库模板 |

### 冒烟测试

每次改 `SKILL.md` 或共享原则后，优先测 6 个最容易暴露问题的场景：

1. `01-bug-report`
2. `05-feature-pr`
3. `09-code-review`
4. `11-readme`
5. `14-release-notes`
6. `17-issue-form-yaml`

把对应 prompt 逐个交给已安装 oh-my-gh-writing 的 agent，要求它直接使用 skill 生成输出，然后覆盖对应 `outputs/<编号>/output.md`。

### README 深测

改 README 规则时，可以单独跑这一条，不必每次跑完整 18 场景：

```text
请直接使用 oh-my-gh-writing 的 README 场景做一次深测。

目标：
1. 先读取当前仓库的 SKILL.md 和 reference/readme.md。
2. 选择一个真实开源 CLI 仓库作为目标仓库，优先 Rust/Go/Node CLI。
3. 在正式写 output.md 前，按照 README 场景规则先问我最多 3 个问题，至少覆盖：交付方式、README 风格、是否允许 emoji / Star History / 截图等视觉组件。
4. 我回答后，再读取目标仓库的 README、LICENSE、包配置文件、入口命令、docs/examples 和 `.github/` 中有助于判断项目定位的文件。
5. 再读取 3 个同类真实 CLI 仓库 README，只借鉴结构和信息层级，不复制项目事实。
6. 根据 oh-my-gh-writing 的 README 标准，重写一份可直接放进目标仓库的 README 草稿。
7. 把结果写入 效果测试/outputs/11/output.md。
8. 输出中只能包含目标仓库可证实的功能、安装方式、命令、平台支持、许可证和链接。
9. 不要虚构 Homebrew/npm/cargo install、release asset、CI、benchmark、Star、截图或路线图。
10. 如果我允许 Star History，只能在目标仓库公开且有明确用途时添加；否则保持不添加。
11. 在最终回复中列出目标仓库和 3 个参考仓库链接，不要把来源清单写进 output.md。
12. 完成后运行 git diff --check。
```

### 全量回归

改动 `reference/` 任一场景标准后，跑 18 个场景全量回归。每个场景只生成一个输出，不再做多版本对比。

推荐给测试 agent 的任务：

```text
请直接使用 oh-my-gh-writing skill 做回归测试。

要求：
1. 先运行 git status，确认工作区状态。
2. 读取当前仓库的 SKILL.md 和对应 reference/*.md；不要使用过期的本机安装副本。
3. 逐个读取 效果测试/prompts/ 下的 18 个 prompt。
4. 每个 prompt 只生成一个标准输出，写入 效果测试/outputs/<编号>/output.md。
5. 按 效果测试/README.md 的“证据分层”获取上下文：
   - README 必须读取一个目标真实仓库，并读取 2-3 个同类真实仓库 README 作为结构参考。
   - README 预计会超过长文阈值时，先问最多 3 个选项问题，再写 output.md。
   - Code Review 必须读取真实 PR diff 或用户贴出的代码；没有 diff 就不要编造行级问题。
   - CONTRIBUTING、Issue Form、PR Template 必须读取目标仓库配置或同类仓库模板。
   - CHANGELOG、Release Notes、Migration Guide、RFC 必须读取真实 release/tag/docs/prior art 或案例来源。
6. 输出文件只保留可直接复制到 GitHub 的正文，不要添加测试元数据。
7. 不要虚构 issue 编号、文件行号、测试通过状态、安装命令、release URL、迁移时间线或支持矩阵。
8. 在最终回复中列出每个重上下文场景实际读过的来源链接；不要把来源清单写进 output.md。
9. 完成后运行 git diff --check，并提交变更。
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
