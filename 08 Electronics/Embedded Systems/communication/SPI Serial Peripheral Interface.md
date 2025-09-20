---
id: SPI_Serial_Peripheral_Interface
aliases: []
tags:
  - electronics
  - embedded_systems
  - communication
Date: 04-01-25
dg-publish: true
---
# Serial Peripheral Interface

#synchronous
used for connecting multiple peripheral devices to a microcontroller or microprocessor

```

Master        Slave 
| MOSI | -> | MOSI | 
| MISO | <- | MISO | 
| SCLK | -> | SCLK | 
| SS/CS| -> | SS/CS| 

```

-  **MOSI (Master Output/Slave Input)** :Line for the master to send data to the slave.
- **MISO (Master Input/Slave Output)** – Line for the slave to send data to the master.
- **SCLK (Clock)** – Line for the clock signal. Used to synchronize the two communicating devices
- **SS/CS (Slave Select/Chip Select)** – Line for the master to select which slave to send data to.

#### SS/CS 
Chip Slect(CS) , Slave Select (SS) lines are normally held at the high voltage level and are dropped down to ground to signal who’s turn it is to speak.

The controller always initiates communication with the peripheral and always generates the clock signal^[https://www.techtarget.com/whatis/definition/serial-peripheral-interface-SPI].
 The controller provides an individual chip selection line for each peripheral, establishing a direct connection between the controller and the peripheral
 ![](https://www.techtarget.com/rms/onlineimages/standard_spi-f.png)

## References
- [Source](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/)
- [Source 2](https://www.techtarget.com/whatis/definition/serial-peripheral-interface-SPI)