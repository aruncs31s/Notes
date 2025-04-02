---
aliases: 
Date: "16-03-25"
---
# BER Calculation
First we have to compare 2 streams inorder to calculate the [[BER vs SNR]] , But we can use the feature of tagged stream inorder to calculate the error . 

Frequency Xlating FIR Filter

Form tutorial 
![[Pasted image 20250402121745.png]]

#### New Method 
1. Attach a lengthy preamble like "111111111111111111" with a 0 last indicating the start of transmission
2. transmit exactly 1000 bits 
3. compare transmitted(source) and received(after removing preample)