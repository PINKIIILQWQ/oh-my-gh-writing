# RFC: Operator Overloading for TypeScript

## Summary
Allow classes and interfaces to define custom behavior for JavaScript operators using an `operator` keyword.

## Motivation
Numeric computing, vector math, and DSL implementations currently require verbose method calls where operators would be more natural.

## Proposed Design (draft)
```ts
class Vector2D {
  constructor(public x: number, public y: number) {}

  operator +(other: Vector2D): Vector2D {
    return new Vector2D(this.x + other.x, this.y + other.y);
  }
}
```

## Operator Table
| Operator | Signature | Example |
|----------|-----------|---------|
| `+` | `operator +(other: T): T` | `a + b` |
| `-` | `operator -(other: T): T` | `a - b` |
| `*` | `operator *(other: T): T` | `a * b` |
| `/` | `operator /(other: T): T` | `a / b` |

## Backwards Compatibility
No breaking changes. Operator overloading is opt-in per class.

## Prior Art
- Python: `__add__`, `__mul__`
- Rust: `std::ops::Add`
- Kotlin: `operator fun plus()`

## Open Questions
1. Should interfaces be able to declare operators?
2. Interaction with `Symbol.toPrimitive`?
3. Transpilation target for ES5 compatibility?
