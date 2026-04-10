---
title: "<% tp.file.title %>"
tags:
  - database
  - design
  - schema
  - etlab
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Database Design

> [!note]- Purpose
> Database schema design for **<% tp.file.title %>**. Documents tables, relationships, indexing, and optimization.

## Overview

<% await tp.system.prompt("Brief description of the schema purpose", "What domain/feature does this schema serve?") %>

## Tables

### Table 1

**Name:** <% await tp.system.prompt("Table name 1 (e.g., staffs)", "staffs") %>

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE | Last update time |
| deleted_at | TIMESTAMP | NULL | Soft delete timestamp |

**Additional Column 1:**
- Name: <% await tp.system.prompt("Column 1 name", "name") %>
- Type: <% await tp.system.prompt("Column 1 type", "VARCHAR(255)") %>
- Constraints: <% await tp.system.prompt("Column 1 constraints", "NOT NULL") %>
- Notes: <% await tp.system.prompt("Column 1 notes", "") %>

**SQL:**
```sql
CREATE TABLE staffs (
    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    name VARCHAR(255) NOT NULL,
    -- Add more columns
    INDEX idx_created_at (created_at),
    INDEX idx_deleted_at (deleted_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### Table 2 (Optional)

**Name:** <% await tp.system.prompt("Table name 2 (optional)", "staff_qualifications") %>

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| staff_id | BIGINT UNSIGNED | FOREIGN KEY → staffs(id) | Reference to staff |

## Relationships

```
staffs
  ├─ ONE-TO-MANY ──→ staff_qualifications
  ├─ ONE-TO-MANY ──→ staff_experiences
  └─ ONE-TO-MANY ──→ staff_subjects_engaged
```

> [!callout]- Foreign Keys
> - Define referential integrity
> - ON DELETE CASCADE / SET NULL / RESTRICT
> - Impact on data deletion

> [!callout]- Indexes
> - Columns frequently filtered/sorted: `name`, `email`, `status`
> - Composite indexes for common queries
> - Index maintenance overhead vs. query performance

> [!callout]- Normalization
> - Normal form (1NF, 2NF, 3NF, BCNF)
> - Denormalization trade-offs
> - Data redundancy justified?

## Queries / Access Patterns

```sql
-- Example: Get staff with qualifications
SELECT s.*, q.*
FROM staffs s
LEFT JOIN staff_qualifications q ON s.id = q.staff_id
WHERE s.deleted_at IS NULL;
```

## Optimization Notes

**Optimization 1:** <% await tp.system.prompt("Query optimization (e.g., eager loading, batch queries)", "") %>  
**Optimization 2:** <% await tp.system.prompt("Caching strategy (e.g., cache top 100 staff)", "") %>  
**Optimization 3:** <% await tp.system.prompt("Partitioning or sharding considerations", "") %>

- Query optimization: eager loading, batch queries
- Caching strategy: cache top 100 staff
- Partitioning or sharding: if table grows large

## Migration / Deployment

**New Column Name:** <% await tp.system.prompt("New column name", "status") %>  
**New Column Type:** <% await tp.system.prompt("New column type", "VARCHAR(50)") %>  
**Default Value:** <% await tp.system.prompt("Default value", "DEFAULT 'active'") %>  
**Index Name:** <% await tp.system.prompt("Index name", "status") %>

```sql
-- Add new column
ALTER TABLE staffs 
ADD COLUMN status VARCHAR(50) DEFAULT 'active';

-- Add index
CREATE INDEX idx_status ON staffs(status);
```

## Rollback Plan
- How to safely undo schema changes
- Data migration reversibility

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_