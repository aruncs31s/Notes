---
id: Functions
aliases: []
tags:
  - cpp
Created: "30-08-2024"
cssclasses:
  - wide-page
---

# Functions

#### Call by Reference

##### In case of a function whose formal parameter is a vector

```cpp
#include <vector>
int myFunction(vector<int>& myVector) {
    // Function code here
    return something;
}
```

This allows to modify original vector elements inside the vector

```cpp
// Example of pass by reference
#include <iostream>
void swap(int &a, int &b) {
  int t;
  t = a;
  a = b;
  b = t;
}
int main() {
  int a = 10, b = 12;

  swap(a, b);
  std::cout << a;
  std::cout << " ";
  std::cout << b;
}e
```

```c
main(){
printf("HI");
}
```

## References

1. Object Oriented Programming with C++ `E Balagurusami`
2.
