---
title: "Templater Guide"
tags:
  - templater
  - obsidian
  - guide
cssclasses:
  - wide-page
---

# Templater Template Guide

Complete guide for using the 8 Obsidian Templater templates in this workspace.

## Quick Start

1. **Open Obsidian Command Palette** (`Cmd+P` on macOS, `Ctrl+P` on Windows/Linux)
2. **Search for "Templater: Open Insert Template"**
3. **Select the template** you need
4. **Fill in the prompts** that appear
5. **Done!** Template is inserted with your values and today's date

---

## Available Templates

### 1️⃣ **Handler** (`handler.md`)
For Gin HTTP handler endpoints in Go/ETLAB Backend.

**When to use:**
- Documenting a new API endpoint
- Recording handler signature, DTOs, validation rules

**Tags:** `handler`, `api`, `go`, `etlab`

**Includes:**
- Endpoint spec (method, path, auth)
- Request/Response DTOs
- Handler implementation skeleton
- Route registration example
- Error handling callout
- Test checklist

**Example prompts filled:**
```
HTTP method: POST
Endpoint path: /api/v1/staff
Handler func name: HandleCreateStaff
Request DTO name: CreateStaffReq
Response DTO name: StaffResp
```

---

### 2️⃣ **Repository** (`repository.md`)
For the repository pattern (data access layer) in Go.

**When to use:**
- Designing data access interface
- Documenting GORM/database queries
- Recording transaction boundaries

**Tags:** `repository`, `go`, `etlab`, `data-access`

**Includes:**
- Repository interface contract
- ORM/driver details (GORM, sqlx, etc.)
- Implementation example (GORM)
- Custom queries section
- Error handling patterns
- Test scenarios

---

### 3️⃣ **Model** (`model.md`)
For Go domain models/entities.

**When to use:**
- Documenting a new struct/entity
- Recording GORM tags, validation rules, relationships

**Tags:** `model`, `go`, `etlab`, `entity`

**Includes:**
- Struct definition with tags
- Field reference table (name, type, JSON key, GORM tags, validation)
- Table name definition
- Validation rules
- Relationships (foreign keys)
- Migration examples

---

### 4️⃣ **Service** (`service.md`)
For business logic layer (orchestration, validation).

**When to use:**
- Documenting service responsibilities
- Recording business rules and validation
- Planning transaction orchestration

**Tags:** `service`, `go`, `etlab`, `business-logic`

**Includes:**
- Service responsibility description
- Dependencies table (repositories, external services)
- Interface contract
- Implementation example
- Transaction patterns
- Business rules & authorization checks
- Test scenarios

---

### 5️⃣ **Interface** (`interface.md`)
For Go interface/contract definitions.

**When to use:**
- Defining interface contracts (separate from implementation)
- Planning mock/test implementations
- Documenting polymorphism patterns

**Tags:** `interface`, `go`, `etlab`, `contract`

**Includes:**
- Interface definition
- Implementation locations table
- Mock example (testify/mock or golang/mock)
- Usage patterns
- Error types
- Test strategies

---

### 6️⃣ **Idea** (`idea.md`)
For brainstorms, investigations, feature ideas.

**When to use:**
- Capturing quick ideas
- Recording design investigations
- Lightweight RFC or feature proposal

**Tags:** `idea`, `etlab`, `brainstorm`

**Includes:**
- One-liner summary & context/motivation
- Key points
- Risks/constraints
- Dependencies
- Action items checklist
- Discussion notes

---

### 7️⃣ **PHP Code** (`php_code.md`)
For PHP components (Laravel, custom code).

**When to use:**
- Documenting a Laravel controller, service, middleware
- Recording PHP class implementation
- Planning PHP test coverage

**Tags:** `php`, `code`, `etlab-php`

**Includes:**
- Component type (Controller, Service, Model, etc.)
- File location
- Code skeleton
- Methods reference table
- Dependencies list
- Usage example
- Error handling
- Testing notes

---

### 8️⃣ **Database Design** (`database_design.md`)
For schema, tables, relationships, and optimization.

**When to use:**
- Designing a new database schema
- Documenting table structure and migrations
- Planning indexes and optimization

**Tags:** `database`, `design`, `schema`, `etlab`

**Includes:**
- Schema overview & purpose
- Tables with field definitions (type, constraints, notes)
- SQL CREATE TABLE statements
- Entity relationship diagram (text-based)
- Foreign keys and referential integrity
- Indexes and query optimization
- Example queries
- Migration/deployment SQL
- Rollback plan

---

## Templater Features Used

