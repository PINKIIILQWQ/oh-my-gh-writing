## Discussion: Microservice granularity strategy

### Background
Our platform runs 12 microservices across 3 domains (auth, billing, content).
Two services handle < 0.5% of total requests each but require full DevOps tooling:
separate K8s deployments, Helm charts, monitoring dashboards, alert rules, and
on-call rotations. The cognitive load of managing 12 codebases for 8 engineers
is causing context-switching overhead.

### Options considered

#### Option A: Merge low-traffic services
- Merge the 2 smallest services into their closest domain neighbor
- Reduces service count to 10
- Simplifies deployment pipeline
- Risk: larger deployment blast radius

#### Option B: Keep current, add tooling
- Invest in internal platform tooling to reduce per-service overhead
- Standardize templates for faster service setup
- Risk: tooling investment may not pay off

#### Option C: Strategic merge + future split
- Merge now, establish clear extraction criteria for future split
- Document bounded contexts for each domain
- Risk: "temporary" merge becomes permanent

### Recommendation
Option A with a 6-month review cycle. Define metrics:
- Service actively receiving feature requests (keep)
- Service unchanged for 3+ months (merge candidate)
