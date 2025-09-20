---
id: Stokes_Theorem
aliases: []
tags:
  - academics
  - btech
  - s6
  - electromagnetics
  - module_1
dg-publish: true
---
# Stokes Theorem

- Stokes theorem explains relationship in between ==line Integration== and ==surface integration==
- Stokes theorem is based on [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Curl|Curl]] of the function

> [!info] Statement 
> The ==Line integral== of a Vector $\overrightarrow A$ around a closed path '$L$' is equal to the Surface integral of the Curl of Vector $\overrightarrow A$ over any close surface  
>$$
\oint \overrightarrow P.dl = \int  \nabla \times \overrightarrow P \ dS
>$$
>Or it states that the circulation of the vector field $\overrightarrow A$ around a closed path $L$ is equal to the surface intrgral og the [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Curl]] of $\overrightarrow A$ over an open surface $S$ bounded by $L$

#proof

1. Curl of a function $\overrightarrow P$ is

$Curl(\overrightarrow P) =  \overrightarrow \nabla \times \overrightarrow P = \underset{\Delta S \to 0}{\lim} \frac {\oint \overrightarrow P dl}{\Delta S}$

2.

=> $\underset{\Delta S \to 0}{\lim} \overrightarrow \nabla \times \overrightarrow P \ \Delta S = \underset{\Delta S \to 0}{\lim} \oint \overrightarrow P dl$

_Which is basically [[Integration|integration]]_

> [!NOTE] Integration
> $\underset{\Delta S \to 0}{\lim} a \ function = its \ integral$

3.

$$
\oint \overrightarrow P.dl = \int \overrightarrow \nabla \times \overrightarrow P \ dS
$$
