---
id: Classes
aliases: []
tags:
  - coding
  - basics
cssclasses: 
Created: 10-10-2024
Status: 
dg-publish: true
---
# Classes

## Constructors 
*It is special function which initializes the objects of its classes*
#rules 
- it is like the [[Python For Engineers#^798cac|Init Function]] in [[python]]
- it invoked automatically when an object is created 
- It's name is same as the class name
- Should be declared in `public` 
- do not `return` anything

```cpp
#include <iostream>
class co_ordinates {
public:
  co_ordinates(void);
  int x;
  int y;
};
co_ordinates::co_ordinates(void) {
  x = 0;
  y = 0;
}
int main(int argc, char *argv[]) {
  co_ordinates x1;
  co_ordinates x2;
  std::cout << x1.x << "\n";
  std::cout << x1.y << "\n";
}

```

### With Parameters 

```cpp
class co_ordinates {
public:
  co_ordinates(int a, int b);
  int x;
  int y;
};
co_ordinates::co_ordinates(int a , int b) {
  x = a;
  y = b;
}
int main(int argc, char *argv[]) {
  co_ordinates x1(1,2);
  std::cout << x1.x << "\n";
  std::cout << x1.y << "\n";
}

```

### Multiple Constructors

```cpp
#include <iostream>
class co_ordinates {
public:
  co_ordinates();
  co_ordinates(int a, int b);

  int x;
  int y;
};
co_ordinates::co_ordinates(void) {
  x = 0;
  y = 0;
}
co_ordinates::co_ordinates(int a, int b) {
  x = a;
  y = b;
}
int main(int argc, char *argv[]) {
  co_ordinates x1(1, 2);
  co_ordinates x2;
  std::cout << x1.x << "\n";
  std::cout << x1.y << "\n";
  std::cout << x2.x << "\n";
  std::cout << x2.y << "\n";
}

```