---
id: Smart City
aliases:
  - Smart city
tags:
  - project,embedded
Completed: false
Starting Date: "6-10-2024"
Status: true
Target Date: "2024-10-28"
---
# Kannur Solar Battery Monitor System
- [[09 Projects/GCE_Kannur/Kannur Solar Battery Monitor/Ledger]]
- [[#Components Used]]
- [[#3D Printing The case]]
- [[#Diagram]]
- [[Versions]]

## Timeline 

```timeline 
[line-3, body-4]
+ 06 October 2024
+ Problem Statement
+ To measure the **SOC** of the Solar Battery </br>
 The initial task is to measure the voltage of the Solar bettery and provide a way for the user to check the battery voltage through web. 

+ October 2024  
+ Initial Solution 
+ The initial solution is to use a [[03 Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] which is a micro-controller , and utilize it [[analog_interfacing|Analog Interfacign]] capability to measure the voltage. But the problem is the **ESP32** can only be used to measure
```
**Aim**: 
>**Revision 1**:
>- Measure the voltage using a Micro-Controller and show that on a website 
>**Revision 2**:
>*{extends the Revision 1}*
>- Measure the voltage as well as the rain volume 
>**Revision 3**:
>*{extends the Revision 2}*>
>- WebSite should include a relay which control the `stree light ` 

[line-3, body-4]
+ 06 October 2024
+ Problem Statement
+ Measure the current consumed by the [[nexysa7.png|Nexys A7]] for the **Differential Power Analysis**
**Components**:
>[!Note|right-small] Relay Module 
>Note that i have used 2 channel relay module because by the time i only have 2 channel relay module and it can be also used to control additional load ;


>**Revision 1**:
>- A Micro-Controller Which has an ADC Pin exposed
>**Suited Micro-Controller** :
>- [[Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] or [[ESP8266]] 
**Revision 2**: 
*{extends the Revision 1}*
>- A $\mu C$ With [[Interrupts|Interrupt pin]]
>**Suited Micro-Controller and Sensor** :
>- [[Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] and [[ESP8266]]
>- [[GCEK Weather Station#^c08e06|This Rain Sensor]]  
**Revison 3**:
>*{extends the Revision 2}*
>- A [[Electronics/Embedded Systems/Sensors/Relay Module|Relay Module]]  and pin supports outputing `LOW` and `HIGH`
**Suited Compontent**
>- [[Electronics/Embedded Systems/Sensors/Relay Module|Relay Module]] 





---


### Components Used
- There are 2 revisions for this project
  1. Using [[Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]]
  2. Using [[ESP8266]]

*This is just initial cost for testing and prototype and does not reflect on the actual cost of the final project , for example `esp32` is in the first table costs `546/-` INR   Which can be reduced also if we're planning to use `ESP8266` the cost will be even less but we will be only getting 1 [[Analog Interfacing|ADC]] Pin*  

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






## Timeline 
```timeline
[line-3, body-1]
+ Start</br>31 Aug 2024 
+ Problem Statement
+ 
- To measure environmental factors like rand fall , humidity , light intensity etc 
- Created [Git repo](https://github.com/aruncs31s/GCEK_Weather_Station/) 
- 
+ 2 Sep 2024 
+ Initial Aproach
+ Due to miss communication inital approach does not meat the requrement because i implemented [[ESP_NOW]] on to this but they were expecting a long range communication 


+ 10 Sep 2024 
+ Correction 
+ Misconsumption was corrected and working on a server hosted in the [[03 Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] which shows the battery voltage and the rain fall , humidity , wind direction wind speed 

+ Version 0.0.1 </br>12 Sep 2024 
+ Big Change
+ Now this version only shows the battery voltage more here [[Version 1]]
- Also changed the project name to  **"Kannur Solar Battery Monitoring System** and [Git repo](https://github.com/aruncs31s/Kannur-Solar-Battery-Monitoring-System)
```
