# Experiment 1
## FM generation and demodulation using PLL 565
Created : 2024-04-29 01:29

## Contents


### Aim:
To generate frequency modulated signal and to demodulate the Frequency Modulated signal using PLL.
### Theory
In FM, frequency of the carrier signal is varied in accordance with the instantaneous amplitude of the modulating signal. PLL is widely used for FM generation. The ==frequency generated by the VCO of the PLL is varied by the input signal applied==. The resistor `R1` and capacitor `C1` decides the carrier frequency of the FM. AF(Audio Frequency) input is capacitively coupled to pin 7 of the IC using R3-Cc network. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==For the demodulation of the FM signal, the center frequency of the VCO of the demodulator is made the same as that of the modulator==. The variation of the input frequency from the center frequency  is converted into the variation of the voltage by the phase comparator of the demodulator. FM input is coupled to the pin 2 using R3-Cc network as shown in figure.2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Major advantage of FM demodulator using PLL is linearity. Linearity is governed by the voltage to frequency characteristics of the VCO within the PLL. As the frequency deviation of the incoming signal swings over a small portion of the PLL bandwidth, and the characteristics of the VCO can be made relatively linear, the distortion levels from PLL demodulators are normally very low.

#### Circuit Diagram
Figure1. FM generator using <b>IC565</b>

![[Drawing 2024-04-29 01.39.09.excalidraw]]
- Figure 2 . FM Demodulation Using IC565
![[Demodulation using IC565.excalidraw]]
#### Design
 - Let $V_+ =10$ and $V_- = -10$
 - Let the center frequency of the FM be $f_o= \frac{1.2}{4\times R1\times C1} =2.5 \ \ kHz$ 
 - Take $C1=0.01μF$ Then we get $R1=12 kΩ$
 - The value of ==R1 satisfies the required condition== $2 kΩ < R1 < 20 kΩ$ as per data sheet. 
 - Take $C_c=10 μF$ and $R_3=12 \ kΩ$ to couple the input to the IC.
- For ==demodulator circuit, since center frequency is same as that of modulator, frequency determining components are the same==.
- Take same set of coupling capacitor and resistor.
- Take $R_2=1 kΩ$, $C2=10 μF$ and $C_3=0.01 \mu F$

#### Procedure
1. Set up the FM generator circuit and apply 5 Vpp, 1KHz sinewave input and observe the output.
2. Note maximum and minimum frequencies, fmax and fmin of FM output. 
3. Calculate frequency deviation $∆f= fmax – fmin.$ Calculate the modulation index $m_i = \Delta f/fm$ where fm is modulating signal frequency.
3. Set up FM demodulator and apply the FM signal to it. Observe the demodulated output.
#### Output

![[Pasted image 20240429092338.png]]



## Using IC4046B

![](https://www.homemade-circuits.com/wp-content/uploads/2023/03/IC-4046-pinout-details.jpg)



## References

1. 