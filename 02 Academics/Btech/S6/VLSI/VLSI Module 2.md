---
id: VLSI Module 2
aliases: []
tags:
  - academics
  - btech
  - s6
  - vlsi
mindmap-plugin: basic
dg-publish: true
---
# VLSI Module 2

Created : 2024-05-24 02:58

## Contents
- [[#Syllabus]]

## Syllabus

- Static CMOS Logic Design
- MOSFET Logic Design
  - NMOS Inverter (Static analysis only)
  - basic logic gates,
- CMOS logic
  - Static and transient analysis of CMOS inverter
  - Switching power dissipation and delays.
  - Realization of logic functions with static CMOS logic,
  - Pass transistor logic, and transmission gate logic

## Contents
1. [[MOSFET]]

### Basic Inverter Circuits
- Inverter is most fundamental logic gate ==that uses single input==.
- The basic principles employed in design and analysis of MOS inverters can be directly applied on more complex logic circuits.Therefore inverter design forms basis for digital circuits.
- The ==basic requirement for producing a complete range of logic circuits is the inverter==. ie, it can be used to produce a large range of logic circuits and fundamental gates.
- Inverter is needed for ==restoring logic levels== for **NAND** and **NOR** gates and for sequential and memory circuits of various forms.

#### Classification
- [[#NMOS Inverter]]
	- Resistive Load
	- Depletion Type Load
	- Enhancement Type Load
	- Pseudo NMOS Load
- CMOS Inverter

#### NMOS Inverter
- The basic inverter circuit requires a transistor with source connected to ground and a load resistor of some sort connected from the drain to the positive supply rail $V_{DD}$.
- The output is taken from the drain and the ==input applied between gate and ground==.
- ==NMOS acts as a switch==

RESISTIVE LOAD NMOS INVERTER

![[Pasted image 20240527000401.png]]

Here the load used is a resistor.
• This arrangement is not often used because of the large space
requirements of resistors produced in a silicon substrate.
• ==Also standby leakage is more==, ==poor noise margin==
• Resistors are not conveniently produced on the silicon substrate;
even modest values occupy excessively large areas so that some
other form of load resistance is required.
• ==A convenient way to solve this problem is to use a transistor as the load.==
##### DEPLETION TYPE LOAD NMOS Inverter
![[Pasted image 20240527000323.png]]
- With no current drawn from the output, the currents Ids for both transistors must be equal.
- For the depletion mode transistor, the gate is connected to the source so it is always on and only the characteristic curve $V_{gs} = 0$ is relevant.
- In this configuration the depletion mode device is called the pull-up (p.u) and the enhancement mode device the pull-down (p.d.) transistor.
- The D-MOS here acts as a nonlinear resistor (as always on)
- D-MOS work in either in Linear region or in saturation region.
- The maximum voltage across the enhancement mode device corresponds to minimum voltage across the depletion mode transistor.
- When $V_{in}$ (= $V_{gs}$ p.d. transistor) exceeds the p.d. threshold voltage current begins to flow.
- The output voltage $V_{out}$, thus decreases and the subsequent increases in Vin will cause the p.d. transistor to come out of saturation and become resistive.
- The pull up transistor is initially resistive

![[Pasted image 20240527002048.png]]

- Dissipation is high, since rail to rail current flows when $V_{in}$ = logical 1.
- Switching of output from 1 to 0 begins when $V_{in}$ exceeds $V_{th}$ of pull down device.
- When switching the output from 1 to 0, the pull up device is non-saturated initially and this presents lower resistance through which to charge capacitive loads.

##### ENHANCEMENT TYPE LOAD NMOS INVERTER
- Dissipation is high since current flows when $V_{in}$ = logical 1 ($V_{GG}$ is returned to $V_{DD}$).
- $V_{out}$ can never reach $V_{DD}$ (logical 1) if $V_{GG}$ = $V_{DD}$ as is normally the case.

![[Pasted image 20240527003509.png]]

##### PSEUDO NMOS LOAD NMOS INVERTER

![[Pasted image 20240527022503.png]]

- The inverter that uses a p-device pull-up or load that has its gate permanently ground

#### CMOS INVERTER
A CMOS inverter ==consists of two opposite polarity MOSFETs== Mn(nMOS) and Mp(pMOS) with their ==gates connected together at the input==.
- The output voltage is taken from common drain terminals

![[Pasted image 20240527024525.png]]![[Pasted image 20240527024518.png]]

﻿  
- An nMOS PMOS group with a common gate is called a ==complementary pair==, which gives us the "C" in "CMOS."  
- The transistors are connected in a manner that ensures that ==only one of the MOSFETs conducts when the input is stable at a low or high voltage==. This is due to the use of the complementary arrangement.  

> [!NOTE] Working
>The circuit topology is complementary push- pull in the sense that ==for high input, the nMOS transistor drives (pulls down) the output node while the PMOS transistor acts as the load==, ==and for low input the pMOS transistor drives (pulls up) the output node while the nMOS transistor acts as the load==.  

> - From the circuit we have  
>$$ \begin{align}V_{GSn} &= V_{in} \\ V_{SGP}&=V_{DD} - V_{in}\end{align}$$
where Vin is assumed to be in the voltage range [0, $V_{DD}$] with $V_{DD}$ the power supply.

> [!NOTE] $V_{GSn}$ and $V_{SGp}$
> $V_{GS_N}$​ and $V_{SG_P}$​ are voltages related to the gate-source junctions of the **NMOS** and **PMOS** transistors, respectively.
> 1. $V_{GS_N}$​ (**Gate-Source Voltage of NMOS**)
> - This is the voltage difference between the gate (G) and the source (S) of the NMOS transistor.
> - For an NMOS transistor to turn on, $V_{GS_N}$​ must be greater than the threshold voltage $V_{TN}$​ of the NMOS transistor.
> 2. $V_{SG_P}$​ (Source-Gate Voltage of PMOS)
> - This is the voltage difference between the source (S) and the gate (G) of the PMOS transistor
> - Note that for PMOS transistors, the source is typically at a higher potential than the drain, so $V_{SG_p}$ is often used instead of $V_{GS_p}$ to keep the sign convention consistent.
> - For a PMOS transistor to turn on, $V_{SG_P}$​ must be greater than the threshold voltage $V_{TP}$​ of the PMOS transistor (where $V_{TP}$​ is negative).

##### Operation
1. When $Vin$ = $Vdd$ => High input
	- $V_{GS_n} = V_{DD}$ and $V_{SG_p} = 0$
	- **Mp** is in ==Cut off Region== and **Mn** is in ==Saturation Region==
	- and **Mn** provide a path to ground resulting in a voltage of 0 at the common drains ,$mmin(Vout) = V_{OL}=0$
2. When $V_{in} =0$ => low input voltage
	-  $V_{GS_n} = 0$ and $V_{SG_p} = V_{DD}$
- The PMOS **Mp**, provides a conductive path to the power supply and gives  $max(Vout) = V_{OH}=V_{DD}$

##### CMOS DC Operation

![[Pasted image 20240527144248.png]]
     ![[Pasted image 20240527144908.png]]![[Pasted image 20240527144847.png]]
###### Region 1: Input = 0

| pMOS                                | ON              |
| ----------------------------------- | --------------- |
| nMOS                                | OFF             |
| Output                              | VDD             |
| Input                               | 0               |
| Current flow btw $V_{dd} \& V_{ss}$ | NO Current Flow |
###### Region 2 : Input = $V_{DD}$
*Opposite of Region 1*

| pMOS                                | OFF             |
| ----------------------------------- | --------------- |
| nMOS                                | ON              |
| Output                              | 0               |
| Input                               | $V_{DD}$        |
| Current flow btw $V_{dd} \& V_{ss}$ | NO Current flow |

###### Region 3 

| nMOS     | Saturation        |
| -------- | ----------------- |
| pMOS     | Linear            |
| Input    | Slowly Increasing |
| Output   | Slowly Decreasing |
| $I_{ds}$ | Slowly Increases  |

###### Region 4 

| nMOS     | Linear                      |
| -------- | --------------------------- |
| pMOS     | Saturation                  |
| Input    | Increasing towards $V_{DD}$ |
| Output   | Decreasing towards 0        |
| $I_{ds}$ | Slowly Decreases            |

###### Region 3

| nMOS      | SAT       |
| --------- | --------- |
| pMOS      | SAT       |
| Current   | MAX       |
| $V_{in}$  | $V_{out}$ |
| $V_{out}$ | $V_{in}$  |

#### Properties
- An important property of CMOS is that the output logic swing V, is given by  
 $$VL = VOH-VOL = V DD$$ 
 - This shows that the CMOS inverter exhibits a full-rail output voltage swing, i.e., the entire power supply range.  
 - This helps provide ==well-defined logic 0 and logic 1== voltages.

##### Input Low voltage ($V_{IL}$)
- The input low voltage $V_{IL}$ represents the ==largest value of $V_{in}$== ==that can be interpreted as a logic 0== input.  
- If the input voltage satisfies Vin<V1 then the output voltage Vout is either at VDD or close to it, indicating that the output can be interpreted as a logic 1.  
- If Vin is increased above VIL, the circuit moves into the transition region. 
-  Using stability arguments, we define $V_{IL}$  as the point where the slope of the VTC has a value of -1, i.e.,  
$$
{dV_{out} \over dV_{in}} = -1
$$

## References

1. Ktu Syllabus
2. https://youtu.be/XEzzYu4wkw4?si=BEvwC6kDAsLNDimd