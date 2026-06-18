# Standard Commit Standard

## Use When

Use when the user asks for a commit message, commit title, commit body, or Conventional Commit.

## Output Boundary

Commit messages summarize committed changes. Do not include uncommitted claims, test results, issue closing keywords, or breaking-change markers unless supported by the diff, user input, or repository convention.

## Standard Structure

Prefer Conventional Commits unless the target repository uses a different style:

```text
type(scope): concise summary

Optional body explaining why and important context.

Optional footer such as:
BREAKING CHANGE: ...
Refs: #123
```

Common types:

- `feat`: new capability
- `fix`: bug fix
- `docs`: documentation only
- `refactor`: behavior-preserving cleanup
- `test`: tests
- `chore`: tooling, config, maintenance
- `perf`: performance improvement with evidence
- `ci`: CI configuration
- `build`: build system or dependencies

## Missing Information

- If scope is unclear, omit it instead of guessing.
- If breaking-change intent is unclear, ask before adding `!` or `BREAKING CHANGE`.
- If issue IDs are unknown, omit `Fixes #...`.

## Do Not Invent

- Do not invent issue IDs, tests, breaking-change status, package names, or scopes.
- Do not use vague summaries such as `update files` or `fix stuff`.
- Do not include long explanations in the subject line.

## Good Output Shape

```text
docs(readme): clarify agent support matrix

Separate direct skill-directory installs from tools that need rule adaptation.
```

## Common Failure

- Adding `Fixes #123` without a real issue.
- Marking `!` or `BREAKING CHANGE` without confirmed breaking behavior.
- Using broad subjects such as `update docs` when the changed area is known.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| Conventional Commits | Type/scope/description and breaking-change footer |
| Commitizen / cz-cli | Prompted commit structure |
| Conventional Changelog | Commit metadata used for changelogs |
| Angular commit convention | Practical type and scope discipline |

## Checklist

- [ ] Subject is concise and imperative enough for git history.
- [ ] Type matches the change.
- [ ] Scope is included only when known.
- [ ] Breaking-change and issue footers are evidenced.
