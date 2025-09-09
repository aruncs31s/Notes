---
id: 20-11-2024-Project
aliases: []
tags:
  - projects
  - electronics
  - transcutaneous_electrical_nerve_stimulation
dg-publish: true
Date: 
Starting: 20-11-2024
Target: 03-12-2024
End: 17-12-2024
Status: 
Working_ON: true
Completed: true
github: 
cssClasses: wide-page
cssClass: image-gallery
---
# Transcutaneous electrical nerve stimulation 

```dataview
Table 
file.ctime as "Created" , Date.Started as "Started" , Date.Target as "Completed"
Where file = this.file

```

- [[TENS Versions]]
- [[09 Projects/Transcutaneous electrical nerve stimulation/Ledger|Ledger]]

### Timeline

```timeline
[line-3, body-2]
+ Started</br> 20th Nov 2024
+ Problem Statement 
+ To design a period pain releaver based on the principle of Transcutaneous electrical nerve stimulation(TENS) is a technique to stimulate the body's nerves.

```

---

```timeline
[line-3, body-2]
+ Started</br> 20th Nov 2024
+ Problem Statement 
+ To design a period pain releaver based on the principle of Transcutaneous electrical nerve stimulation(TENS) is a technique to stimulate the body's nerves.

+ 20 Nov 
+ Desiging
+ For the prototype we are planning to use [[08 Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] and ![[TENS Design.excalidraw]] this is the initial design which contains 
- [[09 Projects/Academics/Iot_based_smart_energy_management_system/ESP32/esp32|esp32]] 
- Step up Transformer 
- 2 resistors to devide the voltage and limit current ? 
- [[MOSFET]] to control the transformer
+ 22 Nov 2024
+ New Design 
+ There is an issue with the current design , which is that it is too costly and the, [[08 Electronics/Embedded Systems/Micro Controllers/ESP32/ESP32|ESP32]] is does not really requred here 

+ 22 Nov AN 
+ Purchase 
+ Add something

+ Modules</br>28 Nov 2024
+ Delay Circuit and Inverter 
+ New Version ![[Tens Version 1.excalidraw]] Contains an inverter circuit and a delay control mechanism , it is hard to control the frequency output of the overall circuit or the output of the transformer , instead we can control the power to the inverter circuit using a [[MonoStable Multi-Vibrator]] and use a potentiometer to control its duration and frequency.

+ Verison 0.1.1</br> 5 Dec 2024 
+ First Prototype
+ ![[version 0.1.0.canvas|version 0.1.0]]
![[Tens Device.png]]

> [!multi-column]
>
>>![[Astable.png]]
>
>>![[Monostable.png]]

> [!multi-column]
>
>>![[Inverter.png]]
>
>>![[Power Supply.png]]

```

## References
1. "Design of Abdominal Pain Reliever based upon the Principle of TENS" , Saurabh P. Pandey ,Saurabh Bansod , Prashant Pal , Shashank Kumar Singh

