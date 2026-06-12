# 效果测试 — oh-my-gh-writing 18 场景输出画廊

> 验证 oh-my-gh-writing skill 在 18 个场景下的实际输出效果。
> 每个场景使用统一的测试输入 prompt，分别生成 concise 和 full-detail 两种模式。

---

## 使用方法

```bash
# 查看某个场景的测试输入 prompt
cat 效果测试/prompts/01-bug-report.md

# 查看 concise 输出
cat 效果测试/outputs/01/concise.md

# 查看 full-detail 输出
cat 效果测试/outputs/01/full-detail.md
```

## 测试结构

```
效果测试/
├── README.md                  ← 本索引文件
├── prompts/                   ← 18 个测试输入 prompt
│   ├── 01-bug-report.md
│   ├── 02-feature-request.md
│   └── ...
└── outputs/                   ← 18 个场景的输出
    ├── 01-bug-report/
    │   ├── concise.md         ← normal 模式输出
    │   └── full-detail.md     ← complete 模式输出
    ├── 02-feature-request/
    └── ...
```

## 场景索引

| # | 场景 | 测试输入 | Concise 输出 | Full-Detail 输出 | 格式 |
|---|------|----------|--------------|------------------|------|
| 1 | Bug Report | [prompt](./prompts/01-bug-report.md) | [concise](./outputs/01/concise.md) | [full-detail](./outputs/01/full-detail.md) | YAML |
| 2 | Feature Request | [prompt](./prompts/02-feature-request.md) | [concise](./outputs/02/concise.md) | [full-detail](./outputs/02/full-detail.md) | YAML |
| 3 | Enhancement | [prompt](./prompts/03-enhancement.md) | [concise](./outputs/03/concise.md) | [full-detail](./outputs/03/full-detail.md) | YAML |
| 4 | Discussion | [prompt](./prompts/04-discussion.md) | [concise](./outputs/04/concise.md) | [full-detail](./outputs/04/full-detail.md) | Markdown |
| 5 | Feature PR | [prompt](./prompts/05-feature-pr.md) | [concise](./outputs/05/concise.md) | [full-detail](./outputs/05/full-detail.md) | Markdown |
| 6 | Bug Fix PR | [prompt](./prompts/06-bug-fix-pr.md) | [concise](./outputs/06/concise.md) | [full-detail](./outputs/06/full-detail.md) | Markdown |
| 7 | Refactor PR | [prompt](./prompts/07-refactor-pr.md) | [concise](./outputs/07/concise.md) | [full-detail](./outputs/07/full-detail.md) | Markdown |
| 8 | Documentation PR | [prompt](./prompts/08-documentation-pr.md) | [concise](./outputs/08/concise.md) | [full-detail](./outputs/08/full-detail.md) | Markdown |
| 9 | Code Review | [prompt](./prompts/09-code-review.md) | [concise](./outputs/09/concise.md) | [full-detail](./outputs/09/full-detail.md) | Markdown |
| 10 | Standard Commit | [prompt](./prompts/10-standard-commit.md) | [concise](./outputs/10/concise.md) | [full-detail](./outputs/10/full-detail.md) | Plain text |
| 11 | README | [prompt](./prompts/11-readme.md) | [concise](./outputs/11/concise.md) | [full-detail](./outputs/11/full-detail.md) | Markdown |
| 12 | CONTRIBUTING | [prompt](./prompts/12-contributing.md) | [concise](./outputs/12/concise.md) | [full-detail](./outputs/12/full-detail.md) | Markdown |
| 13 | CHANGELOG | [prompt](./prompts/13-changelog.md) | [concise](./outputs/13/concise.md) | [full-detail](./outputs/13/full-detail.md) | Markdown |
| 14 | Release Notes | [prompt](./prompts/14-release-notes.md) | [concise](./outputs/14/concise.md) | [full-detail](./outputs/14/full-detail.md) | Markdown |
| 15 | Migration Guide | [prompt](./prompts/15-migration-guide.md) | [concise](./outputs/15/concise.md) | [full-detail](./outputs/15/full-detail.md) | Markdown |
| 16 | RFC | [prompt](./prompts/16-rfc.md) | [concise](./outputs/16/concise.md) | [full-detail](./outputs/16/full-detail.md) | Markdown |
| 17 | Issue Form YAML | [prompt](./prompts/17-issue-form-yaml.md) | [concise](./outputs/17/concise.md) | [full-detail](./outputs/17/full-detail.md) | YAML |
| 18 | PR Template | [prompt](./prompts/18-pr-template.md) | [concise](./outputs/18/concise.md) | [full-detail](./outputs/18/full-detail.md) | Markdown |

## 模式说明

| 模式 | 对应 SKILL.md 级别 | 使用时机 |
|------|-------------------|----------|
| **concise** | normal 模式 | 默认输出，信息密集但简洁 |
| **full-detail** | complete 模式 | 高风险/发布/迁移/Breaking Change 时使用 |

## 参考

- [SKILL.md](../SKILL.md) — 场景路由和模式选择规则
- [案例/](../案例) — 18 场景真实仓库案例
- [reference/](../reference) — 每场景标准写法
