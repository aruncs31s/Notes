---
id: ES_Module_1
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
dg-publish: true
---
# ES Module 1
Created : 2024-06-05 13:25
## Contents
- [Module 1 Syllabus](Old_NOTES/Academics/Btech/S6/Embedded%20Systems/Embedded%20Systems.md#Module%201%20Syllabus)
## Syllabus 
- [ ] Complex Systems and Microprocessors
	- [x] Embedding Computers ✅ 2025-01-02
	- [x] Characteristics of Embedded computing Applications, ✅ 2025-01-02
	- [x] Application of Microprocessors,
	- [ ] The Physics of Software,
	- [ ] Challenges in Embedded Computing System,
	- [ ] Characteristics and quality attributes of an embedded system,
	- [ ] Performance in Embedded Computing
- [x] The Embedded System Design Process
	- [x] Requirements,
	- [x] Specification ,
	- [x] Architecture Design,
	- [x] Designing Hardware and Software Components ,
	- [x] System Integration.
- [ ] Formalisms for System Design
	- [ ] Structural Description,
	- [ ] Behavioral Description,
	- [ ] An embedded system design example.
- [ ] Embedded product development cycle (EDLC)
	- [ ] Different phases of EDLC, EDLC models

### Embedded System

*It an Electro-mechanical which is a ==combination of software and hardware design(working together) to do a specific task==*
*It is any device that includes a programmable computer but is not itself intended to be a general-purpose computer. Thus, a PC is not itself an embedded computing system, although PCs are often used to build embedded computing systems. But a fax machine or a clock built from a microprocessor is an embedded computing system.*

#alt_def 
"it is any device that includes a programmable computer but is not itself intended to be a general-purpose computer"^[Chapter 1 Embedded Computing]

#characteristics
Embedded System that execute limited number of fixed tasks, because the tasks do not change during the life span of an embedded system , it is not general programmable in the way that personal computer is.

1. **Complex algorithms** : The operations performed by the microprocessor may be very sophisticated. For example, the microprocessor that controls anautomobile engine must perform complicated filtering functions to optimize the performance of the car while minimizing pollution and fuel utilization.

2. **User interface** : Microprocessors are frequently used to control complex user interfaces that may include multiple menus and many options. The moving maps in Global Positioning System (GPS) navigation are good examples of sophisticated user interfaces.

3. **Real time** : Many embedded computing systems have to perform in real time— if the data is not ready by a certain deadline, the system breaks. In some cases, failure to meet a deadline is unsafe and can even endanger lives. In other cases, missing a deadline does not create safety problems but does create unhappy customers—missed deadlines in printers,for example,can result in scrambled pages.

4. **Multirate** : Not only must operations be completed by deadlines, but many embedded computing systems have several real-time activities going on at the same time. They may simultaneously control some operations that run at slow rates and others that run at high rates. Multimedia applications are prime examples of multi-rate behavior. The audio and video portions of a multimedia stream run at very different rates, but they must remain closely synchronized. Failure to meet a deadline on either the audio or video portions spoils the perception of the entire presentation.
2. **Manufacturing cost** : The total cost of building the system is very important in many cases. Manufacturing cost is determined by many factors, including the type of microprocessor used, the amount of memory required, and the types of I/O devices.
3. **Power and energy** : Power consumption directly affects the cost of the hardware, since a larger power supply may be necessary. Energy con- sumption affects battery life, which is important in many applications, as well as heat consumption, which can be important even in desktop applications.

#### Why Microprocessor
1. Microprocessors are a very efficient way to implement digital systems.
2. Microprocessors make it easier to design families of products that can be built to provide various feature sets at different price points and can be extended to provide new features to keep up with rapidly changing markets.
3. They also utilize the latest manufacturing technology => Just the use of the latest generation of **VLSI** fabrication technology, rather than one-generation- old technology, can make a huge difference in performance.

#### Challenges in Embedded System Designing
1. **How much hardware do we need?** : We cannot only select the type of microprocessor used, but also select the amount of memory,the peripheral devices,and more. Since we often must meet both performance deadlines and manufacturing cost constraints,the choice of hardware is important—too little hardware and the system fails to meet its deadlines, too much hardware and it becomes too expensive
2. **How do we meet deadlines?** : The brute force way of meeting a deadline is to speed up the hardware so that the program runs faster. Of course, that makes the system more expensive. It is also entirely possible that increasing the CPU clock rate may not make enough difference to execution time,since the program’s speed may be limited by the memory system.However, we want to be able to add features by changing software. How can wedesign a machine that will provide the required performance for software that we haven’t yet written? 
3. **How do we minimize power consumption?** : In battery-powered applications, power consumption is extremely important. Even in nonbattery applications, excessive power consumption can increase heat dissipation. One way to make a digital system consume less power is to make it run more slowly, but naively slowing down the system can obviously lead to missed deadlines. Careful design is required to slow down the noncritical parts of the machine for power consumption while still meeting necessary performance goals
4. **How do we design for upgradability?** : The hardware platform may be used over several product generations, or for several different versions of a product in the same generation, with few or no changes. However, we want to be able to add features by changing software. How can we design a machine that will provide the required performance for software that we haven’t yet written?
5. **Does it really work?** : Reliability is always important when selling products—customers rightly expect that products they buy will work. Reliability is especially important in some applications, such as safety-critical systems. If we wait until we have a running system and try to eliminate the bugs, we will be too late—we won’t find enough bugs, it will be too expensive to fix them, and it will take too long as well. Another set of challenges comes from the characteristics of the components and systems themselves. If workstation programming is like assembling a machine on a bench, then embedded system design is often more like working on a car—cramped, delicate, and difficult. Let’s consider some ways in which the nature of embedded computing machines makes their design more difficult

6. Complex Testing 
7. Limited Observability and controllability.
8. Restricted development environment

### Design Process

1. **Requirement Analysis**
	1. Define the problem : Understand the needs and constrains of the project
	2. Specify Requirements : List functional and non-functional requirements, including performance, power consumption, and cost constraints. 
2. **System Specifications**:
	1. System Architecture : Defining a high level structure for the project both hardware and software.
	2. Component Selection : Choosing the components for the project
3. **System Design** : 
	1. Hardware
		1. Shematic Design : Creating Circuit diagrams etc.
		2. PCB Layout : Designing the physical layout
	2. Software
		1. Software Architecture
		2. Algorithm Development 
		3. Firmware Development:
4. **Prototyping**
   1. Build Prototype : Assembling a working model of the project
   2. Testing and Debugging : Testing and debug the prototype to find bugs and improve the final product.
5. **Integration** 
	1. Hardware and Software Integration
	2. System Testing
6. **Implementation**
	1. Final Design Adjustments:
	2. Manufacturing Preparation
	3. Bill of Materials (BOM)
	4. Assembly Instructions
7. **Deployment**
8. **Maintenance** and Updates
9.  **Documentation**

##### The embedded system design process

#advantages 
1. First, it allows us to keep a scorecard on a design to ensure that we have done everything we need to do,such as optimizing performance or performing functional tests
2. Second, it allows us to develop computer-aided design tools. Developing a single program that takes in a concept for an embedded system and emits a completed design would be a daunting task,but by first breaking the process into manageable steps, we can work on automating (or at least semiautomating) the steps one at a time
3. A design methodology makes it much easier for members of a design team to communicate. By defining the overall process, ==team members can more easily understand what they are supposed to do==,what they should receive from other team members at certain times, and what they are to hand off when they complete their assigned steps.
*Since most embedded systems are designed by teams, coordination is perhaps the most important role of a well-defined design methodology**
*

## References
1. 