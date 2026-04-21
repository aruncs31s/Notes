---
id: 06-API-Testing-Intro
tags: [api, testing, rest]
dg-publish: false
---

# API Testing Introduction

Learn the basics of testing REST APIs with pytest.

## What is an API?

An API (Application Programming Interface) allows applications to communicate. REST APIs use HTTP requests.

## HTTP Methods

| Method | Description | Common Use |
|--------|-------------|------------|
| GET | Retrieve data | Fetch resources |
| POST | Create new data | Submit forms |
| PUT | Update entire resource | Replace data |
| PATCH | Partial update | Modify部分数据 |
| DELETE | Remove data | Delete resources |

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created |
| 204 | No Content - Success, no response body |
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Missing/invalid auth |
| 403 | Forbidden - No permission |
| 404 | Not Found - Resource doesn't exist |
| 500 | Server Error - Internal error |

## Installing Requests

```bash
pip install requests
```

## First API Test

```python
import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    # Check status code
    assert response.status_code == 200
    
    # Get JSON data
    data = response.json()
    
    # Assert data
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "email" in data
```

## Running the Test

```bash
pytest test_api.py -v -s
```

## Common Response Properties

```python
response = requests.get("https://api.example.com/data")

# Response attributes
response.status_code    # HTTP status code
response.headers        # Response headers
response.json()         # Parse JSON body
response.text           # Raw text body
response.content        # Binary content
response.cookies        # Cookies
response.elapsed        # Response time
```

## Test API for Practice

Free APIs to practice with:

| API | Description |
|-----|-------------|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake REST API |
| [ReqRes](https://reqres.in/) | Test API |
| [HTTPBin](https://httpbin.org/) | HTTP testing |
| [Public APIs](https://github.com/public-apis/public-apis) | List of free APIs |

## Setup with Fixtures

```python
import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client(base_url):
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
        
        def get(self, endpoint):
            return self.session.get(self.base_url + endpoint)
        
        def post(self, endpoint, json=None):
            return self.session.post(self.base_url + endpoint, json=json)
    
    return APIClient(base_url)


def test_get_user(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
```

## Practice

1. Make a GET request to `https://jsonplaceholder.typicode.com/posts`
2. Assert the response status is 200
3. Assert the response is a list

---

**Next:** [[07-GET-Requests]] - Testing GET endpoints

**See Also:** [[08-POST-Requests]] - Testing POST endpoints