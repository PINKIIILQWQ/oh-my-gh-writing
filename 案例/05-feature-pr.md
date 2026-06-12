# Feature PR — 经典案例

---

## 精细版（完整 PR 模板）

### 案例 1：freeCodeCamp/freeCodeCamp (412k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
Checklist:
- [ ] I have read and followed the contribution guidelines
- [ ] I have read and followed the how to open a pull request guide
- [ ] My pull request targets the `main` branch of freeCodeCamp
- [ ] I have tested these changes either locally on my machine, or GitHub Codespaces
Closes #XXXXX
```

**特点：** 4 项 checklist + Closes # 关联，志愿者项目风格。

---

### 案例 2：facebook/react-native (119k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## Summary:
[动机 + 解决的问题]

## Changelog:
[ANDROID|GENERAL|IOS|INTERNAL] [BREAKING|ADDED|CHANGED|DEPRECATED|REMOVED|FIXED|SECURITY] - Message

## Test Plan:
[测试证明]
```

**特点：** Summary + Changelog（强制分类标签） + Test Plan，降低发布负担。

---

### 案例 3：tauri-apps/tauri (88k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
Before submitting a PR:
1. Descriptive title (good/bad examples provided)
2. Reference related issue, e.g. closes #123
3. Add change file in `.changes` directory
4. Commits must be signed
5. `cargo test` and `cargo clippy` must pass
6. Draft PR for work in progress
```

**特点：** 8 条前置指引 + good/bad title 示例 + `.changes` 变更文件机制。

---

## 普通版（较短模板）

### 案例 4：apache/airflow (38k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

- AI 工具披露复选框（生成式 AI 是否用于编写此 PR）
- Closes # / Related # 关联
- 贡献指南引用 + Apache 许可证

### 案例 5：curl/curl (37k⭐)

**来源：** `.github/pull_request_template.md`

> IMPORTANT: If you cannot understand or explain your work without using AI then do not file here. Do not paste massive AI generated explanations.

**特点：** 极简但态度鲜明——反对大量 AI 生成的无意义 PR 描述。

### 案例 6：docker/compose (34k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
**What I did**
**Related issue**
**(not mandatory) A picture of a cute animal, if possible in relation to what you did**
```

**特点：** 极简 3 字段 + Docker 标志性可爱动物文化。

---

### 附加参考

**systemd/systemd (15k⭐)** — PR 强调系统级别兼容性检查。
**google/googletest (35k⭐)** — Checklist 驱动，包含 API 兼容性声明。
**apache/thrift (10k⭐)** — 多语言兼容性 PR 模板。

---

> 收集日期：2026-06-12
