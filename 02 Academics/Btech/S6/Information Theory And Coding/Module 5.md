---
id: Module_5
aliases: []
tags:
  - academics
  - btech
  - s6
  - information_theory_and_coding
Date: 29-12-2024
dg-publish: true
---
# Module 5
- [ ] Convolutional Code 

## Convolutional Codes 
- Depends on instananious input and previous info 
- The encoder has  memory 
- (n,k,m) -> (n input ,  k output, m memory)
- $Rate = \frac{k}{n}$ 
- The encoder will have **n number of adders** and **m number of memory registers**a
- **Output is obtained by** $\text{message } \oplus \text{impulse response of the encoder}$^[The output is obtained by convoluting the message with the impulse response of the encoder]
