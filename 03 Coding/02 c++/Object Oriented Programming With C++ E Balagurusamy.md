---
id: Object Oriented Programming With C++ E Balagurusamy
aliases: []
tags:
  - coding
dg-publish: true
---
# Object Oriented Programming With C++ E Balagurusamy

#### Introduction to OOP

- Before only POP(Procedure-Oriented Programming)
- POP employs _Top-Down_ approch
- In **OOP** the problem is considered as collection of number of entities -> _Objects_
  **OOP Features**:
  - Data hiding , Data Encapsulation,Data Abstraction
  - Polymorphism
  - Object
  - Class

```cpp
#include <iostream>
using namespace std;
int main(){
  cout << "Some String\n"; // Prints "Some String"
}

```

if `using namespace std` is not included the above program will become

```cpp
#include <iostream>
int main(){
std::cout << "Some String\n"; // Prints "Some String"
}

```

How to execute this program?

```bash
g++ program_name.cpp -o bin_file_name
./bin_file_name

```

#### Basic I/O Programming

Reading,Printing Input :

```cpp
#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
  string some_string;
  cout << "Enter a string ";
  cin >> some_string;
  cout << "Entered String is " << some_string;
}

```

New datatype `string`

#### Chapter 2 Debugging Exercises

1. Identify the error in the following program

```cpp
#include <iostream>
void main() {
  int i = 0;
  i = i + 1;
  cout << i << "";
  /* comment \*/ / i = i + 1;
  cout << i;
}

```

- program should include `using namespace std;` otherwise `cout` should be replaced with `std::cout`
- Illegal Commenting Syntax , or remove one `/`
- Return type of `main` should be `int`
  Corrected Version

```cpp
#include <iostream>
using namespace std;
int main() {
  int i = 0;
  i = i + 1;
  cout << i << "";
  /* comment */ i = i + 1;
  cout << i;
}

```

2. Identify the errors in the following

```cpp
#include <iostream>
void main() {
  short i = 2500, j = 3000;
  cout >> "i + j = " >> -(i+j);
}

```

- `>>` should be `<<`
- also missing `using namespace std;`

Corrected Version:

```cpp
#include <iostream>
using namespace std;
int main() {
  short i = 2500, j = 3000;
  cout << "i + j = " << -(i + j);
}

```

3. What wiil happen when you run the following program?

```cpp
#include <iostream>
using namespace std;

void main() {
  int i = 10, j = 5;
  int modResult = 0;
  int divResult = 0;
  modResult = i % j;
  cout << modResult << " ";
  divResult = i / modResult;
  cout << divResult;
}

```

- Divided by Zero error ?
- Missing change return type to main.
