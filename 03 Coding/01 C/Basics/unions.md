---
id: unions
aliases: []
tags:
  - coding
  - basics
dg-publish: true
---
### Struct inside a union
#exampleCode

```c
union UnionA{
	struct {
		int x,y;
	}point;
	int z;
}
int main() {
    MyUnion u;
    u.point.x = 10;
    u.point.y = 20;

    std::cout << "x: " << u.point.x << ", y: " << u.point.y << std::endl;

    u.z = 30;
    std::cout << "z: " << u.z << std::endl;

    return 0;
}

```

> [!warning] Memory
> f you modify the value of `z`, for example, by assigning a value to it (`u.z = 30;`), it will overwrite the values of `x` and `y` in the shared memory space. Conversely, if you modify the values of `x` or `y` within `point` (e.g., `u.point.x = 10;`), they will overwrite the value of `z`.
> You cannot access point.x and point.y simultaneously because they occupy the same memory space, and modifying one will affect the other. Similarly, accessing z will overwrite the values of point.x and point.y, and vice versa. why it is inside a struct
> 

