---
id: Pytest-Learning
tags: [pytest, python, testing, api-testing]
cssclasses: []
dg-publish: false
---

# Pytest Learning Path

Welcome to the pytest learning journey! This folder contains comprehensive notes for learning pytest for API testing.

## Overview

- **Goal**: Learn pytest for API testing
- **Duration**: 10 weeks (1-2 hours/week)
- **Level**: Beginner Python

## Learning Path

### Phase 1: Foundations (Weeks 1-2)

| Day | Topic | Note |
|-----|-------|------|
| 1 | Installation & Setup | [[00-Setup]] |
| 2 | Your First Test | [[01-First-Test]] |
| 3 | Running Tests | [[02-Running-Tests]] |
| 4 | Assertions | [[03-Assertions]] |
| 5 | Fixtures | [[04-Fixtures]] |

### Phase 2: Core Concepts (Weeks 3-4)

| Day | Topic | Note |
|-----|-------|------|
| 6 | Parameterized Tests | [[05-Parameterized-Tests]] |
| 7 | Test Organization | [[02-Running-Tests#Test Organization]] |
| 8 | Marks & Config | [[12-Marks-And-Config]] |
| 9 | Shared Fixtures | [[11-Conftest]] |
| 10 | Practice & Review | Practice exercises |

### Phase 3: API Testing (Weeks 5-8)

| Day | Topic | Note |
|-----|-------|------|
| 11 | API Testing Intro | [[06-API-Testing-Intro]] |
| 12 | GET Requests | [[07-GET-Requests]] |
| 13 | POST Requests | [[08-POST-Requests]] |
| 14 | Response Assertions | [[09-Response-Assertions]] |
| 15 | Mocking | [[10-Mocking]] |

### Phase 4: Advanced (Weeks 9-10)

| Day | Topic | Note |
|-----|-------|------|
| 16 | Coverage | [[12-Marks-And-Config#Coverage]] |
| 17 | Best Practices | All notes combined |
| 18 | CI/CD Integration | See external resources |

## Quick Reference

### Common Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Stop on first failure
pytest -x

# Run specific test file
pytest tests/test_api.py

# Run tests matching pattern
pytest -k "test_user"

# Run with coverage
pytest --cov=src --cov-report=html
```

### Test Discovery Rules

- Files: `test_*.py` or `*_test.py`
- Functions: `test_*()`
- Classes: `Test*`

## Resources

- [Real Python - pytest Tutorial](https://realpython.com/pytest-python-testing/)
- [pytest Documentation](https://docs.pytest.org/)
- [Pytest with Eric](https://pytest-with-eric.com/)

## Practice Projects

See `../practice/` folder for hands-on exercises.

---

*Last updated: 2026-04-22*
