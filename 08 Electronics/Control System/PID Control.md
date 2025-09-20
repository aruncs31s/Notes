---
id: PID_Control
aliases: []
tags:
  - electronics
  - control_system
cssclasses: 
Date: 2024-12-10
dg-publish: true
---
# PID Control 

*Proportional Integral Derivative(PID) Controller is a [[Feedback]] based control mechanism*

>[!blank|right-medium]
>![pid1.png](pid1.png)

$$

\begin{aligned}
    e(t) &= r(t) - y(t) \\
    u(t) &= K_p e(t) + K_i \int e(t) dt + K_d \frac{d e(t)}{dt}
\end{aligned}
$$
- *where $r(t)$ is the desired output*
- *and $y(t)$ is the actual output*
- *$e(t)$ is the error signal*

In **PID** control 

1. When i increase the **proportional** constant/gain the system is more aggressive and leads to unstable state where the output never becomes stable which is called **Overshoot
2. When i increase the **integral** part ?
3. When i increase the **differential** part?

## Working

The PID controller automatically compares the desired target value (**setpoint or SP**) with the actual value of the system (**process variable or PV**). The difference between these two values is called the error value, denoted as $e(t)$[^1]

[^1]:https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller

#### Proportional Control
>[!blank|right-medium]
>![](proportional%20Control.excalidraw.md)
![[proportional.excalidraw]]

In **Proportional Control** the control signal will rise to its maximum when an error has been occurred and try to compensate it . This is a continues process where error checking always happen and in some situations the control signal wont be able to correct the output 

![[ball experiment.excalidraw]]

> In the example of balancing the ball it is observed that 
> 1. When the $Kp$ is too high the ball moves too fast and faild to keep it center 
  
## Source 
Image : https://en.wikipedia.org/wiki/File:PID_en.svg

