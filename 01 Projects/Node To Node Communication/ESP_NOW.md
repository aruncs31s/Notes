---
id: ESP_NOW
aliases: []
tags: []
---

# ESP_NOW

- Upto `250-byte` is possible <- Payload Size

### Steps
- Get Receivers MAC Address

##### 1. Get Receiver MAC Address

```c
#include <WiFi.h>
void setup(){
Serial.begin(9600);
WiFi.mode(WIFI_STA);
WiFi.STA.begin();
Serial.println();
}

void loop(){
Serial.print("ESP Board MAC Address: ");
Serial.println(WiFi.macAddress());
delay(500);
}
```

Receiver's MAC: `08:D1:F9:ED:30:D8`

#### Sender Side

```c

#include <esp_now.h>
#include <esp_wifi.h>
#include <WiFi.h>
#include "DFRobot_VEML7700.h" //1.0.0

// For Light Sensor
DFRobot_VEML7700 light_sensor;


uint8_t wifiChannel = 6;

uint8_t broadcastAddress[] = {0x08, 0xD1, 0xF9, 0xED, 0x30, 0xD8};

typedef struct Data {
  uint8_t UID;
  char someChar[50];
  float light_sensor_value;
  int y;
} Data;

Data Message;

esp_now_peer_info_t peerInfo;

// Function that executes when data sends
void sendStatus(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success"
                                                : "Delivery Fail");
}

void setup(){
  Serial.begin(9600);
  light_sensor.begin();
  WiFi.mode(WIFI_STA);
  esp_wifi_set_promiscuous(true);
  esp_wifi_set_channel(wifiChannel, WIFI_SECOND_CHAN_NONE);
  esp_wifi_set_promiscuous(false);
  // Start ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Faild Starting");
    return;
  }
  // Register the callback Function -> executes when data sends
  esp_now_register_send_cb(sendStatus);



  // Register the peer
    // Register the peer
  memcpy(peerInfo.peer_addr, broadcastAddress,6); // 6 -> Number of Bytes sizeof(MAC) = 6
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop(){
  Message.UID = 1;
  strcpy(Message.someChar ,"This is a Message from Node 1");
  esp_err_t result =
      esp_now_send(broadcastAddress, (uint8_t *)&Message, sizeof(Message));
  // Check If the Tx was successful
  if (result == ESP_OK) {
    Serial.println("Success");
  }
  else {
    Serial.println("Failed");
    }

 // delay(1000);
  light_sensor.getALSLux(Message.light_sensor_value);oo
  Serial.print("Lux: ");
  Serial.print(Message.light_sensor_value);
  Serial.println(" lx");
  delay(200);
}
```

#### Receiver Side
```c
// Remove ssid and pass
#include <esp_now.h>
#include <esp_wifi.h>
#include <WiFi.h>
// #include "lib/sensors.h"
// uint8_t broadcastAddress[] = {0x08, 0xD1, 0xF9, 0xED, 0x30, 0xD8};
const char* ssid     = "802.11";
const char* password = "12345678p";
uint8_t wifiChannel = 6;

typedef struct Data {
  uint8_t UID;
  char someChar[50];
  float light_sensor_value ;
  int y;
} Data;

// Create struct same as Sender
Data Message;

// Create struct for different boards
Data from_board_1;
Data from_board_2;

// Pack it together
Data whole_data[2]={from_board_1,from_board_2};

void OnReceive(const uint8_t * mac_addr, const uint8_t *incomingData, int len) {
  char macStr[18];
  Serial.print("Packet received from: ");
  snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x",
           mac_addr[0], mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
  Serial.println(macStr);
  memcpy(&Message, incomingData, sizeof(Message));
  Serial.printf("Board ID %u: %u bytes\n", Message.UID, len);


}
void setup(){
Serial.begin(9600);

// Ignore this and get Contant Reboot :)
 WiFi.mode(WIFI_AP_STA);

  esp_wifi_set_promiscuous(true);
  esp_wifi_set_channel(wifiChannel, WIFI_SECOND_CHAN_NONE);
  esp_wifi_set_promiscuous(false);
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());


  // Once ESPNow is successfully Init, we will register for recv CB to
  // get recv packer info
  esp_now_register_recv_cb(esp_now_recv_cb_t(OnReceive));
}
void loop(){
   // TODO: Implement HTTP Server

  // Update the structures with the new incoming data
  whole_data[Message.UID-1].light_sensor_value = Message.light_sensor_value;
  whole_data[Message.UID-1].y = Message.y;
  Serial.printf("x value: %f \n", whole_data[Message.UID-1].light_sensor_value);
  // Serial.printf("y value: %d \n", boardsStruct[Message.UID-1].y);
  // Serial.println();
}
```
