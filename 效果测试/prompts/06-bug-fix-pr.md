# 测试输入：Bug Fix PR

## 用户请求

```
我修复了 axios 的一个 bug：当使用 CancelToken 配合 AbortController 时，
调用 cancel() 后 promise 永远不会 resolve。

要求：
1. 如果测试时能找到或构造真实 PR diff，先读取 diff 再写 PR 描述。
2. 根因只有在代码、测试或用户说明支持时才能写成确定结论。
3. 不要虚构 Fixes 编号、测试通过状态或具体文件路径。
```

## 期望场景

使用 oh-my-gh-writing 的 Bug Fix PR 场景。
