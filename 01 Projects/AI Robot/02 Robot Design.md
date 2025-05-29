---
aliases: 
Date: 13-11-2024
---
# Robot Design 
# Software
Going to use [[platformio]] for development and [[C++|cpp]] as the programming language , [[vscode]] as the editor(ide). 

## Program Flow 
Here is a quick program functional flow , from the microcontroller perspective 
1. Initializes the wifi 
2. Initializes the Servo Motors
3. Check if they are in their initial positions ?
	 - Servo motors does not support checking of angle. So im gonna use a server for that.
```mermaid
graph TB
A[Initializes the Wifi] & AA[Initializes the Server Endpoints] --> Main_Thread
B[Retrive Data from the Server] --> C
C[Servo Object] --> Main_Thread 
D[API End Points] --> Main_Thread
 ```


```cpp
Adafruit_PWMServoDriver board1 = Adafruit_PWMServoDriver(CONTROLLER_I2C_ADDR);      
```

```cpp
Robo la1(PIN_LA1, board1);
Robo la2(PIN_LA2, board1);
Robo la3(PIN_LA3, board1);
Robo ra1(PIN_RA1, board1);
Robo ra2(PIN_RA2, board1);
Robo ra3(PIN_RA3, board1);
Robo lh(PIN_LH, board1);
Robo rh(PIN_RH, board1);
Robo ll1(PIN_LL1, board1);
Robo ll2(PIN_LL2, board1);
Robo ll3(PIN_LL3, board1);
Robo rl1(PIN_RL1, board1);
Robo rl2(PIN_RL2, board1);
Robo rl3(PIN_RL3, board1);
Robo lf(PIN_LF, board1);
Robo rf(PIN_RF, board1);
```