### Bug: Next.js build fails with EMFILE on large projects

**Environment**
- Next.js 14.2
- Node.js 20.11
- Ubuntu 22.04 (Docker container)
- Project size: 1000+ source files

**Steps to reproduce**
1. Run `next build` in a large Next.js project inside Docker
2. Build fails intermittently with `Error: EMFILE: too many open files`
3. Larger projects (2000+ files) fail more consistently

**Expected behavior**
Build should complete successfully regardless of project size.

**Actual behavior**
Build crashes with EMFILE during file traversal phase.

**Suspected cause**
Node.js file watcher exceeds the Docker container's default open file limit (1024). Next.js uses chokidar internally, which opens a file descriptor per watched file. The inotify watch limit is a different limit (fs.inotify.max_user_watches) and does not affect this.

**Workaround tested**
Increasing `fs.inotify.max_user_watches` had no effect (this controls inotify watches, not file descriptors).

**Suggested fix**
Increase the container's open file limit:
```dockerfile
# docker-compose.yml
services:
  app:
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
```
