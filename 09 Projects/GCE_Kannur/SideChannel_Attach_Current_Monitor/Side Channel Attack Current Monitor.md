---
id: Side Channel Attack Current Monitor
aliases:
  - differential power analysis,sidechannel attack
tags:
  - project,embedded,crypto
Completed: false
Starting Date: "12-10-2024"
Status: true
Target Date: ""
---

# Side Channel Attack Current Monitor

## Components USed

- Nexys A7

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


### Using Shunt Resistor 
![](kicad1.png)
- In this sketch we can adjust the `Ri` and `Rs`(Rf) to get a good measure of the voltage drop across the shunt resistor 
- Can use shunt resistor as small as 1kohm 
- Need to use a voltage divider or use 3.3 V for the power supply for the opamp if it works on 3.3V


### Measurement using DSO 

![[scope_5.png]]

![[scope_1.bmp]]

