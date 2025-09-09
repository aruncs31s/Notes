---
id: Curl
aliases: []
tags:
  - science
  - maths
  - vector_calculus
dg-publish: true
---
# Curl

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

#### Properties

1. The **Curl** of a vector field is an anther vector field
2. The curl of a **scalar** field $V$ ,$\nabla \times V$ make no sense
3. $\nabla \times (A + B) = \nabla \times A + \nabla \times B $
4. $\nabla \times (A + B) = A(\nabla \cdot B ) - B ( \nabla \cdot A ) + (B \cdot \nabla A ) -(A \cdot \nabla ) B$
5. The [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Divergence|divergence]] of the curl of a vector field vanishes , that is $\nabla(\nabla \times A) = 0$
6. The curl of the [[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Gradient of a Scalar|gradient]] of a scalar field also equal to zero $\nabla \times \nabla V = 0$

#### Physical Significance of curl
- If curl is positive the flow is clock wise 
- If the curl is negative flow is anti-clock wise