### 1. **Prompts** – Interactive input during insertion
```html
<% tp.prompt("What is this?", "default value") %>
```
- User sees a dialog box
- Can enter custom value or accept default
- Value is inserted into the template

### 2. **Date/Time** – Auto-insert current date
```html
<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
```
- Automatically fills with current timestamp
- Helps track creation/update dates

### 3. **File Title** – Auto-insert note title
```html
<% tp.file.title %>
```
- Grabs the filename (without extension)
- Useful for headers and frontmatter

### 4. **Conditional** – Show/hide sections
```html
<% if (tp.user.profile()?.name) %>
  Hello, <% tp.user.profile().name %>!
<% endif %>
```
- (Not heavily used in these templates, but available)

---

## Workflow Examples

### Example 1: Create a new handler for `/api/staff/{id}`
1. Create new file: `Staff Get Handler.md`
2. Open Command Palette → "Insert Template" → Select `handler.md`
3. Fill prompts:
   - HTTP method: `GET`
   - Endpoint path: `/api/v1/staff/{id}`
   - Auth required: `yes`
   - Handler func: `HandleGetStaffByID`
   - Request DTO: `GetStaffByIDReq`
   - Response DTO: `StaffResp`
4. ✅ Template inserted! Now write your code.

### Example 2: Design a new `departments` table
1. Create new file: `Departments Table.md`
2. Open Command Palette → "Insert Template" → Select `database_design.md`
3. Fill prompts:
   - Purpose: `Organize staff by department`
   - Table name: `departments`
   - Column 1: `name VARCHAR(255)` / `NOT NULL` / `Department name`
   - Optimization 1: `Add index on name for lookups`
4. ✅ Schema documented with migration SQL ready to go.

### Example 3: Brainstorm staff qualification filtering
1. Create new file: `Qualification Filter Idea.md`
2. Open Command Palette → "Insert Template" → Select `idea.md`
3. Fill prompts:
   - Summary: `Support filtering staff by qualification type`
   - Motivation: `Improve search/discovery for qualified staff`
   - Key point 1: `Add qualification_type column to filter queries`
   - Action item 1: `Investigate query performance with new column`
4. ✅ Idea captured, ready for discussion.

---

## Tips & Best Practices

### ✅ Dos
- **Use consistent naming** within your templates (e.g., always use `Staff` not `staff` or `StaffModel`)
- **Link related notes** using `[[internal links]]` in the frontmatter or body
- **Keep DTOs/Models in sync** – if you update a model field, update the handler/service DTO
- **Tag consistently** – tags help Obsidian's graph and search
- **Fill in examples** – skeleton code is great, but real examples save time later

### ❌ Don'ts
- **Don't ignore the prompts** – they're there to guide you
- **Don't create duplicate structures** – reuse and update existing templates
- **Don't leave TODOs in production** – delete skeleton comments before committing

---

## Customizing Templates

To modify a template (e.g., add a new section or change the default):

1. Open the template file in Obsidian (e.g., `handler.md`)
2. Edit the content as needed
3. **Important:** Keep the `<% ... %>` Templater syntax intact!
4. Save the file
5. Next time you insert the template, your changes will be reflected

**Example:** To add a "Performance Notes" section to `handler.md`:
```markdown
## Performance Notes
- Query optimization: <% tp.prompt("Performance notes", "") %>
- Caching strategy: <% tp.prompt("Cache approach", "") %>
```

---

## Frontmatter Keys Used

All templates include this standard frontmatter:

| Key | Purpose | Example |
|---|---|---|
| `title` | Note title | `"Staff Handler"` |
| `tags` | Search/organization | `["handler", "api", "go"]` |
| `cssclasses` | Styling (e.g., wide-page) | `["wide-page"]` |
| `created` | ISO timestamp | `2025-11-04T14:32:00` |
| `updated` | ISO timestamp | Auto-updated by Obsidian |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Templater plugin not installed | Install from Obsidian Community Plugins |
| Prompts not appearing | Ensure Templater is enabled in Settings → Community Plugins |
| `<% ... %>` shows in final note | Make sure you're using the Templater plugin, not copy/paste |
| Date format looks wrong | Change `YYYY-MM-DDTHH:mm:ss` to your preferred format in the template |

---

## Related Notes

- [[OBSIDIAN_FORMATTING_GUIDE]]
- [[OBSIDIAN_QUICK_REFERENCE]]
- **Repository:** [[ETLAB Backend GO/API/Project Structure]]
- **Database:** [[Database/Database]]

---

_Last updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_