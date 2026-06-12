# PR Template — 经典案例（完整原文）

---

## 精细版（完整 PR 模板原文）

### 案例 1：apache/flink (24k⭐)

**仓库：** https://github.com/apache/flink
**模板来源：** https://raw.githubusercontent.com/apache/flink/master/.github/PULL_REQUEST_TEMPLATE.md

```
<!--
*Thank you very much for contributing to Apache Flink - we are happy that you want to help us improve Flink. To help the community review your contribution in the best possible way, please go through the checklist below, which will get the contribution into a shape in which it can be best reviewed.*

*Please understand that we do not do this to make contributions to Flink a hassle. In order to uphold a high standard of quality for code contributions, while at the same time managing a large number of contributions, we need contributors to prepare the contributions well, and give reviewers enough contextual information for the review. Please also understand that contributions that do not follow this guide will take longer to review and thus typically be picked up with lower priority by the community.*

## Contribution Checklist

  - Make sure that the pull request corresponds to a JIRA issue. Exceptions are made for typos in JavaDoc or documentation files, which need no JIRA issue.
  
  - Name the pull request in the form "[FLINK-XXXX] [component] Title of the pull request", where *FLINK-XXXX* should be replaced by the actual issue number. Skip *component* if you are unsure about which is the best component.
  Typo fixes that have no associated JIRA issue should be named following this pattern: `[hotfix] [docs] Fix typo in event time introduction` or `[hotfix] [javadocs] Expand JavaDoc for PuncuatedWatermarkGenerator`.

  - Fill out the template below to describe the changes contributed by the pull request. That will give reviewers the context they need to do the review.
  
  - Make sure that the change passes the automated tests, i.e., `mvn clean verify` passes.

  - Each pull request should address only one issue, not mix up code from multiple issues.
  
  - Each commit in the pull request has a meaningful commit message (including the JIRA id)

  - Once all items of the checklist are addressed, remove the above text and this checklist, leaving only the filled out template below.

(The sections below can be removed for hotfixes of typos)
-->

## What is the purpose of the change

*(For example: This pull request makes task deployment go through the blob server, rather than through RPC. That way we avoid re-transferring them on each deployment (during recovery).)*

## Brief change log

*(for example:)*
  - *The TaskInfo is stored in the blob store on job creation time as a persistent artifact*
  - *Deployments RPC transmits only the blob storage reference*
  - *TaskManagers retrieve the TaskInfo from the blob cache*

## Verifying this change

*(Please pick either of the following options)*

This change is a trivial rework / code cleanup without any test coverage.

*(or)*

This change is already covered by existing tests, such as *(please describe tests)*.

*(or)*

This change added tests and can be verified as follows:

*(example:)*
  - *Added integration tests for end-to-end deployment with large payloads (100MB)*
  - *Extended integration test for recovery after master (JobManager) failure*
  - *Added test that validates that TaskInfo is transferred only once across recoveries*
  - *Manually verified the change by running a 4 node cluster with 2 JobManagers and 4 TaskManagers*

## Does this pull request potentially affect one of the following parts:

  - Dependencies (does it add or upgrade a dependency): (yes / no)
  - The public API, i.e., is any changed class annotated with `@Public(Evolving)`: (yes / no)
  - The serializers: (yes / no / don't know)
  - The runtime per-record code paths (performance sensitive): (yes / no / don't know)
  - Anything that affects deployment or recovery: JobManager (and its components), Checkpointing, Kubernetes/Yarn, ZooKeeper: (yes / no / don't know)
  - The S3 file system connector: (yes / no / don't know)

## Documentation

  - Does this pull request introduce a new feature? (yes / no)
  - If yes, how is the feature documented? (not applicable / docs / JavaDocs / not documented)

-----

##### Was generative AI tooling used to co-author this PR?

- [ ] Yes (please specify the tool below)

<!--
Generated-by: [Tool Name and Version]
-->
```

---

### 案例 2：apache/rocketmq (21k⭐)

**仓库：** https://github.com/apache/rocketmq
**模板来源：** https://raw.githubusercontent.com/apache/rocketmq/master/.github/PULL_REQUEST_TEMPLATE.md

```
<!-- Please make sure the target branch is right. In most case, the target branch should be `develop`. -->

### Which Issue(s) This PR Fixes

<!-- Please ensure that the related issue has already been created, and link this pull request to that issue using keywords to ensure automatic closure. -->

Fixes #issue_id

### Brief Description

<!-- Write a brief description for your pull request to help the maintainer understand the reasons behind your changes. -->

### How Did You Test This Change?

<!-- In order to ensure the code quality of Apache RocketMQ, we expect every pull request to have undergone thorough testing. -->
```

---

### 案例 3：kubernetes/kompose (9k⭐)

**仓库：** https://github.com/kubernetes/kompose
**模板来源：** https://raw.githubusercontent.com/kubernetes/kompose/main/.github/PULL_REQUEST_TEMPLATE.md

```
#### What type of PR is this?

<!--
Add one of the following kinds:
/kind bug
/kind cleanup
/kind feature
/kind design
/kind documentation
-->

#### What this PR does / why we need it:

#### Which issue this PR fixes:

<!--
Usage: Fixes #<issue number>, or Fixes (paste link of issue)
-->

#### Special notes for your reviewer:

#### Does this PR introduce a user-facing change?

<!--
If no, just write "NONE" in the release-note block below.
If yes, a release note is required:
-->

```release-note

```
```

---

## 普通版（简洁 PR 模板）

### 案例 4：Homebrew/brew (42k⭐)

**仓库：** https://github.com/Homebrew/brew
**模板来源：** https://raw.githubusercontent.com/Homebrew/brew/master/.github/PULL_REQUEST_TEMPLATE.md

```
- [ ] Have you followed the guidelines in our Contributing document?
- [ ] Have you checked to ensure there aren't other open Pull Requests for the same change?
- [ ] Have you added an explanation of what your changes do and why?
- [ ] Performance claims must include Hyperfine benchmarks.
- [ ] Have you written new tests for your changes?
- [ ] Have you successfully run `brew lgtm` with your changes locally?
-----
- [ ] AI was used to generate or assist with generating this PR.
```

### 案例 5：Kubernetes (in general)

Kubernetes 风格的 PR 模板强调：
- What this PR does / why we need it
- Which issue this PR fixes
- Special notes for reviewers
- Checklist: tests, docs, breaking changes

### 案例 6：Docker (34k⭐)

**仓库：** https://github.com/docker/compose
**模板来源：** https://raw.githubusercontent.com/docker/compose/main/.github/PULL_REQUEST_TEMPLATE.md

```
**What I did**

**Related issue**
<!-- If this is a bug fix, make sure your description includes "fixes #xxxx", or "closes #xxxx" -->

**(not mandatory) A picture of a cute animal, if possible in relation to what you did**
```

---

> 收集日期：2026-06-12
