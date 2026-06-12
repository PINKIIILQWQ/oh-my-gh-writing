# 测试输入：Enhancement

## 用户请求

```
现在 Express.js 的 res.send() 方法不支持 streaming 响应。
我希望改进 res.send() 使其能接受 ReadableStream 对象，
这样我们就可以在不加载完整数据到内存的情况下发送大文件。
```

## 期望场景

使用 oh-my-gh-writing 的 Enhancement 场景。
