
#### Refractive Index
- A ray of light travels more slowly in an optically dense medium
$$
n = \frac {\text{volocity of light in vacuum}} {\text{velocity of light in the medium}}
$$

> [!NOTE] Meridional Rays
> **rays that pass through the axis of the optical fiber**

#### Acceptance angle
*The Maximum angle to the axis at which the light may enter the fiber in order to be propagated*

> if angle  > $\Phi_a $
> Then Reflected angle < $\Phi_c$ 
> So No `Total Internal Reflection`

#### Numerical Aperture

![[numerical aperture derivation.excalidraw]]

$$
\begin{align}
n_0 \sin \theta_1 &= n_1 \sin \theta_2 \tag{1.0}
\end{align}
$$
> Consider the triangle ABC (will draw later)

$$
\begin{align}
\phi = \frac {\pi}{2} - \theta_2 \tag{1.1}
\end{align}
$$
> when $\Phi_{in}$ > $\Phi_c$

$$
\begin{align} 
n_o \sin \theta_1 = n_1 \cos \phi \tag{1.2}
\end{align}
$$
> using [[Trigonometry#^d8dee6|This property]]

$$
\begin{align} 
n_0 \sin \theta_1 &= \sqrt{n_1 \left(1 - sin^2\phi \right)} \\
n_0 \sin \theta_1 &= \sqrt{n_1 ^2 - n_2 ^2 }  \tag{1.3} 
\end{align}
$$

$$
\color{cyan}\boxed{ 
NA = \sqrt{n_1 ^ 2 - n_2 ^ 2 }
}
$$

# Module 5
- [ ] Wavelength Division Multiplexing (WDM)

#### WDM 
*Combining number of info carrying wavelength on the same fiber*
- Used to increase the capacity 