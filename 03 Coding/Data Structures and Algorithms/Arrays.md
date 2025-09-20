---
id: Arrays
aliases: []
tags:
  - coding
  - data_structures_and_algorithms
dg-publish: true
---
**Re allocating memory to an array**:

```c
int main(){
int *values = malloc(40);
values[2] = 6;
int x = values[2];
values = realloc(values,2000*sizeof(int));
x  = values[600];
}

```

#### Linear Search

- It sequentially check each and element in a list(array) until a math is found or the whole list is been searched
  Complexity: O(n)

#### Binary Search

Finds the position of a search element within sorted array

- Also called `logerithmic search`,`binary chop` etc .

#### Stack

- simple data structure allows removing and adding elements \
- FILO and LIFO
- Overflow: When completely full
- Underflow: When completely empty
- operations: push,pop etc...

#### Queues

- Open in both ends
- One end is allways used to insert while other end is allways used to remove ,read etc
- FIFO , LILO
- operations: Enqueue(), Dequeue(),isEmpty,isFull,peek->return first element of the queue
