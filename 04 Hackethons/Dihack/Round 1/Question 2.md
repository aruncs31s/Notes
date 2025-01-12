---
dg-publish: true
---

# Question 2 

^e20f4d

You are given two Arduino boards (Arduino A and Arduino B) that are communicating with each other using the [[I2C]] protocol. **Arduino A is acting as the master**, and **B acting as a I2C slave**. ^423454
- Your task is to introduce a third Arduino (Arduino C) to intercept the I2C communication between Arduino A and Arduino B.  ^5f61b8
- Arduino C should listen to the communication without disrupting the original data exchange, capture the messages being transmitted by Arduino A & B, and print the intercepted messages to the serial monitor of Arduino C. ^e44026

### Ans:
![[Arduino intercept I2C.excalidraw]]
#### **Master Code (Arduino A)**:
```c
// Master Code 
// Github  : https://github.com/aruncs31s/
// Date : 2024-10-13
// Time : 20:25
#include <Wire.h> 

uint8_t x = 0;
void setup() {
	Wire.begin();  // Start  I2C Bus as Master
}
void loop() {
	Wire.beginTransmission(10); // transmit to device 10
	// Above address can be used to intercept or the intercepter have to scan the entire address to get 
	Wire.write(x);              // sends x 
	Wire.endTransmission();    
	x=  random(0, 255);;
	delay(1000);
}
```

#### **Slave Code (Arduino B)**
```c
// Slave Code 
// Date : 2024-10-13 
#include <Wire.h>
uint8_t new_data = 0;
void setup() {
	Serial.begin(9600);   
	Wire.begin(10); // Slave address 10
	Wire.onReceive(receiveCallback); // Callback Function when data is recieved
	}
void receiveCallback(int bytes){
	new_data = Wire.read();  
	Serial.println("New Data Recieved " + String(new_data));
	}
void loop() {
	delay(1000);
}
```


#### **Intercepter Code (Arduino C)**:
```c
// Intercepted Code
// Date : 2024-10-13
#include <Wire.h>
int intercepted_data = 0;
uint8_t target_address = 0;
void receiveCallback(int bytes){
	intercepted_data = Wire.read();  
	Serial.println("Intercepted Data = " + String(intercepted_data));
	}
void scan_for_i2c() {
  for (;;) {
    Wire.begin(target_address);
    Serial.println("Tryingt address " + String(target_address));
    delay(5000);
    Serial.println("Intercepted Data = " + String(intercepted_data));
    if (intercepted_data > 0) {
      return;
    }
    Wire.end();
    target_address++;
  }
}
void setup() {
    Serial.begin(9600);
    Wire.onReceive(receiveCallback); // Callback Function when data is recieved
    scan_for_i2c();                  // Scan for I2C device
  }


void loop() { 
	delay(1000);
 }
```




## References

1. https://docs.arduino.cc/learn/communication/wire/