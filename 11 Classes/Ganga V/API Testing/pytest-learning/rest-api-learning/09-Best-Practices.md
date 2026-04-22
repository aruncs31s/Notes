---
id: 09-Best-Practices
tags:
  - rest-api
  - best-practices
dg-publish: true
---

# REST API Best Practices

Guidelines for building great APIs.

## Design Principles

### 1. Use Nouns for Resources

```http
GET /users          # Good
GET /getUsers       # Bad
```

### 2. Use Plural Nouns

```http
/users              # Good
/user               # Bad
```

### 3. Use HTTP Methods Correctly

```http
GET /users/1        # Read
POST /users         # Create
PUT /users/1        # Replace
PATCH /users/1      # Update
DELETE /users/1    # Delete
```

### 4. Use Proper Status Codes

- `200` for successful GET/PUT/PATCH
- `201` for successful POST
- `204` for successful DELETE
- `400` for bad request
- `401/403` for auth errors
- `404` for not found

### 5. Version Your API

```http
GET /v1/users
GET /v2/users
```

### 6. Use Pagination

```http
GET /users?page=1&limit=10
```

### 7. Return Relevant Headers

```http
X-Total-Count: 100
X-Page: 1
Link: <https://api.com/users?page=2>; rel="next"
```

### 8. Secure Your API

- Always use HTTPS
- Implement authentication
- Validate all input
- Sanitize output

### 9. Document Everything

- Clear descriptions
- Request/response examples
- Error codes
- Authentication requirements

### 10. Be Consistent

- Same patterns everywhere
- Consistent naming
- Consistent error format

---

**Next:** [[10-Documentation]] - API documentation

**See Also:** [[05-URL-Design]] - URL design