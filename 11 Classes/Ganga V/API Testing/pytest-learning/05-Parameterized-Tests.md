---
id: 05-Parameterized-Tests
tags: [pytest, parametrized, testing]
dg-publish: false
---

# Parameterized Tests

Run the same test with different inputs using `@pytest.mark.parametrize`.

## Basic Parameterization

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 5, 15),
])
def test_add(a, b, expected):
    assert a + b == expected
```

Running this:
```bash
pytest test_file.py -v
```

Output:
```
test_file.py::test_add[1+2+3] PASSED
test_file.py::test_add[0+0+0] PASSED
test_file.py::test_add[-1+1+0] PASSED
test_file.py::test_add[10+5+15] PASSED
```

## Multiple Parameters

```python
@pytest.mark.parametrize("a,b,operation,expected", [
    (10, 5, "add", 15),
    (10, 5, "subtract", 5),
    (10, 5, "multiply", 50),
    (10, 5, "divide", 2),
])
def test_calculator(a, b, operation, expected):
    if operation == "add":
        assert a + b == expected
    elif operation == "subtract":
        assert a - b == expected
    elif operation == "multiply":
        assert a * b == expected
    elif operation == "divide":
        assert a / b == expected
```

## Parameterized with Fixtures

Combine parameters with fixtures:

```python
@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("endpoint,status_code", [
    ("/posts/1", 200),
    ("/posts/99999", 404),
    ("/users", 200),
])
def test_endpoints(api_base_url, endpoint, status_code):
    import requests
    response = requests.get(api_base_url + endpoint)
    assert response.status_code == status_code
```

## Using pytest.fixture in Parameters

```python
@pytest.mark.parametrize("username,email", [
    ("john", "john@example.com"),
    ("jane", "jane@example.com"),
    ("bob", "bob@example.com"),
])
def test_user_validation(username, email):
    assert len(username) >= 3
    assert "@" in email
```

## Multiple parametrize Decorators

Stack multiple `@pytest.mark.parametrize` decorators:

```python
@pytest.mark.parametrize("username", ["john", "jane", "bob"])
@pytest.mark.parametrize("status_code", [200, 404])
def test_api_responses(username, status_code):
    # This creates 3 x 2 = 6 test cases
    pass
```

## Skip Certain Combinations

```python
import pytest

@pytest.mark.parametrize("a,b", [
    (1, 2),
    (2, 1),
    (0, 0),
])
def test_divide(a, b):
    if b == 0:
        pytest.skip("Cannot divide by zero")
    assert a / b is not None
```

## Practice

Create parameterized tests for:

1. Testing multiple API endpoints
2. Testing different input combinations for a function
3. Testing both valid and invalid inputs

---

**Next:** [[06-API-Testing-Intro]] - Introduction to API testing

**See Also:** [[07-GET-Requests]] - GET requests