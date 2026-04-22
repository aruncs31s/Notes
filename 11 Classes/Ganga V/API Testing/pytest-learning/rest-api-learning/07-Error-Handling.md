---
id: 07-Error-Handling
tags:
  - rest-api
  - errors
  - exceptions
dg-publish: true
---

# Error Handling

Consistent error responses for better developer experience.

## Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ],
    "requestId": "abc123"
  }
}
```

## Common Error Codes

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Request body is invalid"
  }
}
```

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found",
    "details": {
      "resource": "user",
      "id": 999
    }
  }
}
```

```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests",
    "retryAfter": 60
  }
}
```

## Error Code Reference

| Code | HTTP Status | Description |
|------|------------|-------------|
| INVALID_REQUEST | 400 | Malformed request |
| UNAUTHORIZED | 401 | Missing/invalid auth |
| FORBIDDEN | 403 | No permission |
| NOT_FOUND | 404 | Resource missing |
| VALIDATION_ERROR | 422 | Invalid data |
| RATE_LIMITED | 429 | Too many requests |
| INTERNAL_ERROR | 500 | Server error |

## Best Practices

1. **Consistent format** - Same structure for all errors
2. **Include request ID** - For debugging
3. **User-friendly messages** - For end users
4. **Detailed errors** - For developers
5. **Log errors server-side** - Don't expose internals

---

**Next:** [[08-Rate-Limiting]] - Rate limiting

**See Also:** [[02-Status-Codes]] - HTTP status codes