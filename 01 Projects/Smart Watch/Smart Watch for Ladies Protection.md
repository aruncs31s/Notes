---
id: 29-11-2024-Project
aliases:
  - Smart Watch
tags:
  - project,
Date:
  Started: "03-04-2024"
  Target: "01-01-2025"
Status:
  Completed: false
  Working_ON: true
cssclasses:
  - wide-page
dg-publish: true
github: https://github.com/aruncs31s/Smart-Watch-for-Ladies-Protection
---

# Smart Watch for Ladies Protection

- [[Smart Watch Versions]]
- [[#Tasks]]
- [[#Timeline]]

---

```timeline
[line-3, body-2]
+ Started</br> 29th Nov 2024
+ Problem Statement
+ I have told to make a smart watch for ladies protection , which sends a sos message containing the current locatio to the parrent and the police in the following senarios
  - A button is pressed
  - Heart rate is unusual that normal and "HELP" command is detected
 **Requirements**
- Heart Beat -> to Sense
- SOS Switch
- Voice Detection
+ First Meating</br> 30th Nov 02-12-2024
+ Initial requirements
+ - It should have a sos button and when that is pressed
> it the microcontroller will send the watches location to police and parents
- To facilitate failsafe , the watch also senses heart rate and if the heart rate is above some threshold it will also send  location to parents and the police
- Continuesly monitor for the command **HELP!** if help is found do the sos thing

```

![[whole_system.png]]
# Ai Thinker VC-02

```dataview
Table 
file.ctime as "Created" , Date.Started as "Started" , Date.Target as "Completed"
Where file = this.file
```

|Key Spec|Val|
|--|--|
|Operating Voltage|3.3V - 5V|
|No of Commands | 80 Offline| 
| Response time | < 1 sec| 

#### PIN 
Source[^1]

|Pin Number|Pin Name|Description|
|---|---|---|
|1|VCC|Power supply (3.3V - 5V)|
|2|GND|Ground|
|3|TX|UART Transmit (connect to RX of microcontroller)|
|4|RX|UART Receive (connect to TX of microcontroller)|
|5|MIC+|Microphone positive terminal|
|6|MIC-|Microphone negative terminal|

#### Sampe Code 
Source[^1] 
```cpp
#include <SoftwareSerial.h> 
SoftwareSerial vc02Serial(10, 11); // RX, TX 
void setup() { 
	Serial.begin(9600); 
	vc02Serial.begin(9600);
	Serial.println("VC-02 Voice Recognition Module Initialized"); } 
void loop() { 
	if (vc02Serial.available()) { 
		String command = vc02Serial.readStringUntil('\n'); 
		Serial.print("Received Command: "); 
		Serial.println(command); 
		if (command == "TURN ON LIGHT") { 
		Serial.println("Turning on the light...");
		} else if (command == "TURN OFF LIGHT") { 
			Serial.println("Turning off the light...");
			} 
	else { 
		Serial.println("Unknown command"); 
		} 
	} 
}
```

##### Explained Code

```cpp
#include <SoftwareSerial.h> 
// Define the pins for SoftwareSerial 
SoftwareSerial vc02Serial(10, 11);
// RX, TX 
void setup() { 
// Start the hardware serial communication Serial.begin(9600); 
// Start the software serial communication vc02Serial.begin(9600);
Serial.println("VC-02 Voice Recognition Module Initialized"); } 
void loop() { 
// Check if data is available from the VC-02 module 
if (vc02Serial.available()) { 
// Read the incoming data 
String command = vc02Serial.readStringUntil('\n'); 
Serial.print("Received Command: "); 
Serial.println(command); 
// Process the command 
if (command == "TURN ON LIGHT") { Serial.println("Turning on the light...");
// Add code to turn on the light 
} else if (command == "TURN OFF LIGHT") { Serial.println("Turning off the light..."); // Add code to turn off the light } 
else { Serial.println("Unknown command"); } } }
```
[^1]: http://docs.cirkitdesigner.com/component/f16ca64b-e2a0-40b9-ad3d-cfe258eb5c4f/ai-thinker-vc-02

