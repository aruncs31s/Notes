
<h2 align="center" id="relaymodule">Relay Module</h2>

- [Introduction](#introduction)
- [Pinout](#pinout)
- [Sources](#sources)
#### Introduction
*Relay Module is a device that allows to control a high power circuit using a low-power signal*
-  *some come with built-in optocoupler that add an extra “layer” of protection, optically isolating the ESP32 from the relay circuit*


<details><summary>Image</summary>
<img src="https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/12/Relay-1-2-4-8-ch-channel-modules.jpg?w=750&quality=100&strip=all&ssl=1">
</details>

#### Pinout
![|450](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/11/Relay-pinout.png?w=850&quality=100&strip=all&ssl=1)


-> *COM*: connect the current you want to control (mains voltage)
-> **NC (Normally Closed):** the normally closed configuration is used when you want the relay to be closed by default. The NC are COM pins are connected, meaning the current is flowing unless you send a signal from the ESP32 to the relay module to open the circuit and stop the current flow.
-> **NO (Normally Open):** the normally open configuration works the other way around: ==there is no connection between the NO and COM pins==, so the circuit is broken unless you send a signal(==LOW Voltage==) from the ESP32 to close the circuit.
-> *Control Pins*
- The low-voltage side has a set of four pins and a set of three pins. The first set consists of VCC and GND to power up the module, and input 1 (IN1) and input 2 (IN2) to control the bottom and top relays, respectively.

#### Working

- **Normally Closed configuration (NC)**:
    - HIGH signal – current is flowing
    - LOW signal – current is **not** flowing
- **Normally Open configuration (NO)**:
    - HIGH signal – current is **not** flowing
    - LOW signal – current in flowing
#### Sources 
1. https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/
2. 

