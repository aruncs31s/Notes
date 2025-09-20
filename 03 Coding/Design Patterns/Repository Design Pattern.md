---
id: Repository_Design_Pattern
aliases: []
tags:
  - coding
  - design_patterns
dg-publish: true
---
# Repository Design Pattern

## Overview

The Repository Design Pattern is a design pattern that encapsulates the logic needed to access data sources. It centralizes common data access functionality, providing better maintainability and decoupling the infrastructure or technology used to access databases from the domain model layer.

## Purpose

- **Separation of Concerns**: Separates business logic from data access logic
- **Testability**: Makes unit testing easier by allowing mock repositories
- **Maintainability**: Centralizes data access code
- **Flexibility**: Allows switching between different data sources without changing business logic

## Structure

```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client Code   │───▶│   Repository    │───▶│   Data Source   │
│                 │    │   Interface     │    │   (Database)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                ▲
                                │
                       ┌─────────────────┐
                       │   Concrete      │
                       │   Repository    │
                       └─────────────────┘

```

## Implementation Examples

### Interface Definition

```go
type UserRepository interface {
    Create(user *User) error
    GetByID(id string) (*User, error)
    GetByEmail(email string) (*User, error)
    Update(user *User) error
    Delete(id string) error
    List(limit, offset int) ([]*User, error)
}

```

### Concrete Implementation

```go
type userRepository struct {
    db *sql.DB
}

func NewUserRepository(db *sql.DB) UserRepository {
    return &userRepository{db: db}
}

func (r *userRepository) Create(user *User) error {
    query := `INSERT INTO users (id, name, email) VALUES (?, ?, ?)`
    _, err := r.db.Exec(query, user.ID, user.Name, user.Email)
    return err
}

func (r *userRepository) GetByID(id string) (*User, error) {
    query := `SELECT id, name, email FROM users WHERE id = ?`
    row := r.db.QueryRow(query, id)
    
    var user User
    err := row.Scan(&user.ID, &user.Name, &user.Email)
    if err != nil {
        return nil, err
    }
    return &user, nil
}

```

### Usage in Service Layer

```go
type UserService struct {
    userRepo UserRepository
}

func NewUserService(userRepo UserRepository) *UserService {
    return &UserService{userRepo: userRepo}
}

func (s *UserService) CreateUser(name, email string) error {
    user := &User{
        ID:    generateID(),
        Name:  name,
        Email: email,
    }
    return s.userRepo.Create(user)
}

```

## Benefits

### 1. **Testability**

- Easy to create mock implementations for unit testing
- No need for actual database connections in tests

### 2. **Flexibility**

- Can switch between different data sources (SQL, NoSQL, API, etc.)
- Implementation details are hidden from business logic

### 3. **Maintainability**

- Centralized data access logic
- Changes to data access patterns affect only repository implementations

### 4. **Clean Architecture**

- Supports dependency inversion principle
- Domain layer doesn't depend on infrastructure

## When to Use

✅ **Use Repository Pattern when:**

- You have complex data access logic
- You need to support multiple data sources
- You want to improve testability
- You're building a large application with clear layers

❌ **Consider alternatives when:**

- You have simple CRUD operations only
- The application is very small
- You're using an ORM that already provides abstraction

## Common Variations

### 1. **Generic Repository**

```go
type Repository[T any] interface {
    Create(entity T) error
    GetByID(id string) (T, error)
    Update(entity T) error
    Delete(id string) error
    List() ([]T, error)
}

```

### 2. **Unit of Work Pattern**

Often used together with Repository for transaction management:

```go
type UnitOfWork interface {
    UserRepository() UserRepository
    ProductRepository() ProductRepository
    Commit() error
    Rollback() error
}

```

## Best Practices

1. **Keep interfaces focused**: Don't create overly generic repositories
2. **Use dependency injection**: Inject repositories into services
3. **Handle errors appropriately**: Let business logic decide how to handle data access errors
4. **Consider caching**: Implement caching at the repository level if needed
5. **Use transactions**: Implement transaction support for complex operations

## Related Patterns

- **Unit of Work**: Manages transactions across multiple repositories
- **Data Access Object (DAO)**: Similar concept, more focused on CRUD operations
- **Active Record**: Alternative pattern where domain objects contain persistence logic
- **Data Mapper**: Separates domain objects from database schema

## Tags

- Design Patterns
- Data Access
- Clean Architecture
- Go
- Database
- Testing