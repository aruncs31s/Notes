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
fruits2 := make([]string, 0, 10)
```
- creating an empty slice of (`[]string`)
- and setting its initial capacity to `10` 
