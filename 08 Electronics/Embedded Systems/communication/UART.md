---
id: UART
aliases: []
tags:
  - electronics
  - embedded_systems
  - communication
dg-publish: true
---
# UART
 - [[#Data Transmission]]
 - [[#References]]

![](https://www.analog.com/en/_/media/images/analog-dialogue/en/volume-54/number-4/articles/uart-a-hardware-communication-protocol/335962-fig-01.svg?w=577&rev=a39d7f916b404552967cc0579b7c0639)

The UART ==interface does not use a clock signal== to synchronize the transmitter and receiver devices; **it transmits data asynchronously**. Instead of a clock signal, ==the transmitter generates a bitstream based on its clock signal while the receiver is using its internal clock signal to sample the incoming data==.
==The point of synchronization is managed by having the same baud rate on both devices.== Failure to do so may affect the timing of sending and receiving data that can cause discrepancies during data handling. The allowable difference of baud rate is up to 10% before the timing of bits gets too far off.

## Data Transmission
### Prerequisites
- [[Academics/S6/Embedded Systems/Module 2/Parity]]
- A line is in NRZ(Non-Return to Zero) state => when this line is idle it ==will be logic 1==
- The start is signaled by the transition from logic 1 to 0 of the Tx Line.(for a period 1/BoudRate(reciprocal of boadrate))
- **UART** Sending bits consists of
	1. Start Bit
	2. 8 data bit (5:8 Data bits)
	3. Optional Programmable bit (used as parity)
	4. Stop Bit

> [!NOTE] P-Bit
> P-Bit(Programmable Bit) is a one extra bit before the stop bit t is called **TB8** at transmitter side and **RB8** at receiver side

## References
1.https://www.analog.com/en/resources/analog-dialogue/articles/uart-a-hardware-communication-protocol.html
