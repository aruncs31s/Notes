---
id: Analog_Circuits
aliases: []
tags:
  - electronics
  - analog_circuits
Date: 23-11-2024
tag: 
dg-publish: true
---
# Analog Circuits
- [[Capacitors]]
## Oscillators
1. [[#RC Phase Shift Oscillator]]
2. [[Design of sine wave oscillators using op-amp]]
#### RC Phase Shift Oscillator 
![[rcphaseshifosccilator.excalidraw|500x300]]
- uses +ve feedback 

### Design 
This **oscillator** circuit needs to satisfy the followings 
1. 0 , $2\pi$ phase shift 
2. Total loop gain $A\beta = 1$  , for sustained oscillation
$A$ -> Gain of the amplifier , $A=29$
$\beta$ -> Feedback factor  , Here $\frac{1}{\beta}$

**Frequency of Oscillation**:
$$
f = \frac{1}{2 \pi RC \sqrt{ 6 + 4 R_{C} / R }}
$$

$f$ -> Frequency of oscillation  
$R_c$ -> Resistance series with collector 

**Gain of the amplifier** : Here required Gain of Amplifier is $A = 29$ and the feedback mechanism should have $\beta=\frac{1}{29}$ in order for sustainable oscillation

$$
hfe \ge 23  + 29 \frac{R}{R_{c}} + 4 \frac{R_{c}}{R}
$$
