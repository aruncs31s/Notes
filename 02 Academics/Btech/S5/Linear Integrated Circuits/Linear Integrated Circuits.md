---
id: LIC
aliases: []
tags:
  - academics
  - btech
  - s5
  - linear_integrated_circuits
dg-publish: true
---
# Linear Integrated Circuits
## Contents
- [[#Module 1]]
- [[#Module 2]]
- [[#Module 3]]
- [[#Module 5]]

### Module 1
##### Syllabus

###### Operational amplifiers(Op Amps):

- [x] The 741 Op Amp ✅ 2024-06-18
- [x] Block diagram ✅ 2024-06-18
- [x] Ideal op-amp parameters ✅ 2024-06-18
- [x] Typical parameter values for 741
- [ ] Equivalent circuit
- [ ] Open loop configurations
- [ ] Voltage transfer curve
- [ ] Frequency response curve.

##### Differential Amplifiers:

- [ ] Differential amplifier configurations using BJT
- [ ] DC Analysis- transfer characteristics;
- [ ] AC analysis- differential and common mode gains, CMRR, input and output resistance, Voltage gain.
- [ ] Concept of current mirror-the two transistor current mirror, Wilson and Widlar current mirrors.
#### Op Amp

![[Drawing 2024-06-18 13.38.46.excalidraw]]
The Gain of OP-AMP is denoted by "A":

$$
A = {V_o \over (V_1 - V_2 )}
$$

$$
V_o = A \times (V_1 - V_2) 
$$
$$
V_o =  V_1 - V_2
$$

Where
_$V_1$_ => Input voltage at _non-inverting_ input
_$V_2$_ => Voltage applied at _Inverting_ input
$V_o$ => Output Voltage

---

##### IC 741

![[Drawing 2024-06-18 13.38.46_2.excalidraw]]

- The output produced by the non-inverting terminal will be in-phase with the input
  $$
  V_o = A (V_d)
  $$
- The output produced bu the inverting terminal will be out of phase or opposite polarity with input
  $$
  V_o = -A(V_d)
  $$

##### Block Diagram

![[Drawing 2024-06-18 14.04.37.excalidraw]]

1. **Input Stage** : It consists of a dual input , balanced output differential amplifier. Its function is to amplify the difference between 2 input signals . - Provides high differential gain - High input impedance - Low output impedance 2.**Intermediate Stage**: The overall gain of an Op-Amp is very high. Since the input stage alone can not provide such high gain . Intermediate stage is used to provide the required additional voltage gain.

- It consists of another differential amplifier with dual input and unbalanced output.

3. **Level Shifting Circuit(Level Shifting Stage/Buffer):** As the Op-Amp amplifies D.C signals also , the small D.C quiescent voltage level of previous stage may get amplified and get applied as the input to the next stage causing distortion to the final output
   Hence the **level shifting stage** is used to bring down the D.C level to ground potential , when no signal is applied at the input terminals . And the buffer is usually an emiter follower used for impedance matching

4. **Output Stage**: It consists of a push-pull complementary amplifier which provides large A.C output voltage swing and high current sourcing and sinking along with low output impedance

- [ ] Draw the ic internal diagram

- The no. 741 indicates

  - 7 functional pins,
  - 4 input pins,
  - 1 output pin.

- It has high voltage gain.

###### Pin Description of 741

- Pin **7** is the +Ve power supply terminal
- Pin **4** is the -Ve power supply terminal
- The voltage between these two pin will be between **5V** and **18V** .

- Pin **6**

  - The o/p from the op-amp is taken from this pin
  - the output voltage depends on the feedback used and its parameters and the voltage at the input terminals
  - when high voltage is received at the pin 6 , it means the output voltage received is similar to +ve supply voltage(**+VCC**)

- Pins **2** and **3** : Input Pins

  - Pin 2 is the inverting input of the op-amp . pin 3 is the non inverting input of the op-amp

  - When the voltage at pin 2 is greater than the voltage at pin 3 , it means that the inverting terminal has higher voltage . So , the output signal would be low.
  - When the voltage value at the pin 3 is higher than the voltage at pin 2 , the voltage level at non-important input is high . So the output signal obtained would be high .

- Pin **1** & **5** : Offset null

  - Op-Amp 741 provides high gain
  - Because the Op-Amp provides high gain , minor difference in the voltage at the inverting and non-inverting terminals can influence the output
  - To nullify this influence , an offset voltage may be applied to the op-amp. This offset voltage is applied at pin **1** and **5**
  - It is usually done by using a potentiometer

- Pin **8**: NC
- It is not connected to any part of the IC 741 . Used to fill the void space in the standard 8 pin package

##### OP AMP Parameters

##### DC characteristics

- No current will be drawn from the source(but real op-amps draws current from the source)
- response is not temperature dependent
- respond differently to current and voltage due to mismatch in transistors.
- Shifts in operation with temperature

##### These non ideal DC characteristics that add error components to the dc o/p V are.

- i/p bias current
- input offset current
- i/p offset voltage
- Thermal drift
  _These will affect the steady state(DC) response of op-amp only_

###### Input offset voltage $V_{io}$

- ==it is the voltage that must be applied between the two input terminals of the op amp to obtain zero volts at the output==.
- In an ideal op-amp, the DC voltage of the V(+) and V(-) terminals match exactly when the input voltage (Vi) is 0 V.
- But in reality, there are diff.s in input impedance and input bias current between the V(+) and V(-) terminals, causing a slight diff in their voltages.
- This diff called input offset voltage is multiplied by a gain, appearing as an output voltage deviation from the ideal value.

- ==It is necessary to select an op-amp with low input offset voltage==.

![[Drawing 2024-06-18 18.53.00.excalidraw]]

- The input offset is typically 2mV to <6mV.

###### Input offset Current $\color{yellow}I_{io}$

- The input terminals conduct a small value of dc current to bias the input transistors.
- Since the input transistors cannot be made identical, there will always be some small difference between the currents into inv and non inv terminals.
- There exists a difference in bias currents.
- This algebraic diff is called as $I_{io}$

$$
I_{io} = | I_{B1} - I_{B2}|
$$

- _The difference between the bias current at the input terminals of the op-amp is called a input offset current_
- $I_{io(max)}$ for 741 IC is $200nA$

###### Input Bias current $I_B$

- It is the average of $I_{B1}$ and $I_{B2}$
- In ideal op-amp we assume no current is drawn from i/p terminals
- But practically i/p terminals do conduct a small value of dc current to bias the i/p transistors.
- $I_B$ is the average of currents that flow into inverting and non inverting i/p terminals of op amp .

  $$
  I_B = (I_{B1} + I_{B2})/2
  $$

- $I_{B(max)}$ = 700nA for 741 IC

###### Output offset voltage

- It is the Voltage appears at o/p for zero(0) input
- May be due to i/p offset voltage or i/p bias current or both
- Many op-amp provide offset compensation pin to nullify offset Voltage .
- For 741 op-amp , a 10k$\ohm$ potentiometer is connected between offset null pins 1 and 5 and wiper connected to -ve supply pin 4.
- Position of wiper is adjested to nullify the o/p offset voltage.

- [ ] Draw the cirtuit diagram

###### Thermal Drift

- Bias current, offset Voltage and Current change with temperature.
- A circuit nulled at 25 degree may not remain so when temp rise to 35 degree /
- This is called drift
- Offset current in nA/deg C
- Offset Voltage in mV/deg C

##### AC characteristics

###### Frequency Response

- [ ] Complete this

###### Slew Rate

- ==Slew rate is defined as the maximum rate of change of an op amp output voltag==e , and is given in units V/$\micro$s
- ==It is measured by applying a large signal step , such as 1V to the input of the op amp. and measuring the rate of change from 10% to 90% of the output signal's amplitude.
- Slew rate of 10 V/$\micro$s means that when a large step is change is placed on the input , the electronic device would be able to provide an output 10V change in 1$\micro s$

$$
S = {dV_0 \over dt}
$$
- Unit is $\frac{Volt}{\micro s}$
- Ideal Slew Rate is $\infty$
- But practically for 741 IC , SR is 0.5 $V\over \micro s$

### Module 2

#### Syllabus
##### Op-amp with negative feedback
- Voltage Series, Voltage Shunt, current series and current shunt
negative feedback
- Op Amp circuits with voltage series and voltage shunt feedback
- Virtual ground Concept

##### Op-amp Applications
- Summer, 
- Voltage Follower-loading effects,
- Differential and Instrumentation Amplifiers,
- Voltage to current and Current to voltage converters,
- Integrator,
- Differentiator,
- Precision rectifiers,
- Comparators,
- Schmitt Triggers,
- Log and antilog amplifiers
# Module 3 

### Syllabus
##### Op-amp Oscillators and Multivibrators:
- [x] Phase Shift and ✅ 2024-06-20
- Wien-bridge Oscillators,
- Triangular and Sawtooth waveform generators,
- Astable and monostable multivibrators.
##### Active filters:
- Comparison with passive filters,
- First and second order low pass,
- High pass,
- Band pass and
- band reject active filters,
- state variable filters.

#### RC Phase Shift Osfc = {vocillator
$$
fc = {1 \over 2\pi R C \sqrt{6}}
$$
fc -> Frequency of oscillation

#### Wein Bridge Oscillator

$$
f_o = {1 \over 2 \pi RC} = {0.159 \over RC}
$$

##### Gain 

$$
Av = {1 \over \beta} = 3 
$$

![[Pasted image 20240620100439.png]]
![[Pasted image 20240620100605.png]]

# Module 5

### Syllabus
##### Voltage Regulators:
- [ ] Fixed and Adjustable voltage regulators,
- [ ] IC 723 – Low voltage and high voltage configurations,
	- [ ] Current boosting,
	- [ ] Current limiting,
	- [ ] Short circuit and Fold-back protection.
##### Data Converters:
- [x] Digital to Analog converters, ✅ 2024-06-18
	- [x] Specifications, ✅ 2024-06-18
	- [ ] Weighted resistor type and
	- [ ] R-2R Ladder type.
- [ ] Analog to Digital Converters:
	- [ ] Specifications,
	- [ ] Flash type 
	- [ ] and Successive approximation type.