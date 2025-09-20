---
id: Quick_Sort
aliases: []
tags:
  - coding
  - data_structures_and_algorithms
cssclasses: 
Created: 21-09-2024
Status: 
dg-publish: true
---
# Quick Sort

Quicksort (A as Array , low as int , high as int)

```c
if (low < high)
	pivot_location = Partition(A,low,high)
	Quicksort(A,low,pivot_location)
	Quicksirt(A,pivot_location + 1 ,high)

```

Partition(A as array,low as int , high as int)

```c
pivot=A[low]
leftwall = low;
for i = low + 1 to high 
	if (A[i] < pivot) then 
		swap (A[i] , A[leftwall])
		leftwall = leftwal + 1
	swap(pivot,A[leftwall])
return (leftwall)

```

