---
scenario: RFC
mode: full-detail
case-sources: https://github.com/python/peps, https://github.com/kubernetes/enhancements
input-prompt: ../../prompts/16-rfc.md
---

# RFC: Operator Overloading for TypeScript

## Summary
Add an `operator` keyword to TypeScript that allows classes and interfaces
to define custom implementations for JavaScript operators (`+`, `-`, `*`,
`/`, `==`, `>`, etc.) with full type safety.

## Motivation
Numeric computing, vector math, and DSL implementations in TypeScript require
verbose method calls where operators would be more natural. This is a common
pain point in scientific computing, game development, and data processing.

## Design

### operator keyword
```ts
class Matrix {
  data: number[][];

  operator +(other: Matrix): Matrix {
    // element-wise addition
  }

  operator *(scalar: number): Matrix {
    // scalar multiplication
  }
}
```

### Operator table
| Operator | Method signature | Example |
|----------|-----------------|---------|
| `+` | `operator +(other: T): T` | `a + b` |
| `-` | `operator -(other: T): T` | `a - b` |
| `*` | `operator *(other: T): T` | `a * b` |
| `/` | `operator /(other: T): T` | `a / b` |
| `==` | `operator ==(other: T): boolean` | `a == b` |
| `>` | `operator >(other: T): boolean` | `a > b` |

### Transpilation
Compiles to `Symbol.for`-based method calls, compatible with ES6+.

## Backwards Compatibility
- No breaking changes to existing TypeScript code
- Operator overloading is opt-in per class
- Non-overloaded operators continue to produce compile errors

## Prior Art
- C++: `operator+` member functions
- Python: `__add__`, `__mul__` dunder methods
- Rust: `std::ops::Add` trait
- Kotlin: `operator fun plus()`

## Unresolved Questions
1. Should interfaces be able to declare operators?
2. Interaction with existing `valueOf` and `toString`?
3. Performance implications for JIT compilation?
