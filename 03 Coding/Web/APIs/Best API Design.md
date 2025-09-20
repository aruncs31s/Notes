---
id: Best_API_Design
aliases: []
tags:
  - coding
  - web
  - apis
dg-publish: true
---
# Best API Design Practices

## 1. Resource-Based URLs

### Use Nouns, Not Verbs
- ✅ `GET /users` (get all users)
- ✅ `POST /users` (create a new user)
- ❌ `GET /getUsers`
- ❌ `POST /createUser`

### Use Plural Nouns for Collections
- ✅ `/users` (collection of users)
- ✅ `/products` (collection of products)
- ❌ `/user`

### Hierarchical Resource Structure

```

/users/{userId}/orders/{orderId}
/companies/{companyId}/employees/{employeeId}

```

## 2. HTTP Methods (Verbs)

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve data | `GET /users/123` |
| POST | Create new resource | `POST /users` |
| PUT | Update entire resource | `PUT /users/123` |
| PATCH | Partial update | `PATCH /users/123` |
| DELETE | Remove resource | `DELETE /users/123` |

## 3. HTTP Status Codes

### Success Codes (2xx)
- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE

### Client Error Codes (4xx)
- `400 Bad Request` - Invalid request syntax
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource doesn't exist
- `409 Conflict` - Resource conflict
- `422 Unprocessable Entity` - Validation errors

### Server Error Codes (5xx)
- `500 Internal Server Error` - General server error
- `503 Service Unavailable` - Server temporarily unavailable

## 4. Consistent Response Format

### Success Response

```json
{
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2025-08-02T10:30:00Z",
    "version": "1.0"
  }
}

```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  },
  "meta": {
    "timestamp": "2025-08-02T10:30:00Z",
    "request_id": "req_123456"
  }
}

```

## 5. Pagination

### Offset-Based Pagination

```

GET /users?page=2&limit=20

```

### Cursor-Based Pagination (Recommended for large datasets)

```

GET /users?after=cursor_abc123&limit=20

```

### Response Format

```json
{
  "data": [...],
  "pagination": {
    "total": 1000,
    "page": 2,
    "limit": 20,
    "has_next": true,
    "has_previous": true,
    "next_cursor": "cursor_def456"
  }
}

```

## 6. Filtering and Sorting

### Filtering

```

GET /users?status=active&role=admin
GET /products?category=electronics&price_min=100&price_max=500

```

### Sorting

```

GET /users?sort=created_at:desc
GET /products?sort=price:asc,name:desc

```

### Search

```

GET /users?search=john
GET /products?q=smartphone

```

## 7. Versioning

### URL Path Versioning (Recommended)

```

/v1/users
/v2/users

```

### Header Versioning

```

Accept: application/vnd.api+json;version=1
API-Version: 1

```

### Query Parameter Versioning

```

/users?version=1

```

## 8. Authentication & Authorization

### Bearer Token (JWT)

```

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

```

### API Key

```

X-API-Key: your-api-key-here

```

### OAuth 2.0

```

Authorization: Bearer oauth2-access-token

```

## 9. Rate Limiting

### Response Headers

```

X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1625097600
Retry-After: 3600

```

### Rate Limit Exceeded Response

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 1 hour."
  }
}

```

## 10. Security Best Practices

### HTTPS Only
- Always use HTTPS in production
- Redirect HTTP to HTTPS

### Input Validation
- Validate all input parameters
- Use whitelisting over blacklisting
- Sanitize user input

### CORS Configuration

```javascript
// Allow specific origins
Access-Control-Allow-Origin: https://yourapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization

```

### Security Headers

```

Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block

```

## 11. Documentation

### OpenAPI/Swagger Specification

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get all users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: List of users

```

### Include Examples
- Provide request/response examples
- Document error scenarios
- Include authentication examples

## 12. Performance Optimization

### Caching

```

Cache-Control: public, max-age=3600
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"

```

### Compression

```

Content-Encoding: gzip
Accept-Encoding: gzip, deflate

```

### Field Selection

```

GET /users?fields=id,name,email

```

## 13. Error Handling

### Consistent Error Structure

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 123 not found",
    "details": {
      "user_id": 123,
      "timestamp": "2025-08-02T10:30:00Z"
    },
    "help": "https://api.example.com/docs/errors/user-not-found"
  }
}

```

### Validation Errors

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "violations": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Email must be a valid email address"
      },
      {
        "field": "age",
        "code": "OUT_OF_RANGE",
        "message": "Age must be between 18 and 100"
      }
    ]
  }
}

```

## 14. Testing

### Contract Testing
- Use tools like Pact for consumer-driven contracts
- Test API contracts between services

### Load Testing
- Test API performance under load
- Identify bottlenecks and rate limits

### Security Testing
- Test for common vulnerabilities (OWASP Top 10)
- Perform penetration testing

## 15. Monitoring & Logging

### Request Logging

```json
{
  "timestamp": "2025-08-02T10:30:00Z",
  "method": "GET",
  "path": "/users/123",
  "status_code": 200,
  "response_time": 150,
  "user_id": "user_456",
  "request_id": "req_789"
}

```

### Metrics to Track
- Response times
- Error rates
- Request volume
- API usage patterns
- Rate limit hits

## Key Takeaways

1. **Be Consistent** - Follow the same patterns throughout your API
2. **Use Standard HTTP** - Leverage HTTP methods and status codes properly
3. **Think Resource-Oriented** - Design around resources, not actions
4. **Version Early** - Plan for API evolution from the start
5. **Document Everything** - Good documentation is crucial for adoption
6. **Security First** - Implement security measures from day one
7. **Monitor & Measure** - Track API usage and performance
8. **Test Thoroughly** - Test all scenarios including edge cases

## Checkout 
1. https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
2. https://swagger.io/resources/articles/best-practices-in-api-design/
3. https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design