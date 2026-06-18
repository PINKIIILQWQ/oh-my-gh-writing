# Evaluation Fixtures

This directory contains lightweight fixtures for maintaining `oh-my-gh-writing`.

These files are not runtime references. Agents should not load them for normal GitHub writing tasks unless the user is explicitly testing or improving the skill.

## Files

| Path | Purpose |
|------|---------|
| `trigger-queries.json` | Positive and negative prompts for checking whether `SKILL.md` should trigger |
| `evals.json` | Output-quality tasks with expected routes, output types, assertions, and containment checks |
| `schema.json` | Schema for `evals.json` fields such as `expected_route`, `output_type`, `risk_category`, `assertions`, `must_contain`, and `must_not_contain` |
| `expected/` | Short clean outputs that illustrate passable artifact shape |
| `runs/` | Local raw validation outputs only; ignored by git |

## Labels

Use these labels when reviewing eval results:

| Label | Meaning |
|-------|---------|
| `PASS` | Output is usable as the target GitHub artifact without cleanup |
| `PASS_AFTER_CLEANUP` | Content is useful but formatting or residue must be cleaned |
| `ROUTING_FAIL` | The wrong artifact or workflow pack was selected |
| `FORMAT_FAIL` | Markdown/YAML shape is not valid for the target location |
| `FACT_CHECK_REQUIRED` | High-risk facts lack evidence or confirmation |
| `DRAFT_ONLY` | Output is useful only as a rough draft |

## Maintenance

- Validate fixtures with `python3 scripts/validate-evals.py` from the repository root.
- Keep expected outputs short and sanitized.
- Do not add copied private artifacts, large case collections, or raw local validation logs.
- Keep raw run outputs under `evals/runs/`; they are local-only and ignored. Public run results need a reviewed manifest, grading notes, and sanitized excerpts.
- Add or update an eval when changing `SKILL.md` routing, a workflow pack, or an output hygiene rule.
- Expected outputs should demonstrate artifact shape, not claim project-specific facts.
