---
id: Experiment_5
aliases: []
tags:
  - academics
  - btech
  - s7
  - electromagnetics_lab
Date: 13-11-2024
dg-publish: true
---
# Isolation of E,H,Magic Tee

$$
\begin{align}
\text{Isolation(dB)} &= 10 \log_{10}\frac{P_{4}}{P_{3}}  \\
\text{Coupling Coefficient} & = C_{ij} = 10 ^{\alpha/10}
\end{align}
$$
Where 
- $\alpha$ is the Attenuation 
- $i$ = input arm 
- $j$ = output arm 
- $\alpha = 10 \log_{10}\frac{|P_{i}|}{|P_{j}|}$
- $P_{i}$ = Power derived to arm $i$
- $P_{j}$ = Power derived to arm $j$

#### H Plane Tee  

$$
\text{Coupling Coefficient} = P_{1} - P_{3} 
$$

#### E Plane Tee 

$$
\text{Coupling Coefficient} = P_{2} - P_{3}
$$

#### Magic Tee 
$$
\begin{align}  \\
\text{Coupling Coefficient} & = P_{1} - P_{2} \\ \\

\text{Isolation(dB)} &= P_{4} - P_{3} \\

\end{align}
$$