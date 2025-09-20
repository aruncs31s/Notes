---
id: USB
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_2
dg-publish: true
---
1. **USB Host** : This is the area where the USB host controller is installed and where the client software/device driver runs. The USB Host Controller is the interface between the host and the USB peripherals. The host is responsible for the detection of the insertion and removal of USB devices and data flow between the host and the devices. The host also provides power to the attached devices.
2. **USB Hub** : allows multiple USB devices to attach to a single USB port on a USB host
3. **USB Function (Peripheral)** : A USB device that can transmit or receive data or controlinformation over the bus and that provides a function. A function is typically implemented as a separate peripheral device that plugs into a port on a hub using a cable. This is known as a standalone device. However, it is also possible to create a compound device, which is a physical package that implements multiple functions and an embedded hub with a single USB cable. A compound device appears to the host as a hub with one or more non-removable USB devices, which may have ports to support the connection of external devices.

#### Communication
*In USB data communication, the USB encodes the data by using the Non- Return-to-Zero Inverted (NRZI) transmission scheme. In NRZI coding, a “1” bit is represented by a transition of the physical level and “0” bit is represented by no transition of the physical layer. In addition, in order to ensure a minimum density of signal transitions that remains in the bitstream, an additional “0” bit is injected onto the data bus after the occurrence of 6 consecutive “1” bits. Here, in this method, is commonly known as bit stuffing or simply insertion of non-information bits into data. All this is done to ensure the presence of sufficient signal transitions for clock recovery.*t 