# Using ESP32
```c
// Pin definitions under ESP32
#define IN1 27
#define IN2 26
#define IN3 25
#define IN4 33
#define ULTRASONIC_PIN 18
#define LEFT_IR_PIN 34
#define RIGHT_IR_PIN 35
#define PWM_PIN 14
#define LANE_DETECT_LED_PIN 12
#define EMERGENCY_STOP_LED_PIN 13
```
![[Drawing 2025-03-26 09.59.02.excalidraw|800x500]]


```mermaid
graph TB
c1-->a2 
subgraph "Lane Detection"
A1[-->a2 
end 
subgraph two 
b1-->b2 
end 
subgraph three 
c1-->c2 
end

```