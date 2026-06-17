# Standard Commit — 写作标准

## 适用场景
日常代码提交，要求语义清晰的 commit message。

## 输出边界

Commit message 描述一个实际提交。不要编造 PR/Issue 编号、breaking change、Co-authored-by、Signed-off-by 或测试结果。

## 标准结构

```
<type>(<scope>): <subject>

<body>

<footer>
```

`body` 和 `footer` 是可选项；只有复杂变更、breaking change、关联 Issue/PR 或项目规范要求时才写。

**type 表**：
| type | 含义 | 示例 |
|------|------|------|
| feat | 新功能 | `feat(auth): add OAuth2 login` |
| fix | 修复 | `fix(parser): handle empty input` |
| docs | 文档 | `docs: add migration guide` |
| refactor | 重构 | `refactor(core): extract auth module` |
| perf | 性能 | `perf(query): lazy load` |
| test | 测试 | `test: add api regression tests` |
| chore | 杂项 | `chore: update dependencies` |
| style | 格式 | `style: fix indent` |
| revert | 回滚 | `revert: "feat: add X"` |

## 信息不足时

- 无法确认 scope 时省略 scope。
- 不知道 Issue 编号时不写 footer。
- breaking change 不确定时不要写 `!` 或 `BREAKING CHANGE`。

## 禁止编造项

- 不编造 issue/PR 编号、reviewer、co-author、DCO、breaking change 或测试状态。
- 不把多个无关变更塞进一个 commit message。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| Conventional Commits | https://www.conventionalcommits.org/en/v1.0.0/ |
| Angular commit rules | https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit |
| Linux submitting patches | https://www.kernel.org/doc/html/v4.10/process/submitting-patches.html |
| Node.js commit guide | https://github.com/nodejs/node/blob/main/CONTRIBUTING.md#step-3-commit |
| Go commit messages | https://go.dev/doc/contribute#commit_messages |
| Gitea CONTRIBUTING | https://github.com/go-gitea/gitea/blob/main/CONTRIBUTING.md |

## 必含元素 Checklist
- [ ] type(scope): subject
- [ ] 必要时用 body 说明动机
- [ ] 关联 PR/Issue（footer，可选，且只在编号已知时写）
