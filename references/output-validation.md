# Output Validation

## Use When

Apply this internal validation layer before final output for every scenario. It is not a user-facing scenario; it checks whether the artifact can be pasted into the target GitHub location without extra explanation.

## Output Cleanliness

The target output must be the GitHub artifact itself. Conversational explanations, file-separator headings, and fenced wrappers are allowed only as multi-file display wrappers; they must not become part of a single target file.

Forbidden content:

- Conversational prefaces such as "Here is", "You can copy this", or "I wrote this for you".
- Test titles such as `# 02 Feature Request Test`.
- Whole-document outer Markdown fences such as wrapping an entire README or Issue in ```markdown.
- Copy pollution: extra backticks, terminal residue, unrelated docker-compose snippets, or half-open code blocks.
- Source lists, test metadata, source metadata, or input prompts unless the user explicitly asked for a test report.
- Checked checklist items without evidence. Template, future-work, and to-verify items stay unchecked by default.

Allowed content:

- When the user asks to display multiple YAML/Markdown files in chat, use `## File: ...` headings plus fenced blocks. These wrappers are display-only and not file content.
- When writing a single target file, output only file content.
- When Issue/PR bodies need code, logs, diffs, or config, use local fenced code blocks.

## Evidence Boundaries

| Fact type | Valid sources |
|-----------|---------------|
| Version, date, release URL | User input, release page, tag, CHANGELOG |
| PR/Issue number, commit hash | Diff, GitHub page, repository history, user input |
| Test result, CI name, workflow name | Tool output, CI config, user input |
| Install command, package name, Node/Rust/Python version | Package/config files, official docs, user input |
| Platform support, compatibility range, migration timeline | Official docs, release notes, repository files, user input |
| Screenshot, GIF, Star History, badge | Repository assets, user assets, official service, verifiable link |

When evidence is missing:

- Write `TODO`, `TBD`, or `To confirm`.
- Remove optional sections.
- Frame causes as `Suspected cause` or `Needs confirmation`.
- Do not use model memory or reference-project facts as target-project facts.

## Routing Validation

| Output symptom | Label |
|----------------|-------|
| Future capability request is written as an implemented PR | ROUTING_FAIL |
| "Turn a PR postmortem into a Feature Request" is written as a PR description | ROUTING_FAIL |
| Line-level review appears without a diff | FORMAT_FAIL |
| PR description claims tests passed without evidence | FACT_CHECK_REQUIRED |
| Discussion decides the solution for the user | DRAFT_ONLY |
| README is wrapped in a whole-document code block | FORMAT_FAIL |
| README lacks project applicability scope, or uses features/scenarios as applicability scope | FACT_CHECK_REQUIRED |
| YAML file includes explanatory headings when meant for direct file write | FORMAT_FAIL |
| Composite workflow publishes, tags, opens PRs, or modifies remote state by default | FORMAT_FAIL |
| Audit-only readiness review creates files or package drafts | FORMAT_FAIL |

## Validation Labels

| Label | Meaning |
|-------|---------|
| PASS | Can be submitted to the target GitHub location as-is |
| PASS_AFTER_CLEANUP | Content is sound but needs wrapper, title, placeholder, or format cleanup |
| DRAFT_ONLY | Useful draft but not directly submit-ready |
| ROUTING_FAIL | Wrong scenario or workflow route |
| FACT_CHECK_REQUIRED | Fact-heavy content lacks sources or confirmation |
| FORMAT_FAIL | Format is not submit-ready |

## Post-output Submission Notes

Validation is silent by default. Do not add scores.

Add a short `Submission Notes` block after the artifact only when one of these is true:

- The output is a large or multi-file artifact, such as README, CONTRIBUTING, CHANGELOG, release materials, migration guide, RFC, issue forms, PR template sets, or any composite workflow package.
- The output contains unresolved `TODO`, `TBD`, `To confirm`, unrun tests, missing required target-repository fields, or unsupported publication/install/support claims.
- The route is correct but the artifact is still `DRAFT_ONLY`, `PASS_AFTER_CLEANUP`, or `FACT_CHECK_REQUIRED`.
- The user explicitly asks whether the result is ready to submit.

Do not estimate readiness by word count or line count. Use structural signals: number of files, number of target locations, fact density, required confirmations, publishing risk, and whether the draft can be pasted without misleading maintainers.

For small artifacts with no obvious issue, omit the notes. When notes are needed, keep them outside the target artifact:

```markdown
## Submission Notes

- Blocking: confirm the test command before submitting.
- Suggested: replace `TBD` with the real target version.
```

## Pre-submission Checklist

- [ ] No test title or test metadata.
- [ ] No whole-document outer `markdown` fence.
- [ ] No conversational preface or ending.
- [ ] No unrelated code snippet, terminal residue, or copy pollution.
- [ ] No unexplained, unactionable, or submission-inappropriate `#XXXXX`, `Fixes #`, `TODO`, or `TBD`.
- [ ] No checklist item is checked without proof from user input, repository files, diff, or tool output.
- [ ] YAML parses; multi-file display and single-file write boundaries are clear.
- [ ] Markdown tables, code blocks, details, and alerts render correctly.
- [ ] README has clear project applicability scope and does not confuse features, built-in scenarios, or examples with applicability.
- [ ] PR/Review does not claim unrun tests.
- [ ] Scenario route matches the user request.
- [ ] Composite workflows default to local `.github-writing/...` drafts unless publishing is explicitly requested.
- [ ] Audit-only prompts produce recommendations only and do not create files or package drafts.
- [ ] High-risk facts have sources or are marked for confirmation.

## Maintainer Local Validation

For local regression testing, use a three-layer file set:

```text
.local-validation/<number>-<scenario>/
  input.md
  output.raw.md
  output.clean.md
  verdict.md
```

- `output.raw.md` preserves raw agent output to observe pollution.
- `output.clean.md` contains only a submit-ready artifact, without test titles or explanations.
- `verdict.md` records label, source, exposed problem, and whether the skill needs changes.

Do not treat `output.clean.md` as a showcase report. It must satisfy "can be pasted into GitHub without explanation".
