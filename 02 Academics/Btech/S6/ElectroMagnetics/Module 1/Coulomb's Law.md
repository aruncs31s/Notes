---
id: Coulombs_Law
aliases: []
tags:
  - academics
  - btech
  - s6
  - electromagnetics
  - module_1
dg-publish: true
---
# Coulomb's Law
*Coulomb's law is an experimental law formulated in 1785 by Charles Augustin de Coulomb, then a colonel in the French army. It deals with the force a point charge exerts on another point charge* 

> [!info] Point Charge
> point charge we mean a charge that is located on a body whose dimensions are much smaller than ota collection of electric charges on a pinhead may be regarded as a point chargeher relevant dimensions ,a collection of electric charges on a pinhead may be regarded as a point charge

#equation

$$
F = \frac{k \cdot Q_1 \cdot Q_2}{r^{2} \tag{Unit = Coulomb}}
$$
> In Vector Form
$$
F = \frac{k \cdot Q_1 \cdot Q_2}{r^{2} \tag{Unit = Coulomb}}  \ \overrightarrow a
$$
>or
$$
F = \frac{k \cdot Q_1 \cdot Q_2}{R_{21}^{2}} \ \overrightarrow a_{21}\tag{Unit = Coulomb}
$$

> [!NOTE] Parameters
> Where $k = \frac{1}{4 \times \pi \in_0}$ or $k = 9 \times 10^{9}$ m/f  and $\in_0 = 8.854 \times 10^{-12}$
> - $q_{proton} = 1.6 \times 10^{-19}$ C , $q_{electron} = -q_{proton}$  and $q_{nuetron} = 0$
> - $1 C(Coulomb)$ = $6 \times 10^{18}$ electrons
> - For media other than freespace $\large{\epsilon = \epsilon_{0}\epsilon_r}$ where $\epsilon_r$ is the relative permitivity

> [!IMPORTANT] Multiple Chargers 
> When dealing with multiple charges we use [[superposition%20princliple|SuperPosition]] principle
> ,And the #equation for finding the force when dealing with multiple charge is 
>$$
\overrightarrow F ={Q \over 4\pi \epsilon_{0}} \sum_{k=1}^N \frac{Q_{k}\left(\overrightarrow{r} - \overrightarrow{r_k}\right)}{|\overrightarrow{r} - \overrightarrow{r_k}|^3}
>$$

#exampleProblem 

> [!example] Question
> Find the force on charge $Q_1$,$20 \mu C$ due to charge $Q_2$ , $-300 \mu C$ where $Q_{1}$ is at $(0,1,2)m$ and $Q_2$ is at $(2,0,0)m$
> 

> [!success] Answer
> $$
> \begin{align}
F = \frac{k \cdot Q_1 \cdot Q_2}{R_{21}^{2}} \ \overrightarrow a_{21}
\end{align}
> $$
> Here $\overrightarrow R_{21}$ = $-2a_{x}+a_{y}+2a_{z}$ , $R_{21}  = |R_{21}|= \sqrt{-2^{2}+ 1^{2}+2^{2}}= 3$
> Then $\overrightarrow a_{21} = {\overrightarrow R_{21} \over R_{21}} = {1 \over 3 } (-2a_{x}+a_{y}+2a_z)$
>$$\begin{align}
F &= \frac{k \cdot Q_1 \cdot Q_2}{R_{21}^{2}}  \overrightarrow a_{21}\tag{1} \\
&= \frac{20\times 10^{-6} \times 300\times 10^{-6}}{4 \pi \epsilon_{0} 3^{2}} \times  {1 \over 3 } (-2a_{x}+a_{y}+2a_{z)}\tag{2} \\
&=6\times \left({1 \over 3 } (-2a_{x}+a_{y}+2a_{z}\right) \tag{final}
\end{align}
>$$
>Where magnitude of the force is $6N$ and $Q_1$ is attracted to $Q_2$ 

##### Coulomb vector force on point charges Q1 and Q2 .

```python
import numpy as np
import matplotlib.pyplot as plt

# Create vectors
V = np.array([3, 1])
W = np.array([2, 3])

# Calculate resultant vector
R12 = V + W

# Create plot
fig, ax = plt.subplots()

# Add vectors V and W to the plot
ax.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r', label='q1')
ax.quiver(0, 0, W[0], W[1], angles='xy', scale_units='xy', scale=1, color='b', label='q2')
ax.quiver(W[0], W[1], 1,-2, angles='xy', scale_units='xy', scale=1, color='g', label='R12')
ax.annotate('q1', (V[0], V[1]), xytext=(-15, 15), textcoords='offset points', fontsize=12, color='r')
ax.annotate('q2', (W[0], W[1]), xytext=(-15, 15), textcoords='offset points', fontsize=12, color='b')
ax.annotate('R12', (R12[0], R12[1]), xytext=(-15, 15), textcoords='offset points', fontsize=12, color='g')

# Set plot limits
ax.set_xlim([-3, 5])
ax.set_ylim([-3, 6])

# Display grid
plt.grid()
plt.legend()
plt.show()

```

