# 测试输入：Issue Form YAML

## 用户请求

```
请为一个真实开源组件库创建 GitHub Issue Form YAML。
需要 Bug Report 和 Feature Request 两种表单。

要求：
1. 先读取目标仓库现有 `.github/ISSUE_TEMPLATE/`、labels 约定和贡献入口。
2. 再读取 1-2 个同类组件库的 Issue Form YAML。
3. 输出必须覆盖 Bug Report 和 Feature Request 两种表单。
4. 不要添加带假 URL 的 `contact_links`；没有真实 docs/discussion/security 链接就省略。
```

## 期望场景

使用 oh-my-gh-writing 的 Issue Form YAML 场景。
