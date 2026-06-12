# Migrating from REST API v1 to GraphQL v2

## Overview
This guide covers migrating client applications from the legacy REST API
(`/api/v1/`) to the new GraphQL API (`/api/v2/graphql`). The v1 API will
be maintained for 6 months after the v2 GA release.

## Breaking Changes

### 1. Request format: URL params → Query document
**Before (REST):**
```js
const res = await fetch('/api/v1/users?page=1&limit=20');
const data = await res.json();
```

**After (GraphQL):**
```js
const query = `query ($page: Int, $limit: Int) {
  users(page: $page, limit: $limit) { id, name, email }
}`;
const result = await client.query({ query, variables: { page: 1, limit: 20 } });
```

### 2. Response format: Fixed → Flexible
REST returns fixed-shaped responses per endpoint.
GraphQL returns exactly the fields requested — no over-fetching.

### 3. Authentication
Same JWT token, passed as `Authorization` header in both cases.

## Migration Strategy
1. **Phase 1**: Install GraphQL client alongside existing REST calls
2. **Phase 2**: Migrate read operations (queries) one endpoint at a time
3. **Phase 3**: Migrate write operations (mutations)
4. **Phase 4**: Remove REST client and v1 endpoint calls

## Rollback
Set `USE_REST_V1=true` environment variable to fall back to REST.
Both APIs serve identical data during transition period.

## Timeline
- v2 GA: Today
- v1 deprecation notice: +3 months
- v1 sunset: +6 months
