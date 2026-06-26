# Contributing

Thanks for helping improve `oh-my-gh-writing`. This repository is a portable GitHub writing skill, so contributions should keep the runtime path small, evidence-based, and easy for agents to load.

## What to Contribute

- Scenario rule fixes in `references/*.md`
- Source quality updates in `references/source-catalog.md`
- README, install, or cross-agent wording fixes
- Output hygiene and fact-boundary improvements
- Small GitHub Markdown utility additions such as emoji, badges, alerts, or Mermaid guidance
- Case reports that show where the skill works well or fails

## Contribution Principles

- Keep `SKILL.md` focused on routing and shared runtime rules.
- Put scenario-specific guidance in the matching `references/*.md`.
- Keep long reference material out of the normal runtime path.
- Do not add generated test outputs, private notes, or large case collections to the public repository.
- Do not copy project-specific facts from reference repositories into this skill's general rules.

## Reference Sources

When proposing a source link:

- Prefer official docs, official specs, current templates, contribution guides, single release pages, migration guides, or RFC processes.
- Avoid search pages, issue lists, PR lists, discussion lists, repository homepages, and release indexes as primary evidence.
- Explain which rule or field the source improves.
- Check that the link is current before submitting.

## Case Contributions

Cases are valuable, but they can easily bloat the repository or leak irrelevant test material. For now, submit cases through an issue or discussion before opening a PR with files.

Case reports should include:

- Source repository or public artifact URL
- Scenario, such as README, Bug Report, Feature PR, Release Notes, or Issue Form YAML
- What the case is meant to test
- Whether the source is public and safe to reference
- Any privacy, license, attribution, or cleanup notes
- The observed output problem or quality improvement opportunity

Do not submit large batches of copied artifacts without prior discussion. If a case later becomes a public example, it should be cleaned, attributed, and clearly marked as illustrative rather than a factual source for user projects.

## Contributor Recognition

This project uses the [All Contributors](https://allcontributors.org/) specification for README contributor recognition.

If your contribution is merged and you want to be listed, mention the contribution type in your PR or follow-up issue, such as `code`, `doc`, `ideas`, `design`, `maintenance`, or `test`. Maintainers should update `.all-contributorsrc` and the README contributor tables in the same PR or follow-up maintenance commit.

## Pull Request Checklist

- [ ] The change keeps normal runtime loading narrow.
- [ ] New rules distinguish evidence from examples.
- [ ] Links are current and useful for the target scenario.
- [ ] README-facing changes are reflected in `references/readme.md` when needed.
- [ ] No local validation outputs, private notes, or unrelated cases are included.

## Validation Before PR

Before opening a PR:

1. Run `ruby scripts/validate-yaml.rb SKILL.md .github/ISSUE_TEMPLATE/*.yml` when changing skill frontmatter or Issue Forms.
2. Run `python3 scripts/validate-runtime-layout.py` when changing runtime files or installation guidance.
3. Run `python3 scripts/validate-evals.py` when eval fixtures change, and run basic Markdown/JSON checks for changed files.
4. Run `python3 scripts/validate-cases.py` when public case evidence changes.
5. Add or update at least one eval when changing `SKILL.md` routing, description triggers, workflow packs, or output hygiene rules.
6. For scenario rule changes, include either a short `Good output shape` / `Common failure` note or an eval expected output when the change affects artifact shape.
7. Confirm `SKILL.md`, `INDEX.md`, README files, and `references/` paths stay synchronized.
8. Keep `README.md` canonical and update `README.zh-CN.md` when public-facing README content changes.
