---
id: Module_1
aliases: []
tags:
  - academics
  - btech
  - s3
  - ect205-nt
dg-publish: true
---
# NT Module 1
- [[Krichoff's First Law|KCL]]
- [[Kirchoff's Second Law]] 
- Mesh and node analysis
- Supermesh and Supernode analysis 
- Steady-state AC analysis using Mesh and Node analysis .
### Prerequisites
1. [[Electronics]]

###### Q 1.1 : Find the $V1$ 
![[Q 1.1.excalidraw]]
$$
\begin{align}
30 &= 2 + 3 + V_1 + 3 + 5 \\ 
V_1 &= 30 - 13 \\
V_1 &= 17 \tag{volt} 
\end{align}
$$

****

###### Q 1.2 : Find the current on the circuit and voltage across each resistor
![[Q 1.2.excalidraw|200x200]]

$$
\begin{align}
10V &= V_{R_{1}}+  V_{R_{2}} + V_{R_{3}} + V_{R_{4}} \tag{per KVL} 
\end{align} 
$$

also 

$$
\begin{align}
10 - IR_{1}- IR_{2} - IR_{3} - IR_{4} = 0 \\
10 - I\left( R_{1} + R_{2} + R_{3}+ R_{4}\right) = 0 \\
10 - I\left( 10^{6} + 3.1 \times 10^{6} + .4 \times 10^{6} + .5 \times 10^{6} \right) = 0 \\
10 - I\left( 5 \times 10^{6} \right) = 0 \tag{1}
\end{align} 
$$
Equation $1$ gives 
$$
\color{blue}
I = \frac{10}{5 \times 10 ^ {6}} = 2 \micro A 
$$
$$
\begin{align} 
V_{R_{1}}&= I \times R_{1} = 2 \times 10 ^ {-6}  \times  10^{6}= 2 V\\ 
V_{R_{2}}&= I \times R_{2} = 2 \times 10 ^ {-6}\times 3.1 \times 10^{6}= 6.2 V\\ 
V_{R_{3}}&= I \times R_{3}= 2 \times 10 ^ {-6}\times .4 \times 10^{6}= .8 V\\
V_{R_{4}}&= I \times R_{4} = 2 \times 10 ^ {-6}\times .5 \times 10^{6}= 1V \\ 
\end{align} 
$$

### Sources
- [[#Voltage Source]]
- [[#Current Source]]
- [[#Controlled Sources or Dependent Sources]]
	- [[#Voltage Controlled Voltage Source]]
	- [[#Current Controlled Voltage Source]]
	- [[#Voltage Controlled current Source]]
	- [[#Current Controlled Current Source]]
##### Voltage Source 
![[voltage sources.excalidraw]]
In ideal voltage source the voltage will be independent of the **current**, also the internal resistance of an ideal voltage source is *zero*.
$$
V_{t} = v - iR
$$

#### Current Source 

![[current source.excalidraw|200x200]]
The current will be constant irrespective of the change in the terminal voltage in the case of ideal current source . But in practical current source there will be a resistor parallel to the current element
![[ideal current source.excalidraw|200x200]]
where 
$$
i_{t} = i - \frac{v}{R}
$$

