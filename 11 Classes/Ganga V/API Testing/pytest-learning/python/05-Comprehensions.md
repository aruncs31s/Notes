---
id: 05-Comprehensions
tags:
  - python
  - comprehensions
  - list
  - dictionary
dg-publish: true
---

# Comprehensions

Concise ways to create lists and dictionaries.

## List Comprehension

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

## List Comprehension with Condition

```python
evens = [x for x in range(10) if x % 2 == 0]
```

## Dictionary Comprehension

```python
{x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}
```

---

**Next:** [[06-Classes]] - Object-oriented programming

**See Also:** [[04-Functions]] - Functions
