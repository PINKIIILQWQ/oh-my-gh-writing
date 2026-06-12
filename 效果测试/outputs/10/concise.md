---
scenario: Standard Commit
mode: concise
case-sources: https://github.com/semantic-release/semantic-release, https://github.com/nestjs/nest
input-prompt: ../../prompts/10-standard-commit.md
---

fix(connection): prevent connection pool leak in getConnection()

Ensure every getConnection() call returns the connection to the pool
via a finally block, preventing resource exhaustion under concurrent load.

Closes #328
