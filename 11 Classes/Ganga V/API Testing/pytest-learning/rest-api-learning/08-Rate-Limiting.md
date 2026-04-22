---
id: 08-Rate-Limiting
tags:
  - rest-api
  - rate-limiting
  - throttling
dg-publish: true
---

# Rate Limiting

Controlling API usage to protect your service.

## Why Rate Limit?

- Prevent abuse
- Protect infrastructure
- Ensure fair usage
- Reduce costs

## Rate Limit Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1640000000
Retry-After: 60
```

## Common Rate Limits

| Plan | Requests |
|------|----------|
| Free | 100/hour |
| Basic | 1000/hour |
| Pro | 10000/hour |
| Enterprise | Unlimited |

## Rate Limit Strategies

### Fixed Window

```
60 requests per minute
→ Count resets at :00, :01, :02...
```

### Sliding Window

```
60 requests per minute
→ Rolling window, smoother
```

### Token Bucket

```
100 tokens, refills 10/second
→ Burst allowed, then limited
```

## Handling Rate Limits

Client side:

```python
import time

def make_request(url):
    response = requests.get(url)
    
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 60))
        print(f"Rate limited. Waiting {retry_after}s")
        time.sleep(retry_after)
        return make_request(url)
    
    return response
```

---

**Next:** [[09-Best-Practices]] - REST best practices

**See Also:** [[07-Error-Handling]] - Error handling