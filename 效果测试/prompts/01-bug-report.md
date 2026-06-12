# 测试输入：Bug Report

## 用户请求

```
我的 Next.js 应用在构建时偶尔会报错：
Error: EMFILE: too many open files
这个错误不是每次都出现，但大型项目（1000+ 文件）时更频繁。
我试过增加 fs.inotify.max_user_watches 但没有用。
环境：Next.js 14.2, Node.js 20.11, Ubuntu 22.04, Docker 容器部署。
```

## 期望场景

使用 oh-my-gh-writing 的 Bug Report 场景。
