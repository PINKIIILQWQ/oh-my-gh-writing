# Migrating from REST API v1 to GraphQL v2

## Overview
This guide covers migrating client applications from REST (`/api/v1/`) to GraphQL (`/api/v2/graphql`).

## Key Changes

| Area | v1 (REST) | v2 (GraphQL) |
|------|-----------|--------------|
| Endpoint | `/api/v1/users/:id` | `query { user(id: $id) }` |
| Request body | JSON body | Query document + variables |
| Response shape | Fixed per endpoint | Client-specified fields |
| Pagination | `?page=1&limit=20` | Cursor-based (relay-style) |
| Auth | `Authorization: Bearer <token>` | Same header |

## Migration Steps
1. Install a GraphQL client (the specific client depends on your framework)
2. Migrate read operations one endpoint at a time — start with a simple `GET` endpoint
3. Migrate write operations after all reads are verified
4. Remove REST client after all endpoints are migrated

## Rollback
Keep the v1 REST endpoints operational. Set a feature flag to toggle between v1 and v2 clients.

## Timeline
TBD — coordinate with API provider for v1 deprecation schedule.
