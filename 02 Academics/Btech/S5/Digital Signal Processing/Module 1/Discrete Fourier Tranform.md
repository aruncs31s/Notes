---
id: Discrete_Fourier_Tranform
aliases: []
tags:
  - academics
  - btech
  - s5
  - digital_signal_processing
  - module_1
Date: 16-11-2024
dg-publish: true
---
# Discrete Fourier Tranform
 

$$
X(k) = \sum_{n=0}^{N-1} x(n) e^{\frac{-j2\pi n}{N}}
$$

^32d1f3

**Where** $0\le k \le N-1$ 
*an intuitive way to think about the computation is that , we want to find the co-efficient and arrange them in original order eg 
x(n) = {1,1,0,0} gives X(k) = {2,1-j,0,1+j} , so there are equal number of output to a an input .*

# Inverse Fourier Transform 

$$
x(n) = \frac{1}{N} \sum_{n=0}^{N-1} e^{\frac{j 2 \pi n}{N}}
$$

^cf415f

**Where**  $0\le n \le N-1$

# Introduction to Twiddle Factor 

 $W_{N} = e^{\frac{-j 2 \pi}{N}}$

$$
\begin{align}
X(k) &= \sum_{n=0}^{N- 1} x(n) W_{N}^{kn} \tag{DFT}\\
x(n) &= \frac{1}{N} \sum_{n=0}^{N -1} X(k) W_{N}^{-kn} \tag{IDFT}
\end{align}
$$

![[Drawing 2024-11-16 12.38.11.excalidraw|900x100]]

