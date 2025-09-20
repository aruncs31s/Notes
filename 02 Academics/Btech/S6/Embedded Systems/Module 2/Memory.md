---
id: Memory
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_2
dg-publish: true
---
# Memory

## Contents
- [ ] Memory
	- [ ] Memory devices and systems 
	- [ ] ROM-Flash
	- [ ] EEPROM
	- [ ] RAM-SRAM
		- [ ] DRAM
		- [ ] Cache memory
	- [ ] memory mapping and addresses,
	- [ ] memory management unit– DMA

### Memory
Modern microprocessor units (MMUs) perform address translations that provide a larger virtual memory space in a small physical memory.

### Caches
Microprocessor clock rates are increasing at a faster rate than memory speeds, such that memories are falling further and further behind microprocessors every day.As a result,computer architects resort to caches to increase the average performance of the memory system.==A cache is a small,fast memory that holds copies of some of the contents of main memory. Because the cache is fast, it provides higher-speed access for the CPU==

- Caches are widely used to speed up memory system performance
- accesses in the cache will be fast, while access to locations not cached will be slow
 >[!Note] Working Set 
 >Caching makes sense when the CPU is using only a relatively small set of memory locations at any one time; the set of active locations is often called the **working set**.

####  Hit or Miss
A cache controller mediates between the CPU and the memory system comprised of the main memory. The cache controller sends a memory request to the cache and main memory. 
1. *If the requested location is in the cache, the cache controller forwards the location’s contents to the CPU and aborts the main memory request; this condition is known as a ==cache hit==*.
2. *If the location is not in the cache, the controller waits for the value from main memory and forwards it to the CPU; this situation is known as a ==cache miss==*.

![[Drawing 2024-06-04 14.31.33.excalidraw]]

##### Types 
---
id: Memory
aliases: 
tags:
  - module2
  - memmory
---
## Memory
### Contents
- [[Academics/S6/Embedded Systems/Module 2/Memory PDFs]]
- [Syllabus](#syllabus)
---

#### Syllabus 
- Memory devices and systems – ROM-Flash, EEPROM,RAM- SRAM, DRAM, Cache memory, memory mapping and addresses,
- memory management unit– DMA
---

- Modern microprocessor units (MMUs) perform address translations that provide a larger virtual memory space in a small physical memory

---
#### Caches
*A cache is a small,fast memory that holds copies of some of the contents of main memory. Because the cache is fast, it provides higher-speed access for the CPU; but since it is small, not all requests can be satisfied by the cache, forcing the system to wait for the slower main memory*
- [[L1]]
- [[L2]]
- [[L3]]
- *The set of active locations is often called the working set*
#advantages
-  The cache speeds up average memory access time
-  increases the variability of memory access times

->> *Cache Controller* : Mediates between the CPU and the memory system comprised of the main memory
->> *Cache Hit* : If the requested location is in the cache, the cache controller forwards the location’s contents to the CPU and aborts the main memory request; this condition is known as a *cache hit*

->> *Cache Miss* : If the location is not in the cache, the controller waits for the value from main memory and forwards it to the CPU; this situation is known as a *cache miss*

[[memory1.pdf#page=1&selection=61,1,63,11|memory1, page 1]]
![[Pasted image 20240330203604.png]]
#fig The cache in the memory system

![[Academics/S6/Embedded Systems/Files/Pasted image 20240330204044.png]]
#fig Two Level Cache System

