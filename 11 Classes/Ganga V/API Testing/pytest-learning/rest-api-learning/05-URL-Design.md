---
id: 05-URL-Design
tags:
  - rest-api
  - url
  - naming
  - endpoints
dg-publish: true
---

# URL Design

Best practices for naming API endpoints.

## Resource Naming

### Good Practices

```
/users                 # Plural nouns
/users/1               # Resource ID
/users/1/posts          # Nested resources
/posts?userId=1&status=published  # Filtering
/posts?sort=-createdAt&limit=10  # Sorting & pagination
```

### Bad Practices

```
/getUsers              # Don't use verbs
/GetUserById/1        # Don't use camelCase
/user/1/post           # Inconsistent plural
/index.php?action=get  # Technical details exposed
```

## URL Structure

```
https://api.example.com/v1/users/1/posts?page=1&limit=10

[scheme]://[domain]/[version]/[resource]/[id]/[sub-resource]?[query]
```

## Filtering, Sorting, Pagination

### Filtering

```http
GET /posts?userId=1
GET /posts?status=published&category=tech
```

### Sorting

```http
GET /posts?sort=createdAt          # Ascending
GET /posts?sort=-createdAt        # Descending
GET /posts?sort=name,-createdAt   # Multiple fields
```

### Pagination

```http
GET /posts?page=1&limit=10
GET /posts?offset=0&limit=10
GET /posts?cursor=abc123
```

## Nested Resources

Use for hierarchical relationships:

```
/users/1                  # User 1
/users/1/posts             # User 1's posts
/users/1/posts/1/comments   # User 1's post 1's comments
```

## Versioning in URL

```http
/v1/users
/v2/users
```

---

**Next:** [[06-Versioning]] - API versioning strategies

**See Also:** [[00-REST-API-Intro]] - REST basics