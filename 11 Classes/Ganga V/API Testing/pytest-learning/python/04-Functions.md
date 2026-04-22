---
id: 04-Functions
tags:
  - python
  - functions
  - arguments
dg-publish: true
---

# Functions

Learn to write functions in Python.

## Basic Function

```python
def greet(name):
    return f"Hello, {name}!"
```

## Default Parameter

```python
def greet(name="World"):
    return f"Hello, {name}!"
```

## Multiple Return Values

```python
def get_coords():
    return (10, 20)

x, y = get_coords()
```

## *args and **kwargs

```python
def func(*args, **kwargs):
    print(args)    # Tuple of positional args
    print(kwargs)  # Dict of keyword args
```

## Lambda Functions

Anonymous functions (inline functions):

```python
# Regular function
def add(a, b):
    return a + b

# Lambda function
add = lambda a, b: a + b
print(add(10, 20))  # 30
```

## Filter

Filter items from a list:

```python
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6]

# With lambda
evens = list(filter(lambda n: n % 2 == 0, numbers))
```

## Reduce

Apply function cumulatively:

```python
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)  # 15

# With lambda
total = reduce(lambda x, y: x + y, numbers)

# Factorial example
from functools import reduce
factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)  # 120
```

---

**Next:** [[05-Comprehensions]] - List and dictionary comprehensions

**See Also:** [[03-Control-Flow]] - Control flow
