---
scenario: Feature Request
mode: concise
case-sources: https://github.com/apache/dubbo, https://github.com/microsoft/typescript
input-prompt: ../../prompts/02-feature-request.md
---

### Feature: PostgreSQL PARTITION BY support in Prisma

**Current limitation**
Prisma schema cannot define PostgreSQL table partitioning, requiring raw SQL.

**Proposed API**
<code>model EventLog { id String @id @default(cuid()) createdAt DateTime @default(now()) event String @@partitionBy("RANGE (created_at)") @@partition("p2024", "VALUES LESS THAN ('2025-01-01')") }</code>

**Alternatives**
1. Raw SQL in migration - breaks schema readability
2. pg_partman extension - adds external dependency
