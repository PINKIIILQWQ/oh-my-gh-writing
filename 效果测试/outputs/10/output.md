# 10 Standard Commit 测试

fix(db): return connections to pool after use

Refactor `getConnection()` so each borrowed database connection is released back to the pool after the caller finishes with it.

This prevents connection pool exhaustion caused by leaked checked-out connections.
