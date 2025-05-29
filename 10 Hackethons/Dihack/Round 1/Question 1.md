---
dg-publish: true
aliases: 
Date: 31-10-2024
---
# Question 1
Your friend needs some help from you for creating a circuit **without the use of any micro-controllers** (can use simple ICs and basic electronic components).  ^ef38c6
- Whenever an obstacle is in a vicinity of 30 cm of [[HC-SR04]] sensor, run a motor for 5s and then stop. ^5bac7b

- The motor should only be retriggered when the existing obstacle is moved away from the vicinity of 30cm and re-enter the 30 cm range. 


</br>

## Method 1


### Possible steps 
1. Find a way to measure distance using **[[HC-SR04]]** sensor from it datasheet 
2. make a circuit that can replicate the process without using a micro-controller like [[Arduino]]

### Actual Step 
1. Make a triggering circtuit that will trigger the HC-SR04 
- The pulse should be greater than $10us$
3. Make a Mono-Stable Multi-Vibrator using [[555|SE555]] timer 
	> Requirements 
	> - $5Sec$ $T_{on}$
	> - [[Differentiator]] with $f_c = \text{inverse T of the ECHO Out}$ 

#### Astable Multi-Vibrator Design 

##### Design 

 - Choosing $T = 1Sec$
 - Choosing 

#### Mono-Stable Multi-Vibrator Design
**Requirements**:
$T_{on} = 5sec$
$$
\begin{align}
\text{We know}\\
T &= 1.1 RC \\
5 &= 1.1 RC \\
R &= \frac{5}{1.1 C} \\
\text{let C = 0.1} \micro F \\
R &= 45454545 \ohm &= 45 M\ohm \\
\text{By choosing higher value of C} \\
\text{let C = 100} \micro F\\
R &= \frac{5}{1.1 \times 100 \times 10^{-6}} \\
&= 45.454 K\ohm \\
\end{align}
$$
#### Differentiator -> HPF Circuit 
**Requirements**: The [[HC-SR04]] produces a $1.740ms$ pulse when the target is near $30cm$ 
>- So the $Ton$ will be $1.740ms$ 
>- We can have any frequency but it should satisfy some condition like $T_{on} = 1.74ms$ so the best possible frequency is ${1 \over 2ms} = 500Hz$  
![[digital pulse.excalidraw]]

###### Design 
>We Know 
$$
\begin{align} 
R_{1} C_{1} &\le 0.0016T_{t} \\ \\
\end{align}
$$


>let $C_{1} = 0.01 \mu F$ 

$$
\begin{align}
\therefore R_{1} \times 0.01 \times 10^{-6} &\le  0.0016T_{t} 
\end{align}
$$
> We know $T_{t} = 1.74ms$ 

$$
\begin{align}
R_{1} &= \frac{0.0016\times 1.74 \times 10^{-3} }{0.01 \times 10^{-6}} \\
 &= 278.4\ohm
\end{align}
$$

![[rc differentiator.excalidraw]]

#### Designing a Duty Cycle Detector 
In this i will use the theory that `capacitor` will take some time to **charge** which can be utilized get to the $T_{on}$ of a **certain frequency** 
- So the Voltage across a Capacitor is
$$
V_{c} = V_{in}\left( 1-e^{\frac{-t}{RC}} \right) \tag{1.0}
$$

^b7e9da

![[voltage charging.excalidraw]]

According to [[#^b7e9da|Equation 1]] if we take 
- $R = 1k$ and $C=10uF$ and $V_{in} = 5V$

$$
\begin{align}
V_{c} &= V_{in}\left( 1-e^{\frac{-t}{RC}} \right)  \\ \\
&= 5 \times \left(1-e^{\large \frac{-1.74 \times 10^{-3}}{1\times10^3 \times 10 \times 10^-6}}\right) \\
&= 0.7985155117 \text{  volts} \tag{2.0}
\end{align}
$$

##### Designing Comparator 
![[comparator.excalidraw|1000x100]]

![[Pasted image 20241016213103.png]]


![[Pasted image 20241016212724.png]]



#### Designing A Astable Multi-Vibrator 
- [ ] Need to receive from Amarnath

- [[Method 2]]