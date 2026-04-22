---
id: 02-Status-Codes
tags:
  - rest-api
  - http
  - status-codes
dg-publish: true
---

# HTTP Status Codes

Tell the client the result of their request.

## 2xx Success

| Code | Meaning | Use |
|--------|---------|-----|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |

## 3xx Redirection

| Code | Meaning | Use |
|--------|---------|-----|
| 301 | Moved Permanently | Resource moved |
| 304 | Not Modified | Cached response |

## 4xx Client Errors

| Code | Meaning | Use |
|--------|---------|-----|
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method |
| 409 | Conflict | Resource conflict |
| 422 | Unprocessable Entity | Validation error |
| 429 | Too Many Requests | Rate limited |

## 5xx Server Errors

| Code | Meaning | Use |
|--------|---------|-----|
| 500 | Internal Server Error | Unexpected error |
| 502 | Bad Gateway | Upstream error |
| 503 | Service Unavailable | Server down |
| 504 | Gateway Timeout | Timeout |

## Choosing Status Codes

```
POST /users
  → 201 Created (new resource)
  → 400 Bad Request (invalid data)
  → 422 Unprocessable Entity (validation error)

GET /users/1
  → 200 OK (found)
  → 404 Not Found (doesn't exist)

DELETE /users/1
  → 204 No Content (deleted)
  → 404 Not Found (already gone)
```

---

**Next:** [[03-Headers]] - HTTP headers

**See Also:** [[07-Error-Handling]] - Error handling best practices