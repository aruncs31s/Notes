---
title: "<% tp.file.title %>"
tags:
  - interface
  - go
  - etlab
  - contract
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Interface

> [!note]- Purpose
> Defines the contract/interface for **<% tp.file.title %>**. Promotes loose coupling and testability.

## Interface Definition

**Interface Name:** <% await tp.system.prompt("Interface name", "StaffService") %>

**Method 1:** <% await tp.system.prompt("Method 1 signature", "Create(ctx context.Context, req *CreateReq) (*Response, error)") %>  
**Method 2:** <% await tp.system.prompt("Method 2 signature", "GetByID(ctx context.Context, id uint64) (*Response, error)") %>  
**Method 3:** <% await tp.system.prompt("Method 3 signature", "Update(ctx context.Context, req *UpdateReq) (*Response, error)") %>  
**Method 4:** <% await tp.system.prompt("Method 4 signature", "Delete(ctx context.Context, id uint64) error") %>

```go
type StaffService interface {
	Create(ctx context.Context, req *CreateReq) (*Response, error)
	GetByID(ctx context.Context, id uint64) (*Response, error)
	Update(ctx context.Context, req *UpdateReq) (*Response, error)
	Delete(ctx context.Context, id uint64) error
}
```

## Where Implementations Live

**Production Impl File:** <% await tp.system.prompt("Implementation 1 name", "internal/service/staff_service.go") %>  
**Mock Impl File:** <% await tp.system.prompt("Implementation 2 name (e.g., Mock)", "internal/service/mocks/mock_staff_service.go") %>

| Implementation | File | Purpose |
|---|---|---|
| Production | internal/service/staff_service.go | Live implementation |
| Mock | internal/service/mocks/mock_staff_service.go | Testing/mocks |

## Mock Example (for testing)

```go
// Use a library like github.com/golang/mock or github.com/stretchr/testify/mock

type MockStaffService struct {
	mock.Mock
}

func (m *MockStaffService) Create(ctx context.Context, req *CreateReq) (*Response, error) {
	args := m.Called(ctx, req)
	if resp := args.Get(0); resp != nil {
		return resp.(*Response), args.Error(1)
	}
	return nil, args.Error(1)
}
```

> [!callout]- Usage
> - Where this interface is injected (handlers, other services)
> - Polymorphic behavior patterns

> [!callout]- Error Types
> - Custom errors returned by implementations
> - Error handling conventions

## Tests
- [ ] Mock setup and teardown
- [ ] Verify mocked calls
- [ ] Test error scenarios with mock

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_