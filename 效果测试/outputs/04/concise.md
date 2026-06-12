---
scenario: Discussion
mode: concise
case-sources: https://github.com/mozilla/rr, https://github.com/jenkinsci/jenkins
input-prompt: ../../prompts/04-discussion.md
---

### Discussion: Service granularity - finer split or merge?

**Context**
Team of 8 maintaining 12 microservices. Some services have < 1% of total traffic
but each requires separate CI/CD pipeline, monitoring, and on-call rotation.

**Options**

| Approach | Pros | Cons |
|----------|------|------|
| Merge low-traffic services | Fewer pipelines, simpler deploys | Larger deploy scope |
| Keep current split | Independent scaling | High ops overhead |
| Hybrid (merge then split when needed) | Balanced | Requires refactoring discipline |

**Open questions**
1. What threshold (%) justifies a separate service?
2. How to handle shared data between merged services?
