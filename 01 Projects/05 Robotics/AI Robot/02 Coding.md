---
id: 02_Coding
aliases: []
tags:
  - projects
  - robotics
  - ai_robot
Date: 13-11-2024
dg-publish: true
---
# Coding 
- [[replay tester]]

```tasks
not done
path includes 02 Coding.md 

```

## Libs
>```dataview
>TABLE function as "Functions " , args as "Arguments"
>from #c_lib and #ai_robot 
>```

- [[robo.h]]
- [[robot-database.h]]
- 

## Program Flow 
Here is a quick program functional flow , from the microcontroller perspective 
1. Initializes the wifi 
2. Initializes the Servo Motors to previous position 
3. Check if they are in their initial positions ?
	 - Servo motors does not support checking of angle. So im gonna use a server for that.

```mermaid
graph TB
A[Initializes the Wifi] & AA[Initializes the Server Endpoints] --> Main_Thread
B[Retrive Data from the Server] --> C
C[Servo Object] --> Main_Thread 
D[API End Points] --> Main_Thread
 ```

- [ ] Complete the below 📅 2025-05-24 

```mermaid
sequenceDiagram
	 participant PCA9685 
	participant ESP32 
	participant Flask API
	participant SQLite DB
	
	%% ESP32 
	ESP32 -->> ESP32: Initialize -> Boot,WiFi STA ..
	ESP32->>PCA9685: Initialize I2C (i2c_addr)
	%% GET Request
	ESP32->>Flask API: GET /robots?id=$id
	Flask API->>SQLite DB: Query all robots
	SQLite DB-->>Flask API: Return robots data
	Flask API-->>ESP32: JSON response with robots
	
	%% POST Request
	ESP32 ->>Flask API: POST /robots {name, type}
	Flask API->>SQLite DB: Insert new robot
	SQLite DB-->>Flask API: Confirm insertion
	Flask API-->>ESP32: JSON response (201 Created)

```

There are 3 main Hardware componets that will effect the programming 
1. [[PCA9685]] -> For Driving the motor 
2. [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/ESP32|ESP32]] -> Main Controller 
3. [[Raspberry Pi]] -> For hosting the server 

## PCA9685 
![[PCA9685#^914de3]]
This is the PCA9685  driver #sampleCode  , here is its order 
1. Create `driver_object` 
	- **param:** `i2c_addr`
>
>```cpp
>Adafruit_PWMServoDriver board1 = Adafruit_PWMServoDriver(0x40); 
>```

>
>```cpp
>// Adafruit_PWMServoDriver.cpp
>Adafruit_PWMServoDriver();
>Adafruit_PWMServoDriver(const uint8_t addr);
>Adafruit_PWMServoDriver(const uint8_t addr, TwoWire &i2c);
>```

>There are 3 defenitions 
>
>```cpp
>	Adafruit_PWMServoDriver::Adafruit_PWMServoDriver(const uint8_t addr)
>	: _i2caddr(addr), _i2c(&Wire) {}
>	/*!
>	 *  @brief  Instantiates a new PCA9685 PWM driver chip with the I2C address on a
>	 * TwoWire interface
>	 *  @param  addr The 7-bit I2C address to locate this chip, default is 0x40
>	 *  @param  i2c  A reference to a 'TwoWire' object that we'll use to communicate
>```

>
2. Initialize the board 
- [ ] Complete these steps 📅 2025-05-24  

## Servo 
There is mainly x things
### 1. Servo Properties 

>[!blank]
>
>> [!blank|left-small]
>>
>>```cpp
>>#define SERVO_ANGLE_MIN 0
>>#define SERVO_ANGLE_MAX 180
>>#define SERVO_MIN  102   // .5ms
>>#define SERVO_MAX  512   // 2.5ms 
>>#define SERVO_FREQ 50
>>#define CONTROLLER_I2C_ADDR 0x41
>>```

>
>>[!Abstract]- Why 
>>
>>We already know to the ideal values of all the features of [[MG995|Servo]], but those are ideal values and , we need to find out the actual value of those , for example some servos can't do full 180. 
>>These are the ideal charaterestics
>>![[MG995#^90bc64]]
>>But we have to make sure it our self . 
>

^69745d

^15f658
## Database 

## Movements
 

# Software
Going to use [[platformio]] for development and [[C++|cpp]] as the programming language , [[vscode]] as the editor(ide). 

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