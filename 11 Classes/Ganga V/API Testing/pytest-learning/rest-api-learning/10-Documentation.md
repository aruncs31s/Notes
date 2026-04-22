---
id: 10-Documentation
tags:
  - rest-api
  - documentation
  - openapi
  - swagger
dg-publish: true
---

# API Documentation

Tools and practices for documenting your API.

## OpenAPI Specification

Industry standard for API documentation:

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
```

## Swagger/OpenAPI Tools

| Tool | Purpose |
|------|---------|
| Swagger UI | Interactive docs |
| ReDoc | Beautiful docs |
| Redocly | Enterprise docs |
| Stoplight | Design & document |

## What to Document

### Endpoints

- URL and method
- Parameters (path, query, body)
- Request body schema
- Response schema
- Status codes
- Example requests/responses

### Authentication

- How to authenticate
- Example tokens
- Scopes/permissions

### Errors

- Error codes
- Error formats
- Common errors

## Documentation Best Practices

1. **Be complete** - Cover everything
2. **Be accurate** - Keep updated
3. **Be examples** - Show working examples
4. **Be searchable** - Easy to find
5. **Be interactive** - Try-it-out feature

---

**Next:** [[11-Testing]] - Testing REST APIs

**See Also:** [[09-Best-Practices]] - Best practices