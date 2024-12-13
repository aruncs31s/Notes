---
aliases: 
Date: 13-10-2024
---
# Arduino to Arduino I2C Communication
- Uses [[I2C]] to communicate between 2 arduinos 

**Pins Used**:
- `SDA` ,`SCL` ,`GND` -> Common Ground  


**Master Code**:
```c
// Include the required Wire library for I2C<br>
#include <Wire.h> 
uint8_t x = 0;
void setup() {
	Wire.begin();  // Start the I2C Bus as Master
}
void loop() {
	Wire.beginTransmission(9); // transmit to device #9
	Wire.write(x);              // sends x 
	Wire.endTransmission();    
	x++;
	delay(1500);
}
```
**Slave Code**:
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
	Serial.println("New Data Recieved");
	}
void loop() {
	delay(1000);
	}
```
## References
1. https://www.instructables.com/I2C-between-Arduinos/
2. 