---
id: Electronics
aliases: []
tags: []
---

# Electronics

Created : 2024-07-28 15:08

- [[#Basics]]
  - [[#Flow of Energy]]
  - [[#Resisters]]
    - [[#In Series]]
    - [[#In parallel]]
  - [[#Voltage Divider Rule]]
- [[Old_NOTES/Academics/Btech/S6/Embedded Systems/Embedded Systems]]
  - [[Sensors]]

## Basics

#### Flow of Energy

There is a miss conception that the electrons flowing in the wire that carries the energy but in reality the `Electric` and `Magnetic field` that carries the energy.

$$

\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B} \tag{poyniting Theorem}
$$

It defines the power per unit area transmitted by an electromagnetic wave. The [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 3#^1fe371|Poynting Vector]] ($\vec{S}$) points in the direction of energy flow and its magnitude gives the rate of energy transfer per unit area perpendicular to the direction of propagation.

#### Resisters

![[Resistor.excalidraw|200x20]]

##### In Series

$$
R = R_1 + R_2
$$

[[resistors combination.excalidraw#^T_8zWJUbBBX0Nv3szhIBf|resistors in series]]

##### In parallel

$$
\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}
$$

[[resistors combination.excalidraw#^GLen6MvLS1DNA-OIhM3LP|Resisters in parallel]]

#### Voltage Divider Rule
>[!blank|right-small]
>![[Voltage Divider Rule.excalidraw]]


If A Voltage source is connected in series with 2 resistors $R_a$ and $R_b$ then Voltage across the $R_b$ is


$$
V_{Rb} = \frac{R_b}{R_a+R_b} Vin
$$

## References

1. [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 3#^1fe371|Poynting Vector]]
2. [[Academics/S6/ElectroMagnetics_OLD/Electromagnetics]]
