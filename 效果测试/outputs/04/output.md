# 04 Discussion 测试

## Discussion: Should we split services further or consolidate some boundaries?

## Background

Our team is revisiting the current microservice boundaries. Some services may be too broad, while others may be small enough that coordination, deployment, and observability overhead now outweigh the benefits.

We would like to hear from teams that have gone through either direction:

- splitting a service into smaller owned units
- merging several small services back into a larger service
- keeping boundaries stable and improving contracts/tooling instead

## What We Are Trying to Improve

The decision affects day-to-day engineering work, not just architecture diagrams.

Areas we are considering:

- release frequency and deployment risk
- incident ownership
- local development setup
- cross-service transaction complexity
- observability and tracing
- team ownership and on-call load
- API versioning and backwards compatibility

## Options

| Option | Potential benefits | Potential costs |
|--------|--------------------|-----------------|
| Split services further | Smaller ownership units, narrower deploys, clearer domain boundaries | More network calls, more CI/deploy pipelines, harder local setup, more distributed failure modes |
| Consolidate some services | Simpler debugging, fewer deployables, easier local development, fewer cross-service calls | Larger codebase boundaries, broader ownership, potentially slower releases for unrelated areas |
| Keep current boundaries | Avoids churn and migration risk | Does not address existing pain if boundaries are already wrong |
| Improve contracts/tooling first | May solve coordination issues without a service migration | Does not help if the underlying domain boundary is genuinely incorrect |

## Questions for the Community

1. What signals told you a service boundary was too fine-grained?
2. What signals told you a service needed to be split?
3. Did you use team ownership, domain model boundaries, data ownership, traffic patterns, or deployment frequency as the main decision factor?
4. How did you handle migrations when consolidating or splitting services?
5. What metrics helped after the change: incident count, deployment frequency, lead time, local setup time, or something else?

## Current Leaning

We are not looking for a rule like "microservices are good" or "monoliths are better." The useful outcome would be a decision framework we can apply per boundary.

In particular, we are interested in examples where teams reversed an earlier microservice split and what they learned from that process.
