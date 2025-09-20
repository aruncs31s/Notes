---
id: Rust_By_Example
aliases: []
tags:
  - coding
  - rust
dg-publish: true
---
# Rust By Example
Created : 2024-04-12 21:05

## Contents
- [Primitives]()
- [Vectors](#vectors)
- 
### Primitives
### [Scalar Types](https://doc.rust-lang.org/stable/rust-by-example/primitives.html#scalar-types)
- Signed integers: `i8`, `i16`, `i32`, `i64`, `i128` and `isize` (pointer size)
- Unsigned integers: `u8`, `u16`, `u32`, `u64`, `u128` and `usize` (pointer size)
- Floating point: `f32`, `f64`
- `char` Unicode scalar values like `'a'`, `'α'` and `'∞'` (4 bytes each)
- `bool` either `true` or `false`
- The unit type `()`, whose only possible value is an empty tuple: `()`
Despite the value of a unit type being a tuple, it is not considered a compound type because it does not contain multiple values
### [Compound Types](https://doc.rust-lang.org/stable/rust-by-example/primitives.html#compound-types)

- Arrays like `[1, 2, 3]`
- Tuples like `(1, true)`

Variables can always be _type annotated_. Numbers may additionally be annotated via a _suffix_ or _by default_. Integers default to `i32` and floats to `f64`. Note that Rust can also infer types from context.

```rust
fn main() {
    // Variables can be type annotated.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // Regular annotation
    let an_integer   = 5i32; // Suffix annotation

    // Or a default will be used.
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    // A type can also be inferred from context.
    let mut inferred_type = 12; // Type i64 is inferred from another line.
    inferred_type = 4294967296i64;

    // A mutable variable's value can be changed.
    let mut mutable = 12; // Mutable `i32`
    mutable = 21;

    // Error! The type of a variable can't be changed.
 //   mutable = true;

    // Variables can be overwritten with shadowing.
    let mutable = true;
}

```

> [!NOTE] Mutablility
> Variable bindings are immutable by default, but this can be overridden using the `mut` modifier.
>```rust
>let x = 10;
>x = 20;
>```

>It throws errror due to the variable x being `immutable` so we need to make it mutable
>
>```rust
>let mut x = 10;
> x = 20```

> 

>

### Vectors

```rust
fn main() {
    let mut new_vector = vec![33, 44, 55];
    // Accesing the First element
    println!("{:?}", new_vector[0])
}

```

## References
1. https://doc.rust-lang.org/stable/rust-by-example/#rust-by-example