---
id: Coding
aliases: []
tags: []
---

## Install the Libs

```bash
pip install ultralytics

```

_note that after some time i have to reinstall ultralytics_

## Pi to ESP i2c 


```c
// source : https://dronebotworkshop.com/i2c-arduino-raspberry-pi/ 
const int ledPin = 13; 
 
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  
  // Setup pin 13 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
void loop() {
  delay(100);
}
```