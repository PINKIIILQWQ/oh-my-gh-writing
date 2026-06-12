# PR Template — 经典案例

---

## 精细版（完整 PR 模板）

### 案例 1：apache/flink (24k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What is the purpose of the change
## Brief change log
## Verifying this change
## Does this pull request potentially affect:
- Dependencies: (yes / no)
- Public API: (yes / no)
- Runtime compatibility: (yes / no)
## Documentation
- Does this introduce a new feature? (yes / no)
- If yes, how is documentation implemented?
```

---

### 案例 2：apache/rocketmq (21k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What is the purpose of the change
## Brief changelog
## Verifying this change
- [ ] GitHub issue filed for the change
- [ ] Meaningful subject line and body per commit
- [ ] `mvn clean install -DskipTests=false` passes
- [ ] New unit tests if the change is new code
- [ ] Config change documentation
```

---

### 案例 3：kubernetes/kompose (9k⭐)

```markdown
#### What type of PR is this?
- /kind bug / /kind cleanup / /kind feature / /kind design / /kind documentation

#### What this PR does / why we need it

#### Which issue this PR fixes
```

---

## 普通版（简洁 PR 模板）

### 案例 4：Homebrew (42k⭐)

```markdown
- [ ] Contributing guidelines followed
- [ ] No duplicate PRs for same change
- [ ] Performance claims include benchmarks
- [ ] New tests written
- [ ] `brew lgtm` passes
- [ ] AI was used to assist (disclose)
```

### 案例 5：Kubernetes (in general)

K8s 风格的 PR 模板强调：

- What this PR does / why we need it
- Which issue this PR fixes
- Special notes for reviewers
- Checklist: tests, docs, breaking changes

### 案例 6：Docker (34k⭐)

极简风格：
- What I did
- Related issue
- (optional) A picture of a cute animal

---

### 附加参考

**angular/components (100k⭐)** — PR 模板含 commit message 规范引用 + 变更类型检查。
**apache/beam (40k⭐)** — JIRA 号 + 描述 + 测试 + 组件前缀（`[SQL]` / `[CORE]`）。
**microsoft/vscode-extension (165k⭐)** — 最完善的 PR checklist 之一，含 extension host 兼容性。

---

### 参考仓库链接

- https://github.com/apache/flink — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/apache/rocketmq — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/kubernetes/kompose — `.github/PULL_REQUEST_TEMPLATE.md`

> 收集日期：2026-06-12
