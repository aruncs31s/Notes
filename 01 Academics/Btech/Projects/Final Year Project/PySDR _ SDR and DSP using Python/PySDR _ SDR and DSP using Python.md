---
id: PySDR _ SDR and DSP using Python
aliases: []
tags: []
Date: 03-11-2024
---

# PySDR _ SDR and DSP using Python
## Introduction 
**SDR** : Here the software will perform tasks such as filtering etc 
**DSP**: Refer [[Digital Signal Processing]]

## Frequency Domain
![[pydrawing 1.excalidraw]]
If we transform a signal with a single frequency component say $\cos(2\omega t )$ it will have only a single spike in freq domain

### Time Freq Pairs 

> [!multi-column]
>
>> [!note]+ Single Frequency 
>> ![](https://pysdr.org/_images/sine-wave.png)
>> ##### 
>> 
>
>> [!note]+ Impulse 
>> #### Requirement
>![](https://pysdr.org/_images/impulse.png)
>
>> [!note]+ Sqare Wave
>> ![](https://pysdr.org/_images/square-wave.svg)
>> 
>> 

We can see that a single impulse has amplitude in all frequency band how ? 
- For an impulse the timeperiod is zero ? 
- then freq = $\frac{1}{\lambda}$ -> $\infty$ then how on every freq? 
- [[FFT]] 
- here the `fft()` function will be used to compute the fft



```python
import matplotlib.pyplot as plt 
import numpy as np
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)
S = np.fft.fft(s)

plt.plot(t,s)
plt.show() 

```


```python
plt.plot(t,S)
plt.show() 

```

#### Ploting Magnitude and Angle 
```python
import matplotlib.pyplot as plt
S_mag = np.abs(S)
S_phase = np.angle(S)
plt.plot(t,S_mag,'.-')
plt.show()
```

```python
plt.plot(t,S_phase,'.-')
plt.show()
```

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
