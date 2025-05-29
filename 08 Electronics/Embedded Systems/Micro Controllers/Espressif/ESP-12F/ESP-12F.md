---
aliases: 
Date: 24-01-25
---
# ESP-12F


## Programming

### Programmer Circuit

- [ ] CH_PD. ?
## Pins
**CH_PD**: If voltage for CH_EN pin is low, the  chipset ESP8266EX ==will power off==^[https://www.esp8266.com/viewtopic.php?p=42327]. Should connect pullup. **10K**
>This might work on all the esp8266 varients. 

- [ ] Can  i use this CH_EN pin to save power.



### Pin Config

**Programming Mode**

| GPIO 0  | Low  |
| ------- | ---- |
| GPIO 2  | High |
| GPIO 15 | Low  |
| RST     | High |
| EN      | High |
The **GPIO 0** needs to be low in Programming or downlading mode and high in **running** mode so i should put a push button and pull up resistor. 

**Running Mode**: 
- After Programming 

| GPIO 0 | LOW |
| ------ | --- |

*Other pins are same.*
![[Screenshot 2025-02-08 at 12.04.06 AM.png]]
![[Screenshot 2025-02-08 at 12.05.30 AM.png]]
![[Screenshot 2025-02-08 at 12.10.49 AM.png]]



## Power Supply
- There is $10\micro F$ and $100nF$ capacitors are connected between the power rails ? 

$$
X_{c} = \frac{1}{2\pi f_{c} }
$$
$$
\begin{align} \\
\text{Here C = 10 uF} \\

10 \times 10^{-6}  &= \frac{1}{2\pi f_{c}} \\
f_{c} &= \frac{1}{2\pi 10^{-5}}  \\
fc &\approx 16 KHz 
\end{align}
$$
