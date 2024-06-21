# Module 1

## Contents
- [Syllabus](#syllabus)
- 
### Syllabus

- [x] Basic Elements of a DSP system ✅ 2024-06-17
- [x] Typical DSP applications ✅ 2024-06-17
- [x] Finite-length discrete transforms ✅ 2024-06-17
- [ ] Orthogonal transforms 
- [ ] The Discrete Fourier Transform: DFT as a linear transformation (Matrix relations).
- [ ] Relationship of the DFT to other transforms
- [ ] IDFT, Properties of DFT and examples.
- [ ] Circular convolution
- [ ] Linear Filtering methods based on the DFT
- [ ] linear convolution using circular convolution
- [ ] Filtering of long data sequences,
- [ ] overlap save and overlap add methods
- [ ] Frequency Analysis of Signals using the DFT (concept only required)

## Introduction

### Fourier Series
The Fourier series is a mathematical tool used to ==represent a periodic function as the sum of simple sine and cosine functions==. It is named after Jean-Baptiste Joseph Fourier, who introduced the concept in the early 19th century. The Fourier series is particularly useful for ==analyzing signals that are periodic in nature==.
`FS` is represented by $f(t)$ with time period $T$ and it is equal to 
$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)\right]
$$
or
$$
x(t) = \sum_{k=-\infty}^\infty X[k]e^{jk\omega_0t}
$$
and 
$$
X[k] = {1 \over T} \int_{(t)} x(t)e^{-j\omega_0t} dt
$$
$x(t)$ has period T and $\omega_0 = {2 \pi \over T}$ 

> [!IMPORTANT] Applicability
> `Fourier Series` is only used for periodic signals 



### Fourier Transform
The Fourier Transform is a mathematical technique used in signal processing and image analysis, among other fields, ==to transform a function of time (a signl) into a function of frequency==

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt\
$$
where 
- $F(\omega)$ Fourier transform coefficient of $f(t)$
- $\omega$ is the Frequency

> [!NOTE] FT
> The Fourier Transform decomposes a signal into its constituent
 frequencies,  allowing for the analysis of the signal's frequency
 components 
#### Inverse Fourier Transform

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{j\omega t} d
\omega\
$$




### Discrete-Time Fourier Series

$$
x[n] = \sum_{K=0}^{N} X[k]e^{j\Omega_0 n}
$$
$$
X = {1 \over N} \sum_{n=0}^{N} x[n]e^{-jk\Omega_0n}
$$
*$x[n]$ and $X[k]$ have period $N$*
$$
\Omega_0 = {2 \pi \over N}
$$

### Discrete-Time Fourier Transform
- For discrete time non-periodic signals
- Continuous and periodic with a period of 2
- 
$$
x[n] = {1 \over 2 \pi} \int_{-\pi}^{\pi} X\left(e^{j\Omega}\right) e^{j\Omega n} d\Omega\tag{Synthesis Equation}
$$

$$
X(e^{j\Omega}) \sum_{n = -\infty}^{\infty} x[n]e^{-j\Omega n}\tag{Analysis Equation}
$$
*where $X(e^{j\Omega})$ has period $2\pi$*


#### Discrete Fourier Transform(DFT)
- **DFT** of a finite duration sequence $x[n]$ is obtained by sampling **[[#Discrete-Time Fourier Transform|DTFT]]** at **N** equally spaced points over the interval $0\le \omega \le 2\pi$ with spacing $2\pi \over N$

> [!NOTE] Spacing
> The Spacing in the [[#Discrete Fourier Transform(DFT)|DFT]] increases with decrease in the no of sampling points taken , if the N = 4 , The points will be $\large0,{\pi\over 2},\pi,{3 \pi \over 2}$
> - The N points should be located at $$\omega_k = {2\pi \over N} k$$ ,where  $k = 1,2,3,.....,N-1$
- [ ] Complete this above statement

#equation 

$$
X(k) = X(e^{jw}) \ , \omega = {2\pi \over N} k 
$$


##### N Point DFT

- **N point DFT** of a finite duration sequence x[n] of length L($L\le N$) can be calculated as
$$
X(k) = \sum_{n=0}^{N-1} x(n) e^{\large -j2\pi \over N} kn 
$$
*where $k=0,1,2,....N-1$*



### Filtering out long data sequences

#### Overlap - save method  
Let's consider an input sequence $x(n)$ of length $L$, and response $h(n)$ of length $M$, the steps to follow overlap - save method is  
1. : input $x(n)$ is divided into length $L (L>M)$  
2. : Calculate the length $N=L+M-1$  
3. : Add $M-1$ zeros to the start to first segment, each segment (length = L) has its first $M-1$ points coming from previous segment, making each of length $N$  
4. : Make impulse response to length N by adding zeros  
5. ; Find the circular convolution of each new segments with new $h(n)$  
6. : Linearly combine each results and take sequence of length L+M-1 from that by discarding/removing first $M-1$ points