---
id: Advanced_Pyton
aliases: []
tags:
  - coding
  - python
Date: "30-05-2025"
dg-publish: true
---
# Advanced Pyton
## Compression 
### List Compression
#syntax 

```python
[expression for item in iterable if condition]

```

Consider this program 

```python
a = [1,2,3,4]
res = []
for val in a:
	res.append(val**2)
print(res)

```

Now consider , the second one is much better isnt it? 

```python
a = [1,2,3,4]
res = [val ** 2 for val in a]
print(res)

```

***List Compression** allows us to generate a new list by applying an expression to each item in an existing iterable*

##### Creating List

```python
a = [i for i in range(10)]
print(a)
b = [i ** 2 for i in range(10)]
print(b)

```

### Dictionary Compression

```python
keys , values = ['v1','v2','v3','a','b','c'] ,[1,2,3,4,5,6]
newDict = {k:v for (k,v) in zip (keys,values)}
print(newDict)

```

```python
newDict = {x: x**2 for x in range(10)}
print(newDict)

```

Check [this](https://www.geeksforgeeks.org/python-dictionary-comprehension/) out for more
## Lamda Operator
#syntax 

```python
lambda arguments : expression

```

#example

```python
# sum using functions
def _sum(a,b):
	return a + b
print(_sum(10,20))

# sum using lambda function
sum = lambda a,b: a+b
print(_sum(10,20))

```

## Filter

```python
def is_odd(n):
	return (n - 1) % 2 == 0
def is_even(n):
	return n % 2 == 0
a = [i for i in range(10)]
odd_a = list(filter(is_odd,a))
print(new_a)
even_a = list(filter(is_even,a))
print(even_a)

```

## Reduce
*This function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.*[Source](https://www.geeksforgeeks.org/reduce-in-python/)

```python
reduce(fn,seqence)

```

```python
from functools import reduce
def add(x, y):
    return x + y
def multiply(x , y):
	return x * y ; 

a = [1, 2, 3, 4, 5]
sum_a = reduce(add,a)
print(sum_a,sum(a))
multiply_a = reduce(multiply,a)
print(multiply_a)

```

#usecase

```python
# find factorial 

def factorial(n):
	_result = 1
	for i in range(1,n+1):
		_result  = _result * i
	return _result
n = 1

print(factorial(n))

```

```python
from functools import reduce
def fact(x, y):
    return (x * y) if sum([x, y]) else 1
n = 5
print(reduce(fact, [i for i in range(1, n+1)]))

```

Both does the job . But one uses traditional method , looping through `1 to n` and multipliting it , second one uses redue funtion to do the same task but bit more complex but fewer syntax

And if you pair it with `lambda` it becomes a single line operation , but bit more complex

```python
n = 5
result = reduce(lambda x , y:(x * y) if sum([x, y]) else 1 , [i for i in range(1, n+1)])
print(result)

```

- [ ] Complete this 📅 2025-06-01 

