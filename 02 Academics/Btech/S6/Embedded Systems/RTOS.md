---
id: RTOS
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
Created: 2024-04-12
tag: {"Embedded Systems","RTOS"}
dg-publish: true
---
---

# Real Time Operating Systems *By Anil Achoora*

*operating system designed for real-time applications that require immediate processing and response to inputs*
- RTOS is optimized for tasks that have strict timing constraints
---
##### Characteristics of RTOS
1. Deterministic Behavior
2. Priority Scheduling
3. Preemptive Scheduling
4. Resource Management
5. Task Communication
---
#### History
- Early resources like memory and processing power were very less
- Industry Slowly moded from assembly to high level languages like `Fortran`,[[C programming|C]],[[ Coding/C++|C++]] etc
- Operating Systems were there but they were generic
- So people started writing custom operating system tailored to small end micro-controller
- Some of them grew and started supporting many architectures peripherals etc.
---

##### Examples of RTOS
- CMSIS
- QNX
- VxWorks
- FreeRTOS -- Free
- Zephyr -- Free
- Nutx
- OSEK
- OSEK
- OS8
---

#### Basic Concepts
- Task,Threads,Processes or think of it as workers
- Memory , Number of ports, peripheral access think of it as resources
- Each workers may have some or different tasks
- Resources may need to be shared between them
- What if two workers need the same resources at the same time.
---
##### Strategies
- Give preference to some of the workers
- Give a certain time slice to each worker
- Let the workers talk to each other and decide
- This is called Scheduling
- But How the workers can talk to each other
- Communication mechanisms
---

##### Creation

```c
taskSpawn("/task1",107,VX_NO_STACK_FIL_2000,(FUNCPTR)task1,0,0,0,0,0,0,0,0,0);
pthread_create(&ptid,NULL)
xReturned = xTaskCreate(
		vTaskCode, // Function that implements the task
		"NAME", // Text name for the task
		STACK_SIZE, // Stack size in words,not bytes
		(void *)1, // Parameter passed into the task
		tskDLE_PRIORITY, // Priority at which the task is created
		&xHandle); // Used to pass out the created task's handle
)

```

---
##### Creation was the first step
- Sustain
- Terminate
- See that its terminated
- Current state
- The state machine understanding
- Zombies!!
---
##### ISRO , NASA , CERN
- Reliable real time operation is critical for space missions.
- The famous example is about the Mars Path Finder, similar systems will be present at ganayan also
- CERN is a European agency searching for particles from outside.

---
##### Can Linux be used as an RTOS
- There are many companies using Real Time(RT) Linux for their operations.
- Like `FreeRTOS` , `Zephyr`, it is also a good candidate for getting started and doing hands on work as students
---

##### Requirements in Entering In Embedded domain
- HardWare or SoftWare
- PCB or Circuit Design or Chip Design
- `C`,`C++` , `Python`,`Rust` 
- The basic concepts required as operating system concepts,programming skils and then embedded concepts
- There is always demand for skilled people.
- Differentiate yourself as a fresher
---
##### Suggested Class
![esp.png](Academics/S6/Embedded%20Systems/Files/esp.png)

1. https://youtu.be/F321087yYy4?feature=shared

---

##### Take "Real Time" to understand industry
- Billions of device are running RTOS
- There are tens of thousands of companies using RTOS
- So there is always opportunity
- VxWorks and QNX started in 1980s
- But its not for RTOS, applies everywhere
- Focus on learning and upskilling
- Learn about companies and products
- Be Industry ready in something.
---

### Connected To

[[Old_NOTES/Academics/Btech/S6/Embedded Systems/Embedded Systems]]

