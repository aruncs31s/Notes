---
id: Laplace_Transform
aliases:
  - Laplace
  - s-domain
tags:
  - science
  - maths
  - transforms
dg-publish: true
---
# Laplace Transform
Created : 2024-05-18

## Contents
- [[#Definition]]
- [[#Properties]]
- [[#Common Transform Pairs]]
- [[#Relationship with Fourier Transform]]
- [[#Applications]]
- [[#Examples]]
- [[#References]]

## Definition

The **Laplace transform** converts a time-domain function $f(t)$ into a complex frequency-domain function $F(s)$:

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} f(t) e^{-st} dt
$$

Where $s = \sigma + j\omega$ is a complex variable. The integral converges for $\text{Re}(s) > \sigma_0$ (region of convergence).

The **inverse Laplace transform** is:

$$
\mathcal{L}^{-1}\{F(s)\} = f(t) = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} F(s) e^{st} ds
$$

## Properties

| Property | Time Domain $f(t)$ | $s$-Domain $F(s)$ |
|----------|-------------------|-------------------|
| Linearity | $af(t) + bg(t)$ | $aF(s) + bG(s)$ |
| $1^{\text{st}}$ Order Derivative | $f'(t)$ | $sF(s) - f(0^-)$ |
| $2^{\text{nd}}$ Order Derivative | $f''(t)$ | $s^2F(s) - sf(0^-) - f'(0^-)$ |
| Integration | $\int_0^t f(\tau) d\tau$ | $\frac{1}{s} F(s)$ |
| $t$-shift | $f(t-a)u(t-a)$ | $e^{-as}F(s)$ |
| $s$-shift | $e^{at}f(t)$ | $F(s-a)$ |
| Scaling | $f(at)$ | $\frac{1}{a}F\!\left(\frac{s}{a}\right)$ |
| Convolution | $(f * g)(t)$ | $F(s)G(s)$ |
| Initial Value | $f(0^+)$ | $\lim_{s \to \infty} sF(s)$ |
| Final Value | $f(\infty)$ | $\lim_{s \to 0} sF(s)$ |

## Common Transform Pairs

| $f(t)$ | $F(s)$ | ROC |
|--------|--------|-----|
| $\delta(t)$ | $1$ | All $s$ |
| $u(t)$ | $\displaystyle\frac{1}{s}$ | $\text{Re}(s) > 0$ |
| $t\, u(t)$ | $\displaystyle\frac{1}{s^2}$ | $\text{Re}(s) > 0$ |
| $t^n u(t)$ | $\displaystyle\frac{n!}{s^{n+1}}$ | $\text{Re}(s) > 0$ |
| $e^{-at} u(t)$ | $\displaystyle\frac{1}{s + a}$ | $\text{Re}(s) > -a$ |
| $t e^{-at} u(t)$ | $\displaystyle\frac{1}{(s + a)^2}$ | $\text{Re}(s) > -a$ |
| $\sin(\omega t) u(t)$ | $\displaystyle\frac{\omega}{s^2 + \omega^2}$ | $\text{Re}(s) > 0$ |
| $\cos(\omega t) u(t)$ | $\displaystyle\frac{s}{s^2 + \omega^2}$ | $\text{Re}(s) > 0$ |
| $e^{-at} \sin(\omega t) u(t)$ | $\displaystyle\frac{\omega}{(s + a)^2 + \omega^2}$ | $\text{Re}(s) > -a$ |
| $e^{-at} \cos(\omega t) u(t)$ | $\displaystyle\frac{s + a}{(s + a)^2 + \omega^2}$ | $\text{Re}(s) > -a$ |

## Relationship with Fourier Transform

The [[Fourier Transform]] is a special case of the Laplace transform evaluated on the imaginary axis:

$$
\mathcal{F}\{f(t)\} = \mathcal{L}\{f(t)\}\big|_{s = j\omega} = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt
$$

**Key differences:**

| Laplace | Fourier |
|---------|---------|
| $s = \sigma + j\omega$ (complex) | $j\omega$ (pure imaginary) |
| Handles transients | Steady-state only |
| Includes convergence factor $e^{-\sigma t}$ | No convergence factor |
| One-sided ($0$ to $\infty$) | Two-sided ($-\infty$ to $\infty$) |
| Handles unstable/growing signals | Requires absolute integrability |

The **FFT** (Fast Fourier Transform) is a computational algorithm for the [[Discrete Fourier Transform|DFT]]. Since the Laplace transform generalises the Fourier transform, the FFT can approximate the Laplace transform along $s = j\omega$ for sampled signals.

**Bilinear transform** maps the $s$-plane to the $z$-plane (digital domain):

$$
s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}
$$

This is how continuous-time Laplace designs (e.g. analog filters) get converted to digital filters.

## Applications

- **Control Theory** — Transfer functions $H(s) = Y(s)/X(s)$, stability via pole locations
- **Circuit Analysis** — Impedance $Z(s) = R + sL + 1/sC$ for RLC circuits
- **Signal Processing** — Filter design ([[Butterworth Filter|Butterworth]], Chebyshev), system characterisation
- **Vibrations & Mechanics** — Spring-mass-damper systems
- **Heat Transfer** — Solving [[Partial Differential Equations|PDEs]] via transform methods
- **Probability** — [[Moment Generating Function|MGF]] is essentially a Laplace transform of the PDF

## Examples

### Example 1: Solving an ODE

Solve $y'' + 3y' + 2y = u(t)$, $y(0) = 0$, $y'(0) = 0$:

$$
s^2Y(s) + 3sY(s) + 2Y(s) = \frac{1}{s}
$$

$$
Y(s) = \frac{1}{s(s+1)(s+2)} = \frac{1/2}{s} - \frac{1}{s+1} + \frac{1/2}{s+2}
$$

$$
y(t) = \left( \frac{1}{2} - e^{-t} + \frac{1}{2}e^{-2t} \right) u(t)
$$

### Example 2: RLC Circuit

For a series RLC circuit with input $v(t)$:

$$
V(s) = I(s) \left( R + sL + \frac{1}{sC} \right)
$$

$$
H(s) = \frac{I(s)}{V(s)} = \frac{1}{R + sL + 1/sC} = \frac{s}{L\left( s^2 + \frac{R}{L}s + \frac{1}{LC} \right)}
$$

Poles at $s = -\frac{R}{2L} \pm \sqrt{\left(\frac{R}{2L}\right)^2 - \frac{1}{LC}}$ determine damping behaviour.

## References

1. Oppenheim & Willsky — *Signals and Systems*
2. Ogata — *Modern Control Engineering*
3. [[Differential Equations]]
4. [[Fourier Transform]]
5. [[Transforms/LaplaceTransform|Laplace Transform — Python Implementation]]
