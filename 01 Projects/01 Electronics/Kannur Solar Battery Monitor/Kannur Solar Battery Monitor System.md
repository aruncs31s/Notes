---
dg-publish: true
id: 06010-2024-Smart-City
aliases:
  - Smart city
tags:
  - project,embedded,iot
Date:
  Started: 06-10-2024
  Target: 28-10-2024
  Completed: 
Status:
  isCompelete: false
  isWorkingOn: true
  isStall: false
Status: true
github: 
  - https://github.com/aruncs31s/Kannur-Solar-Battery-Monitoring-System
---
# Kannur Solar Battery Monitor System
```dataview
Table 
file.ctime as "Created" , Date.Started as "Started" , Date.Target as "Completed"
Where file = this.file
```


```widgets
type: countdown
date: 2025-06-9 00:00:00
to: Complete the Project 🎉
completedLabel: Project is done 🎉
```

- [[#Components Used]]
- [[#3D Printing The case]]
- [[#Diagram]]
- [[01 Projects/Kannur Solar Battery Monitor/Versions|Versions]]
	- [[Version Control]]
- [[Smart City WebSite]]
- [[Reasearch And Development]]
**Aim**: 
>**Revision 1**:
>- Measure the voltage using a Micro-Controller and show that on a website 
>**Revision 2**:
>*{extends the Revision 1}*
>- Measure the voltage as well as the rain volume 
>**Revision 3**:
>*{extends the Revision 2}*>
>- WebSite should include a relay which control the `stree light ` 

>[!Note|right-small] Relay Module 
>Note that i have used 2 channel relay module because by the time i only have 2 channel relay module and it can be also used to control additional load ;

---
### Components Used
- There are 2 revisions for this project
  1. Using [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/ESP32|ESP32]]
  2. Using [[ESP8266]]

*This is just initial cost for testing and prototype and does not reflect on the actual cost of the final project , for example `esp32` is in the first table costs `546/-` INR   Which can be reduced also if we're planning to use `ESP8266` the cost will be even less but we will be only getting 1 [[03 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/programming/Analog Interfacing|ADC]] Pin*  

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


