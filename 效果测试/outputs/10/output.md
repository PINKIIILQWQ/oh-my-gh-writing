fix(connection): prevent pool leak in getConnection()

Wrap the connection acquisition and release in try/finally to ensure
the connection is always returned to the pool, even when the caller
throws an exception before calling release().

Previously, concurrent requests could exhaust the pool after ~50 rapid
calls because getConnection() did not guarantee release on error paths.
