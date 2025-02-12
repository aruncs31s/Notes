#### Matrix Minor Test
Definitness for any squre  matrix A we define the principle matrix mirror (any submatrix of order m < n) which contains first m elements of the principle diagonal. These principle mirrors decide the nature of definitness of the matrix 

 

$$
\begin{bmatrix}
a_{11} & a_{12} &a_{13}  \\
a_{21} & a_{22} &a_{23} \\
a_{31} & a_{32} &a_{33}
\end{bmatrix}
$$

$$
D_{1} = |a_{11}|
$$
$$
D_{2} =
\begin{bmatrix}
a_{11} & a_{12 } \\
a_{21} & a_{22}
\end{bmatrix}
$$

1. **Positive definit** $D_{1}$ , $D_{2}$ and $D_{3}$ > 0 
2. **Negative Definit** $D_{1} < 0$ $D_{2} > 0$ $D_{3} < 0$ -> D2 and D3 must have alternate signs 
3. Positive Semi Definit $D_{1} > 0 , D_{2} \geq 0 , D_{3} \geq 0$
4. Negative Semi Definit $D_{1} < 0 , D_{2} \geq 0 , D_{3}\leq 0$ $D_{i} =0$ (either one of the 0) 

#### Qst
**Q1** 
Construct the hesien matrix for the function $f(x) = 2x_{1}^2 + x_{2}^2 + 3x_{3}^2 + 10x_{1} + 8x_{2} + 6 x_{3} - 100$

$$
H = \begin{bmatrix}
\frac{\partial^2f}{\partial x_{1}^2} & \frac{\partial^2f}{\partial x_{1}x_{2}} & \frac{\partial^2f}{\partial x_{1}x_{3}}  \\
\frac{\partial^2f}{\partial x_{2}x_{1}} & \frac{\partial^2f}{\partial x_{2}^2} & \frac{\partial^2f}{\partial x_{2}x_{3}}  \\
\frac{\partial^2f}{\partial x_{3}x_{1}} & \frac{\partial^2f}{\partial x_{3}x_{2}} & \frac{\partial^2f}{\partial x_{3}^2} 
\end{bmatrix}
$$


**Q2** $f(X) = 6 x_{1} + 8 x_{2} - x_{1}^2 -x_{2}^2$

$$
H = \begin{bmatrix}
\frac{\partial^2f}{\partial x_{1}^2} & \frac{\partial^2f}{\partial x_{1}x_{2}} & \frac{\partial^2f}{\partial x_{1}x_{3}}  \\
\frac{\partial^2f}{\partial x_{2}x_{1}} & \frac{\partial^2f}{\partial x_{2}^2} & \frac{\partial^2f}{\partial x_{2}x_{3}}  \\
\frac{\partial^2f}{\partial x_{3}x_{1}} & \frac{\partial^2f}{\partial x_{3}x_{2}} & \frac{\partial^2f}{\partial x_{3}^2} 
\end{bmatrix}
$$