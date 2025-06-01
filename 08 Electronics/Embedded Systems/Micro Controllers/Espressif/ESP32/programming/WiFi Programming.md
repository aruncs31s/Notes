---
id: WiFi Programming
aliases: 
tags:
  - esp32
  - code
---

### WiFi Programming

1. [[#Get MAC Address]]
2. [[#Static IP]]
3. [[#CSI]]
#### Get MAC Address

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

##### Methods

| Method                            |                     |
| --------------------------------- | ------------------- |
| `WiFi.begin(ssid, password)`      |                     |
| `WiFi.status()`                   |                     |
| `WiFi.localIP()`                  | **get Local IP**    |
| `.macAddress()`                   | **Returns Mac**     |
| `.SSID()`                         | **Returns SSID**    |
| `.RSSI()`                         | **Signal Strength** |
| `.disconnect()`                   |                     |
| `.reconnect()`                    |                     |
| `.softAP("ESP32_AP", "password")` |                     |

#### Connecting to WiFi

```c
#include <WiFi.h>

const char* ssid     = "change";
const char* password = "change";

void setup(){
	Serial.begin(9600);
	WiFi.begin(ssid,passwd);
	 while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}
void loop(){

}

```

#### Static IP

```c
#include <WiFi.h>

const char* ssid     = "change";
const char* password = "change";

// Local IP
IPAddress local_IP(192, 168, 1, 184);
// Set Gateway IP
IPAddress gateway(192, 168, 1, 1);

IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);   //optional
IPAddress secondaryDNS(8, 8, 4, 4); //optional

void setup(){
if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
    Serial.println("STA Failed to configure");
  }

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  }
```

#### Reconnect After Disconnect

```c
if ((WiFi.status) != WL_CONNECTED ){
  WiFi.disconnect();
  delay(100);
  WiFi.reconnect();
}
```


#### CSI
- First complete [[03 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/ESP_IDF]]
- Then complete [[ESP_CSI]]
HACK: 
```c
#include <stdio.h>
#include "esp_system.h"
#include "esp_wifi.h"
#include "nvs_flash.h"

void wifi_init() {
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_start());
}

void app_main() {
    wifi_init();
    // Start CSI collection
    // (CSI collection logic and configuration goes here)
    printf("CSI collection started.\n");
}

```

**Expected Out**:
```
Packet Number: 1
Subcarrier 1: [Amplitude: 0.32, Phase: 1.57]
Subcarrier 2: [Amplitude: 0.28, Phase: 1.44]
Subcarrier 3: [Amplitude: 0.30, Phase: 1.53]
...
Subcarrier N: [Amplitude: 0.29, Phase: 1.50]
```