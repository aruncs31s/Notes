---
id: Rust By Practice
aliases: []
tags:
  - coding
  - rust
dg-publish: true
---
## Variables

- [Scope](#scope)

1.  A variable can be used only if it has been initialized

```rust

// Fix the error below with least amount of modification to the code
fn main() {
    let x: i32; // Uninitialized but used, ERROR !
    let y: i32; // Uninitialized but also unused, only a Warning !

    assert_eq!(x, 5);
    println!("Success!");
}

```

soln

```rust

// Fix the error below with least amount of modification to the code
fn main() {
    let x: i32=5; // Uninitialized but used, ERROR !
    let y: i32; // Uninitialized but also unused, only a Warning !

    assert_eq!(x, 5);
    println!("Success!");
}

```

2. Use `mut` to mark a variable as mutable

```rust
// Fill the blanks in the code to make it compile
fn main() {
    let __ __ = 1;
    __ += 2;

    assert_eq!(x, 3);
    println!("Success!");
}

```

soln

```rust
// Fill the blanks in the code to make it compile
fn main() {
    let mut x = 1;
    x += 2;

    assert_eq!(x, 3);
    println!("Success!");
}

```

### Scope

1.

```rust
// Fix the error below with least amount of modification
fn main() {
    let x: i32 = 10;
    {
        let y: i32 = 5;
        println!("The value of x is {} and value of y is {}", x, y);
    }
    println!("The value of x is {} and value of y is {}", x, y);
}

```

### Char 

