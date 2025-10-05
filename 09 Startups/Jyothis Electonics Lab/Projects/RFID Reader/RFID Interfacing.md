---
css:
---

```cpp
#define BAUD_RATE 115200
#define RST_PIN 5
#define SS_PIN 15

#include <Arduino.h>
#include "config.h"
#include <MFRC522.h>
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup()
{
  Serial.begin(BAUD_RATE);
  while (!Serial);                              
  SPI.begin();                      
  mfrc522.PCD_Init();               
  delay(4);                          
  mfrc522.PCD_DumpVersionToSerial(); 
  Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}


void loop()
{
  if (!mfrc522.PICC_IsNewCardPresent())
  {
    return;
  }
  if (!mfrc522.PICC_ReadCardSerial())
  {
    return;
  }
  mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
}

```