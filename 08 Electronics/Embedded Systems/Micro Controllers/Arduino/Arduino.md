---
id: Arduino
aliases: []
tags:
  - electronics
  - embedded_systems
  - micro_controllers
  - arduino
Created: "13-08-2024"
cssclasses: 
dg-publish: true
---
### Arduino

- [[#Interfacing]]

### Pinout

![|600x350](https://robu.in/wp-content/uploads/2020/07/1-3.jpg)

#### Button Interfacing

```c
const int button_1 = 2;
bool button_1_state = false;
void setup() {
  Serial.begin(9600);
  pinMode(button_1, INPUT);
}
void loop() {
  button_1_state = digitalRead(button_1);
  if (button_1_state == true) {
    Serial.println("ON");
  } else {
    Serial.println("OFF");
  }
  delay(400);
}

```

## Arduino to Arduino I2C Communication

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
