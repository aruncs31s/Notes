---
id: Basics 1
aliases: []
tags:
  - coding
Created: 14-09-2024
cssclasses: 
dg-publish: true
---
# C++

- [[Functions]]
- [[structs]]
- [[unions]]
- [[03 Coding/02 c++/Basics/Classes]]
- [[Cpp Pointers]]
- [[Data Types]]
- [[#Loops]]
#### lvalues
values(Locator Values) refers to an `object` that has a name and persists beyond the expression that creates it 
- Lvalue is something that appear on the ==left hand side of the an assignment== operation
#eg

```cpp
int x = y;
int k = w;
int array[5];

```

*Here `k` and `x` are lvalues also `array` is an lvalue*

# Basics
**Tockens**: The smallest individual units in a program - Keywords: Reserved Identifiers - Identifiers - Constants - Strings - Operators

- [[Variables]]

```cpp

#include <iostream>
using namespace std;
int main() {
  cout << "Hello World!";
  return 0;
}

```

- `using namespace std` means that we can use names for objects and variables from the standard library.
  - if not `std::cout`

###### Insert newline

```cpp
cout << "Hello World!" << endl;

```

The `endl` line brke

## Variables 

#### Static Variables 
- Static member variables must be defined exactly once outside of the class definition
- Without this definition, you'll get linker errors about undefined references

## Functions
- `extern`: Declares a variable or a function without defining it.
