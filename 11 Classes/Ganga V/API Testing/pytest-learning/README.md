---
id: Pytest-Learning
tags:
  - pytest
  - python
  - testing
  - api-testing
cssclasses: []
dg-publish: true
dg-home: true
---

# Pytest Learning Path
![[README.png]]

These are separate notes you can go one by one.

Refresh Python and REST API Basics.
- [[11 Classes/Ganga V/API Testing/pytest-learning/python/python|python]]
	- [[01-Variables]] - Variables & Data Types
	- [[02-Operations]] - String, List, Dictionary operations
	- [[03-Control-Flow]] - If-else, For, While loops
	- [[04-Functions]] - Functions, args, kwargs
	- [[05-Comprehensions]] - List & Dict comprehensions
	- [[06-Classes]] - OOP classes
	- [[07-Modules]] - datetime, requests, mock
	- [[08-Exception-Handling]] - Try-except, raise
	- [[09-JSON]] - JSON parsing
	- [[10-Files]] - File I/O
	- [[11-Built-in-Functions]] - Built-in functions
	- [[12-Testing-Patterns]] - Testing assertions

- [[11 Classes/Ganga V/API Testing/pytest-learning/rest-api-learning/README|REST API Basics]]
	- [[00-REST-API-Intro]] - What is REST?
	- [[01-HTTP-Methods]] - GET, POST, PUT, DELETE
	- [[02-Status-Codes]] - HTTP status codes
	- [[03-Headers]] - HTTP headers
	- [[04-Authentication]] - Auth methods
	- [[05-URL-Design]] - Endpoint naming
	- [[06-Versioning]] - API versioning
	- [[07-Error-Handling]] - Error responses
	- [[08-Rate-Limiting]] - Rate limiting
	- [[09-Best-Practices]] - Design guidelines
	- [[10-Documentation]] - API docs
	- [[11-Testing]] - Testing REST APIs


---

- [[00-Setup]]
- [[01-First-Test]]
- [[02-Running-Tests]]
- [[03-Assertions]]
- [[04-Fixtures]]
- [[05-Parameterized-Tests]]
- [[06-API-Testing-Intro]]
- [[07-GET-Requests]]
- [[08-POST-Requests]]
- [[09-Response-Assertions]]
- [[10-Mocking]]
- [[11-Conftest]]
- [[12-Marks-And-Config]]


## Overview

- **Goal**: Learn pytest for API testing
- **Duration**: 10 weeks ( 1 hour/week)
- **Level**: Beginner Python

## Learning Path

### Phase 0: Refresh (Week 0)

- [[11 Classes/Ganga V/API Testing/pytest-learning/python/python|python]]
Just read through this.


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
