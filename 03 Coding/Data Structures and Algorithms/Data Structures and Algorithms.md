---
id: Data Structures and Algorithms
aliases: []
tags:
  - coding
  - data_structures_and_algorithms
dg-publish: true
---
# Data Structures And Algorithms

## Contents

- [x] [[Arrays.md]] ✅ 2024-09-18
- [x] [[Linked List]] ✅ 2024-09-18
  - [[Doubly Linked List]]
- [ ] [[Hash Table]]

- [[#Sorting]]
- A program should be efficient if it executes in `minimum time` and takes `minimum memory`

#### Time Complexity

_How much time an Algorithms is taking to solve a problem_

#### Space Complexity

_The amount of working space the algorithm needs_

#### $O(n)$

```c
int sum =0; // 1 times
for(int i = 0 ; i < count/* n+1 times */ ; ++i/*n times*/){

  sum++; /* n times */
// Total 2n+2 times => 0(n)

```

#### Linear Search

1. Best Case: When the the element to be searched is the **first** element
   0(1)
2. Average Case: When the the element to be searched is at the **middle**
   0(n/2)
3. Worst Case: When the the element to be searched is the **last** element
   0(n)

#### Rate of Growth

_How fast a function grows with the input size_ -> Rate of Growth of running time

#### Notations

- $O \text{Notation}$
- $\Omega \text{Notation}$
- $\theta \text{Notation}$

##### Big O Notations

- Tells how fast the algorithm is
- lets you compare the number of operations

##### $\Omega \text{Notation}$

- Provides the best case scenario of running an algorithm
- Gives minimum amount of resources (time or space) an algorithm would take to run

### Sorting

- [[Quick Sort]]

## References

1. https://youtu.be/Lwr3-doAgaI?si=gUm8h1YKggn3lUGw
