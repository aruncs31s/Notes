
### Designing of FIR Filter

#### Windows
1. Rectangular window
- Non Causal
$$
\begin{align}
W_R(n) &= 1 \tag{for -(N - 1)/2 to (N-1)/2 } \\
W_R(n) &= 0 \tag{otherwise}
\end{align}
$$

- Causal
$$
\begin{align}
W_R(n) &= 1 \tag{for 0 to N}\\
&=0  \tag{otherwise}
\end{align}
$$

![[Pasted image 20240622065356.png]]

- [ ] Complete this
      

##### Design Procedure

![[Pasted image 20240622065441.png]]

![[Pasted image 20240622065544.png]]
$$
h(n) = h_d(n) * W(n)
$$
4. The transfer function of the filter is obtained by taking Z-transform of $h(n)$



	