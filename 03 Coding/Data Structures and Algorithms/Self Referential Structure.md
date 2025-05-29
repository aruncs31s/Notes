---
cssclasses: []
---

# Self Referential Structure
It is a `structure` which contains a `pointer` to a structure of the same type.
#example 

```cpp
struct something{
	int x;
	int y;
	struct something *self;
}
```