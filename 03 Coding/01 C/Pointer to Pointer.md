---
tags:
  - c
  - cpp
  - pointer
---


# Pointer to Pointer

```c
int main() {
  int x = 10;
  int *ptr, **pptr;
  ptr = &x;
  pptr = &ptr;
  printf("The value of x is %d\n", **pptr);
}
```

