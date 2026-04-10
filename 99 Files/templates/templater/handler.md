---
title: "<% tp.file.title %>"
tags:
  - handler
  - api
  - go
  - etlab
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Handler

> [!note]- Purpose
> Gin HTTP handler for the **<% tp.file.title %>** endpoint. Documents DTOs, validation, error handling, and tests.

## Endpoint Spec

| Property | Value |
|---|---|
| **Method** | <% await tp.system.prompt("HTTP method (GET/POST/PUT/DELETE/PATCH)", "GET") %> |
| **Path** | <% await tp.system.prompt("Endpoint path (e.g., /api/v1/staff/{id})", "/api/...") %> |
| **Auth Required** | <% await tp.system.prompt("Auth required? (yes/no)", "yes") %> |
| **Content-Type** | application/json |

## Summary

<% await tp.system.prompt("Brief description of what the handler does", "One-line summary here") %>

## Request DTO

**DTO Name:** <% await tp.system.prompt("Request DTO name", "CreateStaffReq") %>

```go
type CreateStaffReq struct {
	// Example fields:
	// Name  string `json:"name" binding:"required"`
	// Email string `json:"email" binding:"required,email"`
}
```

## Response DTO

**DTO Name:** <% await tp.system.prompt("Response DTO name", "StaffResp") %>

```go
type StaffResp struct {
	// Example fields:
	// ID        uint64    `json:"id"`
	// Name      string    `json:"name"`
	// CreatedAt time.Time `json:"created_at"`
}
```

## Handler Implementation

**Handler Function:** <% await tp.system.prompt("Handler func name", "HandleCreateStaff") %>

```go
func HandleCreateStaff(c *gin.Context) {
	var req CreateStaffReq
	
	// Bind request
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	
	// TODO: Call service layer
	
	// Return response
	c.JSON(http.StatusOK, gin.H{"data": result})
}
```

## Route Registration

**HTTP Method:** <% await tp.system.prompt("HTTP method lowercase (get/post/put/delete/patch)", "get") %>  
**Endpoint:** <% await tp.system.prompt("Endpoint path", "/api/...") %>

```go
// In main routes setup
r.GET("/api/v1/staff", HandleCreateStaff)
```

## cURL Example

**Test GET endpoint:**
```bash
curl -X GET "http://localhost:8080/api/v1/staff" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

**Test POST endpoint with JSON body:**
```bash
curl -X POST "http://localhost:8080/api/v1/staff" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

**Test with response pretty-print:**
```bash
curl -X POST "http://localhost:8080/api/v1/staff" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com"}' | jq .
```
> - 400 Bad Request: Invalid input/binding error
> - 401 Unauthorized: Missing/invalid auth token
> - 404 Not Found: Resource not found
> - 500 Internal Server Error: Unexpected error

> [!callout]- Validation
> - Input validation rules
> - Business logic validation
> - Permission/auth checks

## Tests
- [ ] Happy path test
- [ ] Invalid input test
- [ ] Unauthorized test
- [ ] Not found test

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_