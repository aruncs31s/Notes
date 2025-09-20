---
id: Communication_Simulation_with_Error_Correcting_Code_using_Matlab
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: 01-11-2024
dg-publish: true
---
# Communication Simulation with Error Correcting Code using Matlab
**Obj**:- The objective of this study is to evaluate the performance of **different type of error correcting code** in an Additive White Gaussian Noise (AWGN) channel. Error control coding incorporates information into the signal that allows a receiver to find and correct bit error occurring in transmission and storage. Since such coding detects or correct errors incurred in the communication or storage channel, it is often referred to as channel coding

- The error correcting codes that were used are Bose-Chaudhuri Hocquenghem code (BCH) and Hamming code
- The higher the values of N, K and t, the better the performance and in general BCH codes are better than Hamming code.

![[ber calculation.png]]
In this figure the shows a communication system where the **Rayeleigh Fading Channel is Used**
> - $\frac{Eb}{No}$ is varied from $-3 dB$ to $12 dB$

![[ber curve bpsk.png]]
- Blue where no code is used 
- Red is where **BCH**[^1] is used 

[^1]: BCH code, or Bose–Chaudhuri–Hocquenghem code, is a class of cyclic error-correcting codes used in data storage and digital communications.

#### Block Diagram for Simulation of a Communication System without Error Correcting Code. 

![[bpsk and qpsk.png]]

![[BPSK Communication System.canvas|BPSK Communication System]]