---
id: VLSI Module 1
aliases: []
tags:
  - academics
  - btech
  - s6
  - vlsi
mindmap-plugin: basic
dg-publish: true
---
# VLSI Design Methodologies

## Prerequisites
  - 1.  [[MOSFET]]
  - 2. [[VLSI Module 2#CMOS INVERTER|CMOS]]
## Contents
- [[#Syllabus]]
- [[#Introduction]]
- [[#ASIC]]
	- [[#ASIC Classification]]
	- [[#Semi-Custom ASIC]]
	- [[#Standard cell based]]
	- [[#Gate Array Based ASIC]]
- [[#FPGA(Field Programmable Gate Array)]]
- [[#References]]
## Syllabus

- [[#Introduction]]:
  - [[#^xyz|Moore’s law]]
  - ASIC design
    - Full custom ASIC
    - Standard cell based ASICs
    - Gate array based ASICs
  - SoCs
  - FPGA devices
  - ASIC and FPGA Design flows
  - Top-Down and Bottom-Up design methodologies.
  - Logical and Physical design.
  - Speed power and area considerations in VLSI design

### Introduction

Typically, the required computational and information processing power of these applications is the driving force for the fast development of this field. This trend towards portable, distributed system architectures is one of the main driving forces for system integration, even though it does not preclude a concurrent and equally important trend towards centralized, highly powerful information systems such as those required for network computing (NC) and video services.
**The level of integration as measured by the number of logic gates** in a monolithic chip has been steadily rising for almost three decades

#advantages

- Less area/volume and therefore, compactness
- Less power consumption
* Less testing requirements at system level
* Higher reliability, mainly due to improved on-chip interconnects
* Higher speed, due to significantly reduced interconnection length
* Significant cost savings

Digital CMOS (Complementary Metal Oxide Semiconductor) integrated circuits(ICs) have been the driving 'force behind Very Large Scale Integration (VLSI) for high-performance computing and other scientific and engineering application

| Era                                  | Date | Complexity     |
| ------------------------------------ | ---- | -------------- |
| Single Transistor                    | 1958 | <1             |
| Unit Logic(one gate)                 | 1960 | 1              |
| Multi-function                       | 1962 | 2 -4           |
| Complex function                     | 1964 | 5 - 20         |
| Medium Scale Integration (MSI)       | 1967 | 20 - 200       |
| Large Scale Integration (LSI)        | 1972 | 200 - 2,000    |
| Very Large Scale Integration (VLSI)  | 1978 | 2,000 - 20,000 |
| Ultra Large Scale Integration (ULSI) | 1989 | 20,000 - ?     |

> [!NOTE] Moore's Law
> The number of transistors on a microchip doubles about every two years, made by Intel co-founder Gordon Moore in 1965.
> ![Mores Law](https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Moore%27s_Law_Transistor_Count_1970-2020.png/800px-Moore%27s_Law_Transistor_Count_1970-2020.png)
> Level of integration versus time for memory chips and logic chips.
> ^xyz

#### ASIC

An application-specific integrated circuit is an integrated circuit (IC) that’s custom-designed for a particular task or application . Unlike FPGA boards that can be programmed to meet a variety of use case requirements after manufacturing, ==ASIC designs are tailored early in the design process to address specific needs==. The two primary ASIC design methods are gate-array and full-custom.

- ASIC may contain a very large part of the electronics needed on a single integrated circuit
  #example
	1. Chip for toy bear
	2. Chip for satellite
#disadvantages 
- Low level flexibility for programming
- high cost per unit
- large time to market
##### ASIC Classification

![|400x300](https://www.electronicshub.org/wp-content/uploads/2020/01/Types-of-ASIC.jpg)

- Full Custom
- [[#Semi-Custom ASIC|Semi Custom]]
  - Standard Cell Based
  - Gate array based
    - Channeled
    - Channel Less
    - Structured Gate
- Programmable
  - PLD
  - FPGA

##### Semi-Custom ASIC
﻿  
- ==To shorten the design time and cut down the cost of full-custom ASICs==, numerous other design approaches have been developed and these are called as Semi- Custom ASIC Designs.  
- All logic cells are pre-designed & some mask layers are customized.  

###### Standard cell based:  
![](https://www.electronicshub.org/wp-content/uploads/2020/01/Standard-Cell-Design.jpg)

- A Standard Cell based ASIC uses predesigned, pretested & pre-characterised logic cells like Gates, Multiplexers, Flip-flops, Adders etc.  
- Each standard cell can be optimized individually during the design of cell library each and every transistor can be chosen to reduce area & power.  
- These logic cells are known as Standard Cells that are already designed and stored in a library.  
- This library is imported into the CAD tool and the design can performed using the components of the library as inputs.  
-  Standard cell areas are built of rows of standard cells like a wall of bricks.  
- The standard cell design may also contain a larger and more complex predesigned cells like Microcontrollers or Microprocessors.  
- These larger cells are called as Megacells. Also known as megacells, megafunctions, fullcustom blocks, system-level macros (SLMs), fixed blocks, cores, or Functional Standard Blocks (FSBs).  
#advantages 
- Reduced time and less risk compared to full custom designs.
#disadvantages 
- The disadvantage is the time and expense to make a standard library and to fabricate these designs.  

##### Gate Array Based ASIC
- In a gate-array-based ASIC, the transistors are predefined on the silicon wafer.  
- The predefined pattern of transistors is called the base array.  
- The smallest element that is replicated to make the base array is called the base or primitive cell.  
- the ASIC designer can choose predesigned logic cells from the gate array library for better and easy design.  
- The cells present in the gate array library are often called as Macros.  
Three types: 
- Channeled gate array  
- Channelless gate array  
- Structured gate array  

#### SOC(System On Chip)
A **system on a chip** or **system-on-chip** is an integrated circuit that integrates most or all components of a computer or other electronic system.
#### FPGA(Field Programmable Gate Array)
A **field-programmable gate array** (**FPGA**) is a ==type of configurable integrated circuit that can be repeatedly programmed post manufacturing==. FPGAs are a ==subset of logic devices referred to as programmable logic devices ("PLDs")==.

>[!note] PLDs 
>They consist of an array of programmable logic blocks with a connecting grid, that can be configured "in the field" to interconnect with other logic blocks to perform various digital functions.

*FPGAs are often used in limited (low) quantity production of custom-made products, and in research and development, where the higher cost of individual FPGAs is not as important, and where creating and manufacturing a custom circuit wouldn't be feasible.* 

- FPGA Will contain CLB(Configurable Logic Blocks)

> [!NOTE] CLB
> Configurable Logic Blocks will be consist of 4 componets
> Contents

#applications
1. telecommunications
2. automotive
3. aerospace
4. and industrial sectors, which benefit from their flexibility, high signal processing speed, and parallel processing abilities.
## References

1. [Ktu Syllabus]()
2. https://en.wikipedia.org/wiki/Field-programmable_gate_array
3. 

