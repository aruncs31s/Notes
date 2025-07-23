---
id: arrays
aliases: []
tags: []
---

- provides dynamic memory aloc
- allows resizing without creating a new array


## Slices
  
```go
fruits := make([]string, 0)
```
1. The type of the slice 
2. The initial capacity of the underlying array
3. The length of the slice

- `[]string` -> slice of strings
- 0 -> initial length of slice

```go
fruits2 := make([]string, 0)
```
- initial cap 0 
- needs to alocate new memory when appending
```go
fruits2 := make([]string, 0, 10)
```
- creating an empty slice of (`[]string`)
- and setting its initial capacity to `10` 

```go
fruits1 := make([]string, 0)
fruits2 := make([]string, 0, 10)

fmt.Println(len(fruits1)) //  0
fmt.Println(len(fruits2)) //  0
// cap
fmt.Println(cap(fruits1)) // 0
fmt.Println(cap(fruits2)) // 10
```
```go
fruits := make([]string, 0)
fruits = append(fruits, "A")
fmt.Println(fruits)
fruits = append(fruits, "B", "C")
fmt.Println(fruits)
```
```
[A]
[A B C]
```
