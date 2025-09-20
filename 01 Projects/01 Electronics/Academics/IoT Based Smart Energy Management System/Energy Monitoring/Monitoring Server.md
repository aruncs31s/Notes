---
id: Monitoring Server
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - energy_monitoring
dg-publish: true
---
# Monitoring Server

## Contents

- [[Projects/Iot_based_smart_energy_management_system/Energy Monitoring/Monitoring Website]]
- [[Projects/Iot_based_smart_energy_management_system/Energy Monitoring/Thinkspeak]]

## Thinkspeak

- [Source](https://randomnerdtutorials.com/esp32-thingspeak-publish-arduino/)
- [Source 2]()
  #Requirements

1. [[Projects/Iot_based_smart_energy_management_system/Obsidian_Notes/ESP32/esp32|esp32]]

`ThingSpeak` allows you to publish your sensor readings to their website and plot them in charts with timestamps.

#### Setup

> 1.  Installing the ThingSpeak Library
> 2.  [Go to ThingSpeak](https://thingspeak.com/) an click the “**Get Started For Free**” button to create a new account. This account is linked to a Mathworks account. So, if you already have a Mathworks account, you should log in with that account
> 3.  Creating New Channel

    1. After your account is ready, sign in, open the “**Channels**” tab and select “**My Channels**“.
    2. Type a name for your channel and add a description. In this example, we’ll just publish temperature. If you want to publish multiple readings (like humidity and pressure), you can enable more fields later

> 4.  Customizing Chart

    - The chart can be customized, go to your **Private View** tab and click on the edit icon.

> 5.  API Key
> 6.  To send values from the ESP32 to ThingSpeak, you need the Write API Key. Open the “**API Keys**” and copy the key

#exampleCode

```c

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/

#include <WiFi.h>
#include "ThingSpeak.h"
#include <Adafruit_BME280.h>
#include <Adafruit_Sensor.h>

const char* ssid = "REPLACE_WITH_YOUR_SSID";   // your network SSID (name)
const char* password = "REPLACE_WITH_YOUR_PASSWORD";   // your network password

WiFiClient  client;

unsigned long myChannelNumber = X;
const char * myWriteAPIKey = "XXXXXXXXXXXXXXXX";

// Timer variables
unsigned long lastTime = 0;
unsigned long timerDelay = 30000;

// Variable to hold temperature readings
float temperatureC;
//uncomment if you want to get temperature in Fahrenheit
//float temperatureF;

// Create a sensor object
Adafruit_BME280 bme; //BME280 connect to ESP32 I2C (GPIO 21 = SDA, GPIO 22 = SCL)

void initBME(){
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void setup() {
  Serial.begin(115200);  //Initialize serial
  initBME();

  WiFi.mode(WIFI_STA);

  ThingSpeak.begin(client);  // Initialize ThingSpeak
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {

    // Connect or reconnect to WiFi
    if(WiFi.status() != WL_CONNECTED){
      Serial.print("Attempting to connect");
      while(WiFi.status() != WL_CONNECTED){
        WiFi.begin(ssid, password);
        delay(5000);
      }
      Serial.println("\nConnected.");
    }

    // Get a new temperature reading
    temperatureC = bme.readTemperature();
    Serial.print("Temperature (ºC): ");
    Serial.println(temperatureC);

    //uncomment if you want to get temperature in Fahrenheit
    /*temperatureF = 1.8 * bme.readTemperature() + 32;
    Serial.print("Temperature (ºC): ");
    Serial.println(temperatureF);*/

    // Write to ThingSpeak. There are up to 8 fields in a channel, allowing you to store up to 8 different
    // pieces of information in a channel.  Here, we write to field 1.
    int x = ThingSpeak.writeField(myChannelNumber, 1, temperatureC, myWriteAPIKey);
    //uncomment if you want to get temperature in Fahrenheit
    //int x = ThingSpeak.writeField(myChannelNumber, 1, temperatureF, myWriteAPIKey);

    if(x == 200){
      Serial.println("Channel update successful.");
    }
    else{
      Serial.println("Problem updating channel. HTTP error code " + String(x));
    }
    lastTime = millis();
  }
}

```

#requiredLibraries

- `ThingSpeak.h`

- Initialize the The thinkspeak Client `ThingSpeak.begin(client);` inside the `void setup()`

#imporatant

```c
unsigned long myChannelNumber = X;
const char * myWriteAPIKey = "XXXXXXXXXXXXXXXX";

int x = ThingSpeak.writeField(myChannelNumber, 1, temperatureC, myWriteAPIKey);

```

#### Another Thinkspeak

- [Reference: Devcodef1.com](https://devcodef1.com/news/1027971/send-sensor-data-to-thingspeak-using-nodemcu-esp8266-and-arduino-uno#:~:text=Now%20that%20we%20have%20set%20up%20the%20hardware%2C,Upload%20the%20following%20code%20to%20the%20NodeMCU%20ESP8266%3A)
