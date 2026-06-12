## Feature Request: PostgreSQL PARTITION BY in Prisma Schema

### Motivation
Time-series data tables in PostgreSQL benefit greatly from table partitioning.
Currently Prisma has no declarative way to express PARTITION BY in schema.prisma,
forcing users to post-process migrations with raw SQL. This breaks the
declarative workflow and makes partitioning invisible to Prisma Studio,
type generation, and migration previews.

### Use Case 1: Event log time partitioning
An analytics app stores 10M+ event log rows per month. Without partitioning,
query performance degrades and `DELETE` for old data is slow.

### Use Case 2: Multi-tenant data isolation
A SaaS platform partitions customer data by tenant_id for faster scans.

### Proposed API
<code>model EventLog {
  @@partitionBy("RANGE (created_at)")
  @@partition("p2024", "VALUES LESS THAN ('2025-01-01')")
}</code>

### Compatibility
- PostgreSQL 12+ required (declarative partitioning)
- Non-breaking: existing schemas unaffected
- Raw SQL fallback preserved for complex partitioning strategies
