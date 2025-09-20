---
id: BER_Calculation
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
dg-publish: true
---
<<<<<<< Updated upstream:01 Academics/Btech/Projects/Final Year Project/BER Calculation.md
---
aliases: 
Date: "16-03-25"
---
# BER Calculation
The big question that come to mind when dealing with ber calculation in gnu radio is that, where to connect the Ber calculation block. 

First we have to compare 2 streams inorder to calculate the [[BER vs SNR]] , But we can use the feature of tagged stream inorder to calculate the error . 

Frequency Xlating FIR Filter

## Try using Correlation
- [[Correlation Estimator]]
- add correlation estimater
- 

## SER and BER over Gaussian channel

$$
rx_{snl} = tx_{snl} + noise
$$
where $tx_{snl} = {1 , -1}$ 

> [!NOTE] **AWGN**
> **Additive white Gaussian noise** (**AWGN**) is a basic noise model used in [information theory](https://en.wikipedia.org/wiki/Information_theory "Information theory") to mimic the effect of many random processes that occur in nature. The modifiers denote specific characteristics

_**Additive**_ because it is **added to any noise**

- $Eb/N0$ and sometimes it is called SNR per bit
![[Pasted image 20250404005454.png]]

Form tutorial 
![[Pasted image 20250402121745.png]]

#### New Method 
1. Attach a lengthy preamble like "111111111111111111" with a 0 last indicating the start of transmission
2. transmit exactly 1000 bits 
3. compare transmitted(source) and received(after removing preample)
=======
---
aliases: 
Date: "16-03-25"
---
# BER Calculation

First we have to compare 2 streams inorder to calculate the [[BER vs SNR]] , But we can use the feature of tagged stream inorder to calculate the error . 

Frequency Xlating FIR Filter

## Try using Correlation
- [[Correlation Estimator]]
- add correlation estimater
- 

## SER and BER over Gaussian channel

$$
rx_{snl} = tx_{snl} + noise
$$
where $tx_{snl} = {1 , -1}$ 

> [!NOTE] **AWGN**
> **Additive white Gaussian noise** (**AWGN**) is a basic noise model used in [information theory](https://en.wikipedia.org/wiki/Information_theory "Information theory") to mimic the effect of many random processes that occur in nature. The modifiers denote specific characteristics

_**Additive**_ because it is **added to any noise**

- $Eb/N0$ and sometimes it is called SNR per bit
![[Pasted image 20250404005454.png]]

Form tutorial 
![[Pasted image 20250402121745.png]]

#### New Method 
1. Attach a lengthy preamble like "111111111111111111" with a 0 last indicating the start of transmission
2. transmit exactly 1000 bits 
3. compare transmitted(source) and received(after removing preample)

### Introducing Noise
#### Channel Model
- Noise Voltage (The AWGN noise level as a voltage)
- Freq Offset 
- sample timing offset
- seed 
>>>>>>> Stashed changes:01 Academics/Btech/Projects/BER Calculation.md
