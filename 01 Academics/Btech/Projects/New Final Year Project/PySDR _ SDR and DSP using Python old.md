---
id: PySDR _ SDR and DSP using Python
aliases: []
tags: []
Date: "03-11-2024"
---

# PySDR \_ SDR and DSP using Python

**Prerequisites**

- [[python]]
- [[Fourier Series and Transform]]
- [[Digital Signal Processing]]
- [[Information Theory And Coding]]

### 3. IQ Sampling

_It is a type of sampling that an SDR performs_

#### Basics

[[Nyquist Sampling Theorem]]

![noise floor.png](assets/imgs/noise%20floor.png)

$$
\begin{align}
magnitude &= \sqrt{a^2 + b ^2} \\

phase &= \tan^{-\left( b \over a \right)} \\
\end{align}
$$

```python
np.abs(X) # for magnitude
np.angle(x) # for phase
```

![qipoints.png](assets/imgs/qipoints.png)

$$
\begin{align}
x(t) &= I \cos(2\pi ft) + Q \sin(2 \pi f t) \\ \\
&= 0.7 \cos(2\pi f t) - 0.4 \sin (2 \pi ft)
\end{align}
$$

Using [[Trigonometry#^d94692|Identities]] $a\cos(x) + b\sin(x) = A \cos(x = \phi)$ where $A$ is our magnitude found with $\sqrt{ I_{2} + Q^2 }$ and $\phi = \tan^{-1}\left( \frac{Q}{I} \right)$ so the above eqn will become

$$
\begin{align}
x(t) &= 0.806\cos(2\pi ft + 0.519)
\end{align}
$$
