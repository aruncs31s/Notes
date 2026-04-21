---
id: 09-Response-Assertions
tags: [api, assertions, response]
dg-publish: false
---

# Response Assertions

Learn to thoroughly assert API responses.

## Status Code Assertions

```python
import requests

def test_status_codes():
    # GET - OK
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    
    # POST - Created
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "x", "userId": 1})
    assert response.status_code == 201
    
    # DELETE - No Content
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200  # JSONPlaceholder returns 200
    # Real API might return 204
```

## JSON Data Assertions

```python
def test_json_structure():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    
    # Check keys exist
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "address" in data
    
    # Check nested structure
    assert "street" in data["address"]
    assert "geo" in data["address"]


def test_json_values():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    
    # Check specific values
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]
```

## List Response Assertions

```python
def test_list_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    
    # It's a list
    assert isinstance(data, list)
    assert len(data) == 100  # JSONPlaceholder has 100 posts
    
    # Check first item structure
    if data:
        first = data[0]
        assert "id" in first
        assert "title" in first


def test_filtered_list():
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
    data = response.json()
    
    # All items should match filter
    assert all(post["userId"] == 1 for post in data)
```

## Headers Assertions

```python
def test_response_headers():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    # Check content type
    assert "application/json" in response.headers.get("Content-Type", "")
    
    # Check other headers
    assert "Content-Length" in response.headers
```

## Response Time Assertions

```python
import time

def test_response_time():
    start = time.time()
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    elapsed = time.time() - start
    
    assert response.status_code == 200
    assert elapsed < 2.0  # Should respond within 2 seconds
```

## Complete API Test Example

```python
import pytest
import requests
import time

@pytest.fixture
def api():
    return "https://jsonplaceholder.typicode.com"


class TestUserAPI:
    
    def test_get_user_success(self, api):
        response = requests.get(f"{api}/users/1")
        
        # Status check
        assert response.status_code == 200
        
        # JSON parsing
        data = response.json()
        assert data["id"] == 1
        
        # Required fields
        assert "name" in data
        assert "email" in data
        assert "phone" in data
        assert "website" in data
        
        # Email format
        assert "@" in data["email"]
        
        # Nested objects
        assert "address" in data
        assert "company" in data
    
    def test_get_user_not_found(self, api):
        response = requests.get(f"{api}/users/999999")
        assert response.status_code == 404
    
    def test_get_users_list(self, api):
        response = requests.get(f"{api}/users")
        
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0
        assert all("id" in user for user in users)
```

## Practice

Write assertions for:

1. A GET /users response - verify structure and user count
2. A POST response - verify created resource
3. Response time check
4. Headers verification

---

**Next:** [[10-Mocking]] - Mocking external APIs

**See Also:** [[11-Conftest]] - Shared fixtures