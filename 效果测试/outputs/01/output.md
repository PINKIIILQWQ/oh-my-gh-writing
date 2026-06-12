## Bug Report: Next.js build crashes with EMFILE on large projects

### Description
When running `next build` on a project with 1000+ source files in a
Docker container, the build intermittently fails with an EMFILE error.
This occurs during the file system traversal phase where Next.js
discovers and compiles source files. The error is non-deterministic:
sometimes the build succeeds, sometimes it fails. Larger projects
(2000+ files) fail more consistently than smaller ones.

### Environment
- **Next.js version:** 14.2.0
- **Node.js version:** 20.11.0
- **OS:** Ubuntu 22.04 (container)
- **Container runtime:** Docker 24.0
- **Deployment:** Docker Compose
- **File count:** ~1200 source files (.tsx, .ts, .css)

### Steps to reproduce
1. Create a Next.js project with 1000+ components:
   ```bash
   npx create-next-app@latest large-app
   cd large-app
   # Generate many component files
   for i in $(seq 1 200); do
     cp -r src/components/Header.tsx "src/components/Module$i.tsx"
   done
   ```
2. Build in Docker:
   ```bash
   docker build -t large-app .
   ```
3. Run the build:
   ```bash
   docker run --rm large-app npx next build
   ```
4. Observe intermittent failure with:
   ```
   Error: EMFILE: too many open files, open '/app/src/components/Module42.tsx'
       at Object.openSync (fs.js:585:3)
       at readFileSync (fs.js:486:35)
       at Object.readSync (next/dist/compiled/...) …
   ```

### Expected behavior
Build should complete successfully for projects of any size,
given sufficient system resources.

### Actual behavior
Build fails with EMFILE when file descriptor usage exceeds the
container's ulimit (default 1024 in Docker).

### Root cause
Next.js file watcher opens file descriptors for all source files
during the compilation phase. Docker containers have a default
open file limit of 1024, which is insufficient for large projects.

### Logs
```
> next build

  ▲ Next.js 14.2.0
  - Experiments: (none)

Creating an optimized production build ...
Error: EMFILE: too many open files, open '/app/src/components/Header.tsx'
    at Object.openSync (fs.js:585:3)
 ELIFECYCLE  Command failed with exit code 1.
```

### Resolution
```dockerfile
# docker-compose.yml
services:
  app:
    build: .
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
```

Verification: After setting ulimit, `next build` completes reliably on
projects with 2000+ files.
