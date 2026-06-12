---
scenario: PR Template
mode: concise
case-sources: https://github.com/apache/flink, https://github.com/apache/rocketmq
input-prompt: ../../prompts/18-pr-template.md
---

# .github/PULL_REQUEST_TEMPLATE.md

```markdown
## Description
<!-- Describe your changes and the motivation behind them. -->
Closes # (issue)

## Type of change
- [ ] Bug fix (non-breaking)
- [ ] New feature (non-breaking)
- [ ] Breaking change
- [ ] Documentation update

## How was this tested?
- [ ] `cargo test` passes
- [ ] `cargo clippy` passes
- [ ] Added new tests

## Checklist
- [ ] Code follows project style
- [ ] Self-review completed
- [ ] Documentation updated (if needed)
```
