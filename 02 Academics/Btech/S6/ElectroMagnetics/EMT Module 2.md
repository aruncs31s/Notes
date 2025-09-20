---
id: Module 2
aliases: []
tags:
  - academics
  - btech
  - s6
  - electromagnetics
created: "2024-08-17"
status: pending
dg-publish: true
---
# Module 2

## Contents

- [[#Todo]]
- [[#Syllabus]]

## Todo

- [ ] Finish the Module
- [ ] Fill the contents menu

## Syllabus

1.  [ ] [[#Derivation of capacitance of 2 wire Line|Derivation of capacitance]] and inductance of two wire transmission line and coaxial cable.
2.  [ ] Energy stored in Electric and Magnetic field.
3.  [ ] Displacement current density, continuity equation.
4.  [ ] Magnetic vector potential.
5.  [ ] Relation between scalar potential and vector potential.
6.  [ ] Maxwell’s equation from fundamental laws.
7.  [ ] Boundary condition of electric field and magnetic field from Maxwell's equations.
8.  [ ] Solution of wave equation.

#### Capacitance of 2 wire Line

![[capacitance of 2 wire line drawing]]

> - Potential difference btw conductor _a_ and _b_ is given by
>   $$
>   V_{ab} = \frac{1 }{2 \pi \epsilon} \left[ Q_{a}^{+} \ln \frac{D_{ab}}{D_{aa}} + Q_{b}^{-} \ln \frac{D_{bb} }{D_{ba}}\right]\tag{1}
>   $$
> - Here $Q_{a}= +Q , Q_{b}=-Q$ , $D_{aa} = r$ and $D_{ab}=D$.
> - After simplifying using [[Logerithemic#^fceeff|This Property]] and applying the values the equation (2) can be written as
>   $$
>   V_{ab} = \frac{1}{2 \pi \epsilon }Q_{a}^{+} \ln  \left(\frac{D}{r}  \right)^2\tag{3}
>   $$
> - We know [[Logerithemic#^b6e3a2|This property]] the above equation can be simplified as
>   $$
>   V_{ab}=\frac{Q_a^{+}}{\pi\epsilon } \ln{D \over r}\tag{4}
>   $$
> - The capacitance between the conductors is
>   $$
>   C_{ab}= \frac{Q_{a}^{+}}{V_{ab} } =  \frac{Q_{a}^+}{\frac{Q_a^{+}}{\pi\epsilon } \ln{D \over r}}\tag{5}
>   $$
>   $$
>   \boxed{\color{cyan}
>   C_{ab}= \frac{\pi \epsilon }{ln{D \over r}}}
>   $$
>   #summary

- Draw the diagram of 2 conductor separated by a distance $D$
- Write the equation of $V_{ab}$
-

#### Inductance of Two wire

![[Inductance of 2 wire line]]

> In the case of a
>
> - The Flux linkage of conductor a is given by
>   $$
>   \Psi_{a}= \frac{\mu_{0}}{{2}\pi}  \left[ I_{a} \ln {1 \over D_{aa} } + I_{b}\ln{1 \over D_{ab}}  \right]\tag{1}
>   $$
> - Where $I_{a}= +I , I_{b}=-I$ , $D_{aa} = r$ and $D_{ab}=D$. After substituting the this into equation $(1)$
>   $$
>   \Psi_{a}=\frac{\mu_{0}}{2\pi} \left[I  \ln({1 \over r}) -I \ln({1 \over D}) \right]\tag{2}
>   $$
> - By using [[Logerithemic#^fceeff|This Property]] equation $(2)$ can be written as
>   $$
>   \Psi_{a} =  \frac{\mu_{0}}{2\pi} \left[I \ln({D \over r}) \right]
>   $$
> - The inductance of the conductor
>   $$
>   \boxed{
>   L_{a} = \frac{\Psi}{L_{ab}} =\frac{\mu_{0}}{2\pi } \ln({D \over r}) }\tag{H/m}
>   $$

> In the case of b
>
> - The flux linkage of conductor b is given by
>   $$
>   \Psi_{b}= \frac{\mu_{0}}{{2}\pi}  \left[ I_{b} \ln {1 \over D_{bb} } + I_a\ln{1 \over D_{ba}}  \right]\tag{1}
>   $$
> - Where $I_{a}= +I , I_{b}=-I$ , $D_{bb} = r$ and $D_{ba}=D$. After substituting the this into equation $(1)$
>   $$
>   \Psi_{b} = \frac{\mu_0}{2\pi} \left[I \ln\frac{1}{r} - I \ln \frac{1}{D}\right]
>   $$
> - By using [[Logerithemic#^fceeff|This Property]] we can rewrite the equation as
>   $$
>   \Psi_{b}= \frac{\mu_{0 }}{2\pi}  I \ln({r \over D})
>   $$
> - Now the inductance of the conductor _b_ is
>   $$\boxed{L_{a}= \frac{\Psi_{a}}{I} = \frac{\mu_0}{2\pi}\ln({r \over D}) }\tag{H/m}$$
> - $\therefore$ The inductance of both conductor (loop inductance) is
>   $$
>   \color{cyan}
>   \boxed{ L_{a} + L_{b} = \frac{\mu_0}{\pi}\ln \frac{D}{r}} \tag{H/m}
>   $$

---

- [x] Need to check if the equation is right ✅ 2024-05-20

#### Capacitance of coaxial cable

![[capacitance of coax cable diagram]]
coaxial cable is placed in z direction

> Here 1. $a$ -> radius of the inner conductor 2. $b$ -> radius of the outer conductor 3. $z$ -> length of the conductor
>
> - Here V is given by the equation
>   $$
>   V = - \int_b^{a} E \cdot dl\tag{1}
>   $$
> - Where E -> electric field due to an infinite line charge
>   $$E = \frac{\rho_{l}}{2\pi\epsilon\rho} \hat a_\rho\tag{2}$$
>   by substituting equation $(2)$ -> $(1)$ > $$V = -\int_{\rho=a}^b\frac{\rho_{l}}{2\pi\epsilon\rho} \hat a_{\rho}\cdot d\rho \cdot \hat a_\rho\tag{3}$$
>   We know $\hat a_{\rho}\cdot \hat a_{\rho}= 1$ > $$\begin{align}V &=\frac{\rho_{l}}{2\pi\epsilon} \int_{\rho =a}^{b} {d\rho \over \rho }\\ &=\frac{\rho_{l}}{2\pi\epsilon} \ln{b \over a}\end{align}$$
> - Capacitance
>   $$C = {Q \over V} = \frac{\rho_{L}l}{\frac{\rho_{l}}{2\pi\epsilon} \ln{b \over a}} =$$ >$$C = \frac{2\pi \epsilon l}{ln({b\over a})}$$

---

#### Inductance of coaxial cable

- We know magnetic flux through a surface
  $$
  \Psi = \int_{s} B \cdot dS \tag{1}
  $$
- We know Magnetic field due to an infinite current carrying conductor
  $$
  \begin{align}
  H &= \frac{I}{2\pi \rho}\hat a_{\phi}\\
  B &= \mu H
  \end{align}
  $$
- Substituting both the values of $B$ and $H$ in equation $(1)$
  $$
  \begin{align*}
  \Psi &=   \int_{\rho=a}^{b}\int_{z=0}^{l}\frac{\mu I}{2\pi \rho } \hat a_{\phi}\cdot \hat a_{\phi} d_{\rho}d_{z}\\
  &= \frac{\mu I}{2\pi  }\int_{z=0}^{l}d_{z}\int_{\rho=a}^{b} \frac{d\rho}{\rho}
  \end{align*}
  $$
  $$
  \Psi = \frac{\mu I}{2\pi}\ln ({b\over a})
  $$
- Inductance
  $$
  \begin{align*}
   L &= {\Psi \over I}\\
  &= {\frac{\mu I}{2\pi}\ln ({b\over a}) \over I}
  \end{align*}
  $$
  $$
  \color{cyan}\boxed{
  L = \frac{\mu }{2\pi}\ln ({b\over a})}
  $$

#### Energy stored in Electric Field

![[energy stored in electric field diagram]]

- We use **work done**
- In this we consider charges $Q1$ ,$Q2$ and $Q3$ move from $\infty$ to points $P1$ ,$P2$ and $P3$
- Total work done used to bring those charges to respected position is the total work done
  $$
  \begin{align*}
  W_{E}&=  W_{1}+ W_{2}+W_{3}\\
  &= 0 + Q_{2}V_{21}+Q_{3}V_{31}+Q_{3}V_{32}
  \end{align*}
  $$
  > [!NOTE] The 0
  > The zero is due to no charges is being present on the surface when moving the first time , and after the first charge is reached the surface it will create an electric field and it the $Q_{2}$ and $Q_{3}$ will experience that ,Also when moving $Q_3$ there will be 2 charges

![[Pasted image 20240523064927.png]]
![[Pasted image 20240523064959.png]]
![[Pasted image 20240523065013.png]]
![[Pasted image 20240523065030.png]]
![[Pasted image 20240523065053.png]]
![[Pasted image 20240523065105.png]]
At surface S becomes large the first term tends to zero

![[Pasted image 20240523065140.png]]
![[Pasted image 20240523065248.png]]
![[Pasted image 20240523065303.png]]

#### Maxwell's Equations

1.  [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 2/Ampere's Law]]
2.  [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 2/Faraday's Law of induction]]
3.  [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 2/Gauss's Law]]

- [ ] Fix this ⏫

| Point Form                                                                                              | Integral Form                                                                                                                                                              |     |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| $\nabla \times \overrightarrow H=\overrightarrow J_{c} + \frac{\partial \overrightarrow D}{\partial t}$ | $$\oint \overrightarrow H \cdot \overrightarrow dl = \int_s\left(\overrightarrow {J_c}+\frac {\partial \overrightarrow D}{ \partial t}\right)\cdot dS \tag{Ampere's Law}$$ |     |
| $\nabla \times \overrightarrow E = \large - \frac{\partial \overrightarrow B}{\partial t}$              | $$\oint \overrightarrow E \cdot dl = \int_s\left(-\frac {\partial \overrightarrow B}{ \partial t}\right)\cdot dS\tag{Faraday's Law}$$                                      |     |
| $\nabla \cdot \overrightarrow D=\rho$                                                                   | $$\oint_s \overrightarrow D \cdot dS = \int_v \rho \ dv \tag{Gauss's Law}$$                                                                                                |     |
| $\nabla \cdot \overrightarrow B = 0$                                                                    | $$\oint _s \overrightarrow B \cdot dS = 0 \tag{nonexistance of monopole}$$                                                                                                 |     |

##### From Ampere's Circuit Law

##### From [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 2/Gauss's Law]]

$$
\oint D \cdot dS = Q_{enc}\tag{1}
$$

For volume charge

$$
\int_v \rho_{v}dv = Q_{enc}\tag{2}
$$

Where $\rho_v$ is volume charge density
by comparing equations $(1)$ and $(2)$

$$
\oint \overrightarrow D \cdot dS = \int_{v}\rho_{v}dv \tag{A}
$$

- > The above equation is known as _Integral form of [[Maxwell|Maxwell's]] First Equation_
- [ ] Research and complete the derivation .

## References

- 1.
