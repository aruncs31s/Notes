---
id: Experiment_2
aliases: []
tags:
  - academics
  - btech
  - s7
  - electromagnetics_lab
Date: 12-11-2024
dg-publish: true
---
# Experiment 2
**Aim**: To Study mode characteristics of reflex Klystron , plot mode characteristics and hence compute **ETR(Electronic Tuning Range),** and **ESR(Electronic Tuning Sensitivity)**

#### **Bench Setup**

```mermaid
graph LR
A[Klystron Mount] --> B[Isolator] --> C[Variable Attenuator] --> D[Detector Mount] --> E[Matched Termination]

```

Where a Klystron power supply is used to power the klystron and the [[VSWR]] meter is connected to the Detector mount 

#### ETR and ETS 

$$
\begin{align}
ETR & = F_{1} - F_{2} \\ \\
ETS &= \frac{F_{1} - F_{2}}{ |V_{2}| - |V_{1}|}  
\end{align}
$$

#### Keypoints
1. Know how to setup the bench setup 
2. Convert $dB$ to linear $linear = 10^{dB/10}$ 
3. Ripple voltage will not go bellow -90V

