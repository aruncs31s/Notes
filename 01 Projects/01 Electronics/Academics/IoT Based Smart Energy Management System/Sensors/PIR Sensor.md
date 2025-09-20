---
id: PIR_Sensor
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - sensors
dg-publish: true
---
[Source](https://www.electronicwings.com/esp32/pir-sensor-interfacing-with-esp32)
- [Introduction]()
- [Interfacing]()
- [Circuit Diagram]()

#### Introduction
- PIR (Passive Infrared) sensor is a type of electronic sensor used to detect the presence of living beings by measuring changes in the infrared (IR) radiation in the environment. 
- It works by detecting the heat emitted by objects, which is a form of infrared radiation. 
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcqN5CSX5EZQ6oroMNjNpOaExNNKFmg1StFqOIzUxds6b7sjunsLurrNu0lHPwhMZSTos&usqp=CAU">
#### Specs
- Operating Voltage `5V – 12V`
- Output Signal Voltage `3.3V`

##### Operating Modes
1. **Single Trigger Mode**: The constant motion will cause a single trigger.
2. **Multiple Trigger Mode**: The constant motion will cause a series of triggers.

#### Interfacing
[Credit](https://www.electronicwings.com/esp32/pir-sensor-interfacing-with-esp32)

![image|400x300](https://www.electronicwings.com/storage/PlatformSection/TopicContent/444/description/PIR%20Sensor%20Interfacing%20with%20ESP32.jpg)

*Note*
- Keep Far form WiFi Antenna [why](https://www.electronicwings.com/esp32/pir-sensor-interfacing-with-esp32)

##### Code
[Credit](https://www.electronicwings.com/esp32/pir-sensor-interfacing-with-esp32)

```c
const int PIR_SENSOR_OUTPUT_PIN = 13;  /* PIR sensor O/P pin */
int warm_up;

void setup() {
  pinMode(PIR_SENSOR_OUTPUT_PIN, INPUT);
  Serial.begin(115200); /* Define baud rate for serial communication */
  Serial.println("Waiting For Power On Warm Up");
  delay(20000); /* Power On Warm Up Delay */
  Serial.println("Ready!");
}

void loop() {
  int sensor_output;
  sensor_output = digitalRead(PIR_SENSOR_OUTPUT_PIN);
  if( sensor_output == LOW )
  {
    if( warm_up == 1 )
     {
      Serial.print("Warming Up\n\n");
      warm_up = 0;
      delay(2000);
    }
    Serial.print("No object in sight\n\n");
    delay(1000);
  }
  else
  {
    Serial.print("Object detected\n\n");   
    warm_up = 1;
    delay(1000);
  } 
}

```
