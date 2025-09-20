---
id: Module 3
aliases: []
tags:
  - academics
  - btech
  - s6
  - information_theory_and_coding
dg-publish: true
---
# Module 3

Created : 2024-05-31 16:26

## Syllabus

- [ ] Overview of
  1. [x] Groups, ✅ 2024-05-31
  2. [x] Rings, ✅ 2024-06-01
  3. [x] Finite Fields, ✅ 2024-06-01
  4. [ ] Construction of Finite Fields from Polynomial rings,
  5. [ ] Vector spaces.
- [ ] Block codes and parameters.
- [ ] Error detecting and correcting capability.
- [ ] Linear block codes.
- [ ] Two simple examples -- Repetition code and single parity-check code.
- [ ] Generator and parity-check matrix.
- [ ] Systematic form.
- [ ] Maximum likelihood decoding of linear block codes.
- [ ] Bounded distance decoding. Syndrome.
- [ ] Standard array decoding.

## Contents

-

##### Groups

A set _G_ on which binary operation $*$ is defined is called **Group** , and it should satisfy the following conditions

1. The binary operation $*$ is associative
2. $G$ contains an element $\large e$ such that , for any $\large a$ in $G$
   $$
   \large a \ * \ e = e \ * \ a = a
   $$

- e -> identity element of $G$
1. For any element $a$ in $G$, there exists another element $a\prime$ in $G$ such that 
$$
a \times a\prime = a\prime \times a = e
$$
- *Where $a\prime$ is called an inverse of a *

	 ![[Pasted image 20240531203656.png]]

4. A group `G` is said to be commutative if its binary operation , also satisfies the following . For any `a` and `b` `G`
$$
a \times b = b \times a
$$

#example

$$
G = \{0,1\}
$$

![[Pasted image 20240531203923.png]]

##### Rings

![[Pasted image 20240531204032.png]]

![[Pasted image 20240531204825.png]]

![[Pasted image 20240531205039.png]]

![[Pasted image 20240531205239.png]]

![[Pasted image 20240531205301.png]]

##### Block Codes

A block code consists of a set of fixed length **codewords**. ==The fixed length of these codewords is called the Block Length==. And is Typically denoted by $n$ . Thus a code of blocklength $n$ consists of a set of codewords having n componets

> A block code of size M is defined over an alphabet with $q$ symbols is a set of M q-ary sequence , each of length $n$ . In the special case that $q$=2 , the symbol are called bits and the code is said to be binary code .Usually , $M=q^k$ for some integer $k$ , and we call such code as an $(n,k)$ code

![[Pasted image 20240601031450.png]]

![[Pasted image 20240601031508.png]]

![[Pasted image 20240601031816.png]]

![[Pasted image 20240601031926.png]]

![[Pasted image 20240601032145.png]]

![[Pasted image 20240601032452.png]]
![[Pasted image 20240601032731.png]]

Here parity bit is the message itself

## References

1.
