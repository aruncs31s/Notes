---
id: Radar_Sensor
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - sensors
dg-publish: true
---
# RCWL-0516 Radar Sensor
### Introduction
- The [PIR sensor](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/) , because they only detect movement from living things, they will generate fewer false alarms.
- The RCWL-0516 microwave sensor detects any movement from any object and does not rely on heat signatures, making it more reliable in hot environments where a PIR sensor may not be as effective
- It can also be used to detect Static Human Presence

### Specifications
1. Operating Voltage         `4-28V (typically 5V)`
2. Detection Distance       `5-9 meters`
3. Maximum Current Draw            `~ 3mA`
4. Operating Frequency  `` ~3.2GHz`
5. Transmission Power   `30mW (max.)`
6. Output Timing                `~ 2s`
7. Regulated Output         `3.3V, 100mA`

### Pin Diagram
![](https://www.electronicwings.com/storage/PlatformSection/TopicContent/497/description/RCWL-0516%20Pin%20Diagram.jpg)

1. **VIN**: is the power supply for the sensor. You can connect an input voltage anywhere between 4 to 28V to this pin, although 5V is commonly used.
2. **GND**: is the ground pin.
3. **3.3V**: This is the regulated output pin of 3.3V/100mA
4. **OUT**: This is the 3.3V TTL logic output. It goes HIGH for two seconds when motion is detected and goes LOW when idle (no motion detected).
5. **CDS**: CDS is a cadmium sulfide pin where we can connect the LDR to allow the RCWL-0516 to operate only in the dark.

### Working

The RCWL-0516 module employs ==“Doppler Radar”== – a specialized radar that makes use of the **Doppler Effect** (also known as **Doppler shift**) to detect motion and trigger proximity alerts.
- [Doppler Effect](Physics.md#Doppler%20Effect)

> [!NOTE] Doppler Effect
>  The change in frequency observed by a stationary observer when the source of the frequency is moving. This holds true for all sorts of waves, such as water, light, radio, and sound
> Contents

#### Interfacing
#TestCode 

```cpp
int sensorPin = 18;
int motionState = LOW;
 
void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
}
 
void loop() {
  if (digitalRead(sensorPin) == HIGH) {
    if (motionState == LOW) {
     Serial.println("Motion detected!");
      motionState = HIGH;
    }
  }
 
  else {   
    if (motionState == HIGH) {
     Serial.println("Motion ended!");
      motionState = LOW;
    }
  }
}

```

- From [[#References| 1]]

## References
1. https://www.electronicwings.com/esp32/rcwl-0516-microwave-radar-sensor-interface-with-esp32
2. 