---
id: 03-Assertions
tags:
  - pytest
  - assertions
dg-publish: true
---

# Assertions

pytest uses plain Python assertions - no special assertion methods needed.

## Basic Assertions

```python
def test_basic():
    # Equality
    assert 1 + 1 == 2
    
    # Inequality
    assert 5 != 3
    
    # Boolean
    assert True
    assert not False
    
    # None
    value = None
    assert value is None
    assert value is not "something"
```

## Comparison Assertions

```python
def test_comparisons():
    x = 10
    y = 5
    
    assert x > y
    assert x >= 10
    assert y < x
    assert y <= 5
```

## Collection Assertions

```python
def test_collections():
    numbers = [1, 2, 3, 4, 5]
    
    # Check if item in list
    assert 3 in numbers
    assert 99 not in numbers
    
    # Check list length
    assert len(numbers) == 5
    
    # Check string
    text = "Hello pytest"
    assert "pytest" in text
    assert text.startswith("Hello")
    assert text.endswith("pytest")
```

## Dictionary Assertions

```python
def test_dictionary():
    user = {"name": "John", "age": 30}
    
    assert "name" in user
    assert user["name"] == "John"
    assert user.get("age") == 30
```

## Exception Assertions

Use `pytest.raises()` to test that code raises an exception:

```python
import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0


def test_value_error():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("Invalid input")
    
    assert str(exc_info.value) == "Invalid input"
```

## More Examples

```python
def test_api_response():
    response = {"status": "success", "data": [1, 2, 3]}
    
    # Assert status
    assert response["status"] == "success"
    
    # Assert data is a list
    assert isinstance(response["data"], list)
    
    # Assert list contents
    assert len(response["data"]) == 3
    assert 1 in response["data"]
```

## Assertion Details with -vv

Use `-vv` to see detailed assertion output:

```python
def test_detailed():
    expected = {"name": "John", "age": 30}
    actual = {"name": "Jane", "age": 25}
    
    assert actual == expected
```

With `-v`:
```
FAILED - AssertionError
```

With `-vv`:
```
FAILED - AssertionError: assert {'name': 'Jane', 'age': 25} == {'name': 'John', 'age': 30}
```

## Common Mistakes

```python
# WRONG - This doesn't assert anything useful
def test_wrong():
    result = 1 + 1
    # Missing assertion!

# CORRECT
def test_correct():
    result = 1 + 1
    assert result == 2
```

## Practice

Write assertions for:

1. A function that returns a list of users
2. An API response with status code and JSON body
3. Testing that a function raises `KeyError` for missing keys

---

**Next:** [[04-Fixtures]] - Learn about fixtures

**See Also:** [[05-Parameterized-Tests]] - Run tests with multiple inputs