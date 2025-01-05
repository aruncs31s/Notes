---
aliases: 
Date: 04-01-25
---
# Integration
Integration is basicly finding the area under the curve. 

### Problems 
![[areaofTriangle.excalidraw]]
$$
Area = \text{velocity } \times \text{Time}
$$


$$
S = \int_{a}^{b} f(x) dx
$$
$f(x)$ -> velocity with respect to time 

But here velocity is constant

$$
\begin{align}
S &= \int_0^{10} 1 dx \\
&= 10
\end{align}
$$

What if 1 is acceleration intead of velocity? then how to find the displacement 

```
Acceleration  |
			|
			|
			|
		   1|----------------------
			|                      |
			|                      |
            ------------------------
                                10 -> time
```

$$
\begin{align}
S &= \int_0^{10} \int_0^{10} 1 \ dx \\
 &= \int_0^{10} 10 \ dx \\
 & = 100 \\
 \end{align}
$$
Verifing using regular equations 
$$
\begin{align} 
S &= ut + .5 at^2 \\
&=  0 \times 10 + .5 \times 1 \times  10^2 \\
&= 50 \\
\end{align} 
$$
What went wrong? 
$$
\begin{align}
S  & = \int_0^{10} x \ dx  \\
&= {x^2 \over 2 }_0^{10}  \\
& = 50 \tag{what?}
\end{align}
$$

So how did it correct now ?
First find the velocity($v(t)$)
$$
\begin{align} 
v(t) &= \int a(t) \ dt  \\
&= {t^2 \over 2} +C 
\end{align}
$$
Here  $C =V(0) \text{ Initial Velocity} = 0$

