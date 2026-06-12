---
scenario: Bug Report
mode: concise
case-sources: https://github.com/kubernetes/kubernetes, https://github.com/jestjs/jest
input-prompt: ../../prompts/01-bug-report.md
---

### Bug: Next.js build fails with EMFILE error on large projects

**Environment**
- Next.js 14.2 · Node.js 20.11 · Ubuntu 22.04 · Docker container
- Project size: 1000+ files

**Steps to reproduce**
1. Run `next build` in a large Next.js project (1000+ source files)
2. Observe the build failing intermittently with:
   ```
   Error: EMFILE: too many open files, open '/app/src/components/Header.tsx'
   ```
3. The error is non-deterministic – larger projects fail more frequently

**Expected behavior**
Build should complete successfully regardless of project size.

**Actual behavior**
EMFILE error occurs during file traversal phase, causing build to crash.

**Root cause**
Node.js file watcher hits the OS file descriptor limit. Next.js uses
chokidar internally, which opens a file descriptor per watched file.

**Workaround attempted**
```bash
echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf
```

**Suggested fix**
```dockerfile
# Increase ulimit in Docker
ulimit -n 65536
```
