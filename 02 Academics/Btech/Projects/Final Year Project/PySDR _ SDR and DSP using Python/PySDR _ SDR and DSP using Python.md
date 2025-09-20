---
id: PySDR _ SDR and DSP using Python
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
  - pysdr___sdr_and_dsp_using_python
Date: "03-11-2024"
dg-publish: true
---
# PySDR \_ SDR and DSP using Python

## Introduction

**SDR** : Here the software will perform tasks such as filtering etc
**DSP**: Refer [[Digital Signal Processing]]

## Frequency Domain

![[pydrawing 1.excalidraw]]
If we transform a signal with a single frequency component say $\cos(2\omega t )$ it will have only a single spike in freq domain

### Time Freq Pairs

> [!multi-column]
>
> > [!note]+ Single Frequency
> > ![](https://pysdr.org/_images/sine-wave.png)
> >
> > #####
>
> > [!note]+ Impulse
> >
> > #### Requirement
> >
> > ![](https://pysdr.org/_images/impulse.png)
>
> > [!note]+ Sqare Wave
> > ![](https://pysdr.org/_images/square-wave.svg)

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

### FFT

- It is an algorithm to compute the Discrete Fourier Transform

```mermaid
graph LR
A[Time domain Signal]
B[Freq Domain Signal ]
A -- FFT --> B

```

- more Here [[FFT in Python]]

## 3. IQ Sampling

aka **complex sampling** or **quadrature sampling**

- _It is a type of sampling that an SDR performs_

#### Basics

- Check this out [[Nyquist Sampling Theorem]]
- always use sampling rate $Fs > 2B$ where B is the bandwidth of the signal
- we always aproximate the maximum frequency of the signal and after aproximating should place a Low pass filter or a band pass filter to limit (band limit) the signal otherwise it will cause what is known as **Aliasing**
  ![noise floor.png](assets/imgs/noise%20floor.png)

### Quadrature Sampling

In the context of DSP and SDR it refers to two waves that are 90 degrees out of phase^[https://pysdr.org/content/sampling.html#quadrature-sampling]

- The 90 degree phase shift make them [[Quadrature Signal|Orthogonal Signal]]

Consider 2 Signals
![](https://pysdr.org/_images/IQ_wave.png)

$$
\begin{align}
I\cos(2\pi ft) \tag{I} \\
Q \sin (2\pi ft) \tag{Q}
\end{align}
$$

Where

> the $\cos()$ -> In **phase component** > $\sin()$ -> **quadrature component**

$$
x(t) = I\cos(2\pi ft ) + Q \sin(2\pi ft) \tag{1}
$$

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 1000)
y = np.cos(x + np.pi / 4)
y2 = np.cos(x) * np.cos(np.pi / 4) - np.sin(x) * np.sin(np.pi / 4)
y3 = np.cos(x) - np.sin(x)
y4 = np.sin(x) * np.sin(np.pi / 4)
y5 = np.cos(x) * np.cos(np.pi / 4)
plt.plot(x, y, "b-", label="cos(x + π/4)")
plt.plot(x, y3, "g-", label="cos(x) - sin(x)")
plt.plot(x, y2, "r--", label="cos(x)cos(π/4) + sin(x)sin(π/4)")
plt.plot(x, y4, "y--", label=" sin(x) sin(π/4)")
plt.plot(x, y5, "m--", label="cos(x) cos(π/4)")
plt.legend()
plt.grid(True)
plt.show()

```

Think of it like adding **sine** and **cosine** waves which are made to align with each other for a specific values

![](https://pysdr.org/_images/IQ3.gif)

---

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

## Pluto SDR

```bash
cd ~
git clone --branch v0.0.14 https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo python3 setup.py install

```