---
id: Wire
aliases: []
tags:
  - coding
  - arduino
Date: 18-10-2024
dg-publish: true
---
# Wire
Arduino **Wire** Uses the [[08 Electronics/Embedded Systems/communication/I2C|I2C]] Protocol for Communication
- Easy to send binary data as well as text
- It always listen for new data and uses [[Interrupts]]
- 
## Different Modes 
1. Arduino to Arduino Master - Slave 
*This role can be reversed*

```c
// Master Code 
#include <Wire.h>
int SLAVE_ADDR = 50;
char c;
void setup() {
  Serial.begin(9600);
  Wire.begin(); 
}
void loop() {
  Wire.requestFrom(SLAVE_ADDR,1);
  while (Wire.available()){
    c = Wire.read();
}
  Serial.println(c);
  delay(500);
}

```

```c
// Slave Code 
#include <Wire.h>
uint8_t new_data = 0;
void setup() {
	Serial.begin(9600);
 	Wire.begin(50);
	Wire.onRequest(requestThen);
}
void requestThen(){
  Wire.write("V");
}
void loop(){
  delay(1000);
}

```

