---
id: Rotations
aliases: []
tags:
  - science
  - maths
dg-publish: true
---
## Right-Handed System (Standard)

- Thumb (X), Index (Y), Middle Finger (Z) point in +ve directions.
**Rotation:**
- Counter-clockwise rotations are positive (by convention).

used by: OpenGL,  in standart MATH. 

$$
\vec{X} \times \vec{Y} = \vec{Z}
$$

## Left-Handed System
- Thumb (X), Index (Y), Middle Finger (Z) point in +ve directions.
- If you curl fingers from X to Y, your thumb points along −Z (opposite of right-handed).
- Clockwise rotations are positive (opposite convention).

$$
\vec{X} \times \vec{Y} = -\vec{Z}
$$

# 2D

$$
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=
\begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta &  \cos \theta
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

# 3D

- **All rotation matrices are orthogonal:** $R^{-1} = R^T$.  
- **Determinant = +1:** $\det(R) = 1$ (preserves orientation).  
- **Non-commutative:** $R_x R_y \neq R_y R_x$ (order matters!).  

## Rotation Around X axis 

$$
R_x(\theta) = \begin{bmatrix}
1 & 0 & 0 \\
0 & \cos \theta & -\sin \theta \\
0 & \sin \theta & \cos \theta
\end{bmatrix}
$$
- Rotates points in the YZ-plane (around the X-axis).
- Leaves X-coordinates unchanged.
## Rotation around Y-axis 
$$
R_y(\theta) = \begin{bmatrix}
\cos \theta & 0 & \sin \theta \\
0 & 1 & 0 \\
-\sin \theta & 0 & \cos \theta
\end{bmatrix}
$$

^36e3d2

- Rotates points in the XZ-plane (around the Y-axis).
- Leaves Y-coordinates unchanged.
## Rotation around Z-axis

$$
R_z(\theta) = \begin{bmatrix}
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
- Rotates points in the XY-plane (around the Z-axis).
- Leaves Z-coordinates unchanged.