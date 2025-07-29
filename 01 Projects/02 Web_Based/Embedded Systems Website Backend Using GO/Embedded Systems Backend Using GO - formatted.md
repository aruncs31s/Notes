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