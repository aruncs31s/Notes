---
id: Web Programming
aliases: []
tags: []
---

### Web Programming

#### Sending Post

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "";
const char* password = "";

void setup () {

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {

    delay(1000);
    Serial.println("Connecting to WiFi...");

  }

  Serial.println("Connected to the WiFi network");

}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;
    http.begin("http://172.16.0.2:2280/");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    String httpRequestData = "usrname=abc&newpasswd=def&terms=on&page_sid=internal&org_url=http%3A%2F%2F172.16.0.2%3A2280%2F&update_btn=Login";
    int httpResponseCode = http.POST(httpRequestData);

    if (httpResponseCode>0) {
      String response = http.getString();

      Serial.println(httpResponseCode);
      Serial.println(response);

    } else {

      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);

    }

    http.end();
  }

  delay(30000);
}
```
