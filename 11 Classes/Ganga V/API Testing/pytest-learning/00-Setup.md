---
id: 00-Setup
tags: [pytest, setup, installation]
dg-publish: false
---

# Setup & Installation

This guide covers setting up pytest for your development environment.

## Why Use a Virtual Environment?

A virtual environment isolates dependencies per project, preventing version conflicts.

## Installation Steps

### 1. Create a Project Directory

```bash
mkdir pytest-demo
cd pytest-demo
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Environment


**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install pytest

```bash
pip install pytest
```

### 5. Verify Installation

```bash
pytest --version
```

Expected output:
```
pytest 8.x.x
```

## Common Issues

| Issue | Solution |
|-------|----------|
| pytest: command not found | Activate venv or use `python -m pytest` |
| Permission denied | Use `pip install --user pytest` |
| Wrong Python version | Use `python3` explicitly |

## Recommended Additional Packages

```bash
# For API testing
pip install requests

# For mocking
pip install requests-mock

# For coverage
pip install pytest-cov

# For parallel test execution
pip install pytest-xdist
```

## Quick Test

Verify everything works:

```python
# test_verify.py
def test_pytest_works():
    assert 1 + 1 == 2
```

Run:
```bash
pytest test_verify.py -v
```

---

**Next:** [[01-First-Test]] - Write your first test