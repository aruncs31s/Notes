---
id: Using_SOLID_Principle
aliases: []
tags:
  - classes
  - git_by_doing
  - level_6
dg-publish: true
---
# Using SOLID Principles in Go

## 📁 Project Structure

```

database/
├── database.go
├── handlers/
│   └── product_handler.go
├── models/
│   └── product.go
├── repository/
│   ├── interfaces.go
│   └── product_repository.go
└── test.db

```

---

## 📦 `/models` Package

**📖 Description**: Contains data structures and domain entities

### 🎯 SOLID Principles Applied
- **Single Responsibility**: Only defines data structures, no business logic
- **Open/Closed**: Easy to extend with new fields without modifying existing code
- **Dependency Inversion**: Pure data structures with no external dependencies

### 📄 Code Example

```go
package models

import "gorm.io/gorm"

type Product struct {
    gorm.Model
    Code  string `json:"code"`
    Price uint   `json:"price"`
}

```

### 📁 Files
- `product.go`: Defines the Product entity with database tags

---

## 🗄️ `/repository` Package

**📖 Description**: Data access layer - abstracts database operations

### 🎯 SOLID Principles Applied
- **Single Responsibility**: Only handles data persistence operations
- **Interface Segregation**: Small, focused interface for product operations
- **Dependency Inversion**: Uses interfaces, not concrete implementations
- **Open/Closed**: Can add new repositories without changing existing code

### 📄 Code Example

```go
package repository

import "c:/Users/arunc/Git/git_by_doing_level_6/level_6_go/database/models"

type ProductRepository interface {
    Create(product *models.Product) error
    GetByID(id uint) (*models.Product, error)
    GetAll() ([]models.Product, error)
    Update(product *models.Product) error
    Delete(id uint) error
}

```

### 📁 Files
- `interfaces.go`: Defines `ProductRepository` interface
- `product_repository.go`: Implements the interface with GORM

---

## 🎛️ `/handlers` Package

**📖 Description**: Business logic layer - orchestrates operations between UI and data

### 🎯 SOLID Principles Applied
- **Single Responsibility**: Handles business logic for product operations
- **Dependency Inversion**: Depends on repository interface, not concrete implementation
- **Open/Closed**: Can extend with new business rules without modifying core logic

### 📄 Code Example

```go
package handlers

type ProductHandler struct {
    repo repository.ProductRepository
}

func NewProductHandler(repo repository.ProductRepository) *ProductHandler {
    return &ProductHandler{repo: repo}
}

```

### 📁 Files
- `product_handler.go`: Contains business logic and user interaction

---

## 🚀 Root `/database` Package

**📖 Description**: Application entry point and dependency injection

### 🎯 SOLID Principles Applied
- **Dependency Inversion**: Injects dependencies (repository into handler)
- **Single Responsibility**: Only handles application bootstrapping
- **Open/Closed**: Easy to swap implementations via dependency injection

### 📄 Code Example

```go
func NewApp(db *gorm.DB) *App {
    productRepo := repository.NewProductRepository(db)
    productHandler := handlers.NewProductHandler(productRepo)
    
    return &App{
        productHandler: productHandler,
    }
}

```

### 📁 Files
- `database.go`: Main application entry point and dependency wiring

---

## 🤔 What is the PURPOSE of REPOSITORY Pattern?

### 🎯 Core Purpose
The Repository pattern acts as an **abstraction layer** between your business logic and data storage, providing a clean interface for data operations.

### 🔍 Key Purposes

#### 1. **Data Access Abstraction**

```go
// Without Repository - Direct database dependency
func GetUser(db *gorm.DB, id uint) (*User, error) {
    var user User
    return &user, db.First(&user, id).Error
}

// With Repository - Abstracted data access
type UserRepository interface {
    GetByID(id uint) (*User, error)
}

```

#### 2. **Testability & Mocking**

```go
// Easy to mock for testing
type MockProductRepository struct{}

func (m *MockProductRepository) GetByID(id uint) (*Product, error) {
    return &Product{ID: id, Code: "TEST", Price: 100}, nil
}

// Test becomes simple
func TestProductHandler(t *testing.T) {
    mockRepo := &MockProductRepository{}
    handler := NewProductHandler(mockRepo)
    // Test without real database
}

```

#### 3. **Database Independence**

```go
// Can switch from SQLite to PostgreSQL without changing business logic
func main() {
    // SQLite version
    db := gorm.Open(sqlite.Open("test.db"))
    
    // PostgreSQL version  
    // db := gorm.Open(postgres.Open(dsn))
    
    // Same repository interface works with both!
    repo := repository.NewProductRepository(db)
}

```

#### 4. **Centralized Query Logic**

```go
// All product-related queries in one place
type ProductRepository interface {
    GetByID(id uint) (*Product, error)
    GetByCode(code string) (*Product, error)
    GetExpensiveProducts(minPrice uint) ([]Product, error)
    GetByCategory(category string) ([]Product, error)
}

```

### 📊 Repository vs Direct Database Access

| Aspect | Direct DB Access | Repository Pattern |
|--------|------------------|-------------------|
| **Testability** | ❌ Hard to test | ✅ Easy to mock |
| **Code Reuse** | ❌ Scattered queries | ✅ Centralized logic |
| **Database Changes** | ❌ Code changes everywhere | ✅ Change only repository |
| **Business Logic** | ❌ Mixed with data access | ✅ Clean separation |
| **SOLID Compliance** | ❌ Violates DIP & SRP | ✅ Follows all principles |

### 🎭 Real-World Analogy
Think of Repository as a **librarian**:
- You ask the librarian for a book (interface)
- You don't care if books are stored on shelves, in a database, or digitally
- The librarian knows how to find and retrieve books
- If the library changes its storage system, you still ask the librarian the same way

### 🏗️ How Repository Enables SOLID

#### Single Responsibility

```go
// Repository: ONLY handles data persistence
type ProductRepository interface {
    Create(product *Product) error
    GetByID(id uint) (*Product, error)
}

// Handler: ONLY handles business logic
type ProductHandler struct {
    repo ProductRepository
}

```

#### Dependency Inversion

```go
// High-level module (Handler) doesn't depend on low-level module (GORM)
// Both depend on abstraction (ProductRepository interface)

type ProductHandler struct {
    repo ProductRepository // ← Interface, not concrete implementation
}

```

---

## 🎯 Benefits of This Architecture

| Principle | Benefit |
|-----------|---------|
| **Testability** | Easy to mock interfaces for unit testing |
| **Maintainability** | Changes in one layer don't affect others |
| **Scalability** | Can easily add new features/repositories |
| **Flexibility** | Can swap database implementations without changing business logic |
| **Code Reusability** | Handlers can work with any repository implementation |

---

## 🔧 SOLID Principles Summary

- **S** - Single Responsibility: Each package has one reason to change
- **O** - Open/Closed: Open for extension, closed for modification
- **L** - Liskov Substitution: Any repository implementation can replace another
- **I** - Interface Segregation: Small, focused interfaces
- **D** - Dependency Inversion: High-level modules don't depend on low-level modules