---
id: ECT402_PYQ
aliases: []
tags:
  - academics
  - btech
  - s8
  - ect402
dg-publish: true
---
# 2023 Supplementary Exam 
[QP Link](https://drive.google.com/drive/folders/1ye25K0pNKDLqqBM2thufvUbqNqmhWLT5)
#### 1. Compare and contrast the analog and digital cellular systems

| Analog Cellular                 | Digital                |
| ------------------------------- | ---------------------- |
| FM                              | CDMA , TDMA,FDMA,OFDMA |
| Less efficient use of bandwidth | Bandwidth efficient    |
| More noisy                      | Less noisy             |
| Low capacity                    |                        |
| No encryption                   |                        |
| High Power Consumption          |                        |

#### 2. what are the methods adopted for hand-off procedure?


#### Module 1
1. Describe the features of the GSM system architecture with the help of a neat
block diagram.

 
Assume a receiver is located 10Km away from a 50W transmitter. Given f = 900MHz , Gt = 1 and Gr=2. Find the power at the receiver and RMS voltage at receiver antenna matched with $50\ohm$ resistor.
 
 **ANS1** we have
 - d  = 10km
 - Pt = 50W
 - f = 900Mhz = 9* 10^8
 - Gt =1  , Gr = 2 
 - R = 50 

>using ![[01 Academics/Btech/S8/ECT402/ECT402#^648482|this equation]]
> **Step 1: Calculate the wavelength**
>$$
>\lambda = \frac{c}{f} = \frac{3\times10^8}{9\times{10^8}} = \frac{1}{3} m = 0.333m
>$$

> **Step 2: Using Friis equation to get the $P_{r}$**
> ![[ECT402#^648482]]
> $$
> P_{r} = 50 \times 1 \times 2 \left(\frac{0.333}{4 \pi \times 10 \times 10^3 }\right) = 7.02 \times 10^{-10} W
> $$
> - Received Power $P_{r}$ in $dBm$
>$P_{r}(dBm) = 10 \log_{10}(P_{r} \times 1000) = 10 \log_{10} 7.02 \times 10^{-10} = -61.53 \text{ dBm}$
> 
>

>**Step 3: Computing RMS Voltage at the receiver antenna**
>We know 
>$$
\begin{align}
P_{r} &= \frac{V_{rms}^2}{R} \\
\therefore V_{rms} &= \sqrt{P_{r} \times 2}  \\
 &=\sqrt{ 7.02 \times 10^{-10} \times 50 } \\
&= 1.87 \times 10^{-4 }V
\end{align}
>$$
## Q5
How is outage probability computed for a wireless system.
### Ans
Outage Probability is *the probability that the received Signal-to-Noise Ratio* (SNR) or Signal-to-Interference-plus-Noise Ratio (SINR) *falls below a certain threshold required for acceptable communication quality*.

>[!Note] Signal to Interference & Noise Ratio(SNIR)
>- It is used to give theoretical upper bonds on channel capacity (rate of data transfer)
>- Mobile operators tries to maximize the **SNIR** to deliver best possible customer experience
>- **SINR** is an excellent indicator of overall network health
>$$
\mathbf{SINR} = \frac{\text{Signal Power}}{\text{Noise + Interference Power}}
>$$

>[!Note] Outage Probability
>**outage probability** of a communication channel is *the probability that a given information rate is not supported*, because of variable channel capacity. Outage probability is defined as the *probability that information rate is less than the required threshold information rate*. It is *the probability that an outage will occur within a specified time period*[^1]

**Outage Probability**

$$
P_{out} = P_{r} \left(\gamma_{r} < \gamma_{th} \right)
$$

- $P_{\text{out}}$: Outage probability
- $\gamma_{r}$: Instantaneous received SNR
- $\gamma_{th}$: SNR threshold required for reliable communication
- $P_{r}$ Probability operator

[^1]:https://en.wikipedia.org/wiki/Outage_probability

