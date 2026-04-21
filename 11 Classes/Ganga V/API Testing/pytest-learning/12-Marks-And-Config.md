---
id: 12-Marks-And-Config
tags: [pytest, marks, configuration]
dg-publish: false
---

# Markers & Configuration

Organize tests and configure pytest behavior.

## Built-in Markers

```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python_feature():
    pass


@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert False
```

## Custom Markers

```python
# test_file.py
@pytest.mark.slow
def test_slow_api_call():
    pass

@pytest.mark.api
def test_api_endpoint():
    pass

@pytest.mark.unit
def test_unit_function():
    pass

@pytest.mark.integration
def test_integration():
    pass
```

Register markers in `pytest.ini`:

```ini
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow
    api: marks tests as API tests
    unit: marks tests as unit tests
    integration: marks tests as integration tests
```

Or in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow",
    "api: marks tests as API tests",
]
```

## Running Tests by Marker

```bash
# Run only slow tests
pytest -m slow

# Run API tests only
pytest -m api

# Run everything except slow
pytest -m "not slow"

# Run tests with multiple markers
pytest -m "api and unit"
```

## pytest.ini Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers
markers =
    slow: slow running tests
    api: API tests
```

## pyproject.toml Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
minversion = "8.0"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

addopts = [
    "-v",
    "--strict-markers",
    "--tb=short",
]

markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "api: marks tests as API tests",
]
```

## Test Coverage with pytest-cov

Install:
```bash
pip install pytest-cov
```

Run with coverage:
```bash
pytest --cov=src --cov-report=html
pytest --cov=src --cov-report=term
```

Coverage in config:
```ini
# pytest.ini
[pytest]
addopts = --cov=src --cov-report=html --cov-fail-under=80
```

This fails tests if coverage is below 80%.

## Complete Example

```python
# conftest.py
import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: slow running tests")
    config.addinivalue_line("markers", "api: API tests")
    config.addinivalue_line("markers", "unit: unit tests")
```

```python
# test_example.py
import pytest

@pytest.mark.unit
def test_calculator_add():
    assert 1 + 1 == 2

@pytest.mark.api
@pytest.mark.slow  
def test_api_get():
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
```

```bash
# Run all tests
pytest

# Run only unit tests
pytest -m unit

# Run only API tests (not slow)
pytest -m "api and not slow"

# Run with coverage
pytest --cov=. --cov-report=html
```

---

## Summary

| Command | Description |
|---------|-------------|
| `pytest -m slow` | Run slow tests |
| `pytest -m "api and not slow"` | API tests excluding slow |
| `pytest --cov=src` | Run with coverage |
| `pytest -k "test_name"` | Run by pattern |

---

**Congratulations!** You have completed the pytest learning path.

**Next Steps:**
- Practice with real APIs
- Explore pytest plugins
- Set up CI/CD with GitHub Actions
