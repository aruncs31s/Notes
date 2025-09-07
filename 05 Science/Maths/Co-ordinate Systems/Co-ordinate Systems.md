---
id: Co-ordinate Systems
aliases:
  - co-ordinates
  - cartesian
  - cylindrical
  - spherical
tags: []
Created: 2024-05-12
cssclasses:
  - wide-page
---

<h1 align="center"> Co-ordinate Systems</h1>


- [[Polar Co-ordinate system]]
- [[#Cartesian Coordinate System]]
- [[#Cylindrical Coordinate System]]
- [[#Spherical Coordinate System]]

> [!NOTE] Vectors Vs Points
> Points are usually denoted by $P(P_{x},P_{y})$ without the arrow thing but in the case of vectors it is denoted by $\overrightarrow V(V_{x}, V_{y})$ but the difference lies in the fact that the points are measured from the origin but in the case of **Vectors** it has a _tail_ and an _head_ which specifies the _start_ and the _end_ respectively

### Polar Co-ordinate System
>[!blank|right-medium]
>![|400x300](https://www.researchgate.net/publication/338787054/figure/fig3/AS:850680688431104@1579829489913/Polar-coordinate-system-analysis-model.jpg)

In Polar Coordinates, a point in the plane is determined by its ==distance (radius) from the origin==, now called the Pole, and the ==angle theta==, in radians, between the line from the origin to the point and the x-axis, which is now called the Polar Axis.
In this co-ordinate system the $r$ corresponds to the distance between the point and the origin , $\theta$ corresponds to the distance between the x axis and the **point**


>[!blank|right]
>$$
>\begin{align}
>\cos\theta &= \frac{x}{r}\\
>\sin\theta &= \frac{y}{r}\\
>\tan\theta &= \frac{y}{x}\\
>r &= \sqrt{x^{2}+y^2}
>\end{align}
>$$

![[polar co-ordinte system.excalidraw]]


### Cartesian Coordinate System
>[!blank|float-right]
>![[Co-ordinate Systems Drawing]]

A Vector in Cartesian Coordinate is denoted By

$$
\overrightarrow A = A_xa_{x}+ A_ya_{y}+ A_{z}a_z
$$

> One can identify the position of third axis using ==law of screw== 


#### Law of Screw
>[!multi-column]
>
>>[!blank]+
>>![[cartesian coordinate 3rd axis]]
>
>>[!blank]+ 
>> We can find the position or the direction of **x** if only 2 axis are given say **z** & **y**
>> and if you rotate from **y** to **z** then the direction of **x** will be positive ie, **i -> j -> k** this manner the direction will be positive  
>

### Cylindrical Coordinate System
>[!blank|right-medium]
![[cylindrical co-ordinate system.excalidraw|400x200]]



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
### Spherical Coordinate System
![[Pasted image 20240522222416.png]]

### Co-ordinate System Conversion

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


### Matrix Transform 

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
>if we consider eqn $(1)$ as 
>$$
A_{ca} = \overrightarrow T A_{cy}
>$$
>then 
>$$
\overrightarrow T^{-1} A_{ca} = \overrightarrow I A_{cy} = A_{cy}
>$$
>which is equal to 
>$$
\begin{bmatrix}
A_{x} \\ A_{y}  \\ A_z 
\end{bmatrix}
= \begin{bmatrix}
\cos\phi & - \sin\phi & 0 \\ \sin\phi & \cos\phi & 0  \\ 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
A_\rho  \\ A_\phi \\ A_z
\end{bmatrix} 
\tag{2}
>$$
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
>$$
\begin{bmatrix} A_{x} \\ A_{y} \\ A_{z}  
\end{bmatrix}
= 
\begin{bmatrix} \sin\theta \cos\phi & \cos\theta \cos\phi & \cos\theta  \\ \sin\theta \sin\phi & \cos\theta \cos\phi & \cos\phi  \\  \cos\theta & - \sin\theta & 0  \end{bmatrix} \begin{bmatrix} A_{r} \\ A_{\theta} \\ A_{\phi} \end{bmatrix}
>$$

## References
   
1.
