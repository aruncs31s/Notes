---
id: Method_2
aliases: []
tags:
  - hackethons
  - dihack
  - round_1
Date: 16-10-2024
markmap: 
screenshotTextColor: #28F48D
highlight: true
titleAsRootNode: true
dg-publish: true
---
# Method 2
So in our system the [[HC-SR04]] gives a $1.74 \text{ ms}$ pulse or continues pulse if the `triger` signal is continuesly applied 
- [[HC-SR04]] gives $1.74  ms$ signal when the distance between object and the sensor is $30 cm$
- So We the we need to use anything? that senses this pulse and respond to it 
- And Turn the motor for $5s$

## Steps 
- Provide pulse for `trigger` in [[HC-SR04]]
- Detect the output pulse from `echo`
- when the desired signal is coming from the `echo` trigger the `monostable multi-vibrator`

### Trigger Generator
#### Requirements 
**More than** $10\mu s$ $T_{on}$
#### Design
### Pulse Detection

### Monostable Multi-Vibrator
