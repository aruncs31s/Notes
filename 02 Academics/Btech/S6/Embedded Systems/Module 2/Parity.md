---
id: Parity
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_2
Date: 04-01-25
dg-publish: true
---
# Parity
Parity bits redendant  bits that are added to the data while transmission or storage.
They are used in [[Serial Communication]] protocolls like [[08 Electronics/Embedded Systems/communication/UART|UART]] 
## **Odd Parity**
The total number of 1's in the code , including parity bit should be odd  

```

|<-Data Bits->|
|1|0|1|1|0|0|1|1|
              ^
              |
         Parity Bit

```

Here if we consider only the databits the total number of 1's is 4 , and if we are using the odd parity then the total number of 1's should be odd so `parity bit =1` making the total number of ones as **odd** 

```

|<-Data Bits->|
|1|1|0|1|0|1|1|0|
              ^
              |
         Parity Bit

```

Here the total number of 1's in the data is odd so the **parity bit** is **0**

## **Even Parity**
The total number of 1's in the code including the parity bit should be even 
