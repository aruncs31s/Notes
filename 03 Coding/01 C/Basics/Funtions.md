---
id: Funtions
aliases: []
tags:
  - coding
  - basics
dg-publish: true
---
# Functions
As far as i know you can write an entire application which does not have functions except `main()` , this is ok for simple programs that we do first while learning , but as we get hands on the real world problems , functions are must , otherwise you will end up with a file that is few mega bites in size. Using only a single function is not impossible but the main use of functions is to **reduce code** and **reuse code**.   

## Arguments
### Pointers
- using [[Pointers]] 

```cpp
int add(int *number_1, int *number_2) { 
	return *number_1 + *number_2; 
	}
 add(&a, &b);

```

```c
int add(int &number_1, int &number_2) { 
	return number_1 + number_2; 
	}
add(a, b);

```

1. Swap Without using another variable

[[Functions|Source]]

```c
#include <stdio.h>
void swap(int *a, int *b) {
*a = *a ^ *b;
*b = *a ^ *b;
*a = *a ^ *b;
}
int main(int argc, char *argv[]) {
int a = 1, b = 10;
swap(&a, &b);
printf(" a = %d , b= %d ", a, b);
}

```

- Forgot why i used pointer

## References

1.  Object Oriented Programming with C++ `E Balagurusami`
