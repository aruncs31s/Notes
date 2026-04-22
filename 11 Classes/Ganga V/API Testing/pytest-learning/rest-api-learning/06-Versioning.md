---
id: 06-Versioning
tags:
  - rest-api
  - versioning
dg-publish: true
---

# API Versioning

Managing API changes without breaking clients.

## Versioning Strategies

### URL Path (Most Common)

```http
GET /v1/users
GET /v2/users
```

Pros: Simple, visible
Cons: Multiple versions to maintain

### Query Parameter

```http
GET /users?version=1
GET /users?version=2
```

### Header

```http
GET /users
Accept-Version: v1
Accept-Version: v2
```

## When to Version

Create a new version when:
- Breaking change to response format
- Removing fields
- Changing field types
- Changing authentication

## When NOT to Version

Don't version for:
- Adding new optional fields
- Adding new endpoints
- Bug fixes
- New optional parameters

## Deprecation Strategy

1. Announce deprecation in headers
2. Provide migration timeline
3. Keep old version for grace period
4. Monitor usage before removing

```http
Deprecation: true
Sunset: Mon, 01 Jan 2025 00:00:00 GMT
Link: <https://api.example.com/v2/users>; rel="successor-version"
```

---

**Next:** [[07-Error-Handling]] - Error handling

**See Also:** [[05-URL-Design]] - URL design