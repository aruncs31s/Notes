---
dg-publish: true
---

# Electronics

Created : 2024-07-28 15:08

- [[#Basics]]
- [[#Energy]]
  - [[#Flow of Energy]]
  - [[#Resisters]]
    - [[#In Series]]
    - [[#In parallel]]
  - [[#Voltage Divider Rule]]
- [[Analog Circuits]]
- 
- [[03 Electronics/Embedded Systems/Embedded Systems|Embedded Systems]]
- [[Electronics Circuits]]


## Basics

## Energy
![[energy_time.excalidraw|300x300]]

$$
V_{rms} = {Vp \over \sqrt{2}} \tag{1}$$
accoring to equation 1 we can say  that
$$
V_{rms} = 330 \times 0.707 = 231 V
$$



### Flow of Energy

There is a miss conception that the electrons flowing in the wire that carries the energy but in reality the `Electric` and `Magnetic field` that carries the energy.

$$

\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B} \tag{poyniting Theorem}
$$

It defines the power per unit area transmitted by an electromagnetic wave. The [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 3#^1fe371|Poynting Vector]] ($\vec{S}$) points in the direction of energy flow and its magnitude gives the rate of energy transfer per unit area perpendicular to the direction of propagation.

#### Resisters
1. Series

$$
R = R_1 + R_2
$$
2. parallel

$$
\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}
$$


#### Voltage Divider Rule
>[!blank|right-small]
>![[Voltage Divider Rule.excalidraw]]


If A Voltage source is connected in series with 2 resistors $R_a$ and $R_b$ then Voltage across the $R_b$ is


$$
V_{Rb} = \frac{R_b}{R_a+R_b} Vin
$$

## References

1. [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 3#^1fe371|Poynting Vector]]

## Usefull Links
1. http://hyperphysics.phy-astr.gsu.edu/hbase/Electronic/trangate.html
