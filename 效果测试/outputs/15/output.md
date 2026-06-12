# 15 Migration Guide 测试

# Migrating from v1 REST API to v2 GraphQL API

## Overview

This guide describes a draft migration path from a v1 REST API to a v2 GraphQL API.

The prompt does not provide product-specific endpoint names, schemas, dates, authentication changes, deprecation windows, or tooling. Those details are marked as `TODO` or "to confirm" rather than invented.

## Migration Goals

- Replace endpoint-by-endpoint REST calls with GraphQL operations.
- Move response shaping from server-defined REST payloads to client-selected GraphQL fields.
- Keep behavior verifiable during migration by comparing v1 and v2 responses for the same user flows.

## Compatibility Status

| Area | v1 REST | v2 GraphQL | Migration status |
|------|---------|------------|------------------|
| Transport | HTTP endpoints | Single GraphQL endpoint | TODO: confirm endpoint URL |
| Authentication | TODO | TODO | To confirm |
| Pagination | Endpoint-specific | GraphQL connection or list fields | To confirm |
| Errors | HTTP status + response body | GraphQL `errors` plus partial `data` | Requires client handling changes |
| Versioning | URL or header based | Schema evolution | To confirm |

## Step 1: Inventory Existing REST Usage

Create a list of every v1 endpoint used by your application.

```text
GET /v1/users/:id
GET /v1/users/:id/projects
POST /v1/projects
PATCH /v1/projects/:id
```

For each endpoint, record:

- owning feature
- request parameters
- response fields actually used by the client
- error states handled by the client
- tests that cover the flow

## Step 2: Map REST Endpoints to GraphQL Operations

Draft one GraphQL query or mutation per user workflow, not necessarily one operation per REST endpoint.

| v1 REST call | v2 GraphQL operation | Notes |
|--------------|----------------------|-------|
| `GET /v1/users/:id` | `query User($id: ID!)` | Select only fields used by the client |
| `GET /v1/users/:id/projects` | `query UserProjects($id: ID!)` | Confirm pagination model |
| `POST /v1/projects` | `mutation CreateProject($input: CreateProjectInput!)` | Confirm validation errors |
| `PATCH /v1/projects/:id` | `mutation UpdateProject($id: ID!, $input: UpdateProjectInput!)` | Confirm partial update semantics |

## Step 3: Add a GraphQL Client Boundary

Introduce a small client module so feature code does not construct raw GraphQL requests everywhere.

```ts
export async function fetchUser(id: string) {
  return graphqlClient.request(UserDocument, { id })
}
```

Keep the old REST client available during migration so each feature can move independently.

## Step 4: Migrate Read Paths First

Start with low-risk read-only screens.

1. Add the GraphQL query.
2. Compare v1 and v2 data for the same entity.
3. Update the feature to read from the GraphQL client.
4. Keep REST fallback only if the product requires rollback support.

## Step 5: Migrate Write Paths

For mutations, confirm behavior before switching production traffic:

- validation error shape
- authorization failures
- idempotency behavior
- retry behavior
- partial success handling
- audit/logging behavior

Example draft mutation:

```graphql
mutation UpdateProject($id: ID!, $input: UpdateProjectInput!) {
  updateProject(id: $id, input: $input) {
    project {
      id
      name
      updatedAt
    }
    errors {
      code
      message
      field
    }
  }
}
```

## Step 6: Update Error Handling

REST clients often branch on HTTP status codes. GraphQL clients must also handle responses where `data` is partially present and `errors` is non-empty.

```ts
try {
  const result = await fetchUser(userId)
  return result.user
} catch (error) {
  // TODO: map GraphQL transport, auth, validation, and domain errors.
  throw error
}
```

## Step 7: Verification Plan

- [ ] Contract tests compare v1 and v2 responses for representative reads.
- [ ] Mutation tests cover success, validation failure, and authorization failure.
- [ ] Client error handling covers GraphQL `errors` with and without partial `data`.
- [ ] Observability dashboards distinguish v1 REST and v2 GraphQL traffic.
- [ ] Rollback behavior is documented for each migrated feature.

## Rollback Plan

TODO: confirm whether the application can keep both clients during rollout.

If dual clients are supported, use a feature flag or configuration switch per migrated feature. If dual clients are not supported, define a release rollback plan before migrating write paths.

## Deprecation Timeline

TODO: add official dates when available.

Do not remove v1 REST endpoints until:

- all production callers are migrated
- external API consumers have been notified
- monitoring shows no remaining v1 traffic
- support and rollback windows are approved

## Open Questions

- What is the v2 GraphQL endpoint URL?
- Does authentication change between v1 and v2?
- What pagination convention does the schema use?
- Are there schema-generated TypeScript types?
- Is there an official deadline for v1 REST removal?
