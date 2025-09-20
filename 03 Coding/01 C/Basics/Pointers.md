---
id: Pointers
aliases: []
tags:
  - coding
  - basics
dg-publish: true
---
# Pointers
- [[Null Pointer]]
##### **Prerequisites**:
- [[Memory]]
##### **Used In**
- [[Linked List]]
##### **Contents**
- [[#1. Basics]]
1. Basics 
	- pointer to an Array
	- Accessing Next variable
	- Dynamically allocating memory
	- Accessing values inside a struct pointer
2. Generic Pointer
3. Pass by Reference
4. Constant pointer
5. Pointer to a constant 
6. Pointer to pointer
7. Function Pointer 

## 1. Basics
Pointer is a **variable** that holds the memory address of **another variable**

#example

```c
int *x;

```

here `x` is a integer pointer to an integer 

```python
int value = *x ; // get value of the variable the x point to 
int address = x ; // get the address of the variable the x point to

```

#completeCode 1 

```c
#include <stdio.h>
int main() {
  int x = 10;
  int *ptr;
  ptr = &x;
  printf("Value of x = %d\n", x);
  printf("Value of variable ptr points to  = %d\n", *ptr);
  printf("Address of x = %p\n", &x);
  printf("Value of  ptr = %p\n", ptr);
}

```

>[!success]+ **Output**
>```

>Value of x = 10
>Value of variable ptr points to  = 10
>Address of x = 0x7ffc99f1581c
>Value of  ptr = 0x7ffc99f1581c
>```

You can see that `ptr` holds the address of `x` and `*ptr` gives the value of `x`.

### Reassgning the pointer

```c 
#include <stdio.h>
int main(){
    int x = 5;
    int *ptr = &x;
    printf("Value of x = %d\n",*ptr);
    printf("Address of x = %p\n",ptr);
    int y = 10;
    ptr = &y;
    printf("Value of y = %d\n",*ptr);
    printf("Address of y = %p\n",ptr);
}

```

>[!success]- **Output**
>```

>Value of x = 5
>Address of x = 0x7ffde2574808
>Value of y = 10
>Address of y = 0x7ffde257480c
>```

##### Accessing Next Variable

```c
#include <stdio.h>
int main(void) {
  const int a = 10, b = 12;
  int *p;
  p = &a;
  printf("%d", *(p + 1));
}

```

output Using `gcc`

```bash
12

```

output Using `clang`

```bash
-794418688

```

In this program the i was able to access the variable `b` by using `*(p+1)` because the `gcc` assigned **contiguous memory** location for the two variables. 

>[!warning] Dont use this
>This might not work all the time . 
### Changing Values using Pointer 

```c
 #include <stdio.h>
int main(){
    int x = 5;
    int *ptr = &x;
    printf("Value of x= %d\n",x);
    *ptr = 10;
    printf("Value of x after modification = %d\n",x);
}

```

>[!success]+ **Output**
>```

>Value of x= 5
>Value of x after modification = 10
>```

#### Pointer to an array

```c
#include <stdio.h>
int main(int argc, char *argv[]) {
	  int A[2] = {1, 3};
	  int *p = A;
	  printf("%d\n", *p);
	  printf("%d", *(p + 1));
}

```

>[!success]- **Output**
>```

> 1
 >3
>```

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

```

>[!success]- **Output**
>```

>hi
>```

#### Accessing values inside a struct pointer 

```c
 #include <stdio.h>
struct somethin {
  int value;
  int value2;
};

int main(){
    struct somethin s =  {10 ,20};
    struct somethin *ptr = &s; 
    printf(ptr->value == s.value ? "True" : "False");
}

```

```op
True

```

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

### 2. Generic Pointer

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

# Advanced

### 3. Pass by Reference

```cpp
#include <stdio.h>

void print_value(int *x) {
    printf("Value: %d\n", *x);
}

int main(){
    int value = 10;
    print_value(&value);
    return 0;
}

```

```op
Value: 10

```

#explenation
- The `print_value` expects a integer pointer 
- in `print_value(&value)` we pass the address of the variable `value`

## 4. Constant pointer
*the address that is pointing to, cannot be changed*
#syntax 

```cpp
<type-of-pointer> *const <name-of-pointer>

```

^de91e5

```cpp
char x = 'x' ;
char *const ptr = &x; 

```

Assigning new value to that pointer will result in error as the following

```cpp
#include <stdio.h>

int main() {
    char x = 'x';
    char *const ptr = &x; 
    char y = 'y';
    ptr = &y;  // this will throw an error like "variable 'ptr' declared const here"
}

```

> the following is possible 

```cpp
#include <stdio.h>

int main() {
    char x = 'x';
    char *const ptr = &x; 
    *ptr = 'y';
    printf("x is now : %c\n", x);
}

```

```op 
x is now:  y

```

```cpp
#include <stdio.h>

int main() {
    char x = 'x';
    char *const ptr = &x; 
    char y = 'y';
    ptr = &y;  // not possible 
    *ptr = 'z'; // possible 
}

```

## 5. Pointer to a contant 
*pointer cannot change the value at the address pointed by it*

```cpp
const <type-of-pointer> *<name-of-pointer>;

```

if we compare this with ![[#^de91e5]]
#example 

```cpp
#include<stdio.h>

int main(void)
{
    char ch = 'c';
    const char *ptr = &ch;
    ch = 'a'; // possible 
    *ptr = 'b' ; // not possible 
    return 0;
}

```

## 6. Pointer to pointer
You will have to dereference[^1] it twise 

[^1]:accessing the value stored at the memory address that the pointer is holding

```cpp
#include <stdio.h> 

int main(){
    char x = 'x';
    char *ptr = &x;
    char **ptr_to_ptr = &ptr; 
    printf("Value of x: %c " , **ptr_to_ptr); 
}

```

## 7. Function Pointer

```cpp
#include <stdio.h>
void print_sum(int a, int b) {
    printf("Sum: %d\n", a + b);
}
int main() {
    void (*func_ptr)(int, int) = print_sum; 
    func_ptr(5, 10); 
    return 0;
}

```

## References

1. [Source 1](https://embetronicx.com/tutorials/p_language/c/pointers_2/)
2. [Source 2](https://www.cs.cmu.edu/~ab/15-123N09/lectures/Lecture%2005%20-%20Advanced%20pointers.pdf) PDF
