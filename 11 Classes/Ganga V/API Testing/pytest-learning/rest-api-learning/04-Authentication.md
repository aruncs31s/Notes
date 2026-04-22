---
id: 04-Authentication
tags:
  - rest-api
  - auth
  - security
dg-publish: true
---

# Authentication

Securing your API endpoints.

## No Authentication (Public)

```http
GET /posts
GET /posts/1
```

## API Key

Simple key-based authentication:

```http
X-API-Key: your-api-key-here
```

## Basic Authentication

Username and password:

```http
Authorization: Basic base64("user:pass")
```

## Bearer Token (OAuth 2.0)

Token-based authentication:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

## JWT Structure

```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE2MDAwMDAwMDAwMDAwfQ.signature
```

## When to Use What

| Method | Use Case |
|--------|---------|
| None | Public read-only APIs |
| API Key | Server-to-server |
| Basic | Simple apps (with HTTPS) |
| Bearer/JWT | User authentication |

## Security Best Practices

1. **Always use HTTPS** - Never send tokens over HTTP
2. **Token expiration** - Short-lived tokens
3. **Refresh tokens** - Rotate tokens securely
4. **Scope limiting** - Minimal permissions
5. **Rate limiting** - Prevent brute force

## Authorization vs Authentication

- **Authentication**: Who are you? (identity)
- **Authorization**: What can you do? (permissions)

---

**Next:** [[05-URL-Design]] - URL naming conventions

**See Also:** [[09-Best-Practices]] - Security best practices