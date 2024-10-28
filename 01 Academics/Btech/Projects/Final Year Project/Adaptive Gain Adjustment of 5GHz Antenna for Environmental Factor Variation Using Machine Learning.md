---
id: Topic 2
aliases:
  - final year project topic
  - topic 2
tags:
  - topic2
  - advantages
Created: 15-08-2024
cssclasses:
  - wide-page
---

# Adaptive Gain Adjustment of 5GHz Antenna for Environmental Factor Variation Using Machine Learning

## Prerequisites:
- [[Machine Learning]]
- [[Analog and Digital Communication]]
- [[MIMO]]
- [[ESP32]]
---
## Motivation

- Wireless Communication get highly effected by environmental conditions.
- not all power transmitted will reach the receiver due to following facts
	- Attenuation
	- Destructive interference


#### Advantages of 5Ghz

- More Available channels
- Less crowded Which reduces the interference from other devices because the bluetooth also uses the 2.4Ghz so there will be less crowd in `5Ghz`
- High Bandwidth
- Lower Latency

## Objective

- develop adaptive **5GHz** antennas for wireless communication
- adaptive antenna system **that leverages machine learning techniques** to adjust its parameters dynamically in response to **changes in environmental**

## Methodology

We are trying to dynamically change its parameters to maintain signal quality

1. Design and Construction
   1. Type of Antena
   2. Modeling Software
2. Dynamic Parameter Adjustment
   1. Radiation Pattern and Beam Steering: For phased array antennas, we can dynamically control the radiation pattern by altering the phase and amplitude of the signal at each antenna element.Which requires a Micro Controller or Single Board Computer or FPGA Board.
   2. Gain And Bandwidth
   3. Impedance Matching
   4. Polarization adjustiment
3. Integration With Machine learning
   1. Planning to use sensors
   2. Control algorithm using machine learning which will decide which factor to be changed in order to get maximum output
   3. Make a feedback mechanism if possible -> which enable constant control of the parameters through the communication between the reciever and the transmitter


## Learning

1. Wireless Communication Basics
   - 5Ghz frequency Band
2. Antenna Theory

   - Basic Radiation patterns
   - Antenna Design
     - Radiation patterns
     - Gain
     - Impedance Matching
     - Types of Antennas
       - Yagi , patch ,array antennas

3. Machine Learning
   1. Basic
      - supervised and unsupervised learning
      - Model Evaluation
      - overfittig/underfitting
   2. Advanced
      - Reinforcement learning -> realtime adaptation
      - NN -> Complex Pattern Recognition
   3. Related to our project
      - Check how the environmental condition effects antenna performance
4. Simulation Tools

   1. Antanna Simulation Software:
      - CST Microwave Studio
      - HFSS or COMSOL Multiphysics
   2. Machine Learning Framework
      - PyTorch
      - TensorFlow
      - Scikit-learn
   3. SDR Design ? Purchase

5. System Integration
   - Real-Time System -> How to implement realtime data processing and decision making according to sensor data?
   - Control Antenna parameters using MC or SBC? or SDR ?
   -


## Literature survey

1. [[Design and Analysis of Microstrip Patch Antenna for Wireless Communication]]
2. [Enhancing Wi-Fi communication with effective CSI approximations](https://researchoutreach.org/articles/enhancing-wi-fi-communication-with-effective-csi-approximations/)
3. [[#Study of the effect of Inland Water bodies on Line Of Sight Communication using Machine Learning at 5GHz]]
### Study of the effect of Inland Water bodies on Line Of Sight Communication using Machine Learning at 5GHz
Link : [[Study of the effect of Inland Water bodies on Line Of Sight Communication using Machine Learning at 5GHz]]

This paper studied the the effect of inland water bodies on  5GHz Communication and Modeled a Line Of Sight(LOS) communication channel over inland water bodies using **[[Machine Learning]]**

**Result:** The studies found that **when temperature increases the attenuation also increases** for channel Between water bodies also increases. Which show that the the attenuation of signals in the **day** time is greater than attenuation at **night**
**Algorithm Used**: ==Random Forest== -> For predicting channels betweeen water bodies 

**Key Terms**: [[Machine Learning]] ,[[Communication]] ,[[5Ghz]] 

##### How this help our project 
>- This paper shows that when temperature increases attenuation also increases and because there is comp taratively less temperature at night we can **reduce the transmission power** at night and increase at day times.
>	- This also shows that a static non varying system will suffer from attenuation during daytime

>- Also they used the help of machine learning to model the channel between water bodies 
## Working 
### ML Involvement
1. **Predicting CSI at Receiver Side**: CSI is measured at the receiver , so in  usual communication  system the `CSI` details is send back to the transmitter ,  ==This involves significant overhead==, such as on 20-MHz channels with 64 subcarriers i.e. carrier waves that are modulated to send additional information [^2]
> Dr Zhang and his team have discovered that CSI vectors in Wi-Fi networks can be approximated by a linear combination of as few as three sinusoids
>- These findings underpin Zhang’s development of CSIApx, an innovative compression methodology which offers high compression ratios with little loss of accuracy and the added advantage of low computation complexity resulting in a favourable reduction in overhead. [^2]
1. 
[^2]: [Enhancing Wi-Fi communication with effective CSI approximations](https://researchoutreach.org/articles/enhancing-wi-fi-communication-with-effective-csi-approximations/)
#### Resources

1. Cources about
   - Antenna Design -> "Antenna Theory: Analysis and Design" by Constantine A. Balanis for antenna design""
   - Machine Learning -> "Pattern Recognition and Machine Learning" by Christopher M. Bishop "
   - Wireless Communication
