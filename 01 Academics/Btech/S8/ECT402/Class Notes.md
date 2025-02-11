---
id: Class Notes
aliases: []
tags: []
Date:
  Created: "2024-12-17"
cssClasses: wide-page
dg-publish: true
---

# Class Notes

### 2024-12-17

- Multi carrier Modulation
  _if no noise_
  $$
  y(t) = s(t) =  \sum_{i} X_{i} e^{j 2 \pi f_{i}t}
  $$

<!-- $$ -->
<!-- f_{o}\int_0^{T_{o}}y(t) \left( e^{j 2 \pi f_{i}t}\right) dt = {B\over N} \int_0^{N\over  B} \left(\sum_{i} X_{i} e^{j 2\pi i {B\over N} t}\right) e^{} -->
<!-- $$' -->
<!---->

- [ ] OFDM
- [[Intersymbol Interference]]

## 2024-12-31

### MIMO OFDM(OFDMA)

- Combination of multiple-input multiple-output with OFDM
-

```mermaid
graph LR
A[SP Demux for transmit antennas] --> B[S/P Demux]
A --> C[S/P Demux]
B --> EM[N pt FFT]
A --> D[S/P Demux]
C--> E[N pt FFT]
D--> EE[N pt FFT]

E  --> K[MIMO Detection]
EE  --> LK[MIMO Detection]
```

- [ ] Complete

$$
y(n) = \sum_{l=0}^{L-1} H(l)x(n-1) + w(n)
$$

### Effect of Freq Offset in OFDM

- Due to variations in **orthogonality**
- [ ] Inter Carrer Interference (ICI) in OFDM

$$
\large \epsilon = \frac{\Delta f}{{B\over N}}\tag{1}
$$

Where $\epsilon$ -> normalized freq offset

#### Peak to average Power Ratio (PAPR)

$$\text{Peak Power } = \text{Average Power} =  E \large\left\{ |x(f)|^2\right\}= a^2$$

- [ ] Correct

### Single Carrier FDMA(SC-FDMA)

- To reduce the Peak to avg power ratio
- PAPR -> $0dB$

- [ ] Picture

```mermaid
graph LR

AA[Symbol Stram]
A[S/P demux ]
B[N pt FFT]
C[N pt IFFT]
D[P/S Mux]
E[Add CP]

AA --> A --> B --> C --> D --> E
AA --> A --> B --> C --> D --> E
AA --> A --> B --> C --> D --> E
```

Hypothetical

#### SC_FDMA Reciever

- [ ] Sub Carrier Mapping

### Sub carrier mapping in SC-FDMA

> [!Series]
>
> - [ ] LFDMA & I-FDMA -> {Zero Pad , Interleaving Zeros}

#### PathLoss , Shadowing , Doplar Shift

### 06-01-25

#### Path loss

$$
PL(dB) = 10 \log_{10} \left(\frac{4 \pi d}{\lambda}\right)^2
$$

- inv.prop Wavelength

#### Shadowing

Cause-> **Scattering**, **reflection**,and **diffration** -> results in signal degredation
eg: indor wifi signal cant penetrate through walls

[[#Path loss]] & [[#Shadowing]] -> Large scale fading

#### Multi path effect

- [ ]
- Due to reflections
- Causes: Fading , phase change

#### Diversity Techniques

- Used to compensate for fading channels
- implemented by using two or more receiving antenas,
- done by transmitting ultiple copies

- [[#Space Diversity]]
- [[#Freq Diversity]]
- [[#Angle Diversity]]
- [[#Time Diversity]]

##### Space Diversity

```mermaid
graph LR
Tx -- path --> Rx
```

- Multiple antennas are used to receive **Rx**

##### Freq Diversity

- Some freq. fading will be more
- Same info send using multiple carriers
- ie $s_1(t)$ and $s_2(t)$ will carry the same info.

##### Angle Diversity

##### Time Diversity

- Uses different timeslots ,

##### Polarization Diversity

- Uses antennas with different polarization

```mermaid
graph LR

```

---
