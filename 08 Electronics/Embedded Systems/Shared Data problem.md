---
id: Shared_Data_problem
aliases: []
tags:
  - electronics
  - embedded_systems
cssclasses: 
Created: 15-08-2024
Status: 
dg-publish: true
---
# Shared Data Problem
Consider the following Example 

```c
MUL C,A,B
ADD Y,C,A

```

- Shared data problem occurs wen resources are shared by multiple IRSs
- Shared data problem arises in a system when another higher priority task finishes an operation and modifies the data or variable before the completion of previous task operations

- [ ] Semaphores? 
- [ ] How to solve it?