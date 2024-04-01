---
title: "<% tp.file.title %>"
tags:
  - repository
  - go
  - etlab
  - data-access
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Repository

> [!note]- Purpose
> Repository pattern implementation for **<% tp.file.title %>**. Defines the data access contract and implementation.

## Aggregate / Entity

**Entity Name:** <% await tp.system.prompt("Entity name (e.g., Staff)", "Staff") %>  
**Repository Interface:** <% await tp.system.prompt("Repository interface name", "StaffRepository") %>

## Interface Contract

```go
type StaffRepository interface {
	Create(ctx context.Context, m *Staff) error
	GetByID(ctx context.Context, id uint64) (*Staff, error)
	Update(ctx context.Context, m *Staff) error
	Delete(ctx context.Context, id uint64) error
	// Add custom queries below:
	// GetAll(ctx context.Context) ([]*Staff, error)
	// GetByEmail(ctx context.Context, email string) (*Staff, error)
}
```

## Implementation Details

| Detail | Value |
|---|---|
| **ORM** | <% await tp.system.prompt("ORM choice (GORM/sqlx/sql)", "GORM") %> |
| **DB Driver** | <% await tp.system.prompt("Database driver (postgres/mysql/sqlite)", "postgres") %> |
| **Transactions** | <% await tp.system.prompt("Supports transactions? (yes/no)", "yes") %> |

## Example Implementation (GORM)

**Implementation Struct:** <% tp.prompt("Implementation struct name", "staffRepository") %>

```go
type staffRepository struct {
	db *gorm.DB
}

func (r *staffRepository) Create(ctx context.Context, m *Staff) error {
	return r.db.WithContext(ctx).Create(m).Error
}

func (r *staffRepository) GetByID(ctx context.Context, id uint64) (*Staff, error) {
	var m Staff
	if err := r.db.WithContext(ctx).First(&m, id).Error; err != nil {
		return nil, err
	}
	return &m, nil
}
```

> [!callout]- Custom Queries
> - Document complex SQL queries or GORM scopes here
> - Joins, aggregations, filtering logic

> [!callout]- Error Handling
> - Handle `gorm.ErrRecordNotFound` → 404
> - Database connection errors → 500
> - Constraint violations → 409 Conflict

## Tests
- [ ] Create and read back
- [ ] Update existing record
- [ ] Delete existing record
- [ ] Error case: record not found
- [ ] Error case: duplicate key constraint

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_