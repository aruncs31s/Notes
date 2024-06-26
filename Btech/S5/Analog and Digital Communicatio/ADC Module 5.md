---
id: 1719156550-RSGW
aliases:
  - ADC Module 5
tags: []
---

# ADC Module 5

#### BPSK

Coherent Binary Phase Shift Keying

$$
s_1(t) = A \cos(2\pi f_ct )\tag{1}
$$

$$
s_2(t) = -A \cos (2 \pi f_ct)\tag{2}
$$

- Amplitude in terms of _bit energy($E_b$)_ and _Bit Duration($T_b$)_

$$
\begin{align}
Power &= \frac{E_b}{T_b}\tag{3}\\
Rms \ Value = \frac{A}{\sqrt{2}}
&= \frac{A^2}{\sqrt{2}}\tag{4}
\end{align}
$$

By comparing equation(3) and (4)

$$
\begin{align}
\frac{A^2}{\sqrt{2}} &= \frac{E_b}{T_b} \\
A &= \sqrt{\frac{2 E_b }{T}}
\end{align}
$$

now

$$
\boxed{\color{cyan}
\begin{align}
s_1(t) &= \sqrt{\frac{2 E_b }{T}}\cos(2\pi f_ct )\\
s_2(t) &=  \sqrt{\frac{2 E_b }{T}}\cos (2 \pi f_ct)
\end{align}
}
$$

> [!NOTE] Antipodal Signals
> Since $S_1(t)$ and $S_2(t)$ are in $180^o$ out of phase they are called Antipodal Signals

---

$$
\begin{align}
\Phi_1(t) &= {S_1(t) \over \sqrt{E_b} \\
S_1(t) 7= \sqrt{Eb} \frav{2}{T_b} \cos(\pi f_c t) \\
\end{align}
$$

by comparing above equation

$$
\Phi_1(t) = \sqrt{{2\over T_b}  \cos(\pi f_c t)  }
$$

$$
\boxed{
S_1(t) = \sqrt{E_b} \Phi_1(t) \tag{a}
S_2(t) = -\sqrt{E_b} \Phi_1(t) \tag{b}
}
$$

\*For BPSK we only need 1 orthonormal basis function => $\Phi_1{t}$
