---
id: Python For Engineers
aliases:
  - cst445
  - python
tags: []
Created: "2024-07-23"
ExamDate: "2024-11-29"
cssclasses:
  - wide-page
---

# Python For Engineers

```python
print("Hello World")
```

## Contents
- [[01 Academics/Btech/S7/Python For Engineers/Class Notes]]
- [[#Module 4]]


## Module 4 

**Plotting** 
- [ ] An Interactive Session with PyPlot,
- [ ] Basic Plotting,
- [ ] Logarithmic Plots,
- [ ] More Advanced Graphical Output,
- [ ] Plots with multiple axes,
- [ ] Mathematics and Greek symbols,
- [ ] The Structure of matplotlib,
- [ ] Contour and Vector Field Plots.
**File Processing**
- [ ] The os and sys modules, 
- [ ] Introduction to file I/O,
- [ ] Reading and writing text files,
- [ ] Working with CSV files.

### Plotting

```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
plt.plot([1, 2, 3, 2, 3, 4, 3, 4, 5])
plt.show()
```

- By default, the plot function **draws a line** between the data points that were entered.


#### Ploting Sine Wave
```python
x = np.linspace(0, 4.*np.pi, 33)
y = np.sin(x)
plt.plot(x, y)
plt.show()
```