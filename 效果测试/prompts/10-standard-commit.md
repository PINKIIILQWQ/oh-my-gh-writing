# 测试输入：Standard Commit

## 用户请求

```
修复了数据库连接池泄漏问题——重构了 getConnection() 方法，
确保每次调用后连接都正确归还到连接池。
```

## 期望场景

使用 oh-my-gh-writing 的 Standard Commit 场景。
