---
scenario: RFC
mode: concise
case-sources: https://github.com/python/peps, https://github.com/tc39/proposals
input-prompt: ../../prompts/16-rfc.md
---

# RFC: Operator overloading in TypeScript

## Summary
Allow developers to define custom behavior for arithmetic operators
on user-defined types using an `operator` keyword.

## Motivation
```
// Currently impossible:
type Vector2D = { x: number, y: number };
const a: Vector2D = { x: 1, y: 2 };
const b: Vector2D = { x: 3, y: 4 };
const c = a + b; // Error: Operator '+' cannot be applied to types
```

## Proposed API
```ts
class Vector2D {
  constructor(public x: number, public y: number) {}

  operator +(other: Vector2D): Vector2D {
    return new Vector2D(this.x + other.x, this.y + other.y);
  }

  operator *(scalar: number): Vector2D {
    return new Vector2D(this.x * scalar, this.y * scalar);
  }
}
```

## Open Questions
1. Should operators be limited to class members?
2. Interaction with `Symbol.toPrimitive`?
