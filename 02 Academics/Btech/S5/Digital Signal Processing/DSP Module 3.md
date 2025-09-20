---
id: DSP Module 3
aliases: []
tags:
  - academics
  - btech
  - s5
  - digital_signal_processing
dg-publish: true
---
### Designing of FIR Filter

#### Windows

1. Rectangular window

- Non Causal

  $$
  \begin{align}
  W_R(n) &= 1 \tag{for -(N - 1)/2 to (N-1)/2 } \\
  W_R(n) &= 0 \tag{otherwise}
  \end{align}
  $$

- Causal
  $$
  \begin{align}
  W_R(n) &= 1 \tag{for 0 to N}\\
  &=0  \tag{otherwise}
  \end{align}
  $$

![[Pasted image 20240622065356.png]]

- [ ] Complete this

##### Design Procedure

1. Choose desired frequency response of the filter $H_d(e^{j\omega})$
2. Take the inverse [[Fourier Series and Transform#Fourier Transform]] of $H_d(e^{j\omega})$ to obtain $h_d(n)$
3. Choose a window response $W(n)$ and multiply it with $h_d(n)$ to convert infinite duration impulse response to finite duration impulse response
   ![[Pasted image 20240622065544.png]]

$$
h(n) = h_d(n) * W(n)
$$

4. The transfer function of the filter is obtained by taking Z-transform of $h(n)$
