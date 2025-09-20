---
id: HDLC
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_2
type: synchronous
dg-publish: true
---
# HLDC (High Level Data Link Control)

- [Transfer Modes](#transfer%20modes)
- [Types of HDLC Frames](#types%20of%20hdlc%20frames)
- [Structure](#structure)
- 

High-level Data Link Control (HDLC) is a group of communication protocols of the **data link layer** for transmitting data between network points or nodes. Since it is a **data link protocol**, ==data is organized into frames==. A frame is transmitted via the network to the destination that ==verifies its successful arrival==. It is a bit - oriented protocol that is applicable for ==both point - to - point and multipoint communications.==
- Establish and maintain reliable communication between two devices
- It is widely used in ==telecommunications and networking for framing, error detection, and flow control==

#### Transfer Modes
Supports 2 types of transfer modes = Normal Response Mode, asynchronous balanced Mode

1. **Normal Response Mode (NRM)** − Here, two types of stations are there, a primary station that send commands and secondary station that can respond to received commands. It is used for both point - to - point and multipoint communications

![](https://www.tutorialspoint.com/assets/questions/media/15399/transfer_modes.jpg)

2. **Asynchronous Balanced Mode (ABM)** − Here, the configuration is balanced, i.e. each station can both send commands and respond to commands. It is used for only point - to - point communications
![](https://www.tutorialspoint.com/assets/questions/media/15399/abm.jpg)

####  Types of HDLC Frames

- **I-frame** − I-frames or Information frames carry user data from the network layer. They also include flow and error control information that is piggybacked on user data. The first bit of control field of I-frame is 0.
    
- **S-frame** − S-frames or Supervisory frames do not contain information field. They are used for flow and error control when piggybacking is not required. The first two bits of control field of S-frame is 10.
    
- **U-frame** − U-frames or Un-numbered frames are used for myriad miscellaneous functions, like link management. It may contain an information field, if required. The first two bits of control field of U-frame is 11.
![](https://www.tutorialspoint.com/assets/questions/media/15399/hdlc_frame2.jpg)

#### Structure
#arch
![](https://www.tutorialspoint.com/assets/questions/media/15399/hdlc_frame.jpg)

1. **Frame Structure**: HDLC frames consist of a header, data, and trailer, with each part performing specific functions:
    
    - **Header**: Contains control information such as frame type, addressing, and error detection.
    - **Data**: Carries the payload or user data to be transmitted.
    - **Trailer**: Includes error detection mechanisms such as Frame Check Sequence (FCS), typically a CRC (Cyclic Redundancy Check), for ensuring data integrity.
2. **Bit-Oriented Protocol**: HDLC operates at the bit level, meaning it sends and receives data bit by bit. This allows for precise control over data transmission and synchronization between communicating devices.
    
3. **Synchronous Communication**: HDLC is a synchronous protocol, meaning it requires a clock signal to synchronize data transmission between sender and receiver. This clock signal ensures that both devices operate at the same speed, preventing data loss or corruption due to timing discrepancies.
    
4. **Station Types**: HDLC defines two types of stations:
    
    - **Primary Station**: The device that initiates communication and controls the data link.
    - **Secondary Station**: The device that responds to the primary station's requests and follows its instructions.
5. **Control Field**: The control field in the HDLC frame header contains information about frame type, sequence numbers (for error control and flow control), and other control flags used to manage the data link.
    
6. **Modes of Operation**: HDLC supports several modes of operation, including:
    
    - **Normal Response Mode (NRM)**: Suitable for point-to-point communication, where one station acts as the primary and the other as the secondary.
    - **Asynchronous Response Mode (ARM)**: Allows secondary stations to initiate communication with the primary station.
    - **Asynchronous Balanced Mode (ABM)**: Suitable for multipoint communication, where multiple stations can communicate with each other in a peer-to-peer fashion.
7. **Error Detection and Control**: HDLC incorporates mechanisms for error detection and control, including CRC in the trailer for detecting transmission errors and acknowledgment and retransmission mechanisms for ensuring reliable data delivery

## References
1. https://www.tutorialspoint.com/high-level-data-link-control-hdlc
