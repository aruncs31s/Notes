---
id: Study_Session_Materials
aliases: []
tags:
  - interviews
  - digital_core_technologies
dg-publish: true
Date: 03-01-2025
---
# Study Session Materials

## Workshop_25 Basics of Electronics 

## Part 1 Introduction & Basics 
What they are going to cover
- What is Electronics Engineering  / Design ?? 
- **How to analize/design** electronics circuits 

>[!IMPORTANT] Analyzing a circuit
> Analyzing a circuit is important because that helps us to design a new circuit 

- Whom is this workshop for -> 4th year engineers who are planing to enter [[08 Electronics/Embedded Systems/Embedded Systems|Embedded Systems]] domain 

---
### Parts 
- Basics Concepts and Passive components 
- Semi-conductor Components and circuits
- Digital Circuits , Microprocessors and its interfacing 
---
### Part 1 

---
In this part we're  going to learn **Different perspective** of looking at circuits and it's behaviors 

- "How to Learn ?" has given more priority/focus than what to learn 

---
 - Learning is a **self involved process** , not passive activity 

---
#### Exercise 
**Prerequisites**
1. Keep a **Pen** , **Pencil** & **Eraser** ?book???
2. There will many Questions in every session. Do pause the video and answer that ourselves 
3. To get maximum benefits from the series, it is highly recommended that:
	- You **Pause the video** for every question 
	-  **Think** , and **try to write down** ==your answer==(do it ourselves) on the **paper**
	- Then continue and listen to the answers in the video, **Pause video** & **Analyse** 
	- For every such question, there will **multiple right answers** not the right answer.
	- Many times, **the way we analyze the problem  and arrive at the solution** is more valuable than just the answer to the question(trust the process ? the the result?)
---
### What is Engineering 
Engineering is finding **Practical Solutions** (also optimal solutions) to ==real life problems==, using **Engineering principles**.

**Eg:** 

| Ideal Problem            | **Real Life Problems** |
| ------------------------ | ---------------------- |
| $2\times 2 = 4$          | Crossing a river       |
| $\tan ({\pi \over 4})=1$ |                        |
What is so special about **Crossing a river** ?
**Solutions:** 
1. Swimm across -> provided you know swimming & the river is safe to swim 
2. Using a boat
3. Using Bridge 
"You have to choose the right solution according to the context"

#### What is Electronics Engineering
**Electronics Engineering** is finding **practical solutions** to real-life problems using **Electronics principles** 
or
Engineering branch which make use of **Electrons** to **Solve Real Life Problems** 
or 
Engineering branch which make use ==Behaviour==  of **Electrons** to **Solve Real Life Problems**  

##### Electrons

- From where do we get our **Workforce (Electrons)?**
- How to **Motivate** the **workforce Electrons**? 

##### Electro-Motive Force (EMF)

If you move a coil in a magnetic field the electron in the coil get a electro-motive force or a potential difference is induced in that -> **Electric Generators**

###### Way of Motivating Electrons
1. Chemical Batteries 
2. Generators
3. Solar Energy 

#### How do we quantify the motivation (Quantization)
1. What is Voltage: Potential of the electron do the work  -> **Potential difference** , Unit $Volts(V)$ 
2. Current: Flow rate(count per seconds) , Unit  $Amps(A)$
**Cause** <->  **Effect** Relationship
eg: 
**Cause** = **Current** , **Effect** is **potential difference**

3. Power: $\text{Potential} \times \text{Current}$ , Unit $Watts(W)$ 
$$
\begin{align}
P &= V \times i \\
P &= \large {V^2 \over R} \\
P &= i^2 \times R
\end{align}
$$
Where 
$R$ -> Resistance
$i$ -> Current
$P$ -> Power 
$V$ -> Potential difference 

4. Energy: $\text{Power} \times \text{Time}$ ,Unit $\text{Jules} = \text{Watt- Sec}$ , $Watt-Hr(Wh)$
or $\text{Potential} * \text{Current (integrated over time)}$ 

#### Sources of Motivated Electrons 
![[voltage_current_sources.excalidraw]]
**Voltage Source:** They regulate the output voltage 
**Current Source:** They regulate the output current 

**Q:** How the current source is limiting the current?

### Resistance 
Parameters when choosing  -> Tolerence,Power,Size,Cost 

When current flows through it it there will be a voltage drop across it , The current flow causes heating up the resistor 
### Capacitors
Unit -> Farada
Reactance/Impedence
Params -> Voltage,Capacity,ESR,Size,Cost
It does not allow suddent change in **voltage** across the capacitor.
- It stores energy in electric field
$$
X_C = \frac{1}{2\pi f c}
$$
- When the frequency increases Reactance/Impedence decreases
- That cause it to act as short circuit in high frequency 
### Inductor
Unit -> Henry
Reactance/Impedance
Param -> Tolerence,Current,ESR,Size,Cost,
Inductor does not like sudden **change** in **Current** through it. 
- Change in **current flow through** an inductor causes change in **Magnetic field** around it  , It oposes current by inducing a voltage around it.

$$
X_L = 2\pi fL
$$
- This is directly contredictory to the capacitor 
- when the frequency increases the **Reactance/Impedance** also increases , causing to act as **open circuit** in high frequency and **short circuit in low frequency** 
>[!Important] Inductor on Steady Currents 
>Steady current does not effect the inductor , only the **change** in current that effects the inductor 

---

