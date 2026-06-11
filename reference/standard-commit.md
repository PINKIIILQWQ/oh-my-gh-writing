# Standard Commit — 精细标准

## 适用场景
日常代码提交，要求语义清晰的 commit message。

## 精细标准（angular, torvalds/linux, nodejs）

### 结构
```
<type>(<scope>): <subject>

<body>

<footer>
```

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

### 参考仓库写法

**angular/angular**
- Conventional Commits 的定义者（https://www.conventionalcommits.org/）
- 严格 lint：不符合的 commit 被 CI 拒绝
- 完整 body 说明 why 而非 what

**torvalds/linux**
- 标题 50 字符内，body 72 字符折行
- body 说明："Change the way we do X because Y"
- 最老牌的 commit 规范，细节极致

**nodejs/node**
- `pkg: title` 格式规范
- body 含 PR # + 审查建议
- 单 commit = 单变更

## Standard Commit — 中等标准（react, golang, gitea）

### 结构
```
<scope>: <subject>

<body>
```

### 参考仓库写法

**facebook/react**
- 标题简洁：`[package] Title`
- body 含动机 + 测试说明

**golang/go**
- `pkg: description` → `net/http: fix timeout on keep-alive connections`
- body 可省略（简单变更）
- Go 标准是事实上的另一种规范

**go-gitea/gitea**
- 团队 commit 规范：类型前缀 + 描述
- 多 reviewer approve

## 必含元素 Checklist
- [ ] type(scope): subject
- [ ] 动机说明（body）
- [ ] 关联 PR/Issue（footer，可选）
