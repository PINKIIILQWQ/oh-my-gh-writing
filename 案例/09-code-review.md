# Code Review — 经典案例

---

## 精细版

### 案例 1：google/eng-practices (20.5k⭐)

**黄金法则：** CL 提升整体代码健康即应批准，即使不完美。

**What to Look For:**
1. Design — 交互合理？
2. Functionality — 做了预期的事？
3. Complexity — 能快速理解？
4. Tests — 正确有用？
5. Naming — 名称清晰？
6. Comments — 解释"为什么"
7. Style — 与指南一致
8. Documentation — 是否更新

**Severity:** `Nit:` 标记可选建议

### 案例 2：rails/rails (56k⭐)
- GitHub PR inline review
- All changes must be reviewed
- CI must be green
- `[ci skip]` for doc-only changes

### 案例 3：swiftlang/swift (67.5k⭐)
- Small incremental changes preferred
- Explicit approval required
- `[tag]` in commit messages
- Review others' changes to build goodwill

## 普通版

### 案例 4：knonm/code-review-checklist (0.5k⭐)
14-point checklist: magic numbers, defensive code, naming, DRY, SOLID...

### 案例 5：awesome-skills/code-review-skill (0.8k⭐)
4-phase review: Context → High-Level → Line-by-Line → Summary
Severity: blocking / important / nit / suggestion / learning / praise

### 案例 6：mntnr/awesome-contributing (0.3k⭐)
Curated list of great CONTRIBUTING.md examples.
