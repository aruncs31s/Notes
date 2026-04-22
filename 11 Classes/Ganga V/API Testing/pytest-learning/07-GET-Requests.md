---
id: 07-GET-Requests
tags:
  - api
  - get
  - http
dg-publish: true
---

# Testing GET Requests

Learn to test GET endpoints for retrieving data.

## What is GET?

GET requests retrieve data from a server. They should not modify data.

## Basic GET Test

```python
import requests

def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
```

## GET with Query Parameters

```python
def test_get_posts_by_user():
    params = {"userId": 1}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )
    
    assert response.status_code == 200
    posts = response.json()
    
    # All posts should be from user 1
    for post in posts:
        assert post["userId"] == 1


def test_get_with_multiple_params():
    params = {
        "userId": 1,
        "_limit": 5
    }
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 5
```

## GET with Headers

```python
def test_get_with_headers():
    headers = {
        "Authorization": "Bearer your_token_here",
        "Accept": "application/json"
    }
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers
    )
    
    assert response.status_code == 200
```

## Testing 404 (Not Found)

```python
def test_get_nonexistent_resource():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/999999"
    )
    
    assert response.status_code == 404


def test_get_with_invalid_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/invalid"
    )
    
    assert response.status_code == 404
```

## Using Fixtures for GET Tests

```python
import pytest
import requests

@pytest.fixture
def api():
    return "https://jsonplaceholder.typicode.com"


def test_get_users(api):
    response = requests.get(f"{api}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id(api):
    response = requests.get(f"{api}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert "@" in data["email"]


def test_get_user_posts(api):
    response = requests.get(f"{api}/posts?userId=1")
    data = response.json()
    assert response.status_code == 200
    assert all(post["userId"] == 1 for post in data)
```

## Practice

Test these GET endpoints:

1. Get all users from JSONPlaceholder
2. Get a single comment by ID
3. Get posts filtered by userId
4. Verify 404 for non-existent resource

---

**Next:** [[08-POST-Requests]] - Testing POST endpoints

**See Also:** [[09-Response-Assertions]] - More response assertions