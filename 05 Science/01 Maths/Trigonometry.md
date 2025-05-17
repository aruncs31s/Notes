# Trigonometrics
Created : 2024-05-14 20:50


## Contents
- 

### Identities

^d94692

1. Unit Hypotenuse
$$
\sin^2 \theta + \cos^2 \theta = 1
$$ ^d8dee6
2. sico + cosi
$$
\sin(x+y) = \sin x \cos y + \cos x \sin y 
$$
3. coco - sisi
$$
   \cos\left(x+y\right) = \cos x \cos y - \sin x \sin y
$$
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 1000)
y = np.cos(x + np.pi / 4)
y2 = np.cos(x) * np.cos(np.pi / 4) - np.sin(x) * np.sin(np.pi / 4)
plt.plot(x, y, "b-", label="cos(x + y)")
plt.plot(x, y2, "r--", label="cos(x)cos(y) + sin(x)sin(y)")
plt.legend()
plt.grid(True)
plt.show()
```

### Properties
1. $\sin(90-x) = \cos(x)$
1. $\cos(90-x) = \sin(x)$
## References

1. 