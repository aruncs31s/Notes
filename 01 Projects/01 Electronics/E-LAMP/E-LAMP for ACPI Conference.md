---
id: E-LAMP_for_ACPI_Conference
aliases: []
tags:
  - projects
  - electronics
  - e-lamp
github: https://github.com/aruncs31s/e-vilakku-for-IEEE-ACPI-conference-GCEK
Status: Done
cssclasses: 
dg-publish: true
---
# E - Vilakku 
>[!SUMMARY]- Table of Contents
>- [[E-LAMP for ACPI Conference#E - Vilakku |E - Vilakku ]]
>    - [[E-LAMP for ACPI Conference#Circuit|Circuit]]
>    - [[E-LAMP for ACPI Conference#Coding|Coding]]
>        - [[E-LAMP for ACPI Conference#MACs|MACs]]
>    - [[E-LAMP for ACPI Conference#Sender|Sender]]
>            - [[E-LAMP for ACPI Conference#New Code with debounce error reduce|New Code with debounce error reduce]]
>        - [[E-LAMP for ACPI Conference#Reducing Debouncing|Reducing Debouncing]]
## Circuit

**Sender** and **Receiver**

![[e-vilaku-ckt.png]]
**Relay Module**
![[Pasted image 20250705192052.png]]

## Coding

### MACs
// New Receiver : `C4:D8:D5:12:C6:03`
%% Receiver %%: `48:3F:DA:47:80:41` 
Sender: `24:D7:EB:EE:BC:40`

### Sender

```cpp
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <espnow.h>

// `48:3F:DA:47:80:41`
// New mac `C4:D8:D5:12:C6:03`
// New MAC ESP32 78:42:1c:6c:90:2c
// NOTE: This is the mac of the ESP32 receiver
uint8_t brodcastAddress[] = {0x78, 0x42, 0x1C, 0x6C, 0x90, 0x2C};

#define BUTTON_PIN D5

volatile int button_pressed_count = 0;

void IRAM_ATTR button_isr() {
    Serial.println("Button pressed!");
    button_pressed_count++;
  }
}
// Structure example to send data
// Must match the receiver structure
typedef struct struct_message {
  int count;
} struct_message;

struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 2000;

// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0) {
    Serial.println("Delivery success");
  } else {
    Serial.println("Delivery fail");
  }
}
void IRAM_ATTR button_isr() {
  Serial.println("Button pressed!");
  button_pressed_count += 1;
}

void setup() {
  // Init Serial Monitor
  Serial.begin(115200);

  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(BUTTON_PIN, button_isr, FALLING);
  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);

  // Register peer
  esp_now_add_peer(brodcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop() {
  myData.count = button_pressed_count / 2;

  if ((millis() - lastTime) > timerDelay) {

    esp_now_send(brodcastAddress, (uint8_t *)&myData, sizeof(myData));

    lastTime = millis();
  }
  delay(50);
}

```

#### New Code with debounce error reduce

```cpp
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <espnow.h>

// `48:3F:DA:47:80:41`
// New mac `C4:D8:D5:12:C6:03`
// New MAC ESP32 78:42:1c:6c:90:2c
// NOTE: This is the mac of the ESP32 receiver
uint8_t brodcastAddress[] = {0x78, 0x42, 0x1C, 0x6C, 0x90, 0x2C};

#define BUTTON_PIN D5
#define DEBOUNCE_DELAY 50 // ms

volatile unsigned long last_button_press_time = 0;
volatile int button_pressed_count = 0;

void IRAM_ATTR button_isr() {
  unsigned long current_time = millis();
  // Check if this works as expected.
  if (current_time - last_button_press_time > DEBOUNCE_DELAY) {
    Serial.println("Button pressed!");
    button_pressed_count++;
    last_button_press_time = current_time;
  }
}
// Structure example to send data
// Must match the receiver structure
typedef struct struct_message {
  int count;
} struct_message;

struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 2000;

// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0) {
    Serial.println("Delivery success");
  } else {
    Serial.println("Delivery fail");
  }
}
void IRAM_ATTR button_isr() {
  Serial.println("Button pressed!");
  button_pressed_count += 1;
}

void setup() {
  // Init Serial Monitor
  Serial.begin(115200);

  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(BUTTON_PIN, button_isr, FALLING);
  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);

  // Register peer
  esp_now_add_peer(brodcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop() {
  myData.count = button_pressed_count / 2;

  if ((millis() - lastTime) > timerDelay) {

    esp_now_send(brodcastAddress, (uint8_t *)&myData, sizeof(myData));

    lastTime = millis();
  }
  delay(50);
}

```

### Reducing Debouncing
![[debounce-ckt.png]]
