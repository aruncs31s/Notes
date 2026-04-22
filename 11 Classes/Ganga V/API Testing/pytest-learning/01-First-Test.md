---
id: 01-First-Test
tags:
  - pytest
  - basics
  - first-test
dg-publish: true
---

# Your First Test

Learn to write your first pytest test.

## Test File Naming

pytest automatically discovers test files with these patterns:
- `test_*.py` (recommended)
- `*_test.py`

## Your First Test

Create a file `test_example.py`:

```python
# test_example.py

def test_addition():
    """Test that 2 + 2 equals 4"""
    result = 2 + 2
    assert result == 4


def test_string():
    """Test string operations"""
    name = "pytest"
    assert name.upper() == "PYTEST"
    assert len(name) == 6
```

## Running the Test

```bash
pytest test_example.py -v
```

Expected output:
```
test_example.py::test_addition PASSED
test_example.py::test_string PASSED

========== 2 passed in 0.01s ==========
```

## Test Functions

Key points:
- Function name must start with `test_`
- No need to import anything special
- Use plain Python `assert` statements
- Docstrings (`"""..."""`) describe what the test does

## Anatomy of a Test

```python
def test_name():  # 1. Function starts with test_
    """  # 2. Optional docstring
    Description of what this test verifies
    """
    # 3. Setup (if needed)
    data = {"name": "test"}
    
    # 4. Act - execute the code being tested
    result = len(data)
    
    # 5. Assert - verify the result
    assert result == 1  # 6. Plain assert
```

## Practice Exercise

Create tests for a calculator:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

Write tests in `test_calculator.py`:

```python
from calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
```

---

**Next:** [[02-Running-Tests]] - Learn how to run tests

**See Also:** [[03-Assertions]] - More about assertions