---
id: 11-Testing
tags:
  - rest-api
  - testing
dg-publish: true
---

# Testing REST APIs

How to test your REST API endpoints.

## Testing Tools

| Tool | Description |
|------|-------------|
| Postman | GUI API client |
| curl | Command line |
| pytest | Python testing |
| Newman | Postman CLI |

## Testing with curl

### GET Request

```bash
curl https://api.example.com/users/1
```

### POST Request

```bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'
```

### With Authentication

```bash
curl https://api.example.com/users \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Testing with pytest

```python
import requests

def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_create_user():
    payload = {"name": "John", "email": "john@example.com"}
    response = requests.post(
        "https://api.example.com/users",
        json=payload
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John"
```

## What to Test

### Happy Path

- All endpoints return correct data
- Status codes are correct
- Response format matches

### Edge Cases

- Empty results
- Maximum limits
- Special characters
- Null values

### Error Cases

- Invalid input
- Unauthorized access
- Not found scenarios
- Rate limiting

### Performance

- Response time
- Concurrent requests
- Large payloads

---

**See Also:** [[pytest-learning/00-Setup]] - pytest setup for API testing