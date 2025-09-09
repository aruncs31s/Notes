---
id: ESP32_Web_Programming
aliases: []
tags:
  - electronics
  - embedded_systems
  - micro_controllers
  - espressif
  - esp32
cssclasses: 
Created: 25-08-2024
Status: 
dg-publish: true
---
# ESP32 Web Programming

### Using Web Sockets
>[!float|right-small] WebSocket
>WebSocket is a computer communications protocol, providing a simultaneous two-way communication channel over a single Transmission Control Protocol connection[^1] 

When using `HTTP` page method in [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/ESP32|ESP32]] , some problem arises when multiple users are accessing the same page like all the pages are not getting refreshed.Also there is a problem when two users try to change the same thing(like toggling the same led)
To fix this we use **bi-directional capabilities of `WebSocket`** to build a responsive system as said in [This tutorial](https://lastminuteengineers.com/esp32-websocket-tutorial/)

[^1]:https://en.wikipedia.org/wiki/WebSocket
>[!blank|left-small]
>![](https://lastminuteengineers.com/wp-content/uploads/iot/HTTP-vs-Websocket-Protocol.png)
>

#### Inbuilt LED Control using WebSocket Comm. Protocol 
[source](https://lastminuteengineers.com/esp32-websocket-tutorial/)
1. Required Libs ->
	1. `WiFi.h` 
	2. AsyncTCP.h>
#include <ESPAsyncWebServer.h>

```

2. Connect to wifi [[WiFi Programming#Connecting to WiFi|Using This]]
3. 
