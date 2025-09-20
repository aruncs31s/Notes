---
id: Arm_Architecture
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_3
dg-publish: true
---
# ARM Processor architecture

## Prerequisites
- [[Academics/S6/Embedded Systems/Module 3/RISC]]
## Contents
- [[#Syllabus]]

## Syllabus
- [x] The Acorn RISC Machine. ✅ 2024-06-04
- [ ] Architectural inheritance
- [ ] The ARM programmer's model
- [ ] ARM development tools.

### Acron RISC Machine
The ARM was originally developed at Acorn Computers Limited of Cambridge, England, between 1983 and 1985. It was the first RISC microprocessor developed for commercial use and has some significant differences from subsequent RISC architectures.
In 1990 ARM Limited was established as a separate company specifically to widen the exploitation of ARM technology, since when the ARM has been licensed to many semiconductor manufacturers around the worl

The ARM architecture incorporated a number of features from the Berkeley RISC design, but a number of other features were rejected. Those that were used were:
1. a load-store architecture
2. fixed-length 32-bit instructions
3. address instruction formats.
*There are also some features that are rejected like `Register Window` , `Delayed branches` .. etc*

### Architectural inheritance
The ARM architecture incorporated a number of features from the Berkeley RISC design, but a number of other features were rejected

#### Used Features
- a load-store architecture;
- fixed-length 32-bit instructions;
- 3-address instruction formats.

#### Rejected Features
The features that were employed on the Berkeley RISC designs which were rejected by the ARM designers were:
1. Register windows
2. Delayed branches
3. Single Cycle Execution of all instructions : Most of the instructions in **ARM** are executed in single cycle but some requires multiple cycles

---
The **stored-program** digital computer keeps its instructions and data in the same program memory system, ==allowing the instructions to be treated as data when necessary.== This Computer enables the processor itself to generate instructions which it can subsequently execute.

> [!question] Stored Program
> This  Computer enables the processor itself to generate instructions which it can subsequently execute.  Although programs that do this at a fine granularity (self-modifying code) are generally considered bad form these days since they are very difficult to debug
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

