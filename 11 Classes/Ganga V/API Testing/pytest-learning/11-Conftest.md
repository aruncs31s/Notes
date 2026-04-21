---
id: 11-Conftest
tags: [pytest, conftest, fixtures]
dg-publish: false
---

# Shared Fixtures with conftest.py

`conftest.py` is a special file that shares fixtures across multiple test files.

## What is conftest.py?

- A Python file named `conftest.py`
- Automatically loaded by pytest
- Fixtures in this file are available to all tests in that directory

## Basic conftest.py

```python
# conftest.py (in tests/ folder)
import pytest
import requests

@pytest.fixture
def api_base_url():
    """Base URL for the API"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client(api_base_url):
    """Reusable API client"""
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
        
        def get(self, endpoint):
            return self.session.get(self.base_url + endpoint)
        
        def post(self, endpoint, data):
            return self.session.post(self.base_url + endpoint, json=data)
        
        def delete(self, endpoint):
            return self.session.delete(self.base_url + endpoint)
    
    return APIClient(api_base_url)
```

Now use in any test file:

```python
# tests/test_users.py
def test_get_user(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
```

```python
# tests/test_posts.py
def test_get_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
```

## Example conftest.py for API Testing

```python
# conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """API base URL"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def session_client(base_url):
    """Requests session with base URL configured"""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


@pytest.fixture
def sample_user():
    """Sample user data for tests"""
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }


@pytest.fixture
def sample_post():
    """Sample post data"""
    return {
        "title": "Test Post",
        "body": "This is test content",
        "userId": 1
    }
```

Using in tests:

```python
# test_api.py
def test_get_user(session_client, base_url):
    response = session_client.get(f"{base_url}/users/1")
    assert response.status_code == 200


def test_create_post(session_client, base_url, sample_post):
    response = session_client.post(f"{base_url}/posts", json=sample_post)
    assert response.status_code == 201
```

## Multiple conftest.py Files

```
project/
├── conftest.py          # Root - available to all tests
├── tests/
│   ├── conftest.py     # Tests folder - overrides root
│   ├── test_api.py
│   ├── test_users.py
│   └── test_posts/
│       ├── conftest.py  # Posts folder
│       └── test_posts.py
```

Each `conftest.py` only loads fixtures from its directory and parent directories.

## Adding Hooks in conftest.py

```python
# conftest.py
import pytest

@pytest.fixture(autouse=True)
def print_test_name(request):
    """Print test name before each test"""
    print(f"\nRunning: {request.node.name}")
    yield
```

## Pytest Config in conftest.py

```python
# conftest.py
def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line("markers", "api: mark test as API test")
    config.addinivalue_line("markers", "slow: mark test as slow")
```

## Best Practices

1. Keep fixtures focused and simple
2. Use clear, descriptive names
3. Set appropriate scope (session/module/class/function)
4. Document fixtures with docstrings

---

**Next:** [[12-Marks-And-Config]] - pytest configuration

**See Also:** [[04-Fixtures]] - More about fixtures