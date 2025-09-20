---
id: Module_4
aliases: []
tags:
  - academics
  - btech
  - s6
  - information_theory_and_coding
dg-publish: true
---
# Module 4
Created : 2024-04-15 00:23

## Contents
- [Syllabus](#syllabus)

## Syllabus
- [Cyclic codes]().
- Polynomial and matrix description.
- Interrelation between polynomial and matrix view point.
- Systematic encoding.
- Decoding of cyclic codes.
(Only description, no decoding algorithms)
- Hamming Codes,
- BCH codes,
- Reed-Solomon Codes.

## Previous Year Questions
### Questions
1. The generator polynomial of a $(7,4)$ cyclic code is $G(p) = p^3 + p +1$ .find the code vectors corresponding to the message vectors $1011$ in Non-systematic form
### Answers

1. Express the message polynomial �(�)m(x) in terms of �x.
2. Multiply $m(x)$ by $x^3$ to match the degree of $G(p)$.
3. Perform polynomial division to find the remainder, which represents the codeword.
>Step 1: Express the message polynomial
The message vector is $1011$, so the message polynomial $m(x)$ is:
> $m(x) = x^3 + x + 1$

>Step 2: Multiply by $x^3$
>Multiply $m(x)$ by $x^3$ to match the degree of $G(p)$
>$m(x) \times x^3 = x^6 +x^4 + x^3$

>Step 3: Polynomial Division
>Perform polynomial division of $x^6 +x^4 + x^3$ by $p^3 + p + 1$
>

 p^3 + p + 1   |   x^6 + x^4 + x^3
 -             |   (x^6 + 0x^4 + x^3) + (x^3 + 0x^2 + 0x + 0)
--------------------------
                x^4 + x^2 + 1

