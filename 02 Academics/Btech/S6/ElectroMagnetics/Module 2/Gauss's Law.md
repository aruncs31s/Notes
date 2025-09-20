---
id: Gausss_Law
aliases: []
tags:
  - academics
  - btech
  - s6
  - electromagnetics
  - module_2
dg-publish: true
---
# Gauss's Law

> [!NOTE] Statement
> Gauss's Law for Electric field states that the *total flux through any surface is the charge enclosed by the surface divided by $\epsilon_0$*
$$
\psi = \oint E \cdot dS = \frac{Q}{\epsilon_0 }  
$$

![[closed surface electric field]] ^b81c17

> [!Note] Statement 2  From Edminister
> Gauss's Law states that the *total flux out of a closed surface is equal to the net charge within the surface*
> Mathematicaly
>$$
\oint D \cdot dS = Q_{enc}
>$$
>

- If the flux is leaving like shown in [[#^b81c17|figure]] then the $\psi$ is positive if entering then the $\psi$ is negative

![[Academics/S6/ElectroMagnetics_OLD/Electric field direction.excalidraw]]

$$
\psi = \oint D \cdot dS = Q_{enc}\tag{E Flux Positive}
$$
$$
\psi = \oint D \cdot dS = - Q_{enc} \tag{E Flux negative}
$$

![[case 3 total flux zero]]

## Use case

![[Gauss's law example 1.1|300x300]]
In this example the total $\psi$ is 

$$
\psi = \oint \overrightarrow E \cdot dS = \frac{(Q_{1} + Q_{2}+ Q_3)}{\epsilon_0 }
$$
or 
$$
\psi = \oint \overrightarrow D \cdot dS = (Q_{1} + Q_{2}+ Q_3)
$$
Note that the $Q_{4}$ isn't accounted because the total flux entering will be equal to total flux leaving in case of $Q_{4}$ because it is outside of the closed surface

#### Gauss's Law in Differential Form
> Gauss's Law in integral form is given by
>$$
\oint \overrightarrow{D} \cdot dS = Q_{enc}\tag{1}
>$$
>  Let the closed surface S encloses a volume v . If charge density (charge per unit volume) is $\rho$ then the net charge enclosed by the surface $S$ within the volume $v$ will be $Q_{enc} = \int_v \rho dv$ 
>  Then the equation $(1)$ can be modified as 
>$$
\oint D \cdot dS = \int_{v} \rho dv
>$$
>As the volume considered is reduced to element volume, this becomes the point relation 
>$$
\nabla \cdot \overrightarrow{D} = \rho
>$$

## Prerequisites
1. [[Academics/S6/ElectroMagnetics_OLD/Electric Flux and Electric Flux Density]]
## References
1. 