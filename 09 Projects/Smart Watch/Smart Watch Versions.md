---
id: Smart Watch Versions
aliases: []
tags: []
Date:
  Created: "2024-12-20"
cssclasses:
  - wide-page
---

# Smart Watch Versions

#### Requirements

1. [ ] Should contain a sos button
2. [ ] Should detect "HELP" command
3. [ ] Should Send location to the parents
4. [ ] Should measure the heart rate

## Version 1
![[Smart Watch.canvas|Smart Watch]]


> [!multi-column]
>
> > [!blank]+ Use Case
> > ![[Smart Watch PCB Board GPS.excalidraw]]
>
> > [!blank]+ Resources
> > ![[Smart Watch PCB Board GSM.excalidraw]]

#### SIM800L Interfacing

```c
#define BAUD_RATE 9600
#define MIC_PIN A0

#if defined(ARDUINO)
#define GSM_TX 3
#define GSM_RX 2
#elif defined(ESP8266)
#define GSM_TX D5
#define GSM_RX D6
#endif
/* --- Config.h --- */
/* Source: https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/
 */

#include "Config.h"
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

#### Neo 6m GPS

```c
/*
 * Source:
 * https://randomnerdtutorials.com/esp8266-nodemcu-neo-6m-gps-module-arduino/
 */
#define BAUD_RATE 9600
#define MIC_PIN A0
#define GPS_BAUD_RATE 9600

#if defined(ARDUINO)
#define GSM_TX 3
#define GSM_RX 2
#elif defined(ESP8266)
#define GSM_TX D5 // This should connect to the TX pin of the GPS module
#define GSM_RX D6 // This should connect to the RX pin of the GPS module
#endif
/* --- Config.h ---*/
#include "Config.h"
#include <SoftwareSerial.h>
#include <TinyGPS++.h>

TinyGPSPlus gps;

// Create an instance of Software Serial
SoftwareSerial gpsSerial(GPS_RX, GPS_TX);

void setup() {
  // Serial Monitor
  Serial.begin(115200);

  // Start Serial 2 with the defined RX and TX pins and a baud rate of 9600
  gpsSerial.begin(GPS_BAUD_RATE);
  Serial.println("Software Serial started at 9600 baud rate");
}

void loop() {
  // This sketch displays information every time a new sentence is correctly
  // encoded.
  unsigned long start = millis();

  while (millis() - start < 1000) {
    while (gpsSerial.available() > 0) {
      gps.encode(gpsSerial.read());
    }
    if (gps.location.isUpdated()) {
      Serial.print("LAT: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("LONG: ");
      Serial.println(gps.location.lng(), 6);
      Serial.print("SPEED (km/h) = ");
      Serial.println(gps.speed.kmph());
      Serial.print("ALT (min)= ");
      Serial.println(gps.altitude.meters());
      Serial.print("HDOP = ");
      Serial.println(gps.hdop.value() / 100.0);
      Serial.print("Satellites = ");
      Serial.println(gps.satellites.value());
      Serial.print("Time in UTC: ");
      Serial.println(String(gps.date.year()) + "/" + String(gps.date.month()) +
                     "/" + String(gps.date.day()) + "," +
                     String(gps.time.hour()) + ":" + String(gps.time.minute()) +
                     ":" + String(gps.time.second()));
      Serial.println("");
    }
  }
}
```

```c
      Serial.print("LAT: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("LONG: ");
      Serial.println(gps.location.lng(), 6);
```

### MIC Interfacing

![[Drawing 2024-12-20 22.44.37.excalidraw]]

![[Pasted image 20241220232146.png]]

number of points/samples = **4581**

> starting of help

$$
(4581 / 3 ) \times 1.86 = 2840.22 \tag{1}
$$

let this be $\large s_{start}$

> Ending of help

$$
\left( \frac{4581}{3} \right) \times 1.96 = 2992.92 \tag{2}
$$

let this be $S_{stop}$

help took $S_{stop} - S_{start} = 152$ samples

- Picovoice Rhino Speech-to-Intent

#### Pyaudio Setup

```bash
# Debian
sudo apt-get install libasound-dev
# Fedora
sudo dnf install portaudio-devel
```

## Sajesh Kumar Sir Suggestions
