---
id: Newtons_Method
aliases: []
tags:
  - science
  - maths
  - methods
dg-publish: true
---
# Newton's Method
Created : 2024-05-12 14:58

## Contents
`

```python
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**5 + x**2 - x - 0.2

# Create a range of x values
x = np.linspace(-2, 2, 10000)

# Calculate the corresponding y values
y = f(x)

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot y as a function of x
ax.plot(x, y)

# Add a title and labels
ax.set_title('Plot of x^5 + x^2 - x - 0.2 = 0')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Find the roots of the function
roots = np.roots([1, 0, 0, 1, 0, -1, -0.2])

# Add vertical lines at the roots
for root in roots:
    ax.axvline(x=root, color='r', linestyle='--')

# Display the plot
plt.show()

```

## References
1. https://youtu.be/-RdOwhmqP5s?si=IqjEDFoufcb04VTp