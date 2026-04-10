---

tags:
  - etlab
  - model
cssclasses:
  - wide-page
status:
---
<%*
let tableName = await tp.system.prompt("Enter the table name (e.g., staff_qualifications):");
%>
# Go Model: <% tableName %>

<%*
// Auto-generate struct name from table name (snake_case to PascalCase)
let structName = tableName.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
%>

## GORM Model

```go
package models

import (
    "time"
    "gorm.io/gorm"
)

type <% structName %> struct {
    ID          uint           `gorm:"primaryKey" json:"id"`
    CreatedAt   time.Time      `gorm:"autoCreateTime:milli" json:"created_at"`
    UpdatedAt   time.Time      `gorm:"autoUpdateTime:milli" json:"updated_at"`
    DeletedAt   gorm.DeletedAt `gorm:"index" json:"deleted_at,omitempty"`
}

func (<% structName %>) TableName() string {
    return "<% tableName %>"
}
```

## Model Methods

```go
// BeforeCreate hook
func (m *<% structName %>) BeforeCreate(tx *gorm.DB) error {
    // Add any pre-create logic here
    return nil
}

// BeforeUpdate hook
func (m *<% structName %>) BeforeUpdate(tx *gorm.DB) error {
    // Add any pre-update logic here
    return nil
}

// Custom methods
func (m *<% structName %>) IsActive() bool {
    return m.DeletedAt.Time.IsZero()
}

func (m *<% structName %>) SoftDelete() {
    m.DeletedAt = gorm.DeletedAt{Time: time.Now(), Valid: true}
}
```

## Validation

```go
type <% structName %>CreateRequest struct {
    // Add validation tags here
}

type <% structName %>UpdateRequest struct {
    // Add validation tags here
}
```

## Repository Interface

```go
type <% structName %>Repository interface {
    Create(ctx context.Context, req *<% structName %>CreateRequest) (*<% structName %>, error)
    GetByID(ctx context.Context, id uint) (*<% structName %>, error)
    Update(ctx context.Context, id uint, req *<% structName %>UpdateRequest) (*<% structName %>, error)
    Delete(ctx context.Context, id uint) error
    List(ctx context.Context, filter *<% structName %>Filter) ([]*<% structName %>, error)
}
```

## Service Interface

```go
type <% structName %>Service interface {
    Create(ctx context.Context, req *<% structName %>CreateRequest) (*<% structName %>, error)
    GetByID(ctx context.Context, id uint) (*<% structName %>, error)
    Update(ctx context.Context, id uint, req *<% structName %>UpdateRequest) (*<% structName %>, error)
    Delete(ctx context.Context, id uint) error
    List(ctx context.Context, filter *<% structName %>Filter) ([]*<% structName %>, error)
}
```

## Handler/Controller

```go
type <% structName %>Handler struct {
    service <% structName %>Service
}

func New<% structName %>Handler(service <% structName %>Service) *<% structName %>Handler {
    return &<% structName %>Handler{
        service: service,
    }
}

// HTTP handlers
func (h *<% structName %>Handler) Create(c *gin.Context) {
    // Implementation
}

func (h *<% structName %>Handler) GetByID(c *gin.Context) {
    // Implementation
}

func (h *<% structName %>Handler) Update(c *gin.Context) {
    // Implementation
}

func (h *<% structName %>Handler) Delete(c *gin.Context) {
    // Implementation
}

func (h *<% structName %>Handler) List(c *gin.Context) {
    // Implementation
}
```

## Notes

- **Table**: `<% tableName %>`
- **Struct**: `<% structName %>`
- **Relationships**: Add any belongs_to, has_many, has_one relationships here
- **Indexes**: Define any additional indexes needed
- **Business Logic**: Add any specific business rules or constraints
=======
title: "<% tp.file.title %>"
tags:
  - model
  - go
  - etlab
  - entity
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm") %>
---

# <% tp.file.title %> Model

- [ ] Link To SQL Table 🍽
- [ ] Create repository ✨
- [ ] Create service ✨
- [ ] Create interface ✨
- [ ] Create Handler ✨
- [ ] Create Tests ✨


