# Maintainer Response Standard

## Use When

Use when the user wants to draft a GitHub comment or reply in an existing issue, pull request, pull request review thread, or discussion.

This also covers saved replies for GitHub issues, pull requests, and discussions when the requested output is reusable comment text.

Route here for:

- Issue triage comments: request more information, confirm actionable status, explain duplicate or not planned decisions, provide workaround notes, or close with context.
- Pull request replies: respond to reviewer comments, summarize addressed feedback, explain why a suggestion was not taken, or request re-review.
- Discussion replies: answer a question, summarize current direction, explain next steps, or suggest converting a discussion into an issue, RFC, or PR.
- Saved reply drafts: reusable maintainer responses that do not depend on hidden repository policy.

Do not use this for a new bug report, feature request, PR description, code review finding, release note, or discussion starter. Route those to their own artifact standards.

## Output Boundary

Output the comment body itself. Do not post the comment, close issues, resolve conversations, request changes, approve PRs, mark answers, lock discussions, apply labels, assign milestones, or modify remote state unless the user explicitly asks and the active environment supports that operation.

For normal single-comment requests, produce only the comment body. For complex or high-risk replies, put any caveats after the comment under `Submission Notes`, not inside the comment body.

## Required Evidence

Use target-repository evidence before relying on generic wording when the response depends on project policy or maintainer authority.

Evidence is required for:

- Duplicate issue or PR numbers.
- Labels, milestones, projects, assignees, support channels, or security policy.
- Maintainer decisions such as closing, locking, marking as not planned, accepting a proposal, requesting changes, or approving a PR.
- Test results, CI status, fixed commits, release versions, regression status, or reproduction status.
- Discussion category behavior, including whether answers can be marked.

If evidence is missing, ask briefly when the missing fact changes the action. Otherwise use neutral phrasing such as `I cannot confirm this yet` or `To make this actionable, please provide...`.

## Standard Shapes

### More Information Request

```markdown
Thanks for the report.

I need a little more information before this is actionable:

- ...

Once you provide that, we can confirm whether this is reproducible and decide the next step.
```

### Duplicate / Existing Thread

```markdown
Thanks for opening this.

This appears to overlap with #TBD. I am going to keep the discussion there so the context stays in one place.

If your case is different, please add the missing details here before this is closed:

- ...
```

Use only when the duplicate target is provided or confirmed.

### PR Review Reply

```markdown
Thanks for the review.

I addressed this by ...

Verification:

- ...

Could you take another look when you have a chance?
```

If the feedback was not implemented, explain the reason and offer an alternative without sounding dismissive.

### Discussion Answer

```markdown
Thanks for the context.

The current direction I would suggest is ...

Reasoning:

- ...

Next step:

- ...
```

Do not claim consensus, roadmap commitment, or maintainer approval unless the user provided that evidence.

### Saved Reply

```markdown
Thanks for reaching out.

To help us investigate, please provide:

- Minimal reproduction:
- Expected behavior:
- Actual behavior:
- Environment:

Without those details, we may not be able to confirm whether this is a bug.
```

Keep saved replies generic enough to reuse. Do not include repository-specific policy unless it is sourced from the target repository.

## Tone Rules

- Be direct, calm, and respectful.
- Prefer specific next steps over vague thanks-only replies.
- Separate empathy from unsupported promises.
- Avoid blame, sarcasm, passive aggression, or public shaming.
- When declining or closing, explain the reason and what would change the decision.
- Use `we` only when the speaker is actually representing maintainers; otherwise use neutral phrasing.

## Missing Information

Ask a short follow-up when the response requires one of these choices:

- Whether the comment should close, defer, or keep the thread open.
- Whether a PR reply should say the feedback was implemented or intentionally not implemented.
- Whether the response is from a maintainer, contributor, or neutral helper.
- Which duplicate issue, policy, version, test result, or support channel should be cited.

Do not ask when a conservative comment can safely request missing information.

## Do Not Invent

- Do not invent duplicate links, issue IDs, PR IDs, labels, milestones, owners, support policy, security policy, test results, fix commits, or release versions.
- Do not say `Fixed`, `Resolved`, `Closing`, `Marked as answer`, `Approved`, `Requested changes`, or `LGTM` unless the user explicitly wants that action or wording and provides evidence.
- Do not imply that a comment has been posted.
- Do not include private or security-sensitive information in public comment text.
- Do not turn a reply into a full issue, PR description, or review unless the user asks for that artifact.

## Common Failure

- Writing a new issue instead of a reply to an existing issue.
- Producing code review findings when the user asked to respond to existing review feedback.
- Closing or rejecting a report without explaining the evidence boundary.
- Saying a fix was verified when tests or CI were not provided.
- Hiding required maintainer decisions inside a friendly comment.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub PR comments docs | Conversation comments, line comments, and replying to existing review comments |
| GitHub PR review docs | Separating comment, approve, and request-changes actions |
| GitHub Discussions docs | Discussion replies, answers, and community participation |
| GitHub saved replies docs | Reusable replies across issues, PRs, and discussions |
| GitHub Issues docs | Closing or converting issue context requires evidence and user intent |

## Checklist

- [ ] The output is a comment/reply body, not a different GitHub artifact.
- [ ] The response states a concrete next step.
- [ ] Any maintainer action is evidenced or framed as a suggestion.
- [ ] No repository policy, issue ID, status, or test result is invented.
- [ ] Submission notes, if needed, are outside the comment body.
