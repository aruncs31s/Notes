---
id: 02-Operations
tags:
  - python
  - operations
  - strings
  - lists
  - dictionaries
dg-publish: true
---

# Common Operations

Operations on strings, lists, and dictionaries.

## String Operations

```python
"hello" + " world"     # Concatenation
"hello" * 3            # Repetition
"hello"[0]              # Indexing
"hello"[1:4]            # Slicing
len("hello")            # Length
"hello".upper()         # UPPERCASE
"hello".lower()         # lowercase
"hello world".split()   # Split into list
```

## List Operations

```python
[1, 2, 3] + [4, 5]     # Concatenate
[1, 2, 3] * 2          # Repeat
[1, 2, 3][0]           # Get first item
[1, 2, 3].append(4)   # Add item
[1, 2, 3].pop()        # Remove last item
len([1, 2, 3])         # Length
```

## Dictionary Operations

```python
user["name"]            # Get value
user.get("name")        # Get with default
user.keys()             # All keys
user.values()           # All values
user.items()           # Key-value pairs
```

---

**Next:** [[03-Control-Flow]] - Control flow statements

**See Also:** [[01-Variables]] - Data types
