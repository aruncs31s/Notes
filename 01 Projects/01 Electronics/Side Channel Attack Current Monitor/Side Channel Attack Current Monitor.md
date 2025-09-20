---
id: 7-PROJECT
aliases: []
tags:
  - projects
  - electronics
  - sidechannel_attach_current_monitor
Date: 
Started: "12-10-2024"
GithubLink: https://github.com/aruncs31s/Amplifier-Circuit-For-Side-Channel-DPA-
Status: 
Completed: false
Working_ON: true
dg-publish: true
---
# Side Channel Attack Current Monitor

- [[09 Projects/GCE_Kannur/Kannur Solar Battery Monitor/Versions]]
> [!float|right-small] Components
> **Components USed**
>
> - Nexys A7
> - [[LM358]]

### Nexys A7

**To power fro USB**: Set jumper `JP3` to `USB`

- Out of the box the demo draws ~400ma

#### Powering the Board

- External power supply can be used by pluggin into the power jack **(J13)** and setting jumper to `JP3` to **WALL**
  > [!Important] Connection Type
  > The supply must be coax , **center-positive**
  >
  > - 2.1mm internal diameter
  > - atleast 1A current (5v , 1A = 5W)

#### Powering the board using battery Pack

![](nexysA7pdf.png)

#### Components Suggestion

##### For Measuring Current

- [[#CJMCU-219 INA219 I2C Bidirectional Current / Power Supply Monitoring Module]]
- [[#Voltage Devider]]

###### CJMCU-219 INA219 I2C Bidirectional Current / Power Supply Monitoring Module

[Source](https://robu.in/product/cjmcu-219-ina219-i2c-interface-no-drift-bi-directional-current-power-monitoring-sensor-module/)

- It supports current , voltage and power

| Spec        | Value     |
| ----------- | --------- |
| $I_max$     | +/- 3.2A  |
| Resolution  | +/- 0.8ma |
| Bus Voltage | 0 - 26V   |
| Interface   | I2C       |

###### Voltage Devider

- Selecting 1k$\ohm$ ohm with series `5v`

## Using Shunt Resistor

![](kicad1.png)

- In this sketch we can adjust the `Ri` and `Rs`(Rf) to get a good measure of the voltage drop across the shunt resistor
- Can use shunt resistor as small as 1kohm
- Need to use a voltage divider or use 3.3 V for the power supply for the opamp if it works on 3.3V

#### Measurement using DSO

![[scope_5.png]]

![[scope_1.bmp]]

### Amplifier Design 1

Designing a Differential amplifier like [[LM358#Differential Amplifier]] this

- Required Gain ? $x$
  > - Let required gain be $10$
  > - According to the relationship
  $$
  V_{out} = \left(V_{in2}  - V_{in1}\right) \frac{R_{f}}{R_{i}}
  $$
  > - taking $R_{f}$ as $10 \times R_{i}$ -> if $R_{f}$ is $100k$ then $R_{i}$ is $10k$

![[diff amp.png]]

#### Analysis

- Consider the Nexys A7 Draws $.65 Amps$

![[current measre]]

$$
\begin{align} \\
\hspace{1cm}
R &= 7.69  \\
\text{We know } R &= R_{shunt} + R_{load}  \\
\text{Where}  R_{shunt} & = .22 \ohm \\
R_{load} &= R - .22\ohm  \\
\newline \\
R &=  7.47 \ohm \\

\end{align}
$$

### Amplifier Design 2

Considering An Instumentation Amplifier
![[Instrumentation Amp.excalidraw|900x200]] ^a111b9
![[Schematics.png]]
![[PCB_Draw.png]]

## Timeline

```timeline
[line-3, body-4]
+ 06 October 2024
+ Problem Statement
+ Measure the current consumed by the [[nexysa7.png|Nexys A7]] for the **Differential Power Analysis**

+ 06th October
+ Initial Solution
+ Initial solution was to use a **Shunt resistor** across the power supply and measure the voltage drop across the resistor

+ 07th October
+ Problem with initial Solution
+ The main problem with initial solution is that there is lot of noise even at the level of $10mV$ so the actual reading might get effected by the **noise**
+ 13 November
+ Final Solution
+ The final Soution is to use a [[LM358#Instrumentation Amplifier|Instrumentation amplifier]] , which provides high input impedence and the gain can be easily controlled
+ 14 November
+ Prototype
+ The prototype is made ![[./attachments/PCB_Draw.png]]

```
