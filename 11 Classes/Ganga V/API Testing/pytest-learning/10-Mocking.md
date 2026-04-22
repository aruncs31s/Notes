---
id: 10-Mocking
tags:
  - mocking
  - unittest
  - api
dg-publish: true
---

# Mocking

Mocking replaces real API calls with simulated responses for testing.

## Why Mock?

- Test without relying on external APIs
- Faster tests (no network calls)
- Test edge cases and errors
- Avoid rate limits

## Install Mock Library

```bash
pip install requests-mock
# or use built-in unittest.mock
```

## Using unittest.mock

```python
import requests
from unittest.mock import patch, Mock

@patch('requests.get')
def test_get_user_mock(mock_get):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
    mock_get.return_value = mock_response
    
    # Call the function
    response = requests.get("https://api.example.com/users/1")
    
    # Assertions
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


@patch('requests.post')
def test_create_user_mock(mock_post):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "id": 123,
        "name": "Jane Doe",
        "email": "jane@example.com"
    }
    mock_post.return_value = mock_response
    
    # Call the function
    response = requests.post(
        "https://api.example.com/users",
        json={"name": "Jane Doe", "email": "jane@example.com"}
    )
    
    assert response.status_code == 201
    assert response.json()["id"] == 123
```

## Using requests-mock

```python
import requests
import requests_mock

def test_with_requests_mock():
    with requests_mock.Mocker() as m:
        # Mock GET
        m.get(
            "https://api.example.com/users/1",
            json={"id": 1, "name": "John"},
            status_code=200
        )
        
        response = requests.get("https://api.example.com/users/1")
        
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "John"}
```

## Mocking POST Requests

```python
def test_create_post_mock():
    with requests_mock.Mocker() as m:
        # Mock POST
        m.post(
            "https://api.example.com/posts",
            json={"id": 101, "title": "New Post"},
            status_code=201
        )
        
        response = requests.post(
            "https://api.example.com/posts",
            json={"title": "New Post", "userId": 1}
        )
        
        assert response.status_code == 201
        assert response.json()["id"] == 101
```

## Mocking Errors

```python
def test_mock_404():
    with requests_mock.Mocker() as m:
        m.get(
            "https://api.example.com/users/999",
            status_code=404,
            json={"error": "Not found"}
        )
        
        response = requests.get("https://api.example.com/users/999")
        
        assert response.status_code == 404


def test_mock_timeout():
    import requests.exceptions
    from requests_mock import Mocker
    
    with requests_mock.Mocker() as m:
        # Mock a timeout
        m.get(
            "https://api.example.com/slow",
            exc=requests.exceptions.Timeout
        )
        
        with pytest.raises(requests.exceptions.Timeout):
            requests.get("https://api.example.com/slow")
```

## Using Mocks with Fixtures

```python
import pytest
import requests
import requests_mock

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m


def test_with_fixture(mock_api):
    mock_api.get(
        "https://api.example.com/users",
        json=[{"id": 1, "name": "John"}]
    )
    
    response = requests.get("https://api.example.com/users")
    assert response.json() == [{"id": 1, "name": "John"}]


class TestWithMock:
    
    def test_get_users(self, mock_api):
        mock_api.get(
            "https://api.example.com/users",
            json=[{"id": 1}, {"id": 2}]
        )
        
        response = requests.get("https://api.example.com/users")
        assert len(response.json()) == 2
    
    def test_create_user(self, mock_api):
        mock_api.post(
            "https://api.example.com/users",
            json={"id": 1, "name": "New User"},
            status_code=201
        )
        
        response = requests.post(
            "https://api.example.com/users",
            json={"name": "New User"}
        )
        assert response.status_code == 201
```

## Practice

1. Mock a GET request to return user data
2. Mock a POST request and verify the request body
3. Mock a 404 response
4. Mock multiple endpoints in one test

---

**Next:** [[11-Conftest]] - Shared fixtures with conftest.py

**See Also:** [[12-Marks-And-Config]] - Configuration