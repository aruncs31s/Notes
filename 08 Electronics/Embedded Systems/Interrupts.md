---
id: Interrupts
aliases: []
tags:
  - electronics
  - embedded_systems
cssclasses: 
Created: 15-08-2024
Status: 
dg-publish: true
---
# Interrupts
Used in 
- [[Interrupt Programming]]
- Hardware interrupts related to internal Devices they uses the `INT1` and `INT2`
- External devices sends interrupt informations
- ISRs are processor or program specific
- Software interrupt are related to execptions

#### Interrupt Latency
Time taken to start interrupt service 
$$
T_{latency} - T_{Switching}
$$
When interrupt service starts immediately after context switching
- IRS Does not start immediately and [[Context Switching]] happens after all higher priority interrupt are executed 
$$
  T_{lat} = T_{Exec} + T_{Switching}
$$

- When the program executes a critical section all the interrupts will get disabled.
so 
$$
T_{Lat} = T_{exec} + T_{Switch} + T_{disable}
$$