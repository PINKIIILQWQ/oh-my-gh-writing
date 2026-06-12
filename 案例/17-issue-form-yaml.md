# Issue Form YAML — 经典案例

---

## 精细版（完整 YAML 表单）

### 案例 1：Prometheus (56k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: Bug Report
about: Report a bug in Prometheus
---

### Bug Description

### Steps to Reproduce

### Expected vs Actual Behavior

### Environment
- Prometheus version:
- OS:
- Deployment (Docker/K8s/binary):
```

---

### 案例 2：Apache Cassandra (9k⭐)

**来源：** JIRA (非 GitHub Issues)

Cassandra 使用 JIRA 进行 issue 管理，Bug Report 必填字段：

- Description
- Steps to Reproduce  
- Environment (Cassandra version, OS, Java)
- Logs

---

### 案例 3：Envoy Proxy (25k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.yml`

Envoy 的 YAML Issue Form：

- Title with area prefix（`[area]`）
- Description (required)
- Reproduction (required) — config + steps
- Environment (required) — Envoy version, OS
- Logs (optional)

---

## 普通版（精简 YAML 表单）

### 案例 4：Hashicorp Nomad (15k⭐)

简洁 Markdown 模板：

```markdown
#### Overview
#### Reproduction Steps
#### Environment
#### Logs
```

### 案例 5：Mozilla (Firefox)

Bugzilla 模板：

- Summary
- Steps to Reproduce
- Expected Results
- Actual Results
- Additional Information

### 案例 6：Envoy Proxy (25k⭐)

Markdown 模板：Description → Reproduction → Config → System Info

---

### 附加参考

**apache/hive (15k⭐)** — JIRA Issue 表单：组件 + 版本 + 环境 + 日志。
**hashicorp/terraform-docs (45k⭐)** — Provider 级 Issue 表单：Terraform 版本 + Provider 版本 + 配置。
**grpc/grpc-go (42k⭐)** — 语言绑定的环境字段，自动采集 label。

---

> 收集日期：2026-06-12
