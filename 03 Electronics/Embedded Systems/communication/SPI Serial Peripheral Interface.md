[Source](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/)
#synchronous
used for connecting multiple peripheral devices to a microcontroller or microprocessor

-  **MOSI (Master Output/Slave Input)** :Line for the master to send data to the slave.
- **MISO (Master Input/Slave Output)** – Line for the slave to send data to the master.
- **SCLK (Clock)** – Line for the clock signal. Used to synchronize the two communicating devices
- **SS/CS (Slave Select/Chip Select)** – Line for the master to select which slave to send data to.

#### SS/CS 
Chip Slect(CS) , Slave Select (SS) lines are normally held at the high voltage level and are dropped down to ground to signal who’s turn it is to speak.
