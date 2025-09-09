---
id: Thinkspeak
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - energy_monitoring
dg-publish: true
---
# Thinkspeak

Created : 2024-05-04 02:13

## Contents

-

#### Config

1. Needed Libraries

```cpp
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ThingSpeak.h>

```

2. Connect to a wifi

```cpp
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* server = "api.thingspeak.com";
const char* apiKey = "YOUR_THINGSPEAK_API_KEY";
WiFiClient client;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  ThingSpeak.begin(client);
}

```

3. Send data to thinkspeak

```cpp
void loop() {
  float sensorValue = analogRead(A0);

  ThingSpeak.setField(1, sensorValue);

  int httpCode = ThingSpeak.writeFields(CHANNEL_ID, apiKey);

  if (httpCode == 200) {
    Serial.println("Sensor data sent to ThingSpeak!");
  } else {
    Serial.println("Error sending sensor data to ThingSpeak.");
  }

  delay(10000);
}

```

## References

1. [DevCodef1](https://devcodef1.com/news/1027971/send-sensor-data-to-thingspeak-using-nodemcu-esp8266-and-arduino-uno#:~:text=Now%20that%20we%20have%20set%20up%20the%20hardware%2C,Upload%20the%20following%20code%20to%20the%20NodeMCU%20ESP8266%3A)
