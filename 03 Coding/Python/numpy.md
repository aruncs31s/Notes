---
id: numpy
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# Numpy

[Source](https://www.geeksforgeeks.org/introduction-to-numpy/?ref=lbp)
- Its an array processing library

#Uses
- A powerful N-dimensional array object
- Sophisticated (broadcasting) functions
- Tools for integrating C/C++ and Fortran code
- Useful linear algebra, Fourier transform, and random number capabilities

```python
import numpy as np

# Row vector
a = np.array([1, 2, 3])

# Column vector
b = np.array([4,5,6]).T

# Dot product
result = np.dot(a, b)

print(result)

```

```python
import numpy as np 
# Define two vectors 
vector1 = np.array([1, 2, 3]) 
vector2 = np.array([4, 5, 6]).T 
# Compute the cross product 
cross_product = np.cross(vector1, vector2) 
print("Cross product:", cross_product)

```

#### Finding Error Perfomance of Binary Phase Shift Keying

```python
import numpy as nP

```