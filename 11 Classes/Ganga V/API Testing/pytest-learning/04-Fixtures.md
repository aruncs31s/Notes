---
id: 04-Fixtures
tags: [pytest, fixtures]
dg-publish: false
---

# Fixtures

Fixtures provide a way to set up and tear down test data or resources.

## What Are Fixtures?

Fixtures are functions decorated with `@pytest.fixture` that run before each test that uses them.

## Basic Fixture

```python
import pytest

@pytest.fixture
def sample_user():
    """Returns a sample user dictionary"""
    return {"name": "John", "email": "john@example.com"}


def test_user_name(sample_user):
    assert sample_user["name"] == "John"


def test_user_email(sample_user):
    assert sample_user["email"] == "john@example.com"
```

## Fixtures with Setup/Teardown

```python
import pytest

@pytest.fixture
def database_connection():
    """Setup: Create connection, Teardown: Close connection"""
    print("\n[Setup] Connecting to database...")
    conn = {"connected": True}
    
    yield conn  # Test runs here
    
    print("\n[Teardown] Closing database connection...")
    conn["connected"] = False


def test_query_database(database_connection):
    assert database_connection["connected"] is True
    # Perform queries...


def test_another_query(database_connection):
    assert database_connection["connected"] is True
```

Output with `-s`:
```
[Setup] Connecting to database...
test_file.py::test_query_database PASSED
[Teardown] Closing database connection...

[Setup] Connecting to database...
test_file.py::test_another_query PASSED
[Teardown] Closing database connection...
```

## Fixture Scope

Control when fixtures run:

```python
# Function scope (default) - runs before each test
@pytest.fixture
def my_fixture():
    return "function"


# Class scope - runs once per test class
@pytest.fixture(scope="class")
def class_fixture():
    return "class"


# Module scope - runs once per module
@pytest.fixture(scope="module")
def module_fixture():
    return "module"


# Session scope - runs once per session
@pytest.fixture(scope="session")
def session_fixture():
    return "session"
```

## Fixture with Arguments

```python
@pytest.fixture
def api_client():
    """Create an API client"""
    import requests
    return requests.Session()


def test_get_users(api_client):
    response = api_client.get("https://api.example.com/users")
    assert response.status_code == 200
```

## Using Fixtures in Multiple Files

Place fixtures in `conftest.py` - they're automatically shared:

```python
# conftest.py
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
```

Now use `base_url` in any test file in the same directory.

## Fixture as Dependency

```python
@pytest.fixture
def user_id():
    return 1


@pytest.fixture
def user_api_client(base_url):
    """API client that includes base URL"""
    import requests
    return requests.Session(base_url=base_url)


def test_get_user(user_id, user_api_client):
    response = user_api_client.get(f"/users/{user_id}")
    assert response.status_code == 200
```

## Practice

Create fixtures for:

1. A sample API response data
2. A temporary file (with teardown)
3. An authenticated API client

---

**Next:** [[05-Parameterized-Tests]] - Run tests with multiple inputs

**See Also:** [[11-Conftest]] - More about conftest.py