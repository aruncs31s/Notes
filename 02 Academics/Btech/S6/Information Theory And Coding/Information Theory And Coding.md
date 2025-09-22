---
id: Information_Theory_And_Coding
aliases: {Itc}
tags:
  - academics
  - btech
  - s6
  - information_theory_and_coding
ExamDate: 2024-12-31
dg-publish: true
---
# Information theory and Coding

## Contents

- [[Old_NOTES/Academics/Btech/S6/Information Theory And Coding/Module 1|Module 1]]
- [[01 Academics/Btech/S6/Information Theory And Coding/Module 2|Module 2]]
- [[02 Academics/Btech/S6/Information Theory And Coding/Module 5]]
- [[PYQ]]
- Shannon Limit

#### Shannon Limit
[https://www.gaussianwaves.com/2008/04/channel-capacity/](https://www.gaussianwaves.com/2008/04/channel-capacity/)

> [!Defenition] Defenition
1>
Given a channel with particular bandwidth and noise characteristics, Shannon showed how to calculate the maximum rate at which data can be sent over it with zero error. He called that rate the channel capacity, but today, it’s just as often called the Shannon limit.  
> - So the ideal code would minimize the number of extra bits while maximizing the chance of correcting  
> - But Shannon knew that better error-correcting codes were possible. In fact, he was able to prove that for any communications channel, there must be an error-correcting code that enables transmissions to approach the Shannon limit.  
> - Consider the case in which the channel is noisy enough that a four-bit message requires an eight-bit code. The receiver, like the sender, would have a codebook that correlates the 16 possible four-bit messages with 16 eight-bit codes. Since there are 256 possible sequences of eight bits, there are at least 240 that don’t appear in the codebook. If the receiver receives one of those 240 sequences, she knows that an error has crept into the data. But of the 16 permitted codes, there’s likely to be only one that best fits the received sequence — that differs, say, by only a digit
