# 16 RFC 测试

# RFC Draft: Operator Overloading for TypeScript

## Summary

This RFC proposes an experimental operator overloading model for TypeScript that lets user-defined types declare behavior for operators such as `+`, `-`, `*`, and `/`.

This is a draft. It does not claim that TypeScript has accepted, scheduled, or implemented operator overloading.

## Motivation

Some TypeScript domains model values where operator notation is clearer than method calls:

- vectors and matrices
- complex numbers
- decimal or fixed-precision numeric types
- units of measure
- symbolic expressions

Today, these APIs usually use methods:

```ts
const total = price.add(tax).multiply(quantity)
```

Operator overloading could allow a more direct form:

```ts
const total = (price + tax) * quantity
```

The benefit is readability for mathematical domains. The risk is that operators can hide surprising behavior if overloads do not match user expectations.

## Prior Art

TypeScript issue #42218 proposes operator overloading and primitive type declarations and remains open with `Suggestion` and `Awaiting More Feedback` labels.

Rust exposes overloadable operators through traits in `std::ops`; only operators backed by traits can be overloaded, and Rust does not allow creating new operators through that module.

Python uses special methods such as `__add__` and related numeric protocol methods to emulate numeric behavior.

Kotlin uses named functions such as `plus`, `minus`, and `times`, marked with the `operator` modifier.

## Goals

- Let libraries define operator behavior for specific user-defined types.
- Keep overload resolution statically checkable.
- Preserve JavaScript runtime compatibility by lowering to method calls or helper calls.
- Avoid allowing arbitrary new operators.
- Make overload declarations discoverable in type definitions.

## Non-Goals

- Changing JavaScript runtime semantics.
- Adding custom operator precedence.
- Adding arbitrary symbolic operators.
- Guaranteeing algebraic laws such as commutativity or associativity.

## Proposed Design

### Operator Declaration

Operator overloads are declared with a reserved `operator` member syntax.

```ts
class Vector2 {
  constructor(
    readonly x: number,
    readonly y: number,
  ) {}

  operator +(right: Vector2): Vector2 {
    return new Vector2(this.x + right.x, this.y + right.y)
  }
}
```

This syntax is a proposal placeholder. The final syntax is an open question.

### Type Checking

For an expression:

```ts
left + right
```

The checker would:

1. Preserve current behavior for built-in JavaScript types.
2. If built-in behavior does not apply, look for a compatible overload on the left operand type.
3. Optionally look for a reflected overload on the right operand type if the left operand does not define one.
4. Report an error when overload resolution is ambiguous.

### Emit Strategy

The emit strategy is unresolved. A possible lowering is:

```ts
left[Symbol.operatorPlus](right)
```

or:

```ts
__operatorAdd(left, right)
```

This RFC does not assert that either strategy is viable. Runtime interop with plain JavaScript must be evaluated before adoption.

## Examples

```ts
const a = new Vector2(1, 2)
const b = new Vector2(3, 4)

const c = a + b
```

Expected static type:

```ts
Vector2
```

## Compatibility

Operator overloading would be a language-level addition and may affect parsing, type checking, declaration emit, editor tooling, and transpilation.

Potential compatibility concerns:

- Existing JavaScript expressions must keep current semantics.
- Mixed built-in and overloaded operands need predictable rules.
- Declaration files need a stable representation for overloads.
- Tooling must surface overload targets clearly in hover and go-to-definition.

## Drawbacks

- Operators can make code less obvious when overload behavior is surprising.
- Overload resolution may add complexity to the checker.
- Runtime lowering may be difficult to make ergonomic and efficient.
- JavaScript itself does not currently provide general operator overloading.

## Alternatives

### Keep method-based APIs

```ts
price.add(tax).multiply(quantity)
```

This is explicit and works today, but can be noisy for mathematical APIs.

### Use named static helpers

```ts
Decimal.add(price, tax)
```

This avoids language changes but does not improve expression readability.

### Wait for a JavaScript-level proposal

This would avoid TypeScript-only runtime semantics, but it depends on TC39 progress and may not address TypeScript-specific type modeling needs.

## Open Questions

- What syntax should declarations use?
- Should overloads be instance members, static members, symbols, interfaces, or declaration-only constructs?
- Should reflected operations such as `number + Decimal` be supported?
- How should overloads interact with union types and generics?
- How should `.d.ts` files represent operator declarations?
- Can emit preserve debugging and stack traces well enough?

## Implementation Plan

1. Collect use cases and constraints from TypeScript issue #42218 and related discussion.
2. Prototype parser and checker behavior behind an experimental flag.
3. Test a small set of operators first: `+`, `-`, `*`, `/`.
4. Validate declaration emit and editor tooling.
5. Revisit runtime lowering after prototype feedback.
