---
id: PWM
aliases: []
tags:
  - electronics
  - control_system
Date: 28-12-2024
dg-publish: true
---
# PWM
"**Pulse Width Modulation** (PWM) is a technique of producing varying analog signals from a digital source"^[https://docs.onion.io/omega2-maker-kit/maker-kit-servo-dimming-led.html] . It is basically turning on and of a voltage which simulates different voltage levels withing *0 to Vcc* 

![[pwmduty.excalidraw]]
$$
V_{avg} = D \times V_{in} \tag{1}
$$
Where $D = \large \frac{T_{on}}{T_{on} + T_{off}}$

### Potential Applications 
- LED Brightness controll 
- Servo Motor Control 
