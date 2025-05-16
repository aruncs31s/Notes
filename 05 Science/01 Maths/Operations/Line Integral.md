# Line Integrals
Line integrals are related to given integration of a vector $A$ along a paths situated on a curve in space

$$
\int_L A.dl = \int_{x_1}^{x_2} \left| A \right| dl \cos \theta
$$

> If the path integral is a closed loop along $x_1$ and $x_2$ then

$$
\int_L A.dl = \oint A.dl
$$
>and this is known as contour integral or path intrgral



#exampleProblem 
![[Old_NOTES/Academics/Btech/S6/ElectroMagnetics/Module 1/Drawings/line integrals.excalidraw]]
Given $F = x^2ya_x + 2xy^2 a_{y^,}$ , find the circulation of $F$ along a closed path OABC as shown Above
#answer

>$$
\begin{align}
\oint F .d = \int_{OA} + \int_{AB}+ \int_{BC}+ \int_{CO} F.dl
\end{align}
>$$
>
>Given $F = x^2ya_x + 2xy^2 a_{y^,}$ and $dl = dxa_{x}+ dya_{y}$ 
>and $F.dl = F_xdx+ F_ydy$ 
>By calculating the F through individual path
>$$
\begin{align}
 \int_{OA} &= 0
\end{align} \tag{1}
>$$
> result of equation $(1)$ = 0 because For path **OA** , $dy = 0$ , $y =0$ , $F=0$
>- For Path **AB** $dx = 0$ <- Change in $x$ is zero in case of path **AB** and $x=1$ , $F=ya_{x}+ 2y^2a_y$ 
>$$
\begin{align}
 \int_{AB} F\cdot dl &= \int_{0^{1}} 2y^{2}dy \\
 &= \frac{2y^3}{3} \\
 &= {2\over3 }(1-0) = {2 \over 3}
\end{align}
>$$
>- For path **BC** $y$ is constant and only the $x$ is changing 
> $\therefore$ $dy =0$ , $y=1$ , $F=x^2a_{x}+ 2xa_y$
>$$
\int_{BC} F \cdot dl = \int_{1^{0}x^{2}dx}= {x^{3} \over 3} = {1\over 3}
>$$
> - For path **CO** $\int_{CO} F \cdot dl = 0$ 
> $\therefore$
>$$
\oint F \cdot dl = {2 \over 3} - {1 \over 3 } = {1 \over 3}
>$$