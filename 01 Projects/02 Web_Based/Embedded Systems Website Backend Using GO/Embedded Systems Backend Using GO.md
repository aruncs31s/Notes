---
tags:
  - "#backend"
  - "#go"
  - "#website"
  - "#project"
---

# Embedded Systems Backend Using Go

## Project Structure

The project follows a clean architecture pattern with separated concerns:

- **handlers/**: Contains HTTP request handlers
- **initializers/**: Database and environment initialization
- **routes/**: API route definitions

```
├── es_website_gcek_backend
├── go.mod
├── go.sum
├── handlers
│   ├── register.go
│   └── test.go
├── initializers
│   ├── initDB.go
│   └── loadEnvVars.go
├── main.go
└── routes
    ├── routes.go
    └── test.go

4 directories, 11 files
```

## 🛢Database

>[!NOTE] GORM Context
### Repositories 
```go
package repositories

import (
	"github.com/aruncs31s/es_website_gcek_backend/database/model"
	"gorm.io/gorm"
)

type UserRepository interface {
	CreateUser(user *model.User) error
	GetUserById(id uint) (*model.User, error)
	GetAllUsers() ([]*model.User, error)
}

type userRepository struct {
	db *gorm.DB
}

func NewUserRepository(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}

func (ur *userRepository) CreateUser(user *model.User) error {
	return ur.db.Create(user).Error
}

func (ur *userRepository) GetUserById(id uint) (*model.User, error) {
	var user model.User
	err := ur.db.First(&user, id).Error
	if err != nil {
		return nil, err
	}
	return &user, nil
}

func (ur *userRepository) GetAllUsers() ([]*model.User, error) {
	var users []*model.User
	err := ur.db.Find(&users).Error
	if err != nil {
		return nil, err
	}
	return users, nil
}
```

#### Flow 
1. Defines the `UserRepository` interface with methods for user operations.
>[!ABSTRACT]- **Why?**
> **Abstraction & Decoupling**: The interface abstracts the data layer from business logic. Your handlers and services depend on the interface, not the concrete implementation, making the code more modular and testable.
>
> **Testability**: You can easily create mock implementations of `UserRepository` for unit testing without needing a real database connection.
>
> **Flexibility**: Want to switch from GORM to raw SQL or a different ORM? Just implement the interface differently - no changes needed in your handlers or business logic.
>
> **Dependency Inversion**: High-level modules (handlers) don't depend on low-level modules (database). Both depend on abstractions (interfaces).
>
> **Example**: Your handler receives `UserRepository` interface, not `*gorm.DB` directly:
> 
> ```go
> type UserHandler struct {
>     userRepo UserRepository // Interface, not concrete type
> }
> ```

```go
type UserRepository interface {
	CreateUser(user *model.User) error
	GetUserById(id uint) (*model.User, error)
	GetAllUsers() ([]*model.User, error)
}
```

>[!TIP]- **Interface Implementation in Go**
> In Go, any type that has these exact methods automatically implements the `UserRepository` interface. This is called **implicit interface satisfaction**.
>
> **Examples of different implementations:**
>
> ```go
> // GORM implementation
> type gormUserRepository struct {
>     db *gorm.DB
> }
>
> // Redis implementation  
> type redisUserRepository struct {
>     client *redis.Client
> }
>
> // Mock implementation for testing
> type mockUserRepository struct {
>     users []model.User
> }
>
> // API client implementation
> type apiUserRepository struct {
>     httpClient *http.Client
>     baseURL    string
> }
> ```
>
> **All of these are `UserRepository`** as long as they implement the three methods! This is the power of Go's interface system - you don't need to explicitly declare "implements UserRepository" like in other languages.

>[!SUCCESS]- **No Explicit Declaration Needed!**
> In Go, you never need to say "this implements UserRepository".
>
> **Other languages (Java/C#):**
> ```java
> class DatabaseUserRepo implements UserRepository { // ← Explicit declaration
>     // methods...
> }
> ```
>
> **Go way:**
> ```go
> type userRepository struct {
>     db *gorm.DB
> }
> // No "implements" keyword needed!
> // Just having the methods makes it a UserRepository
>
> func (ur *userRepository) CreateUser(user *model.User) error { ... }
> func (ur *userRepository) GetUserById(id uint) (*model.User, error) { ... }
> func (ur *userRepository) GetAllUsers() ([]*model.User, error) { ... }
> ```
>
> **The compiler automatically recognizes** that `userRepository` satisfies the `UserRepository` interface because it has all the required methods with correct signatures.

1. Implements the `userRepository` struct that uses GORM for database operations.
2. Provides concrete implementations of all interface methods using GORM's API.

## Multiple Implementations Example

The beauty of the `UserRepository` interface is that we can have multiple implementations:

```go
type UserRepository interface {
    CreateUser(user *model.User) error
    GetUserById(id uint) (*model.User, error)
    GetAllUsers() ([]*model.User, error)
}

type userRepository struct {
    db *gorm.DB
}
```

So the idea is that `UserRepository` is the contract and we can have multiple implementations of it:

```go
// GORM implementation
type gormUserRepository struct {
    db *gorm.DB
}

// Redis implementation
type redisUserRepository struct {
    client *redis.Client
}

// Mock implementation for testing
type mockUserRepository struct {
    users []model.User
}

// API client implementation
type apiUserRepository struct {
    httpClient *http.Client
    baseURL    string
}
```
^diffimplementations

>[!ABSTRACT]- **How to use them individually?**
> All of these variables can hold ANY implementation of `UserRepository`:
>
> ```go
> var repo UserRepository
>
> repo = NewGormRepository(db)      // Uses database
> repo = NewMockRepository()        // Uses in-memory data
> repo = NewAPIRepository(client)   // Uses external API
>
> // Your handler code stays exactly the same!
> handler := NewUserHandler(repo)
> ```

**Benefits**: It is easier to test this way because you can swap implementations without changing your business logic! 

---

### Creation 

```go

func NewUserRepository(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}

```

if i want i can have an another one by using ![[#^diffimplementations]]
Like the following
```go
func NewUserRepositoryTwo(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}
func NewUserRepositoryTwo(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}
func NewUserRepositoryTwo(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}
func NewUserRepositoryTwo(db *gorm.DB) UserRepository {
	return &userRepository{db: db}
}
```