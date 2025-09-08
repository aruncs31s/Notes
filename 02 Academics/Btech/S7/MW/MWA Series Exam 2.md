---
aliases: 
Date: 15-10-2024
---
# MWA Series Exam 2
## Topics 
- Microstrip antenna (Fringing Principle),(Neat diagram ,working principle) 
- Design Steps (Example Problem)

## Answers

![[microstrip patch.excalidraw]]
![[microstrip patch side view.excalidraw]]

#### Design Steps of Microstrip Patch Antenna
1. Find the practical width $W$
$$
W = \frac{c}{2 f_r} \sqrt{\frac{2}{\epsilon_r + 1}} \tag{1.0}
$$
*Here*
- $\epsilon_r$ -> Dielectric Constant
- $f_r$ -> Resonant Frequency
- $c$ -> Speed of Light

2. Find the effective dielectric constant 
$$
\epsilon_{effective} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left(1 + 12 \frac{h}{W}\right)^{-1/2} \tag{2.0}
$$
3. Find the ethe length of the patch $L_{efff}$
 *Because of the  fringing effect the effective length is greater than the actual length*
 
$$
\Delta L  = 0.412 h \frac{(\epsilon_{eff} + 0.3 )} {(\epsilon_{eff} - 0.258)} \frac{\frac{W}{h} + 0.264}{\frac{W}{h} + 0.8} \tag{3.0}
$$
$$
L_{eff} = \frac{c}{2 f_r \sqrt{\epsilon_{eff}}} \tag{4.0}
$$
4. Find the physical Length ($L$)
$$
L = L_{eff} - 2 \Delta L
$$


##### Example Problem 
**Q**: Design a rectangular microstrip antenna using  a substrate (RT/duroid 5880 ) with *dielectric constant of 2.2* , *h = 0.1588cm* so to resonate at *$10GHz$*
**Ans**: 
We have 
- $fr$ = $10GHz$
- $\epsilon_r$ = $2.2$
- $h = 0.1588cm$
1. Finding Practical width $W$
$$
\begin{align}
W &= \frac{c}{2 f_r} \sqrt{\frac{2}{\epsilon_R + 1}} \\
&= \frac{3 \times 10^8}{2 \times 10 \times 10^ 9} \sqrt{\frac{2}{2.2 + 1}} \\
&= 1.18585423_m  \tag{1.0}
\end{align}
$$
2. Find effective dielectric constant
$$
\begin{align} 
\epsilon_{effective} &= \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left(1 + 12 \frac{h}{W}\right)^{-1/2} \\
\epsilon_{eff} &= \frac{2.2 +1}{2} + \frac{2.2 -1 }{2} \sqrt{1 + 12{0.1588 \times 10^-1\over 1.18585423}}
\end{align}
$$