> [!note]- Purpose
> Domain model / entity for **<% tp.file.title %>**. Defines structure, validation, and business rules.

## Struct Definition

**Model Name:** <% await tp.system.prompt("Model name", "Staff") %>

```go
type Staff struct {
	ID        uint64    `gorm:"primaryKey"`

    <% await tp.system.prompt("Field 1 definition", "Name string `gorm:\"column:name\"`") %>
    <% await tp.system.prompt("Field 2 definition", "Email string `gorm:\"column:email\"`") %>
    <% await tp.system.prompt("Field 3 definition", "Phone string `gorm:\"column:phone\"`") %>

    // Optional Fields
    StaffID uint   `gorm:"column:staff_id"`
    Status uint8 `gorm:"column:status"`
    // Must Have Fields ✨
	CreatedAt time.Time `gorm:"column:created_at"`
	UpdatedAt time.Time `gorm:"column:updated_at"`
    CreatedBy uint   `gorm:"column:created_by"`
	UpdatedBy uint   `gorm:"column:updated_by"`
    Agent string   `gorm:"column:agent"`
    IP       string   `gorm:"column:ip"`

    // Relation
    Staff Staff `gorm:"foreignKey:StaffID"`
}
```

## Field Reference

**Additional Field 1:**
- Name: <% await tp.system.prompt("Field 1 name", "Name") %>
- Type: <% await tp.system.prompt("Field 1 type", "string") %>
- JSON Key: <% await tp.system.prompt("Field 1 JSON key", "name") %>
- GORM Tags: <% await tp.system.prompt("Field 1 GORM tags", "column:name") %>
- Validation: <% await tp.system.prompt("Field 1 validation", "required") %>
- Notes: <% await tp.system.prompt("Field 1 notes", "") %>

| Field | Type | JSON Key | GORM Tags | Validation | Notes |
|---|---|---|---|---|---|
| ID | uint64 | id | primaryKey | - | Auto-increment |
| CreatedAt | time.Time | created_at | - | - | Auto-set by GORM |
| UpdatedAt | time.Time | updated_at | - | - | Auto-set by GORM |
| DeletedAt | gorm.DeletedAt | - | index | - | Soft delete |

## Table Name (GORM)

**Table Name:** <% await tp.system.prompt("Table name (plural)", "staffs") %>

```go
func (m *Staff) TableName() string {
	return "staffs"
}
```

## Validation Rules
- Field constraints (required, max length, format)
- Business logic validation

## Migrations (GORM)

```go
// Auto-migration
db.AutoMigrate(&Staff{})

// Or explicit migration:
db.Migrator().CreateTable(&Staff{})
```

## SQL to GORM Conversion Reference

### SQL → Go Type Mapping

| SQL Type | Go Type | GORM Tag |
|---|---|---|
| INT / BIGINT | int / int64 / uint64 | `gorm:"column:name"` |
| VARCHAR(255) | string | `gorm:"column:name;size:255"` |
| TEXT | string | `gorm:"column:name;type:text"` |
| BOOLEAN | bool | `gorm:"column:name"` |
| TIMESTAMP | time.Time | `gorm:"column:name"` |
| DECIMAL(10,2) | float64 | `gorm:"column:name"` |
| JSON | datatypes.JSONType | `gorm:"column:name;type:json"` |
| ENUM | string | `gorm:"column:name;type:enum('a','b')"` |

### SQL Constraints → GORM Tags

| SQL | GORM Tag | Example |
|---|---|---|
| PRIMARY KEY | `primaryKey` | `` `gorm:"primaryKey"` `` |
| NOT NULL | `not null` | `` `gorm:"not null"` `` |
| UNIQUE | `unique` | `` `gorm:"unique"` `` |
| FOREIGN KEY | `foreignKey` | `` `gorm:"foreignKey:UserID"` `` |
| DEFAULT value | `default` | `` `gorm:"default:0"` `` |
| INDEX | `index` | `` `gorm:"index"` `` |
| UNIQUE INDEX | `uniqueIndex` | `` `gorm:"uniqueIndex"` `` |


---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_
>>>>>>> d291f79 (feat: Add 8 optimized Templater templates for Go/PHP/Database development)
