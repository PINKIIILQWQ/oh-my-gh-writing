### Discussion: Microservice granularity strategy

**Background**
A team of 8 manages 12 microservices. Two services handle < 1% of requests each but require separate CI/CD pipelines, Kubernetes deployments, monitoring dashboards, and on-call rotations.

**Options**

| Approach | Pros | Cons |
|----------|------|------|
| Merge low-traffic services | Fewer pipelines, simpler deploys | Larger deployment blast radius |
| Keep current split | Independent scaling per service | High per-service operational overhead |
| Strategic merge with extraction criteria | Balanced approach | Requires clear bounded-context definition |

**Questions for community**
1. What traffic or team-size threshold justifies a separate service?
2. When merging, how do you handle databases that were per-service?
3. How do you decide between merging now vs. investing in tooling to reduce per-service overhead?
