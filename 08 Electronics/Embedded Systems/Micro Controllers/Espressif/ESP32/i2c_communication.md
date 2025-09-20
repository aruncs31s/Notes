---
id: i2c_communication
aliases: []
tags:
  - electronics
  - embedded_systems
  - micro_controllers
  - espressif
  - esp32
dg-publish: true
---
# I2C Communication

_Inter Integrated Circuit(I2C) ( I-squared-C), and it is a synchronous, multi-master, multi-slave communication protocol_

- **Multiple Slave Devices** can be connected to a single line

> [!NOTE] Pull Up Resistors
> When using I2C both the `SDA` and `SCL` must be connected to the VCC using 2.4k$\ohm$ `pull up` resistors
> $4.7k\ohm$ for $5V$ devices and $2.4k\ohm$ for $3.3V$ devices.

#### Specs

- Standard mode (100 Kbit/s)
- Fast mode (400 Kbit/s)
- Up to 5 MHz, yet constrained by SDA pull-up strength
- 7-bit/10-bit addressing mode
- Dual addressing mode.

### Programming

> Commonly used `I2C` pins are `GPIO21`-> `SDA` and `GPIO22` -> `SCL`

#### Find The address

[Source](https://randomnerdtutorials.com/esp32-i2c-communication-arduino-ide/)

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(9600);
  Serial.println("\nI2C Scanner");
}

void loop() {
  byte error, address;
  int nDevices;
  Serial.println("Scanning...");
  nDevices = 0;
  for(address = 1; address < 127; address++ ) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address<16) {
        Serial.print("0");
      }
      Serial.println(address,HEX);
      nDevices++;
    }
    else if (error==4) {
      Serial.print("Unknow error at address 0x");
      if (address<16) {
        Serial.print("0");
      }
      Serial.println(address,HEX);
    }
  }
  if (nDevices == 0) {
    Serial.println("No I2C devices found\n");
  }
  else {
    Serial.println("done\n");
  }
  delay(5000);
}

```

#### Using Different Pins

Almost any pin can be used for `I2C` in eps32

1. Include `Wire.h`
2. Pass desired pins to `begin()` method in the `Wire.h` header

```cpp
Wire.begin(SDA_PIN, SCL_PIN);

```

## Resources

1. https://randomnerdtutorials.com/esp32-i2c-communication-arduino-ide/
