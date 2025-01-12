---
dg-publish: true
aliases: 
Date: 29-10-2024
tags:
  - abs_link
---
# Question 3
Construct a system for below home garden.
![[Pasted image 20241014001145.png]] 
- **I2C Master** side controls the **water pump and water valves**. ^8c7ea1
- All I2C slaves are on **same bus**, collects Moisture data individually.
- I2C master collects Moisture data every 5 seconds and runs the motor for 2 seconds if moisture level is low, enabling the required valve only. ^7c2864
>Water Pump- 28VDC, 500mA
>Water Valve- 12VDC, 300mA (Normally closed.)
## Answers 
- [[Method 1]]

#### Code
```c
int val = 0; 
int soilPin = A0;
int soilPower = 7; // for sensor power to prevent corrosion of the sensor 

void setup(){
	Serial.begin(9600); 
	pinMode(soilPower, OUTPUT);
	digitalWrite(soilPower, LOW);
}

void loop(){
	Serial.print("Soil Moisture = ");    
	delay(1000);//take a reading every second
	digitalWrite(soilPower, HIGH);// turn on the sensor
	delay(10);
	val = analogRead(soilPin); 
	digitalWrite(soi lPower, LOW);//turn off the sensor
	Serial.print(val);
}
```


### Ans
#### Requirements
- **I2C** Master controls the water pump 
- **I2C** Master controls the water values 
- All **I2C** will be on same bus 


>Water Pump- 28VDC, 500mA
>Water Valve- 12VDC, 300mA (Normally closed.)

1. Water Pump
$$
\begin{align}
V &= 28 \\
i & = .5 A \\
\therefore R &= 56 \ohm
\end{align}
$$
2. Water Valve 
$$
\begin{align}
V &= 12 V \\
i &= 300 mA = .3 A \\
R &= 40 \ohm   \\
\end{align}
$$

### Method 1
So i have to make the **I2C as master** using 

##### Receiver Code
Initial Codes
1. Just read 
```c
// Receiver Code
#incude <Wire.h>
int x = 0;

void setup(){
	Serial.begin(9600); 
	Wire.begin();
}
void loop() {
	Wire.requestFrom(8, 6);    // request 6 bytes from peripheral device #8
	while (Wire.available()) { 
		char c = Wire.read(); // receive a byte as character
		Serial.print(c);         // print the character
		}
	delay(500);
}
```

2. Multi slave 
```c
#include <Wire.h>
#include <stdio.h>
#include <stdlib.h>

uint8_t SLAVE_1_ADDR = 0x10;
uint8_t SLAVE_2_ADDR = 0x11;
uint8_t SLAVE_3_ADDR = 0x12;
#define MESSAGE_SIZE 5
int _index=0;

float float_valueFromOne,float_valueFromTwo,float_valueFromThree;

float get_data(uint8_t _addr){
  char _message[MESSAGE_SIZE];
  Wire.requestFrom(_addr,MESSAGE_SIZE);
  _index  = 0; 
  while (Wire.available()){
    _message[_index] = Wire.read();
    ++_index;
 } 
   return atof(_message);
}
void setup() {
  Serial.begin(9600);
  Wire.begin(); 
}

void loop() {
  float_valueFromOne = get_data(SLAVE_1_ADDR);
  float_valueFromTwo = get_data(SLAVE_2_ADDR);
  float_valueFromThree = get_data(SLAVE_3_ADDR);
  
  Serial.println("Value From One: " + String(float_valueFromOne));
  Serial.println("Value From Two: " + String(float_valueFromTwo));
  Serial.println("Value From Three: " + String(float_valueFromThree));
  delay(1000);
}
```

##### Sender  Code 
1. Single Slave 
```c
// Sender Code

#include <Wire.h>
void setup() {
	Wire.begin(8); // join i2c address 8 i think it must be uniqe to every device
	Wire.onRequest(requestEvent);
}
void loop() {
	delay(100);
}
void requestEvent() {
	Wire.write("10"); // respond with message of 6 bytes
  // as expected by master
}
```

2. Multi slave 
```c
// Slave 1
#include <Wire.h>
uint8_t myAddress = 0x10;
void setup() {
 	Wire.begin(myAddress);
	Wire.onRequest(requestThen);
}
void requestThen(){
	Wire.write("543.2");
}
void loop(){
	delay(100);
}
```

```c
// Slave 2
#include <Wire.h>
uint8_t myAddress = 0x11;
void setup() {
 	Wire.begin(myAddress);
	Wire.onRequest(requestThen);
}
void requestThen(){
	Wire.write("555.5");
}
void loop(){
	delay(100);
}
```

```c
// Slave 1
#include <Wire.h>
uint8_t myAddress = 0x12;
void setup() {
 	Wire.begin(myAddress);
	Wire.onRequest(requestThen);
}
void requestThen(){
	Wire.write("444.4");
}
void loop(){
	delay(100);
}
```
### Stes
1. [ ] created a program that communicates with multiple slaves ⏫ 
2. [ ] Now interface the moisture sensor 
3. [ ] Share the moisture value with the Master and let the master decide 

### Ans 
