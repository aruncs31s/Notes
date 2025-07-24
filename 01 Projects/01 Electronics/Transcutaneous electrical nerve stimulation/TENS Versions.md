---
dg-publish: true
aliases: 
Date: 23-11-2024
cssClasses: wide-page
---

# TENS Versions
## Initial Design 
![[TENS Design.excalidraw|900x100]]
### Components Required

| Name                          | Cost         |
| ----------------------------- | ------------ |
| ESP32/Arduino                 | 500/-        |
| Transformer                   | 250/-        |
| MOSFET                        | 15/-         |
| Dot PCB                       | 50/-         |
| 3.7 V Battery                 | 70/-         |
| DC up Converter               | 90/- or 70/- |
| Resistors                     | 5/-          |
| miscellaneous                 | 20/-         |
| Battery Management System<br> | 40/-<br>     |
| Total                         | 1040/-       |

## Version 0.1.0
Version 1 -> 0.1.0 in this version i'm planning to use the monostable followed by astable , switch , inverter 

```mermaid 
graph LR
A[Monostobele] -- Reset Pin--> B[Astable] -->C[Mosfet SWITCH] --> D[Inverter]  
```

**Monostable Multivibrator**:  [[555]]
>The monostable will provide a varying duration , it is best not exceed the duration morethan 10 second and less than one second 

**Astable Multivibrator**: [[555]] , 
>The [[Astable Multivibrator]] is used to control the turning on and turning of of the inverter , in theory the inverter will run only on the frequency which is able to work , which is the same frequency as the oscillation of the **feedback transistor** , so this **Astable Multivibrator** is not actually controlling the output frequency of the transformer which is high voltage , but rather turning on and of the transformer , which simulates the a low frequency turning on and off.

**Inverter Circuit**: SMPS [[Transformer]]
Here i have used a high frequency transformer from the [Mosquito Bat](https://www.electrothinks.com/2019/09/mosquito-killer-bat-circuit-working-explanation.html)
 ![[Tens Version 0.1.0.excalidraw|900x300]]
### Inverter Circuit
![[Inverter Circuit.excalidraw]]

### Duration Circuit 
![[monostablemultivibrator.excalidraw]]

#### Design 

Required Duration : 

![[555#^aeeb05]]

Using this relation to obtain 1seconds to 30 seconds duration 

$$
\begin {align}
30 \text{ sec} &= 1.1 R \times C \\
\text{let C = 0.01uF} \\
R &= \frac{30}{1.1 \times 0.01 \times 10^{-6} } = 2.727 \times 10^{7}K \ohm \\
\text{the resistance value is too high so } \\
\text{taking C = 680 uF} \\
R &= \frac{30}{1.1 \times 680 \times 10^{-6}} = 40.1K\ohm
\end{align}
$$
*we can use 100k pot to adjust an obtain duration 30sec and 1 sec*

### Astable Multivibrator 

#### Design 
Required Freq : $1 Hz \text{ to } 50 Hz$

| Components  | Value |
| ----------- | ----- |
| Rb          | 200k  |
| Transformer | x:x   |


#### References

1. https://www.electrothinks.com/2019/09/mosquito-killer-bat-circuit-working-explanation.html
2. 