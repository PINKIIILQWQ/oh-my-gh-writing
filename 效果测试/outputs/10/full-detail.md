---
scenario: Standard Commit
mode: full-detail
case-sources: https://github.com/nestjs/nest, https://github.com/conventional-changelog/commitlint
input-prompt: ../../prompts/10-standard-commit.md
---

fix(connection): prevent connection pool leak in getConnection()

The getConnection() method acquires a connection from the pool but
does not guarantee release when the caller throws an exception before
calling release(). Under concurrent load this causes pool exhaustion
after ~50 rapid requests.

Wrap the critical section in try/finally to ensure release() is called
even on error:

- try: acquire + execute callback
- finally: release connection back to pool

Added unit test that simulates 100 concurrent requests and verifies
pool size returns to baseline after each batch.

Fixes #328
