# Changelog

## [0.9.0] - TBD

### Breaking Changes
- Python 3.8 support dropped
- Deprecated `--format` CLI flag removed

### New Rules
- `ruff rule --generate-docs` generates documentation for all rules
- New `flake8-tidy-imports` rules (TID251, TID252)

### Changes
- `[tool.ruff]` to `[tool.ruff.lint]` migration in configuration

### Fixes
- False positive in `F841` for tuple unpacking
- `RUF012` crash on class methods

**Source**: https://github.com/astral-sh/ruff/releases
