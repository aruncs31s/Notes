---
id: Module_1
aliases: []
tags:
  - academics
  - btech
  - s6
  - information_theory_and_coding
dg-publish: true
---
# ITC Module 1
Created : 2024-05-30 14:40

## Syllabus
- [x] Entropy, ✅ 2024-05-31
	- [x] Properties of Entropy ✅ 2024-05-31
	- [ ] Joint and Conditional Entropy,
- [ ] Mutual Information,
	- [ ] Properties of Mutual Information.
- [ ] Discrete memoryless sources
- [ ] Source code
- [ ]  Average length of source code,
- [ ] Bounds on average length
- [ ] Uniquely decodable and prefix-free source codes.
- [ ] Kraft Inequality (with proof), Huffman code.
- [x] Shannon’s source coding theorem (both achievability and converse) and operational meaning of entropy ✅ 2024-05-31

## Contents

### Entropy
$$
H(X) = P(X) \cdot \log({1\over P(X)})
$$

#### Information Rate/Entropy Rate

$$
R = r_s \cdot H\tag{bits/sec}
$$
-> $\large r_s$ = Symbol Rate 
-> $R$ = Information Rate

#### Properties of Entropy 
1. The entropy function is continuous in each and every independent variable $P_k$ in the interval $(0,1)$.  
*Since p1 is continuous in the interval (0,1), logarithm of a continuous function is also continuous*.
2.  $H(S) = 0$, if and only if the probability $P_k = 1$ for some k and the remaining probabilities in the set are all zero; this lower bound on entropy corresponds to no uncertainty.  
3. $H(S) = \log_2K$, if and only if $P_k = \large{1\over K}$ for all k (i.e., all the symbols in the alphabet S are equiprobable); this upper bound on entropy ==corresponds to maximum uncertainty.==

## References
1. 