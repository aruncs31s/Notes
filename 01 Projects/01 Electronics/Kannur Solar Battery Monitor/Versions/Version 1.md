---
id: Version_1
aliases: []
tags:
  - projects
  - electronics
  - kannur_solar_battery_monitor
  - versions
dg-publish: true
Date: 24-10-2024
---
# Version 1

- [ ] change to h2
##### Only Volt Meter -> Version 1

## Requirements

1. **Should Display Voltage** : [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/ESP32|ESP32]] or [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/ESP8266]] can be used
2. **Remote Control** : Both
3. **Dash Board** : Both

## Components Required
^51726b

| Components       | Cost      |
| ---------------- | --------- |
| [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/ESP8266]]      | 350/-     |
| L7805            | 15        |
| 5V Relay Module  | 25        |
| .22uF Capacitor  | 1         |
| .1uF Ceramic Cap | 1         |
| bc548 BJT        | 3?        |
| 470E Resistor    | 1         |
| 4.7 K Resistor   | 1         |
| 1K Resistor      | 1         |
| Dot PCB          | 1/2 -> 25 |
| PVC Box          | 18        |
| miscellaneous    | 20        |
| Total            | 561/-     |
|                  |           |

^dc412a

</br>

## Module Wise Cost

1. Relay Module

| Component     | Cost |
| ------------- | ---- |
| Relay         | 25   |
| bc547         | 3    |
| 470E Resistor | 1    |
| --            | --   |
| Total         | 29   |

2. Power Supply

| Component           | Cost |
| ------------------- | ---- |
| L7405CV             | 15   |
| .22uF Capacitor     | 1    |
| .1uF Ceramic Cap    | 1    |
| Optional Heate Sink | 10   |
| miscellaneous       | 6    |
| Total               | 33/- |

3. Voltage Meter

| Component     | Cost |
| ------------- | ---- |
| 4.7 Resistor  | 1    |
| 1 K Resistor  | 1    |
| miscellaneous | 10   |
| Total         | 12/- |

miscellaneous -> 2 Pin Connecting Wire

![[p1.png]]
![[p2.png]]
![[p3.png]]

#### 24-10-2024

- I have used bc548 as switch but should change to something else

![[relay change.png]]
