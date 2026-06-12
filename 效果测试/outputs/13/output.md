# 13 CHANGELOG 测试

## [v10.0.0] - 2026-02-06

### Breaking Changes

- Require Node.js `^20.19.0 || ^22.13.0 || >=24` (#20160).
- Remove eslintrc support (#20037).
- Remove deprecated rule context methods (#20086).
- Remove deprecated `SourceCode` methods (#20137).
- Update `eslint:recommended` configuration (#20210).
- Enable JSX reference tracking (#20152).
- Report `eslint-env` comments as errors (#20128).
- Remove deprecated `LintMessage#nodeType` and `TestCaseError#type` (#20096).
- Replace `chalk` with Node.js `styleText` in the stylish formatter and add `color` to `ResultsMeta` (#20227).
- Deprecate `"always"` and `"as-needed"` options of the `radix` rule (#20223).

### Features

- Add `Array.fromAsync` handling in `array-callback-return` (#20457).
- Add `self` to the `no-implied-eval` rule (#20468).
- Improve handling of function and class expression names in `no-shadow` (#20432).
- Add RuleTester assertion option `requireData` (#20409).
- Output RuleTester test case failure index (#19976).
- Add `countThis` option to `max-params` (#20236).
- Add error assertion options (#20247).

### Bug Fixes

- Detect default `this` binding in `Array.fromAsync` callbacks (#20456).
- Fix regression of global mode report range in the `strict` rule (#20462).
- Remove fake `FlatESLint` and `LegacyESLint` exports (#20460).
- Fix failing test location estimation by using `Error.prepareStackTrace` (#20436).
- Ensure `filename` is passed as the third argument to `verifyAndFix()` (#20405).
- Correct RuleTester typings (#20105).
- Correct `no-restricted-import` messages (#20374).

### Documentation

- Add the v10.0.0 migration guide (#20143).
- Document `meta.docs.frozen` (#20475).
- Document support for the `:is` selector alias (#20454).
- Document policies about ESM-only dependencies (#20448).
- Keep v10 migration guide references consistent (#20328).

### Chores and Build

- Add type integration test for `@html-eslint/eslint-plugin` (#20345).
- Rename workflows (#20463).
- Pin dependencies (#20397).
- Update `js-yaml` to v4 for security (#20319).

### Migration Notes

See the v10 migration guide for concrete upgrade steps, especially Node.js version support, flat config requirements, JSX reference tracking, and removed deprecated APIs.
