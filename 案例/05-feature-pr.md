# Feature PR — 经典案例

---

## 精细版（完整 PR 模板）

### 案例 1：freeCodeCamp/freeCodeCamp (412k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
Checklist:

<!-- Please follow this checklist and put an x in each of the boxes, like this: [x].
     It will ensure that our team takes your pull request seriously. -->

- [ ] I have read and followed the [contribution guidelines](https://contribute.freecodecamp.org).
- [ ] I have read and followed the [how to open a pull request guide](https://contribute.freecodecamp.org/how-to-open-a-pull-request/).
- [ ] My pull request targets the `main` branch of freeCodeCamp.
- [ ] I have tested these changes either locally on my machine, or GitHub Codespaces.

<!--If your pull request closes a GitHub issue, replace the XXXXX below with the issue number.-->

Closes #XXXXX

<!-- Feel free to add any additional description of changes below this line -->
```

**特点：** 4 项 checklist + Closes # 关联，志愿者项目风格——强调贡献指南阅读和本地测试。

---

### 案例 2：facebook/react-native (119k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## Summary:

<!-- Explain the **motivation** for making this change. What existing problem
     does the pull request solve? -->

## Changelog:

<!-- Help reviewers and the release process by writing your own changelog entry.

Pick one each for the category and type tags:

[ANDROID|GENERAL|IOS|INTERNAL] [BREAKING|ADDED|CHANGED|DEPRECATED|REMOVED|FIXED|SECURITY] - Message

For more details, see:
https://reactnative.dev/contributing/changelogs-in-pull-requests
-->

## Test Plan:

<!-- Demonstrate the code is solid. Example: The exact commands you ran and
     their output, screenshots / videos if the pull request changes the UI. -->
```

**特点：** Summary + Changelog（带分类标签系统）+ Test Plan。强制写 changelog entry，降低发布负担。

---

### 案例 3：tauri-apps/tauri (88k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
<!--
Before submitting a PR, please read https://github.com/tauri-apps/tauri/blob/dev/.github/CONTRIBUTING.md

1. Give the PR a descriptive title.
  Examples of good title:
    - fix(windows): fix race condition in event loop
    - feat: add `Window::set_fullscreen`
  Examples of bad title:
    - fix #7123
    - update docs
    - fix bugs

2. If there is a related issue, reference it in the PR text, e.g. closes #123.
3. If this change requires a new version, then add a change file in `.changes` directory.
4. Ensure that all your commits are signed.
5. Ensure `cargo test` and `cargo clippy` passes.
6. Propose your changes as a draft PR if your work is still in progress.
-->
```

**特点：** 8 条前置指引 + good/bad title 示例 + change file 机制（类似 changesets）。

---

## 普通版（较短模板）

### 案例 4：apache/airflow (38k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

- 感谢致辞 + 贡献指南引用
- Closes # / Related # 关联
- AI 工具披露复选框（生成式 AI 是否用于编写此 PR）
- 许可证头 + 签入说明

**特点：** AI 生成代码的披露策略是行业趋势，Apache 风格。

> 完整内容：https://raw.githubusercontent.com/apache/airflow/main/.github/PULL_REQUEST_TEMPLATE.md

---

### 案例 5：curl/curl (37k⭐)

**来源：** `.github/pull_request_template.md`

```markdown
<!--
        IMPORTANT:
        If you cannot understand or explain your work without using
        Artificial Intelligence (AI) then do not file here. Do not paste
        massive AI generated explanations. We accept the use of AI as long as
        it is digestible. Please explain your issues or improvements briefly
        and clearly in your own human voice.
-->
```

**特点：** 极简但态度鲜明——反对 AI 生成的大量无意义 PR 描述。

---

### 案例 6：docker/compose (34k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
**What I did**

**Related issue**
<!-- If this is a bug fix, make sure your description includes "fixes #xxxx",
     or "closes #xxxx" -->

**(not mandatory) A picture of a cute animal, if possible in relation to what you did**
```

**特点：** 极简 3 字段——做了什么 + 关联 issue + 可选可爱动物图（Docker 标志性文化）。

---

> 收集日期：2026-06-12
