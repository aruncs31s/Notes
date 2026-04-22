---
id: 03-Headers
tags:
  - rest-api
  - http
  - headers
dg-publish: true
---

# HTTP Headers

Metadata about requests and responses.

## Request Headers

### Content Negotiation

```http
Accept: application/json
Accept: application/xml
```

### Authentication

```http
Authorization: Bearer <token>
Authorization: Basic <base64>
```

### Custom Headers

```http
X-Request-ID: abc123
X-API-Key: your-api-key
```

## Response Headers

### Content Type

```http
Content-Type: application/json
```

### Cache Control

```http
Cache-Control: max-age=3600
Cache-Control: no-cache
```

### Rate Limiting

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1640000000
```

### Pagination

```http
X-Total-Count: 100
X-Page: 1
X-Per-Page: 10
```

## CORS Headers

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

## Common Headers Reference

| Header | Direction | Purpose |
|--------|----------|--------|
| Content-Type | Request/Response | Body format |
| Accept | Request | Preferred format |
| Authorization | Request | Authentication |
| Cache-Control | Response | Caching rules |
| X-Request-ID | Request/Response | Tracing |
| Location | Response | Resource URL |

---

**Next:** [[04-Authentication]] - Authentication methods

**See Also:** [[02-Status-Codes]] - Status codes