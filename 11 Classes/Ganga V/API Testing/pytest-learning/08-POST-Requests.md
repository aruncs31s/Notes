---
id: 08-POST-Requests
tags:
  - api
  - post
  - http
dg-publish: true
---

# Testing POST Requests

Learn to test POST endpoints for creating data.

## What is POST?

POST requests send data to create new resources.

## Basic POST Test

```python
import requests

def test_create_post():
    payload = {
        "title": "My New Post",
        "body": "This is the post content",
        "userId": 1
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My New Post"
    assert "id" in data  # Server assigns ID
```

## POST with JSON Body

```python
def test_create_user():
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    
    # Server echoes back the data with new ID
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data
```

## POST with Form Data

```python
def test_create_post_form():
    data = {
        "title": "Form Post",
        "body": "Content",
        "userId": 1
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=data
    )
    
    assert response.status_code == 201
```

## POST with Headers

```python
def test_create_with_auth():
    headers = {
        "Authorization": "Bearer my_token",
        "Content-Type": "application/json"
    }
    
    payload = {"title": "Private Post", "userId": 1, "body": "..."}
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload,
        headers=headers
    )
    
    assert response.status_code == 201
```

## Testing Invalid POST

```python
def test_create_post_missing_required_field():
    payload = {
        "title": "Missing body and userId"
        # Missing required fields
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    
    # JSONPlaceholder always returns 201, but real APIs might return 400
    assert response.status_code in [201, 400]


def test_create_post_invalid_data():
    payload = {"userId": "not_a_number"}  # Invalid type
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    
    # Some APIs return 400 for invalid data
    assert response.status_code in [201, 400]
```

## Complete POST Test Example

```python
import pytest
import requests

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"


class TestPOSTRequests:
    
    def test_create_post_success(self, api_url):
        payload = {
            "title": "Test Post",
            "body": "Test body content",
            "userId": 1
        }
        
        response = requests.post(f"{api_url}/posts", json=payload)
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["userId"] == payload["userId"]
        assert "id" in data
    
    def test_create_post_empty_body(self, api_url):
        payload = {}
        
        response = requests.post(f"{api_url}/posts", json=payload)
        
        assert response.status_code in [201, 400]
    
    def test_create_comment(self, api_url):
        payload = {
            "postId": 1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a comment"
        }
        
        response = requests.post(f"{api_url}/comments", json=payload)
        
        assert response.status_code == 201
        assert response.json()["postId"] == 1
```

## Practice

1. Create a new post with valid data
2. Create a post and verify the response contains the created ID
3. Test creating a comment on a post
4. Test POST with invalid/empty data

---

**Next:** [[09-Response-Assertions]] - Response assertions

**See Also:** [[10-Mocking]] - Mocking APIs