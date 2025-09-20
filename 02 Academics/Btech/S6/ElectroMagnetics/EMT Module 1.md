---
id: EMT Module 1
aliases: []
tags:
  - academics
  - btech
  - s6
  - electromagnetics
Created: "22-08-2024"
dg-publish: true
---
# Module 1

> ## Syllabus
>
> - [x] Introduction to Electromagnetic Theory. ✅ 2024-08-22
> - [x] [[#Review of Vector Calculus]] - curl, divergence gradient. ✅ 2024-08-22
> - [ ] [[Co-ordinate Systems]] - Rectangular, cylindrical and spherical coordinate systems.
> - [ ] Expression of curl divergence and Laplacian in cartesian, cylindrical and spherical coordinate system.
> - [ ] Electric field and magnetic field, Review of Coulomb’s law, Gauss law and Amperes current law.
> - [ ] Poisson and Laplace equations, Determination of E and V using Laplace equation.

### Introduction

_Electromagnetic theory is a branch of physics that deals with the study of electromagnetic fields, which are the interaction of electric and magnetic fields. It encompasses the laws and principles that govern these fields, as well as their behavior and effects on matter._

### Review of Vector Calculus

1. [[#Curl]]
2. [[#Divergence]]

#### Curl

_Curl of function explains rotation of a body at different position , means torque at the position_

- If `Curl` of a function is ==greater than 0 then body will rotate in Anti-Clockwise direction==
- If `Curl` of a function is ==less than 0 then the body will rotate in Clockwise direction==

$$
Curl \ \overrightarrow A = \nabla \times \overrightarrow A = \lim_{\Delta S \to 0}  \left( \frac {\oint \overrightarrow A . dl}{ \Delta S }  \right) a_n
$$

Where $\Delta S$ is the area bounded by the curve $L$
Curl is also defined as ==Circulation per unit area==

$$
 Curl \overrightarrow A = \frac{Circulation}{Area}
$$

> Where area is $\Delta S$ is bounded by the curve $L$ and $a_n$ the unit vector normal to the surface

---

- A vector is said to be irrotational if its curl is $0$

$$
 \nabla \times \overrightarrow A = \begin{bmatrix} \hat a_{x} & \hat a_{y} & \hat a_{z} \\ \frac{\partial}{\partial x} & \frac{\partial }{\partial y}& \frac{\partial }{\partial z} \\ A_x & A_y & A_z \end{bmatrix} \tag{Cartesian}
$$

$$
 \nabla \times \overrightarrow A = \begin{bmatrix} \hat a_{\rho} & \rho \hat a_{\phi} & \hat a_{z} \\ \frac{\partial}{\partial \rho} & \frac{\partial }{\partial \phi}& \frac{\partial }{\partial z} \\ A_\rho & \rho A_\phi & A_z \end{bmatrix} \tag{Cylindrical}
$$

$$
 \nabla \times \overrightarrow A = \begin{bmatrix} \hat a_{r} & r\hat a_{\theta} & r\sin \theta\hat a_{z} \\ \frac{\partial}{\partial r} & \frac{\partial }{\partial \theta}& \frac{\partial }{\partial \phi} \\ A_\rho & r A_\theta & r \sin \theta A_\phi \end{bmatrix} \tag{Spherical}
$$

> The cul of $A$ is a rotational vector whose magnitude is the maximum circulation of $A$ per unit area as the area tends to zero and where direction is the normal direction of the area when the area is oriented so as to make the circulation maximum.

---

###### Properties

1. The **Curl** of a vector field is an anther vector field
2. The curl of a **scalar** field $V$ ,$\nabla \times V$ make no sense
3. $\nabla \times (A + B) = \nabla \times A + \nabla \times B $
4. $\nabla \times (A + B) = A(\nabla \cdot B ) - B ( \nabla \cdot A ) + (B \cdot \nabla A ) -(A \cdot \nabla ) B$
5. The [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Divergence|divergence]] of the curl of a vector field vanishes , that is $\nabla(\nabla \times A) = 0$
6. The curl of the [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Gradient of a Scalar|gradient]] of a scalar field also equal to zero $\nabla \times \nabla V = 0$

#### Divergence

_The Divergence of Vector $\overrightarrow A$ at a given point $P$ is the outward flux per unit volume as the volume shrinks about P_

#equation

$$
\nabla \cdot \overrightarrow A = \lim_{\Delta V \to 0} \frac{\oint \overrightarrow A \, dS}{\Delta V}
$$

_Where $\Delta V$ - Small differential Volume_

> If the ==Divergence== of a vector field is non zero then that region is said to contain ==source== or ==sync==

```

source_or_sync = (divergence > 0) ? Source : Sync

```

or

```

 if (divergence = positive){
	 return source ;
 }
else
	return sync ;

```

#exampleProblem

> [!Problem] Example 1
> Given the Vector field $A = 5x^{2}\left(\sin \frac{\pi x }{2}\right) \hat a_x$

> [!Answer] Answer 1
> Contents

- [ ] Do 3 #exampleProblem on [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Divergence]]

###### Derivation

![[divergence drawing]]

- [ ] https://youtu.be/EJ-rs4zocVo?si=0BE-c_NoRvZHpO00 Complete the derivation

#### Gradient of a Scalar $\nabla V$

_Gradient of any scalar is the ==maximum space rate of change of that function==_

- ==Gradient of a scalar is a vector==

#eg If V represents electric potential $\nabla V$ represents the potential gradient, then

- _Cartesian Coordinates_
  $$
  \nabla V = \frac{\partial V  }{\partial x}\hat a_ x +\frac{\partial V  }{\partial y}\hat a_ y+\frac{\partial V }{\partial z}\hat a_ z
  $$
- _Cylindrical Coordinates_
  $$
  \nabla V = \frac{\partial V \hat a_ \rho }{\partial \rho}+ {1\over \rho} \frac{\partial V \hat a_ \phi }{\partial \phi}+\frac{\partial V \hat a_ z }{\partial z}
  $$
- _Spherical Co-ordinates_

$$
\nabla V = \frac{\partial V \hat a_ r }{\partial r}+ {1 \over r}\frac{\partial V \hat a_\theta }{\partial \theta}+ {1\over r\sin\theta }\frac{\partial V \hat a_ \phi }{\partial \phi}
$$

#question
Find the gradient of the following

1. $u=x^2y+xyz$
2. $v = \rho = \sin\phi + z^2\cos\phi + \rho^2$

3. $\nabla u =\frac{\partial }{\partial x}(x^2y+xyz) \hat a_{x}$
   $+\frac{\partial }{\partial y}(x^2y+xyz) \hat a_{y}$
   $+\frac{\partial }{\partial z}(x^2y+xyz) \hat a_{z}$
   $$
   = (2xy+yz) \hat{a_x} + (x^2 +xy)\hat a_y +(xy)\hat a_z
   $$

### Co-ordinate Systems

- [[Polar Co-ordinate system]]
- [[#Cartesian Coordinate System]]
- [[#Cylindrical Coordinate System]]
- [[#Spherical Coordinate System]]

> [!NOTE] Vectors Vs Points
> Points are usually denoted by $P(P_{x},P_{y})$ without the arrow thing but in the case of vectors it is denoted by $\overrightarrow V(V_{x}, V_{y})$ but the difference lies in the fact that the points are measured from the origin but in the case of **Vectors** it has a _tail_ and an _head_ which specifies the _start_ and the _end_ respectively

#### Polar Co-ordinate System

> [!blank|right-medium] >![|400x300](https://www.researchgate.net/publication/338787054/figure/fig3/AS:850680688431104@1579829489913/Polar-coordinate-system-analysis-model.jpg)

In Polar Coordinates, a point in the plane is determined by its ==distance (radius) from the origin==, now called the Pole, and the ==angle theta==, in radians, between the line from the origin to the point and the x-axis, which is now called the Polar Axis.
In this co-ordinate system the $r$ corresponds to the distance between the point and the origin , $\theta$ corresponds to the distance between the x axis and the **point**

> [!blank|right]
>
> $$
> \begin{align}
> \cos\theta &= \frac{x}{r}\\
> \sin\theta &= \frac{y}{r}\\
> \tan\theta &= \frac{y}{x}\\
> r &= \sqrt{x^{2}+y^2}
> \end{align}
> $$

![[polar co-ordinte system.excalidraw]]

#### Cartesian Coordinate System

> [!blank|float-right]
> ![[Co-ordinate Systems Drawing]]

A Vector in Cartesian Coordinate is denoted By

$$
\overrightarrow A = A_xa_{x}+ A_ya_{y}+ A_{z}a_z
$$

> One can identify the position of third axis using ==law of screw==

##### Law of Screw

> [!multi-column]
>
> > [!blank]+
> > ![[cartesian coordinate 3rd axis]]
>
> > [!blank]+
> > We can find the position or the direction of **x** if only 2 axis are given say **z** & **y**
> > and if you rotate from **y** to **z** then the direction of **x** will be positive ie, **i -> j -> k** this manner the direction will be positive

#### Cylindrical Coordinate System

> [!blank|right-medium]
> ![[cylindrical co-ordinate system.excalidraw|400x200]]

Cylindrical coordinates are a natural extension of polar coordinates in 3D space.

##### Differential Displacement

$$
dl = d_{\rho} a_{\rho} + \rho d_{\phi}a_{\psi} + d_{z}a_z
$$

##### Differential surface area

$$
\begin{align*}
dS &= \rho d_{\phi}d_{z}a_\rho\\
&= d_{\rho}d_za_\phi\\
&= \rho d_{\rho}d_{\phi}a_z
\end{align*}
$$

##### Differential volume

$$
dv= \rho d_{\rho}d_{\phi}d_z
$$

##### Spherical Coordinate System

![[Pasted image 20240522222416.png]]

#### Co-ordinate System Conversion

1. Cartesian -> Cylindrical

| Given | Transform                        |
| ----- | -------------------------------- |
| $x$   | $r= \sqrt{x^2+y^2}$              |
| $y$   | $\phi  = \tan^{-1}(\frac{y}{x})$ |
| $z$   | $z$                              |

2. Cylindrical -> Cartesian ^9663b2

| Given  | Transform        |
| ------ | ---------------- |
| $r$    | $x=r\cos \phi$   |
| $\phi$ | $y= r \sin \phi$ |
| $z$    | $z$              |

3. Cartesian -> Spherical

| Given | Transform                                    |
| ----- | -------------------------------------------- |
| $x$   | $r = \sqrt{x^2 + y^2 + z^2}$                 |
| $y$   | $\theta = \tan^{-1}\sqrt{\frac{x^2+y^2}{z}}$ |
| z     | $\phi = \tan^{-1}\left(\frac{y}{x}\right)$   |

4. Spherical -> Cartesian

| Given    | Transform                     |
| -------- | ----------------------------- |
| $r$      | $x = r \sin \theta \cos \phi$ |
| $\theta$ | $y= r\sin \theta \sin \phi$   |
| $\phi$   | $r \cos \theta$               |

5. Cylindrical -> Spherical

| Given  | Transform                                       |
| ------ | ----------------------------------------------- |
| $\rho$ | $r = \sqrt{\rho^2 + z^2}$                       |
| $\phi$ | $\theta = \tan^{-1}\left(\frac{\rho}{z}\right)$ |
| z      | $\phi = \phi$                                   |

6. Spherical -> Cylindrical

| Given    | Transform             |
| -------- | --------------------- |
| $r$      | $\rho = r\sin \theta$ |
| $\theta$ | $\phi = \phi$         |
| $\phi$   | $z = r \cos \theta$   |

#### Matrix Transform

1. Cartesian -> cylindrical

   $$
   \begin{bmatrix}
   A_\rho  \\ A_\phi \\ A_z
   \end{bmatrix} = \begin{bmatrix}
   \cos\phi & \sin\phi & 0 \\ - \sin\phi & \cos\phi & 0  \\ 0 & 0 & 1
   \end{bmatrix}
   \begin{bmatrix}
   A_{x} \\ A_{y}  \\ A_z
   \end{bmatrix}\tag{1}
   $$

   > if we consider eqn $(1)$ as
   >
   > $$
   > A_{ca} = \overrightarrow T A_{cy}
   > $$
   >
   > then
   >
   > $$
   > \overrightarrow T^{-1} A_{ca} = \overrightarrow I A_{cy} = A_{cy}
   > $$
   >
   > which is equal to
   >
   > $$
   > \begin{bmatrix}
   > A_{x} \\ A_{y}  \\ A_z
   > \end{bmatrix}
   > = \begin{bmatrix}
   > \cos\phi & - \sin\phi & 0 \\ \sin\phi & \cos\phi & 0  \\ 0 & 0 & 1
   > \end{bmatrix}
   > \begin{bmatrix}
   > A_\rho  \\ A_\phi \\ A_z
   > \end{bmatrix}
   > \tag{2}
   > $$
   >
   > If we compare both eqn $(1)$ and $(2)$ we can see that it uses the it uses the [[Matrices#^fcc442|Inverse Matrix Property]]

1. Cartesian -> Spherical

$$
\begin{bmatrix}
A_{r} \\ A_{\theta}  \\ A_{\phi}
\end{bmatrix}
= \begin{bmatrix}
\sin\theta \cos\phi & \sin\theta \sin\phi & \cos\theta \\ - \cos\theta \cos\phi  & \cos\theta \sin\phi  & - \sin\theta  \\ - \sin\phi  & \cos\phi & 0
\end{bmatrix}
\begin{bmatrix}
A_\rho  \\ A_\phi \\ A_z
\end{bmatrix}
\tag{3}
$$

> We can do the same here by Multiplying the inverse of of the transformation matrix
>
> $$
> \begin{bmatrix} A_{x} \\ A_{y} \\ A_{z}
> \end{bmatrix}
> =
> \begin{bmatrix} \sin\theta \cos\phi & \cos\theta \cos\phi & \cos\theta  \\ \sin\theta \sin\phi & \cos\theta \cos\phi & \cos\phi  \\  \cos\theta & - \sin\theta & 0  \end{bmatrix} \begin{bmatrix} A_{r} \\ A_{\theta} \\ A_{\phi} \end{bmatrix}
> $$

### Fields

**Field is a function that specifies a particular quantity everywhere in a region**

There are 2 types of fields

1. Scalar Fields : If the quantity is scalar eg : sound intensity in a theater
2. Vector Fields : If the quantity is vector eg: Velocity of raindrops in the atmosphere

#### Electric Field

**It is defined as the electric force per unit charge**, The **Electric Field** is radially outward from positive charge and the radially inward in the case of negative charge

#### Electric Field Due to a Point charge

![[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/2 charges sep by r drawing]]
Consider two charges $Q_1$ and $Q_2$ separated by a distance $R$

- If $Q_{1} \times Q_{2} > 0$ similar charges
- If $Q_{1} \times Q_{2} < 0$ opposite charges

Where Magnitude of force

$$
F = \frac{1}{4 \pi \epsilon_0} \frac{Q_{1} Q_{2}}{R^{2}}\tag{Opposite charges}
$$

$$
F = -\frac{1}{4 \pi \epsilon_0} \frac{Q_{1} Q_{2}}{R^{2}}\tag{Similar charges}
$$

The electric field by a point charge $Q$ is the amount of force on $IC$ charge

$$
\begin{align*}

E &= {F \over Q} = F \tag{Q = 1C}
\end{align*}
$$

$\therefore$ Electric field due to a point charge is

$$
\color{cyan}
\boxed{
E = \frac{1}{4 \pi \epsilon_0} \frac{Q} {R^{2}}}
$$

![[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Electric field direction.excalidraw]]

- If we have ==positive charge== then the electric field will happening in ==outward direction==.
- If we have ==negative charge== then the electric field will happening in ==inward direction==.

#### Electric Field Intensity

It is defined as the ==Force per unit charge on Q== ,the unit is $N/C$ or $V/m$

$$
E = \frac{F_t}{Q_{r}}
$$

$$
E = \frac{Q}{4\pi \epsilon_{0}r^{2}} \overrightarrow a_{r}\tag{Spherical}
$$

$$
E = \frac{Q}{4 \pi \epsilon_{0} R^{2}} \overrightarrow a_R\tag{Cartesian}
$$

#### Electric Flux Density

The flux

#### Charge Distributions

- [[#Line charge]]
- [[#Sheet Charge]]
- [[#Volume Charge]]

##### Line Charge Distribution

It describes a charge distribution in which the ==charge is distributed over a curved line== ,and each differential charge $dQ$ along the line produces electric field It is the total charge by the length of the line , it's denoted by $\rho_l$ and unit is $(C/m)$

> Differential electric field $dE$
>
> $$
>  dE = \frac{qQ}{4\pi \epsilon_{0 }R^{2}}\overrightarrow a_R
> $$
>
> Total electric field at P is given no other charges present in that region
>
> $$
> E = \int_{L} \frac{\rho_l \overrightarrow a_{R} }{4\pi \epsilon_{0 R^{2}}} dl
> $$

##### Sheet Charge Distribution

Where the charge is distributed along a surface or sheet , so also called surface charge distribution , Denoted by $\rho_S$ unit is $(C/m^2)$

> Here the differential charge $qQ$ on the surface/sheet results in an electric field
>
> $$
> dE = \frac{dQ}{4\pi \epsilon_{0 R^{2}}}\overrightarrow a_R
> $$
>
> $$
> E = \int_{S} \frac{\rho_{S}\overrightarrow a_{R}}{4\pi \epsilon_{0 R^2}}dS
> $$

##### Volume Charge Distribution

Distribution of charge within a volume of space , Denoted by $\rho_V$

$$
\rho = \frac{dQ}{dv} \tag{C/m3}
$$

> The differential charges $dQ$ produces a differential electric field
>
> $$
> dE = \frac{dQ}{4\pi \epsilon_{0 R^{2}}}dv
> $$
>
> And the total electric field is
>
> $$
> E = \int_{L} \frac{\rho_{v} \overrightarrow a_{R}}{4\pi \epsilon_{0 R^2}}dv
> $$

---

#### Standard Charge Configurations

##### Contents

- [[#Point Charge]]
- [[#Infinite Line Charge]]

> [!NOTE] NOTE
>
> Charges are not on a **conductor** it is suspended in space,fixed in the specified configuration

#### Point Charge

- Electric Field of a point charge is
  $$
  E = \frac{Q}{4\pi \epsilon_{0 r^{2}}} \overrightarrow a_{r}\tag{spherical }
  $$

#### Infinite Line Charge

If charge is distributed with uniform density $\rho_{l} (C/m)$ along an infinite, straight line (z axis) , then the field is given by

$$
E = \frac{\rho_{l}}{2\pi \epsilon_{0 r}}\overrightarrow a_r\tag{Cylindrical}
$$

---

#### Net charge in a region

^f4a3fd

$$
dQ = \rho \cdot dv \tag{C}
$$

By integrating the above equation

$$
Q = \int_{v} \rho \cdot dv\tag{C}
$$

> This equation can be used to find the net charge present in a specified volume

#exampleProblem

> [!Problem] Example 3.1
> Find the charge in the volume defined by $1 \le r \le 2 \ m$ by integration, in spherical coordinates, if
>
> $$
> \rho = \frac{5 \cos^{2}\phi}{r^{4}}
> $$

> [!Success] Answer
> We know [[#Net charge in a region]] so by integrating the above equation

$$
\begin{align*}
Q &= \int_{v} \rho \cdot dv
\end{align*}
$$

- [ ] Learn More and solve the problem 📅 2024-05-20

```tasks
due 2024-05-20

```

## References

1. Joseph A Edminister "Electromagnetics" ,SHAUM's Outlines
