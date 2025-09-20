---
id: Rust
aliases: []
tags:
  - coding
  - rust
dg-publish: true
---
# Rust
- [[Rust By Practice]]
- [[Coding/Rust/Rust By Example/Rust By Example|Rust By Example]]
- 
## Contents
- [[#Directives]]
- [[#Format Specifiers]]
- [[#If Else]]
- [Vectors](#vectors)
- [[Borrow Checker]]

### Directives

```rust
#![allow(unused)]

```

*To permit unused variables*

### Format Specifiers
`{}` ->  like `%d` in c 
- [ ] Research More about this 
`{:?}` -> it support more data types like `arrays` and stuff and used when `rustc` tells can not be formatted with the default formatter 
#example 

```rust
println!("result = {} ",result )

```

```rust
fn main() {
    let some_array = [ 1,2,3,4,5,6,7,8];
    println!("{}",some_array);
}

```

### Conditional Statements

#### If Else

```rust
fn main(){
    let some_value: i32 = 50;
    if some_value == 50 {
        println!("True");
    }
    else {
        println!("False");
    }
}

```

#### Match

```rust
#![allow(unused)]

fn main() {
    let some_variable = 10;
    match some_variable{
        1..=9 => println!("Under 10"),
        10 => println!("Equal to 10"),
        _ => println!("Invalid")
    }
}

```

`1..=i32::MAX` -> to get max value the 32 bit integer can provide = $2^{32}$
`_` -> to match everything else

##### Ordering

```rust
#![allow(unused)]
use std::cmp::Ordering;
// use std::sync::atomic::Ordering;

fn main() {
    let some_variable = 10; // This the actual variable 
    let some_other_variable = 20 ; // This var is only used to compare
    match some_variable.cmp(&some_other_variable){
    Ordering::Less => println!("some var is less that some other var"),
    Ordering::Greater => println!("Some var is greater than some other var"),
    Ordering::Equal => println!("The both Variables Matched"),
    }
}

```

When using `Ordering` we should import `cmp::Ordering`

### Vectors

### Match
![[Pasted image 20240303195835.png]]

