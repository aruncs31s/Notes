---
id: Funtions
aliases: []
tags: []
---

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
