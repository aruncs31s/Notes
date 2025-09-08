---
aliases: 
Date: 29-10-2024
tags:
  - abs_link
---
# Method 1

- **I2C** Master controls the water pump 
- **I2C** Master controls the water values 
- All **I2C** will be on same bus 

So I have to make a communication system using the `i2c` protocol where i have make 
- 1 Arduino as the master where 
	- He controls the **water pump**
	- Master controls the **Water valves**

### Master 
```c
#include <Wire.h>
#include <stdio.h>
#include <stdlib.h>

uint8_t SLAVE_1_ADDR = 0x10;
uint8_t SLAVE_2_ADDR = 0x11;
uint8_t SLAVE_3_ADDR = 0x12;
#define MESSAGE_SIZE 3
#define MoistureThreshold 500  

int _index=0;

int float_valueFromOne,float_valueFromTwo,float_valueFromThree;

float get_data(uint8_t _addr){
  char _message[MESSAGE_SIZE];
  Wire.requestFrom(_addr,MESSAGE_SIZE);
  _index  = 0; 
  while (Wire.available()){
    _message[_index] = Wire.read();
    ++_index;
 } 
   return atoi(_message);
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
  //Serial.println("Value From Two: " + String(float_valueFromTwo));
  //Serial.println("Value From Three: " + String(float_valueFromThree));
  delay(1000);
}
```

### Slave Code 
#### Version 1 
```c
// Slave 1 Just Communication
#include <Wire.h>
uint8_t myAddress = 0x10;
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


```c
// Slave 1
#include <Wire.h>
int val = 0; 
int soilPin = A0;
int soilPower = 7; // for sensor power to prevent corrosion of the sensor 

uint8_t myAddress = 0x10;

void setup() {
  	Serial.begin(9600);
 	Wire.begin(myAddress);
	Wire.onRequest(requestThen);
  	pinMode(soilPower, OUTPUT);
	digitalWrite(soilPower, LOW);
}
void requestThen(){
  
	Wire.write(val);
}
void loop(){
  	Serial.print("Soil Moisture = ");    
	delay(1000);//take a reading every second
	digitalWrite(soilPower, HIGH);// turn on the sensor
	delay(10);
	val = analogRead(soilPin); 
	digitalWrite(soilPower, LOW);//turn off the sensor
	Serial.println(val);
	delay(100);
}


```

```c
#include <Wire.h>
#include <stdio.h>
#include <stdlib.h>

uint8_t SLAVE_1_ADDR = 0x10;
uint8_t SLAVE_2_ADDR = 0x11;
uint16_t new_val = 0;
uint8_t SLAVE_3_ADDR = 0x12;
#define MESSAGE_SIZE 4
#define MoistureThreshold 500  

int _index=0;

int float_valueFromOne,float_valueFromTwo,float_valueFromThree;

float get_data(uint8_t _addr){
  char _message[MESSAGE_SIZE];
  Wire.requestFrom(_addr,MESSAGE_SIZE);
  _index  = 0; 
  while (Wire.available()){
    new_val = Wire.read();
 //   _message[_index] = Wire.read();
 //   ++_index;
 } 
   return atoi(_message);
}
void setup() {
  Serial.begin(9600);
  Wire.begin(); 
}

void loop() {
  
  float_valueFromOne = get_data(SLAVE_1_ADDR);
  float_valueFromTwo = get_data(SLAVE_2_ADDR);
  float_valueFromThree = get_data(SLAVE_3_ADDR);
  
  Serial.println("Value From One: " + String(new_val));
  //Serial.println("Value From Two: " + String(float_valueFromTwo));
  //Serial.println("Value From Three: " + String(float_valueFromThree));
  delay(1000);
}

```