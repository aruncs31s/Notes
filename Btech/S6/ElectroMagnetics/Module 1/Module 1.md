---
id: Module 1
aliases:
  - emt module 1
tags:
  - todo
  - emt
  - emt_module1
---
# Module 1

## [[Notes/Tasks]] 

```tasks
due 2024-05-20 
short mode
```
## Contents

- [[#Syllabus]]
- [[#Part 1]]
- [[#Part 2]]

## Prerequisites
- [[Vector Calculus]]
 - [[Stokes Theorem]]
 - [[Divergence]]
 - [[Gauss Divergence Theorem]]
 - [[Curl]]
 - [[Co-ordinate Systems]]
 - [[coulomb's law]]

## Short Equations 

| Var                          | Val               |     |
| ---------------------------- | ----------------- | --- |
| **Electric Field Intensity** | $$E = -\nabla V$$ |     |
|                              |                   |     |


### Introduction

_Electromagnetic theory is a branch of physics that deals with the study of electromagnetic fields, which are the interaction of electric and magnetic fields. It encompasses the laws and principles that govern these fields, as well as their behavior and effects on matter._
## Syllabus

- Part 1
  - Introduction to [[#Introduction|Electromagnetic Theory]].
  - Review of vector calculus - curl[^1.1], divergence[^1.2], gradient[^1.3].
  - Rectangular[^3.1], cylindrical[^3.2] and spherical coordinate systems[^3.3].
  - Expression of curl, divergence, and Laplacian in cartesian, cylindrical and spherical coordinate system.
- Part 2
  - Electric field and magnetic field, Review of Coulomb’s law, Gauss law and Amperes current law.
  - Poisson and Laplace equations, Determination of E and V using Laplace equation.

---

## Part 1
 - [[Vector Calculus]]
 - [[Stokes Theorem]]
 - [[Divergence]]
 - [[Gauss Divergence Theorem]]
 - [[Curl]]
 - [[Co-ordinate Systems]]
### Curl , Divergence ,Gradient 


| Var                             | Val                                                                                                                                                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Curl$$\nabla \times A $$        | $$\nabla \times \overrightarrow A = \begin{bmatrix} \hat a_{x} & \hat a_{y} & \hat a_{z} \\ \frac{\partial}{\partial x} & \frac{\partial }{\partial y}& \frac{\partial }{\partial z} \\ A_x & A_y & A_z \end{bmatrix} \tag{Cartesian}$$ |
| [[Divergence]]<br>$$\nabla A $$ | $$\nabla A$$                                                                                                                                                                                                                            |
|                                 |                                                                                                                                                                                                                                         |

### Differential Volume , Surface, and Line Elements

When the co-ordinates of point P are expanded to $(x + dx,y+dy+z+dz)$ or $(r + dr,\phi + d\phi , z+ dz)$ or $(r+dr , \theta + d\theta , \phi + d\phi)$ a **differential volume** $dv$ is formed
![[differential volume ,surface and line elements.excalidraw]]
#todo

## Part 2

### Contents

1. Electric field and magnetic field
2. Review of Coulomb’s law
3. Gauss law and Amperes current law
4. [[coulomb's law]]
### Fields

**Field is a function that specifies a particular quantity everywhere in a region**

There are 2 types of fields

1. Scalar Fields : If the quantity is scalar eg : sound intensity in a theater
2. Vector Fields : If the quantity is vector eg: Velocity of raindrops in the atmosphere

#### Electric Field
**It is defined as the electric force per unit charge**, The **Electric Field** is radially outward from positive charge and the radially inward in the case of negative charge


#### Electric Field Due to a Point charge

![[2 charges sep by r drawing]]
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

![[Electric field direction.excalidraw]]

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
>$$
 dE = \frac{qQ}{4\pi \epsilon_{0 }R^{2}}\overrightarrow a_R 
>$$
>Total electric field at P is given no other charges present in that region 
>$$
E = \int_{L} \frac{\rho_l \overrightarrow a_{R} }{4\pi \epsilon_{0 R^{2}}} dl
>$$
>
>

##### Sheet Charge Distribution
Where the charge is distributed along a surface or sheet , so also called surface charge distribution , Denoted by $\rho_S$ unit is $(C/m^2)$ 

> Here the differential charge $qQ$ on the surface/sheet results in an electric field 
>$$
dE = \frac{dQ}{4\pi \epsilon_{0 R^{2}}}\overrightarrow a_R
>$$
>$$
E = \int_{S} \frac{\rho_{S}\overrightarrow a_{R}}{4\pi \epsilon_{0 R^2}}dS
>$$
>

##### Volume Charge Distribution
Distribution of charge within a volume of space , Denoted by $\rho_V$

 
$$
\rho = \frac{dQ}{dv} \tag{C/m3}
$$
>The differential charges $dQ$ produces a differential electric field
>$$
dE = \frac{dQ}{4\pi \epsilon_{0 R^{2}}}dv
>$$
> And the total electric field is 
>$$
E = \int_{L} \frac{\rho_{v} \overrightarrow a_{R}}{4\pi \epsilon_{0 R^2}}dv
>$$

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
>$$
\rho = \frac{5 \cos^{2}\phi}{r^{4}}
>$$


>[!Success] Answer
> We know [[#Net charge in a region]] so by integrating the above equation 
$$
\begin{align*}
Q &= \int_{v} \rho \cdot dv
\end{align*}
$$
- [ ] Learn  More and solve the problem 📅 2024-05-20
```tasks
due 2024-05-20
```

## References
1. Joseph A Edminister "Electromagnetics" ,SHAUM's Outlines