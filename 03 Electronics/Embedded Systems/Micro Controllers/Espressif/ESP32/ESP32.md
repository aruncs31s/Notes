---
dg-publish: true
id: ESP32
aliases: []
tags: []
Created: "20-08-2024"
cssclasses:
  - wide-page
---

# ESP32

- [Introduction](#introduction)
- [Programming](#programming)
  - [ESP IDF](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/ESP_IDF.md)
  - [ADC](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/ESP-ADC.md)
  - [WiFi Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/WiFi%20Programming.md)
  - [Interfacing](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Interfacing.md)
  - [Multitasking](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/MultiTasking.md)
  - [ESP-NOW](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/ESP-NOW.md)
  - [Interrupt Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Interrupt%20Programming.md)
  - [ESP32 Web Programming|Web Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Web%20Programming.md)

# Introduction

![](https://lastminuteengineers.com/wp-content/uploads/iot/ESP32-Pinout.png)

- Built with TSMC low-power 40 nm technology
- Designed to achieve best power and RF Performance?
- [Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)

---

#### WiFi Features

- 802.11b/g/n
- 802.11n (2.4 GHz), up to 150 Mbps
- WMM
- TX/RX A-MPDU, RX A-MSDU
- Immediate Block ACK
- Defragmentation
- Automatic Beacon monitoring (hardware TSF)
- Four virtual Wi-Fi interfaces
- Simultaneous support for Infrastructure Station, SoftAP, and Promiscuous modes ,Note that when ESP32 is in Station mode, performing a scan, the SoftAP channel will be changed.
- Antenna diversity
  > [!blank|right-big] >![Pin Out|500x400](https://lastminuteengineers.com/wp-content/uploads/iot/ESP32-Pinout.png)

> MAC : `08:D1:F9:ED:30:D8`
> Z's MAC: `E4:65:B8:71:3E:D4` : Rev

## Programming

- [ESP IDF](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/ESP_IDF.md)
- [WiFi Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/WiFi%20Programming.md)
- [Interfacing](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Interfacing.md)
- [Multitasking](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/MultiTasking.md)
- [ESP-NOW](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/ESP-NOW.md)
- [Interrupt Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Interrupt%20Programming.md)
- [ESP32 Web Programming|Web Programming](03%20Electronics/Embedded%20Systems/Micro%20Controllers/Espressif/ESP32/programming/Web%20Programming.md)
