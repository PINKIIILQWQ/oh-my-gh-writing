# 09 Code Review 测试

## Reviewed PR

`nextauthjs/next-auth` PR #12876: Improve error validation for Microsoft EntraID provider errors before decoding token.

The diff changes `packages/core/src/lib/actions/callback/oauth/callback.ts` to parse the OAuth token response JSON once, throw `OAuthCallbackError` when the Microsoft Entra ID response includes `error`, and only decode `id_token` after that check.

## Findings

No blocking findings.

The change is directionally sound: it prevents an OAuth error response from being treated as a JWT decode problem, which should make Entra ID callback failures easier to diagnose.

## Residual Risk

### `packages/core/src/lib/actions/callback/oauth/callback.ts` around the new `responseJson` branch

**Severity:** minor

The new branch checks `responseJson.error` before decoding `responseJson.id_token`, but it still assumes the non-error response contains a valid `id_token`.

That was also true before this PR, so it is not introduced as a new regression. Still, this area would benefit from a small regression test that covers:

- Entra ID error response with `error`
- successful response with `id_token`
- malformed non-error response without `id_token`

## Suggested Verification

- Add or confirm a test where the token endpoint returns an Entra-style body containing `error`.
- Assert that the thrown error message includes the provider error rather than a misleading JWT decode failure.
- Confirm the existing tenant-specific issuer re-processing still works when a valid `id_token` is present.

## Summary

I would not block this PR based on the reviewed diff. The main follow-up is test coverage around the new error branch and the existing malformed-response edge case.
