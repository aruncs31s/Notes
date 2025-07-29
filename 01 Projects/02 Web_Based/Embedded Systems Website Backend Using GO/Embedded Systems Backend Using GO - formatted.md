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

2. Implements the `userRepository` struct that uses GORM for database operations.
3. Provides concrete implementations of all interface methods using GORM's API. 