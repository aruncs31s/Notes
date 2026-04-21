---
id: 02-Running-Tests
tags: [pytest, cli, running-tests]
dg-publish: false
---

# Running Tests

Learn the various ways to run pytest tests.

## Basic Commands

### Run All Tests

```bash
pytest
```

Runs all tests in the current directory and subdirectories.

### Run a Specific File

```bash
pytest test_example.py
pytest path/to/test_file.py
```

### Run a Specific Test Function

```bash
pytest test_example.py::test_addition
```

### Run Tests in a Directory

```bash
pytest tests/
pytest path/to/tests/
```

## Useful Flags

| Flag | Description | Example |
|------|-------------|---------|
| `-v` | Verbose - show test names | `pytest -v` |
| `-vv` | Very verbose - show assert details | `pytest -vv` |
| `-x` | Stop on first failure | `pytest -x` |
| `--collect-only` | List tests without running | `pytest --collect-only` |
| `-k EXPRESSION` | Run tests matching expression | `pytest -k "test_user"` |
| `-m MARKER` | Run tests with specific marker | `pytest -m "slow"` |
| `-s` | Show print statements | `pytest -s` |
| `-q` | Quiet mode | `pytest -q` |

## Verbose Output (-v)

```bash
pytest -v
```

Output:
```
test_example.py::test_addition PASSED
test_example.py::test_string PASSED
test_example.py::test_api_call FAILED
```

## Stop on First Failure (-x)

```bash
pytest -x
```

Useful for debugging - stops at the first failure instead of running all tests.

## Filter Tests by Name (-k)

```bash
# Run tests with "user" in the name
pytest -k "user"

# Run tests with "test" but not "api"
pytest -k "test and not api"
```

## Run Tests by Marker (-m)

```python
import pytest

@pytest.mark.slow
def test_large_dataset():
    pass

@pytest.mark.api
def test_api_endpoint():
    pass
```

```bash
pytest -m "slow"
pytest -m "api"
pytest -m "not slow"
```

## Show Print Output (-s)

```python
def test_debug_example():
    print("Debug: Starting test")
    result = do_something()
    print(f"Debug: Result = {result}")
    assert result == expected
```

```bash
pytest -s
```

## Using python -m pytest

```bash
# Same as `pytest` but uses the Python from current venv
python -m pytest
python -m pytest test_file.py -v
```

Useful when pytest isn't in PATH.

## Test Organization

### Recommended Folder Structure

```
project/
├── src/
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_api.py
│   └── conftest.py
└── pytest.ini
```

### Test Discovery Rules

pytest automatically finds:
- Files: `test_*.py` or `*_test.py`
- Functions: `test_*()`
- Classes: `Test*`

## Practice Commands

Try these:

```bash
# List all tests without running
pytest --collect-only

# Run with verbose and stop on first failure
pytest -v -x

# Run only API tests
pytest tests/test_api.py -v

# Run user-related tests
pytest -k "user" -v
```

---

**Next:** [[03-Assertions]] - Understanding assertions

**See Also:** [[04-Fixtures]] - Fixtures for setup/teardown