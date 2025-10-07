---
tags:
  - academics
  - btech
  - s5
  - supplementary
---
# Analog and Digital Communication

## Contents

[[#ADC Module 5]]

## Syllabus

### Module 1 Analog Communication

- Block diagram of a communication system.
- Need for analog modulation.
- Amplitude modulation.
- Equation and spectrum of AM signal.
- DSB-SC and SSB systems.
- Block diagram of SSB transmitter and receiver.
- Frequency and phase modulation.
- Narrow and wide band FM and their spectra.
- FM transmitter and receiver.

### Module 2 : Review of Random Variables and Random Processes

- Review of random variables – both discrete and continuous.
- CDF and PDF
- statistical averages. (Only definitions, computations and significance)
- Entropy, differential entropy.
- Differential entropy of a Gaussian RV.
- Conditional entropy, mutual information.
- Stochastic processes, Stationarity.
- Conditions for WSS and SSS.
- Autocorrelation and power spectral density.
- LTI systems with WSS as input

### Module 3: Source Coding

- Source coding theorems I and II (Statements only).
- Waveform coding.
- Sampling and Quantization.
- Pulse code modulation, Transmitter and receiver.
- Companding.
- Practical 15 level A and mu-law companders.
- DPCM transmitter and receiver.
- Design of linear predictor.
- Wiener-Hopf equation.
- Delta modulation.
- Slope overload

### Module 4 : G-S Procedure and Effects in the Channel

- Gram-Schmitt procedure.
- Signal space.
- Baseband transmission through AWGN channel.
- Mathematical model of ISI.
- Nyquit criterion for zero ISI.
- Signal modeling for ISI, Raised cosine and Square-root raised cosine spectrum, Partial response signalling and duobinary coding.
- Equalization.
- Design of zero forcing equalizer.
- Vector model of AWGN channel.
- Matched filter and correlation receivers.
- MAP receiver, Maximum likelihood receiver and probability of error.
- Capacity of an AWGN channel (Expression only) -- significance in the design of communication schemes.

## References

1.

# ADC Module 5

#### BPSK

^77bd04

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
\Phi_1(t) &= {S_1(t) \over \sqrt{E_b}} \\
S_1(t) &= \sqrt{Eb} \frac{2}{T_b} \cos(\pi f_c t) \\
\end{align}
$$

by comparing above equation

$$
\Phi_1(t) = \sqrt{{2\over T_b}  \cos(\pi f_c t)  }
$$

$$
\begin{align}
S_1(t) = \sqrt{E_b} \Phi_1(t) \tag{a}\\
S_2(t) = -\sqrt{E_b} \Phi_1(t) \tag{b}\\
\end{align}
$$

\*For BPSK we only need 1 orthonormal basis function => $\Phi_1{t}$
