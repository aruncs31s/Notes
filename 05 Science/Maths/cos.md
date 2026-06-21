---
id: cos
aliases:
  - cosine
  - Euler cosine
tags:
  - science
  - maths
  - trigonometry
dg-publish: true
---
# Cosine
Created : 2024-06-15

## Contents
- [[#Euler's Formula]]
- [[#Identities]]
- [[#Relation to Other Transforms]]

## Euler's Formula

From [[Euler Angle|Euler's formula]] $e^{ix} = \cos x + i\sin x$, cosine is expressed as the average of complex exponentials:

$$
\boxed{\cos x = \frac{e^{ix} + e^{-ix}}{2}}
$$

^88e638

Derivation:

$$
\begin{aligned}
e^{ix} &= \cos x + i\sin x \\
e^{-ix} &= \cos x - i\sin x \\
\text{Adding: } e^{ix} + e^{-ix} &= 2\cos x
\end{aligned}
$$

Similarly, $\displaystyle \sin x = \frac{e^{ix} - e^{-ix}}{2i}$.

## Identities

| Identity | Formula |
|----------|---------|
| Pythagorean | $\cos^2 x + \sin^2 x = 1$ |
| Double angle | $\cos(2x) = 2\cos^2 x - 1 = 1 - 2\sin^2 x$ |
| Sum of angles | $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$ |
| Product-to-sum | $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$ |
| Hyperbolic | $\cos(ix) = \cosh x$ |
| Laplace transform | $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2 + \omega^2}$ |

## Relation to Other Transforms

Using the exponential form:

$$
\mathcal{L}\{\cos(\omega t)\} = \frac{1}{2}\left( \frac{1}{s - i\omega} + \frac{1}{s + i\omega} \right) = \frac{s}{s^2 + \omega^2}
$$

See: [[Laplace Transform]], [[Fourier Transform]], [[Trigonometry]]
