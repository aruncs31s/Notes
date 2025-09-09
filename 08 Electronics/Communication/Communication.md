---
id: Communication
aliases: []
tags:
  - electronics
  - communication
dg-publish: true
---
# Communication

**Prerequisites**

- [[Digital Signal Processing]]

<!-- ![](https://pysdr.org/_images/fourier_series_triangle.gif) -->

![[fourier_series_triangle.gif]]
![[fourier_series_arbitrary_function.gif]]
[Source](https://pysdr.org/content/frequency_domain.html)

- Can Make any shape by adding multiple `sine` waves and some require infinite amount of sine wave to obtain certain shapes

### Time Frequency Properties

1. Linearity Properties

$$
ax(t) + by(t) = aX(f) + bY(f)
$$

2. Frequency Shift Property

$$
e^{2\pi j f_0 t} x(t) \rightarrow X(f - f_0)
$$

3. Scaling in time Property
   $$
   x(at) \leftrightarrow X \left( f \over a \right)
   $$

![](https://pysdr.org/_images/time-scaling.svg)

4. Convolution in Time Property:

$$
\int x(\tau) y(t - \tau) d\tau \leftrightarrow X(f) Y(f)
$$

- [ ] Complete Convolution property and its usecases
