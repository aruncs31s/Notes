---
id: python
aliases: []
tags: []
---

# Python
- [[pySDR]]
## Modules

- [Numpy](numpy.md)
- [matplotlib](./matplotlib.md)
- [[Pyaudio]]
- [[Python Regex]]
- [[Manim]]
## Contents
a
- [ ]
- [Zip](#zip)
- [List](#list)

### Arrays

```python 
a = [ 1,2,3]
b = [a,a,a]
print(b[1][1])
```
#### Zip

- [Iterating over the zip objects](#iterating%20over%20the%20zip%20objects)

```python
x = [1, 0]
y = [2, 0]
z = zip(x, y)
print(tuple(z))
```

#output

```
((1, 2), (0, 0))
```

- The zip() function adds i_th element at the end of the i_th element of weights

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
# You can iterate over the zip object to see its contents
for item in zipped: print(item)
'''output
(1, 'a') (2, 'b') (3, 'c')
'''
```

###### Iterating over the zip objects

```python
for item in zip(weights,biases):
	print(item)
'''
	([2, 4, 5], 2) ([3, 4, 5], -1) ([0.1, 0.2, 0.3], -2)
	'''
```

- Or convert it to a list to see its contents explicitly

```python
print(list(zip(weights, biases)))
'''
[([2, 4, 5], 2), ([3, 4, 5], -1), ([0.1, 0.2, 0.3], -2)]
'''

```

- without `list` the code wont work
  - - In Python 3, `zip(weights, biases)` returns an iterator that aggregates elements from the `weights` list and the `biases` list in tuples

#### List

- [List](#list)
- [Shapes](#shapes)

#### List

[Source](https://www.w3schools.com/python/python_lists.asp)

- [Example](#list%20example)
- [Finding The length](#finding%20the%20length)

_Lists are used to store multiple items in a single variable._

###### List Example

```python
someList = [1,2,3]
print(someList)
```

###### Finding the length

```python
print(len(someList))
```

##### Shapes

| Name In python       | Name of the shape | Dimension | Type   | Eg                      | Shape   |
| -------------------- | ----------------- | --------- | ------ | ----------------------- | ------- |
| List                 | Array             | 1         | Vector | [1,2,4,5]               | 4       |
| List of List(lol)    | Matrix            | 2         | Vector | \[[1,2,3,4],[2,3,4,5\]] | (2,4)   |
| List of List of List | Matrix            | 3         | Vector | [Lists](python.md#list) | (1,3,3) |

> More about [Lists](python.md#list)

> [!NOTE] List of List
> List is a List where its element itself is a list or a group of list
> Used to represent
>
> - Tabular Data
> - Matrices etc..

> [!NOTE] List of List of List
> List of List of List is a list where its element itself is a list and the element also contains a list of some type

```python

a_3D_list = [
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 3, 4],
    ],
    [
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 6],
    ],
]
print(a_3D_list[0][0][2])
# 3
```

- In the above example the first index corresponds to the 1 element in the outermost list that is consider this example an_lol\[i]\[j\]\[k]
  - ==i== = index of outer most list
  - ==j== = index of the column of the selected list
  - ==k== = index
