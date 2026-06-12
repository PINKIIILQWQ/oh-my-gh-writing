# 测试输入：Feature PR

## 用户请求

```
我实现了一个新功能：在 Vite 插件中添加对 .vue 文件的
自定义 block 类型支持。用户可以写 <docs>、<i18n> 等
自定义块，插件会自动提取和注册。

要求：
1. 如果测试时能找到或构造真实 PR diff，先读取 diff 再写 PR 描述。
2. 如果没有 diff，只能基于本 prompt 写草稿，不要虚构文件路径、测试通过状态或 Issue 编号。
3. 可读取 1-2 个真实 Feature PR 案例作为结构参考。
```

## 期望场景

使用 oh-my-gh-writing 的 Feature PR 场景。
