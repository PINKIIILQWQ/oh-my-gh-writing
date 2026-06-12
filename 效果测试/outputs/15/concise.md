---
scenario: Migration Guide
mode: concise
case-sources: https://github.com/mui/material-ui, https://github.com/remix-run/react-router
input-prompt: ../../prompts/15-migration-guide.md
---

# v1 REST → v2 GraphQL Migration

## Overview
Migrate from REST API (`/api/v1/`) to GraphQL (`/api/v2/graphql`).

## Key Changes
| v1 (REST) | v2 (GraphQL) |
|-----------|--------------|
| `GET /api/v1/users` | `query { users { ... } }` |
| `POST /api/v1/users` | `mutation { createUser(...) { ... } }` |
| `GET /api/v1/users/:id` | `query { user(id: ...) { ... } }` |

## Migration Steps
1. Replace `fetch` calls with GraphQL client (Apollo/URQL)
2. Update type definitions from REST responses to generated GraphQL types
3. Migrate pagination from `?page=1&limit=20` to cursor-based pagination

## Rollback
Keep v1 endpoints operational during transition period.
