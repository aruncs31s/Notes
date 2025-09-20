---
id: Number_Theory
aliases: []
tags:
  - science
  - maths
dg-publish: true
---
# Number Theory
Created : 2024-05-18 18:56

## Contents
- [[#Mandelbrot Set]]
- [[The Golden Ratio]]
### Mandelbrot Set
$$
f(z_{n+1}) = {z_n}^2 \ + c
$$
- Where `C` is the complex number
> Points inside the Mandelbrot set remain bounded under this iteration
> 

```python
# Mandelbrot
import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # Create a grid of c-values
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # Mandelbrot iteration
    z = c
    for j in range(N_max):
        z = z**2 + c

    # Determine membership in the Mandelbrot set
    mandelbrot_set = (abs(z) < some_threshold)
    return mandelbrot_set

# Compute the Mandelbrot set
mandelbrot_set = compute_mandelbrot(50, 50., 601, 401)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()

```

 

## References
1. 
