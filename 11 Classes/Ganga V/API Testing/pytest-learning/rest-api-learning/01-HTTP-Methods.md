---
id: 01-HTTP-Methods
tags:
  - rest-api
  - http
  - methods
  - crud
dg-publish: true
---

# HTTP Methods

The verbs that tell the server what action to perform.

## CRUD Operations

| Method | CRUD | Description |
|--------|------|-------------|
| GET | Read | Retrieve data |
| POST | Create | Create new resource |
| PUT | Update | Replace entire resource |
| PATCH | Update | Partial update |
| DELETE | Delete | Remove resource |

## GET

Retrieve data (should be idempotent and safe):

```http
GET /users
GET /users/1
GET /posts?userId=1
```

## POST

Create new resource:

```http
POST /users
Body: {"name": "John", "email": "john@example.com"}
```

Returns: `201 Created` with location header

## PUT

Replace entire resource (idempotent):

```http
PUT /users/1
Body: {"name": "Jane", "email": "jane@example.com"}
```

## PATCH

Partial update to resource:

```http
PATCH /users/1
Body: {"email": "newemail@example.com"}
```

## DELETE

Remove resource (idempotent):

```http
DELETE /users/1
```

Returns: `204 No Content`

## Method Properties

| Method | Safe | Idempotent |
|--------|------|----------|
| GET | Yes | Yes |
| POST | No | No |
| PUT | No | Yes |
| PATCH | No | No |
| DELETE | No | Yes |

- **Safe**: Doesn't modify data
- **Idempotent**: Same result when called multiple times

---

**Next:** [[02-Status-Codes]] - HTTP status codes

**See Also:** [[00-REST-API-Intro]] - REST basics