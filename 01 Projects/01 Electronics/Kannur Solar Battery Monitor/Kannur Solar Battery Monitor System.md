---
id: 06010-2024-Smart-City
aliases: []
tags:
  - projects
  - electronics
  - kannur_solar_battery_monitor
Date: 
Started: 06-10-2024
Target: 28-10-2024
Status: Done
dg-publish: true
github: 
---
# Kannur Solar Battery Monitor System

```dataview
Table
file.ctime as "Created" , Date.Started as "Started" , Date.Target as "Completed"
Where file = this.file

```

```widgets
type: countdown
date: 2025-06-09 00:00:00
to: Complete the Project 🎉
completedLabel: Project is done 🎉

```

- [[#Components Used]]
- [[#3D Printing The case]]
- [[#Diagram]]
- [[01 Projects/Kannur Solar Battery Monitor/Versions|Versions]]
  - [[Version Control]]
- [[01 Projects/01 Electronics/Smart City/website/Smart City WebSite]]
- [[Reasearch And Development]]
  **Aim**:
  > **Revision 1**:
  >
  > - Measure the voltage using a Micro-Controller and show that on a website
  >   **Revision 2**:
  >   _{extends the Revision 1}_
  > - Measure the voltage as well as the rain volume
  >   **Revision 3**:
  >   _{extends the Revision 2}_>
  > - WebSite should include a relay which control the `stree light `

> [!Note|right-small] Relay Module
> Note that i have used 2 channel relay module because by the time i only have 2 channel relay module and it can be also used to control additional load ;

---

### Components Used

- There are 2 revisions for this project
  1. Using [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/ESP32|ESP32]]
  2. Using [[ESP8266]]

_This is just initial cost for testing and prototype and does not reflect on the actual cost of the final project , for example `esp32` is in the first table costs `546/-` INR Which can be reduced also if we're planning to use `ESP8266` the cost will be even less but we will be only getting 1 [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/programming/Analog Interfacing|ADC]] Pin_

| Component Name                                                                                      | Quantity | Price | Total |
| --------------------------------------------------------------------------------------------------- | -------- | ----- | ----- |
| **[ESP32](https://www.amazon.in/Easy-Electronics-Development-Bluetooth-Consumption/dp/B07TYCFX5C)** | 1        | 546/- | 546   |
| [Relay Module](https://amzn.in/d/abbcGc6)                                                           | 1        | 90/-  | 636   |
| 7semi SHT40                                                                                         | 1        |       |       |
| VEML7700 Light                                                                                      | 1        |       |       |
|                                                                                                     |          |       |       |

### 3D Printing The case

| Dimensions | value | accounted | +accouting |
| ---------- | ----- | --------- | ---------- |
| Length     | 7.5cm | 1.5mm     | 7.8cm      |
| Width      | 4 cm  | 1.5mm     | 4.3cm      |
| Height     |       |           |            |

### Diagram

![[initial circuit diagram.png]]
