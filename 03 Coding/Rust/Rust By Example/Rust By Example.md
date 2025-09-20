---
id: Rust_By_Example
aliases: []
tags:
  - coding
  - rust
  - rust_by_example
dg-publish: true
---
# Rust By Example
Created : 2024-06-07 23:20

## Contents
-

### Variables

```rust
// Fix the error with the use of define_x
fn main() {
  let x =  define_x();
    println!("{}, world", x); 
}

fn define_x()->String {
    let x = "hello".to_string();
    x
}

```

#### Shadowing
 can declare a new variable with the same name as a previous variable, here we can say **the first one is shadowed by the second one.**
 5. 

```rust

// Only modify `assert_eq!` to make the `println!` work(print `42` in terminal)
fn main() {
    let x: i32 = 5;
    {
        let x = 12;
        assert_eq!(x, 12);
    }

    assert_eq!(x, 5);

    let x = 42;
    println!("{}", x); // Prints "42".
}

```

6.

```rust

// Remove a line in the code to make it compile
fn main() {
    let mut x: i32 = 1;
    x = 7;
    // Shadowing and re-binding
    x += 3;

    let y = 4;
    // Shadowing
    let y = "I can also be bound to text!"; 

    println!("Success!");
}

```

## References

