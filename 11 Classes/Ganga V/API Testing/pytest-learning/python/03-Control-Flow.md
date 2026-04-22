---
id: 03-Control-Flow
tags:
  - python
  - control-flow
  - if-else
  - loops
dg-publish: true
---

# Control Flow

Learn if-else statements and loops in Python.

## If-Else

```python
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

## For Loop

```python
for item in [1, 2, 3]:
    print(item)

for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)
```

## While Loop

```python
while x > 0:
    x -= 1
```

---

**Next:** [[04-Functions]] - Writing functions

**See Also:** [[02-Operations]] - Operations on data types
