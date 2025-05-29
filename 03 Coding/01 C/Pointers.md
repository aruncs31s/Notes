---
id: Pointers
aliases:
  - c pointer
tags: []
---

# Pointers
**Prerequisites**:
- [[Memory]]

**Contents **
- [[#Basics]]
- [[Null Pointer]]
- [[Pointer to Pointer]]
- Variable that holds the address of another `Variable`
#example
```c
int *x;
```

here `x` is a integer pointer to an integer 
```c
int value = *x ;  // get value of the variable the x point to 
int address = x ; // get the address of the variable the x point to
```

### Basics


```c
#include <stdio.h>
int main(){
  int *x;
  int k = 10 ;
  x = &k;
  printf("%d\n",x);
  printf("%d\n",*x);
}
/*
-498828788 // address of k
10  // Value of k
*/
```

#### Pointer to an array

```c
#include <stdio.h>
int main(int argc, char *argv[]) {
  int A[2] = {1, 3};
  int *p = A;
  printf("%d\n", *p);
  printf("%d", *(p + 1));
}
/* output
 1
 3
 */
```

---

#### Accessing Next Variable

```c
#include <stdio.h>
int main(void) {
  const int a = 10, b = 12;
  int *p;
  p = &a;
  printf("%d", *(p + 1));
}
```

#output Using `gcc`

```bash
12
```

#output Using `clang`

```bash
-794418688
```

In this program the i was able to access the variable `b` by using `*(p+1)` because the `gcc` assigned **contiguous memory** location for the two variables.

#### Dynamically allocating memory

```c
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
  char *string;
  string = (char *)malloc(sizeof(char) * 3);
  string[0] = 'h';
  string[1] = 'i';
  string[2] = '\0'; // Null-terminate the string
  printf("%s\n", string);
  return 0;
}
/* output
hi
*/
```
#### Accessing values inside a struct pointer 
```c
#include <stdio.h>
struct somethin {
  int value;
  char *name;
};
int main(int argc, char *argv[]) {
  struct somethin *new_struct;
  new_struct->value = 10;

  printf("value = %d", (*new_struct).value);
  return 0;
}
```
- This compiled and run successfully on `gcc version 14.2.1 20240805 (GCC)` but failed to run in `clang 18.1.8`
#correctCode
```c
#include <stdio.h>
#include <stdlib.h>
struct somethin {
  int value;
  char *name;
};
int main(int argc, char *argv[]) {
  struct somethin *new_struct = malloc(sizeof(struct somethin));
  new_struct->value = 10;

  printf("value = %d", (*new_struct).value);
  return 0;
}
```

- `->` operator combines both `*` and `.` so `(*new_struct).value` and `new_struct->value` will do the same thing.



### Generic Pointer

It has a `void` datatype

```c
void *ptr;
```

- It can not be dereferenced , so casting is required.

```c
int main() {
  int x = 10;
  void *ptr;
  ptr = &x;
  printf("The value of x =%d ", *(int *)ptr);
}
```



## References

1. [Source 1](https://embetronicx.com/tutorials/p_language/c/pointers_2/)
2. [Source 2](https://www.cs.cmu.edu/~ab/15-123N09/lectures/Lecture%2005%20-%20Advanced%20pointers.pdf) PDF
3.
