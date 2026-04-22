---
id: 11-Built-in-Functions
tags:
  - python
  - built-in
dg-publish: true
---

# Useful Built-in Functions

Common Python built-in functions.

## Type Checking

```python
isinstance(5, int)           # True
isinstance("hello", str)    # True
```

## String Checking

```python
"hello".startswith("he")    # True
"hello".endswith("lo")      # True
"hello" in "hello world"    # True
```

## Logical Checking

```python
any([True, False, False])   # True
all([True, True, False])    # False
bool(1)                      # True
bool(0)                      # False
bool("")                     # False
bool("text")                 # True
```

## Quick Reference

| Operation | Code |
|-----------|------|
| Length | `len(x)` |
| Type | `type(x)` |
| Round | `round(3.7)` |
| Absolute | `abs(-5)` |
| Sum | `sum([1,2,3])` |
| Min/Max | `min([1,2,3])` / `max([1,2,3])` |
| Sorted | `sorted(list)` |
| Enumerate | `enumerate(list)` |
| Zip | `zip(list1, list2)` |

---

**Next:** [[12-Testing-Patterns]] - Testing patterns

**See Also:** [[10-Files]] - Files