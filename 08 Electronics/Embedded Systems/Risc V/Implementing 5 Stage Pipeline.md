---
aliases: 
Date: 2024-08-09
cssclasses:
  - wide-page
---


# Implementing 5 Stage Pipeline
The 5 stages being used are[^1]
- Instruction Fetch (IF),
- Instruction Decode (ID), 
- Execute (EX), 
- Memory (MEM) and
- Write Back (WB)

### Prerequisites
- Know [[RTL]]

>[!multi-columns]
>
>>[!info]+ Contents 
>> 
>
>>[!note]+ Tasks
>> - [ ] RTL
>>  - [x] MIPS ✅ 2024-08-09
>>  - [ ] Types of instruction 



>[!info] MIPS
>**MIPS** is an architecture which represent the lowering of the compiler to hardware level[^2] 
>- The MIPS processor implemented a smaller, simpler instruction set
>- Instructions implemented on this chip run in a single clock cycle
>- Used Pipelining to improve performance
>- Used 32 bit registers



### Single and MultiCycle CPU's

#### Single Cycle
- All the operation take equal amount of time to complete

### Types of instructions 
- R-Type
- I-Type
- J-Type
- Jump


### 5 Stage Pipeline[^3]
There are 5 stages 
- Fetch
- Decode 
- Execute 
- Memory
- Write Back 
*More about this check [[Architecture design#Instruction Execution|Here]]*
#### Types of Code
1. load type,
2. store type, 
3. branch, 
4. jump,
5. or  R Type of code

##### 1. Load Type 
>[!blank|right-small]
>````mermaid
>graph TB
>A[Fetch] --> B[Decode] --> C[Execute] --> D[Memory] -->E[Write Back]

This load type needs to go through all 5 stages to complete the instruction
- This type is usually used to  **read data from memory and place it into a register**.
#example 
```c
R1 <- [1]
```
*This instruction loads `1` the registor `R1`  just like `R1 = 1` in `c`*
- `<-` This is an assignment operator
##### 2. Store Type 
>[!blank|right-small]
>```mermaid
>graph TB
>A[Fetch] --> B[Decode] --> C[Execute] --> D[Memory]
>```
- This type is used to write data from a register to memory

#example 
```c
[A] <- R1
```
*This represents a store operation in which the contents of `R1` to *


[^3]: https://levelup.gitconnected.com/five-stages-of-risc-pipeline-aad0c3eb1233

## References
[^1]:https://scholarworks.calstate.edu/concern/theses/w0892f37n
[^2]:https://cs.stanford.edu/people/eroberts/courses/soco/projects/risc/mips/index.html