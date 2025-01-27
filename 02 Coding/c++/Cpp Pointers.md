---
aliases: 
Date: 23-01-25
---
# Cpp Pointers


## Function Pointers

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