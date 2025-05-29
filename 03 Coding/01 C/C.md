---
id: C
aliases: 
tags: 
dg-publish: true
---

# C

- [[Functions]]
- [[mathFunctions]]
- [[Pointers]]

## Data Types

#### Constant Strings

```c
const char *str = "Hello, World!";
```

#### Ternary

```c
if ( a > b){
a = 10;
}
else {
a = 20
}
```

```c
a = (a> b) ? 10 : 20
```

#### Switch Statement

[Source](https://www.geeksforgeeks.org/c-switch-statement/)

```c
switch(expression)
{
case value1: statement_1;
             break;
case value2: statement_2;
             break;
case value_n: statement_n;
              break;
default: default_statement;
}
```


## Operators
1. Unary Operator (1 Operand) ->  `++, --, sizeof()`
2. Binary Operators  (2 operand) -> `+, -, *, /, %, <, >, <=, >=, ==, !=, &&, ||, !, &, |, <<, >>, ~, ^, =, +=, -=, *=, /=, %=`
3. Ternary Operator (3 operand) -> `?, :`

```c
varible = <operand> <operator> <operand> ;
```
#example 
```c
sum = a+b;
```

### Unary Operators
#### Increment and Decryment 
```cpp
int x =10;
x = ++x;  // same as just ++x -> pre-increment -> 1 1
x = --x ;  // pre-decrement --x -> 9
x = x++; // post-increment  ;  x is still 10 . this is no use 
x = x--;  // post decrement ; x is still 10 no use
```

#### sizeof operator 
```c
sizeof(int) ; // returns (int) 4 
sizeof(short); // returns 2 
```
### Binary Operators
1. Arithmetic Operator (+,-,\*,/,%)
2. Assignment Operator (=,+=,-=,*=,/=,%=)
3. Logical Operator (&&,||,!)
4. Relational Operator (<,>,<=,>=,==,!=)
5. Bitwise Operator (&,|,^,~,<<,>>)

#### Arithmetic Operator
```cpp
int x = 10 ;
x + 10 ; // 20 
x - 10 ; // 0 
x * 10 ; // 100
x / 10 ; // 1 
x % 10 ; // 0 
```
#### Assignment Operator 
```c
int x = 10;

x = x + 5 ;  // 15 
x +=5 ; // 15
x -= 5; // 5 
x *=5 ; // 50
x /=5; // 2 
x == 5 ; // returns false
x !=5.; // returns true
```

#### Logical Operators
```c
int a = 10 , b = 20 , c = 30 ;

// logical and 
a > b && a < c ; // false && true -> false
a < b && a < c ; // true && true -> true 

// logical or 
a > b || a < c ; // false | true -> true 

// logical not

!(a > b) ; // !false -> true 
!(a < b) ; // !true -> false 
```

#### Relational Operator
```c
int a = 10 ;
int b = 20;

// Equal to ;
a == b; // false 
a == 10 ; // true 

// Not equal to 
a != b; // true
a != 10; // false

// Greater than 
a > b ; // false
// Greater than or equal to 
a >= 10 ; // true 

// Less than 
a < b; // true 
a <= 10; // true
```

#### Bitwise Operator
```c
int a = 10 ; // 1010 
int b = 5 ; // 0111
// bitwise or
c = a | b ; // c = 1010 or 0111 = 1111 -> 15 

// bitwise xor
c = a ^ b; // c = 1010 or 0111 = 1101 -> 13 

// bitwise not
c = ~a; // c =  not 1010 -> 0101 -> 5

// bitwise and 
c = a & b ; // c = 1010 & 0111 = 0010 -> 2 

// bitwise left shift 
c = a << 2; // c = 1010 << 2 = 0b101000 -> 40  

// bitwise right shift 
c = a >> 2 ; // c = 1010 >> 2 = 0b0010 -> 2 
```

### Ternary Operator
```c
condition? True : False 
```
#example 
```c
#include <stdio.h>

int main(){
    int x = 10,y =15;
    int bigger = x < y ? y : x ; // bigger = 15
}
```
### Precedence

```c
float x = 1 / 10 + 1 ; // 1.1 
```


| Precedence | Operator(s)                                         | Description                                                                         | Associativity                                |               |               |
| ---------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------- | ------------- | ------------- |
| 1          | `()` `[]` `.` `->` `++` `--`                        | Parentheses, Array Subscript, Dot, Structure Ptr, Postfix inc/dec                   | Left-to-Right                                |               |               |
| 2          | `++` `--` `+` `-` `!` `~` `(type)` `*` `&` `sizeof` | Prefix inc/dec, Unary plus/minus, NOT, Bitwise NOT, Cast, Deref, Address-of, Sizeof | Right-to-Left                                |               |               |
| 3          | `*` `/` `%`                                         | Multiplication, Division, Modulus                                                   | Left-to-Right                                |               |               |
| 4          | `+` `-`                                             | Addition, Subtraction                                                               | Left-to-Right                                |               |               |
| 5          | `<<` `>>`                                           | Bitwise Shift Left/Right                                                            | Left-to-Right                                |               |               |
| 6          | `<` `<=` `>` `>=`                                   | Relational Operators (less/greater than)                                            | Left-to-Right                                |               |               |
| 7          | `==` `!=`                                           | Equality/Inequality                                                                 | Left-to-Right                                |               |               |
| 8          | `&`                                                 | Bitwise AND                                                                         | Left-to-Right                                |               |               |
| 9          | `^`                                                 | Bitwise XOR                                                                         | Left-to-Right                                |               |               |
| 10         | `                                                   | `                                                                                   | Bitwise OR                                   | Left-to-Right |               |
| 11         | `&&`                                                | Logical AND                                                                         | Left-to-Right                                |               |               |
| 12         | `                                                   |                                                                                     | `                                            | Logical OR    | Left-to-Right |
| 13         | `?:`                                                | Ternary Conditional                                                                 | Right-to-Left                                |               |               |
| 14         | `=` `+=` `-=` `*=` `/=` `%=` `&=` `^=` `            | =` `<<=` `>>=`                                                                      | Assignment and Compound Assignment Operators | Right-to-Left |               |
| 15         | `,`                                                 | Comma (Expression Separator)                                                        | Left-to-Right                                |               |               |




