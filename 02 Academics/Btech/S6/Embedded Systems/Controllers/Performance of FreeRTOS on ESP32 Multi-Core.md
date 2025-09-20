---
id: Performance_of_FreeRTOS_on_ESP32_Multi-Core
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - controllers
dg-publish: true
---
# Performance of FreeRTOS on ESP32 Multi-Core
Created : 2024-05-11 00:20

## Contents

#### Report

- The operations are measured on ESP32-WROOM-32 development kit equipped with XTENSA dual-core processor running FreeRTOS. 

==The speed of a given operation does not increase linearly with the number of added CPUs, but according to Amdahl's law==.

## References

1. https://www.sciencedirect.com/science/article/pii/S2405896322003639
	- ![[Embedded Sys]]