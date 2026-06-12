### Feature: PostgreSQL PARTITION BY support in Prisma schema

**Motivation**
Time-series data tables (event logs, metrics, audit trails) benefit from PostgreSQL's declarative table partitioning. Currently Prisma has no way to express `PARTITION BY RANGE` or `PARTITION BY LIST` in schema.prisma, forcing users to post-process migrations with raw SQL.

**Use cases**
1. Event log table with 10M+ rows/month partitioned by `created_at` for query performance
2. Multi-tenant data partitioned by `tenant_id` for faster full-table scans
3. Archival: drop old partitions instead of running `DELETE` or `VACUUM`

**Proposed API (draft)**
```prisma
model EventLog {
  id        String   @id @default(cuid())
  createdAt DateTime @default(now())
  event     String

  @@partitionBy("RANGE (created_at)")
  @@partition("p2024", "VALUES LESS THAN ('2025-01-01')")
  @@partition("p2025", "VALUES LESS THAN ('2026-01-01')")
}
```

**Alternatives considered**
1. Raw SQL in migration files — works but schema doesn't reflect actual table structure
2. pg_partman extension — adds external dependency, not Prisma-managed
3. Application-level sharding — moves concern to app layer, adds complexity

**Compatibility**
Non-breaking additive change. PostgreSQL 12+ required for declarative partitioning. Existing schemas without `@@partitionBy` continue working identically.
