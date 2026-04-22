---
id: 08-Exception-Handling
tags:
  - python
  - exceptions
  - error-handling
dg-publish: true
---

# Exception Handling

Handle errors gracefully in Python.

## Try-Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Done")
```

## Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

**Next:** [[09-JSON]] - Working with JSON

**See Also:** [[07-Modules]] - Common modules