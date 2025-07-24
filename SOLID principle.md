# SOLID Principles
- essential part of oop

## 1. Single Responsibility Principle (SRP): Principle states that a class or module should **have only one reason** to change
```go
type User struct {
    FirstName string
    LastName  string
}
func (u *User) GetFullName() string {
    return u.FirstName + " " + u.LastName
}
func (u *User) Save() error {
    // Save user to the database
    // ...
}
```
- the `User` struct now handles **both** data and persistence. 

```go
type User struct {
    FirstName string
    LastName  string
}
func (u *User) GetFullName() string {
    return u.FirstName + " " + u.LastName
}
type UserRepository struct {
    // DB connection or context
}
func (r *UserRepository) Save(u *User) error {
    // Save user to the database
    // ...
}
```

- **Domain-Driven Design (DDD)**, Version 2 is preferred
## 2. Open/Closed Principle (OCP)
should be open for extension but closed for modification.