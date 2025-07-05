---
id: Interfacing
aliases: 
tags:
  - "#esp32"
  - "#code"
---

# Interfacing

- [[#Sensors]]
- [[#LDR Interfacing]]
- [[#PIR Interfacing]]
- [[#Servo Motor Interfacing]]
- [[#Servo Motor Interfacing 2]]
- [[#Ultrasonic Sensor Interfacing]]
- [[#Light Intensity Sensor]] VEML7700
- [[#SIM800L|SIM800L ,GSM Module]]

## Sensors

### LDR Interfacing

LDR is basicly a photo sensitive resistor , ie it varies resistance according to the available light

- Uses ADC
- Use Voltage Devider

```c
const int LDR_PIN = 36;

void setup() {
   Serial.begin(9600);
   analogReadResolution(10); //default is 12. Can be set between 9-12.
}
void loop() {
   float LDR_Voltage = ((float)LDR_Reading*3.3/1023);
   Serial.print("Reading: ");Serial.print(LDR_Reading); Serial.print("\t");Serial.print("Voltage: ");Serial.println(LDR_Voltage);
}

```

### PIR Interfacing

[Source](https://www.electronicwings.com/esp32/pir-sensor-interfacing-with-esp32)

```c
  Serial.println("Waiting For Power On Warm Up");
  delay(20000); /* Power On Warm Up Delay */
  Serial.println("Ready!");
}
int sensor_output;
void loop() {

  sensor_output = digitalRead(PIR_SENSOR_OUTPUT_PIN);
  Serial.println(sensor_output + "\n");
  delay(100);
  // if( sensor_output == LOW )
  // {
  //   if( warm_up == 1 )
  //    {
  //     Serial.print("Warming Up\n\n");
  //     warm_up = 0;
  //     delay(2000);
  //   }
  //   // Serial.print("No object in sight\n\n");
  //   delay(1000);
  // }
  // else
  // {
  //   // Serial.print("Object detected\n\n");
  //   warm_up = 1;
  //   delay(100);
  // }
}
```

### Servo Motor Interfacing

```c
/*********
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/
  Written by BARRAGAN and modified by Scott Fitzgerald
*********/

#include <Servo.h>

static const int servoPin = 13;

Servo servo1;

void setup() {
  Serial.begin(115200);
  servo1.attach(servoPin);
}

void loop() {
  for(int posDegrees = 0; posDegrees <= 180; posDegrees++) {
    servo1.write(posDegrees);
    Serial.println(posDegrees);
    delay(20);
  }

```

### Servo Motor Interfacing 2

#TestCode
[Source](https://chat.openai.com/)

```c
#include <ESP32Servo.h>

// Define the GPIO pin connected to the servo
const int servoPin = 2;

// Create a Servo object
Servo myservo;

void setup() {
  Serial.begin(9600);

  // Attach the servo to the GPIO pin
  myservo.attach(servoPin);
}

void loop() {
  // Sweep the servo back and forth
  for (int angle = 0; angle <= 180; angle += 1) {
    myservo.write(angle);
    delay(15);
  }
  for (int angle = 180; angle >= 0; angle -= 1) {
    myservo.write(angle);
    delay(15);
  }
}
```

#### Ultrasonic Sensor Interfacing

[Source](https://randomnerdtutorials.com/esp32-hc-sr04-ultrasonic-arduino/)

- $distance\ to\ an\ object = ((speed\ of\ sound\ in\ the\ air)*time)/2$

![|400x300](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2021/06/ESP32-Ultrasonic-Sensor-Wiring-Fritzing-Diagram.png?w=846&quality=100&strip=all&ssl=1)
#exampleCode
[Source](https://randomnerdtutorials.com/esp32-hc-sr04-ultrasonic-arduino/)

```c


const int trigPin = 5;
const int echoPin = 18;

//define sound speed in cm/uS
#define SOUND_SPEED 0.034
#define CM_TO_INCH 0.393701

long duration;
float distanceCm;
float distanceInch;

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  distanceCm = duration * SOUND_SPEED/2;

  // Convert to inches
  distanceInch = distanceCm * CM_TO_INCH;

  // Prints the distance in the Serial Monitor
  Serial.print("Distance (cm): ");
  Serial.println(distanceCm);
  Serial.print("Distance (inch): ");
  Serial.println(distanceInch);

  delay(1000);
}
```

---

#### VEML7700 Light Sensor

> [!blank|right-small]
> ![[veml7700.png]]

- Connect Sensor's VCC to 3.3
- Connect GND
- Connect Sensor's SDA to ESP32's SDA
- Connect Sensor's SCL to ESP32's SCL

**Dimensions**

- 16.6mm x 16.5mm x 4.0mm

#exampleCode

```c
#include <Wire.h>
#include "DFRobot_VEML7700.h"

DFRobot_VEML7700 light_sensor;
float intensity;
void setup() {
  Serial.begin(9600);
  als.begin();
}

void loop() {

  light.getALSLux(intensity);
  Serial.print("Lux: ");
  Serial.print(intensity);
  Serial.println(" lx");
  delay(200);
}

```

### SIM800L

```c
#define BAUD_RATE 9600
#define GSM_TX D5
#define GSM_RX D6
/* Source: https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/
 */

#include <Arduino.h>
#include <SoftwareSerial.h>

// #if defined(ARDUINO)
SoftwareSerial gsmSerial(GSM_TX, GSM_RX); // 3 -> SIM800L Tx & 2 -> SIM800L Rx
// #elif defined(ESP8266)
// SoftwareSerial gsmSerial(D5, D6); // D5 -> SIM800L Tx & D6 -> SIM800L Rx
// #endif

void updateSerial() {
  delay(500);
  while (Serial.available()) {
    gsmSerial.write(
        Serial.read()); // Forward what Serial received to Software Serial Port
  }
  while (gsmSerial.available()) {
    Serial.write(
        gsmSerial
            .read()); // Forward what Software Serial received to Serial Port
  }
}
void setup() {
  Serial.begin(9600);

  // Start GSM Serial
  gsmSerial.begin(9600);

  Serial.println("Initializing...");
  delay(1000);

  gsmSerial.println(
      "AT"); // Once the handshake test is successful, it will back to OK
  updateSerial();

  gsmSerial.println("AT+CMGF=1"); // Configuring TEXT mode
  updateSerial();
  gsmSerial.println(
      "AT+CMGS=\"+917902504188\""); // change ZZ with country code and
                                    // xxxxxxxxxxx with phone number to sms
  updateSerial();
  gsmSerial.print(
      "Last Minute Engineers | lastminuteengineers.com"); // text content
  updateSerial();
  gsmSerial.write(26);
}

void loop() {
  updateSerial();
  delay(1000);
}
```
