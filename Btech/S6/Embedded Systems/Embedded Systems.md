---
id: Module 2
aliases: []
tags: []
---
# Embedded Systems

*It an Electro-mechanical which is a ==combination of software and hardware design(working together) to do a specific task==*
*It is any device that includes a programmable computer but is not itself intended to be a general-purpose computer. Thus, a PC is not itself an embedded computing system, although PCs are often used to build embedded computing systems. But a fax machine or a clock built from a microprocessor is an embedded computing system.*



## Contents
- [Module 1](Embedded%20Systems.md#Module%201)
	- - [Module 1 Syllabus](Embedded%20Systems.md#Module%201%20Syllabus)
	- 
- [[Module 2]]
	- [[Serial Comm|Serial Communication]]
	- [[Btech/S6/Embedded Systems/Files/Module 2/Memory|Memory]]
	- [[I_O Devices|I_O Devices]]
- [[ES Module 5]]
## Concepts
- [RTOS](RTOS.md)
- [Context Switching]()
- Shared Memory
- Dead Lock

> [!NOTE] Dead Lock
> If two task were tring to access the same resource at the same time ,This situation is known as `Dead Lock` 


## Module 1
### Contens
- [Module 1 Syllabus](Embedded%20Systems.md#Module%201%20Syllabus)

### Module 1 Syllabus 
- Complex Systems and Microprocessors
	- Embedding Computers
	- Characteristics of Embedded computing Applications,
	- Application of Microprocessors,
	- The Physics of Software,
	- Challenges in Embedded Computing System,
	- Characteristics and quality attributes of an embedded system,
	- Performance in Embedded Computing
- The Embedded System Design Process
	- Requirements,
	- Specification ,
	- Architecture Design,
	- Designing Hardware and Software Components ,
	- System Integration.
- Formalisms for System Design
	- Structural Description,
	- Behavioral Description,
	- An embedded system design example.
- Embedded product development cycle (EDLC)
	- Different phases of EDLC, EDLC models
---

## Module 3

### Syllabus
1. ARM Processor architecture
	- The Acorn RISC Machine.
	- Architectural inheritance
	- The ARM programmer's model
	- ARM development tools.
2. ARM Assembly Language Programming
	-  Data processing instructions
	- Data transfer instructions
	- Control flow instructions
	- writing simple assembly language programs.
3. ARM Organization and Implementation
	- Three stage pipeline ARM organization
	- Five stage pipeline ARM organization
	- ARM instruction execution
	- ARM implementation
	- The ARM coprocessor interface. 
### ARM Processor architecture
The **stored-program** digital computer keeps its instructions and data in the same program memory system, allowing the instructions to be treated as data when necessary. This Computer enables the processor itself to generate instructions which it can subsequently execute.

> [!question] Stored Program
> This 
Computer enables the processor itself to generate instructions which it can subsequently execute. 
Although programs that do this at a fine granularity (self-modifying code) are gener-
ally considered bad form these days since they are very difficult to debug, use at a 
coarser granularity is fundamental to the way most computers operate. Whenever a 
computer loads in a new program from disk (overwriting an old program) and then 
executes it the computer is employing this ability to change its own program. 
Computer Because of its programmability a stored-program digital computer is universal,
applications which means that it can undertake any task that can be described by a suitable algo-
rithm. Sometimes this is reflected by its configuration as a desktop machine where 
the user runs different programs at different times, but sometimes it is reflected by 
the same processor being used in a range of different applications, each with a fixed 
program. Such applications are characteristically embedded into products such as 
mobile telephones, automotive engine-management systems, and so on.

#### Reduced Instruction Set Computer



##### Pipelining

A processor executes an individual instruction in a sequence of steps. A typical sequence is
1. Fetch the instruction from memory (fetch). 
2. Decode it to see what sort of instruction it is (dec). 
3. Access any operands that may be required from the register bank (reg). 
4. Combine the operands to form the result or a memory address (ALU). 
5. Access memory for a data operand, if necessary (mem). 
6. Write the result back to the register bank (res). 
Not all instructions will require every step, but most instructions will require most 
of them. These steps tend to use different hardware functions, for instance the ALU is 
probably only used in step 4. Therefore, if an instruction does not start before its pred-
ecessor has finished, only a small proportion of the processor hardware will be in use 
in any step.
An obvious way to improve the utilization of the hardware resources, and also the 
processor throughput, would be to start the next instruction before the current one has 
finished. This technique is called pipelining, and is a very effective way of exploiting 
concurrency in a general-purpose processor.

###### CPSR
>CPSR is crucial for maintaining the execution state of the processor and controlling its behavior during program execution. It's frequently accessed and modified by the processor during instruction execution.


##### 3 Stage Pipelining In ARM


#### ARM Assembly Programming







## References
1. 
