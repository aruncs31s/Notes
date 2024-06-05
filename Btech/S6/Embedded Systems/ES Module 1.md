# ES Module 1
Created : 2024-06-05 13:25
## Contents
- [Module 1 Syllabus](Embedded%20Systems.md#Module%201%20Syllabus)
## Syllabus 
- [ ] Complex Systems and Microprocessors
	- [x] Embedding Computers ✅ 2024-06-05
	- [ ] Characteristics of Embedded computing Applications,
	- [ ] Application of Microprocessors,
	- [ ] The Physics of Software,
	- [ ] Challenges in Embedded Computing System,
	- [ ] Characteristics and quality attributes of an embedded system,
	- [ ] Performance in Embedded Computing
- [ ] The Embedded System Design Process
	- [ ] Requirements,
	- [ ] Specification ,
	- [ ] Architecture Design,
	- [ ] Designing Hardware and Software Components ,
	- [ ] System Integration.
- [ ] Formalisms for System Design
	- [ ] Structural Description,
	- [ ] Behavioral Description,
	- [ ] An embedded system design example.
- [ ] Embedded product development cycle (EDLC)
	- [ ] Different phases of EDLC, EDLC models


#### Embedded System
*It an Electro-mechanical which is a ==combination of software and hardware design(working together) to do a specific task==*
*It is any device that includes a programmable computer but is not itself intended to be a general-purpose computer. Thus, a PC is not itself an embedded computing system, although PCs are often used to build embedded computing systems. But a fax machine or a clock built from a microprocessor is an embedded computing system.*

#characteristics
Embedded System that execute limited number of fixed tasks, because the tasks do not change during the life span of an embedded system , it is not general programmable in the way that personal computer is.


1. **Complex algorithms** : The operations performed by the microprocessor may be very sophisticated. For example, the microprocessor that controls anautomobile engine must perform complicated filtering functions to opti mize the performance of the car while minimizing pollution and fuel utilization.

2. **User interface** : Microprocessors are frequently used to control complex user interfaces that may include multiple menus and many options. The moving maps in Global Positioning System (GPS) navigation are good examples of sophisticated user interfaces.

3. **Real time** : Many embedded computing systems have to perform in real time— if the data is not ready by a certain deadline, the system breaks. In some cases, failure to meet a deadline is unsafe and can even endanger lives. In other cases, missing a deadline does not create safety problems but does create unhappy customers—missed deadlines in printers,for example,can result in scrambled pages.
4. **Multirate** : Not only must operations be completed by deadlines, but many embedded computing systems have several real-time activities going on at the same time. They may simultaneously control some operations that run at slow rates and others that run at high rates. Multimedia applications are prime examples of multirate behavior. The audio and video portions of a multimedia stream run at very different rates, but they must remain closely synchronized. Failure to meet a deadline on either the audio or video portions spoils the perception of the entire presentation.
5. **Manufacturing cost** : The total cost of building the system is very important in many cases. Manufacturing cost is determined by many factors, including the type of microprocessor used, the amount of memory required, and the types of I/O devices.
6. **Power and energy** : Power consumption directly affects the cost of the hardware, since a larger power supply may be necessary. Energy con- sumption affects battery life, which is important in many applications, as well as heat consumption, which can be important even in desktop applications.

## References
1. 