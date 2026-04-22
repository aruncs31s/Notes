---
id: 00-REST-API-Intro
tags:
  - rest-api
  - basics
  - introduction
dg-publish: true
---

# REST API Introduction

Learn what REST APIs are and how they work.

## What is REST?

REST (Representational State Transfer) is an architectural style for designing web APIs.

## REST Principles

1. **Client-Server** - Clients and servers are independent
2. **Stateless** - Each request contains all information
3. **Cacheable** - Responses can be cached
4. **Uniform Interface** - Consistent resource identification

## Resources

Resources are the key abstractions in REST:

```
/users        # Collection of users
/users/1      # Single user
/posts        # Collection of posts
/posts/1      # Single post
```

## API vs REST API

| Aspect | API | REST API |
|--------|-----|---------|
| Protocol | Any | HTTP only |
| Format | Any | JSON (usually) |
| Structure | Varies | Resource-based |

## Practice

Identify resources in these URLs:
1. `/books/123`
2. `/orders/456/items`
3. `/products?category=electronics`

---

**Next:** [[01-HTTP-Methods]] - HTTP methods

**See Also:** [[05-URL-Design]] - URL naming conventions