---
title: "<% tp.file.title %>"
tags:
  - service
  - go
  - etlab
  - business-logic
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Service

> [!note]- Purpose
> Business logic layer for **<% tp.file.title %>**. Orchestrates repositories, validation, and domain rules.

## Responsibility

<% await tp.system.prompt("Brief description of business responsibility", "Service coordinates domain logic between handlers and repositories") %>

## Dependencies

**Main Dependency 1:** <% await tp.system.prompt("Repository interface 1", "StaffRepository") %>  
**Dependency 2 (optional):** <% await tp.system.prompt("Service/dependency 2 (optional)", "Logger") %>  
**Dependency 3 (optional):** <% await tp.system.prompt("Service/dependency 3 (optional)", "Cache") %>

| Dependency | Type | Purpose |
|---|---|---|
| StaffRepository | Repository | Data access |
| Logger | Service | Logging |
| Cache | Service | Caching |

## Interface Contract

**Service Interface:** <% await tp.system.prompt("Service interface name", "StaffService") %>  
**Entity Type:** <% await tp.system.prompt("Entity name", "Staff") %>

```go
type StaffService interface {
	Create(ctx context.Context, dto *CreateStaffReq) (*Staff, error)
	GetByID(ctx context.Context, id uint64) (*Staff, error)
	Update(ctx context.Context, dto *UpdateStaffReq) (*Staff, error)
	Delete(ctx context.Context, id uint64) error
}
```

## Implementation Example

**Service Struct:** <% await tp.system.prompt("Service struct name", "staffService") %>

```go
type staffService struct {
	repo StaffRepository
	// Add other dependencies
}

func (s *staffService) Create(ctx context.Context, dto *CreateStaffReq) (*Staff, error) {
	// 1. Validate input
	if err := dto.Validate(); err != nil {
		return nil, err
	}
	
	// 2. Business logic / domain rules
	// e.g., check if email already exists
	
	// 3. Call repository
	m := &Staff{
		// map DTO to model
	}
	if err := s.repo.Create(ctx, m); err != nil {
		return nil, err
	}
	
	// 4. Return result
	return m, nil
}
```

> [!callout]- Transactions
> - Transactional operations (when service calls multiple repos)
> - Rollback scenarios
> - Error handling within transactions

> [!callout]- Business Rules
> - Validation logic
> - Authorization checks
> - Invariants maintained by this service

## Tests
- [ ] Happy path: Create, Get, Update, Delete
- [ ] Validation error: Invalid input
- [ ] Business rule error: Duplicate email, invalid state transition
- [ ] Repository error: DB connection failure
- [ ] Authorization error: User lacks permission

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_