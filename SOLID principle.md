# SOLID Principles
- [[Factory Design Pattern]]

| Principle                               | Meaning                                                                        | Related Design Patterns                                      |
| --------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **S** – Single Responsibility Principle | A class should have **only one reason to change**.                             | [[Factory Design Pattern\|Factory]] , [[Builder]] , Observer |
| **O** – Open/Closed Principle           | Classes should be **open for extension but closed for modification**.          | Strategy, Decorator, Template Method                         |
| **L** – Liskov Substitution Principle   | Subclasses should be usable wherever the parent class is.                      | All polymorphism-based patterns                              |
| **I** – Interface Segregation Principle | Use **small, specific interfaces** rather than big general ones.               | Adapter, Proxy                                               |
| **D** – Dependency Inversion Principle  | High-level modules should not depend on low-level ones — **use abstractions**. | Dependency Injection, Facto                                  |
|                                         |                                                                                |                                                              |



##### 1. Single Responsibility Principle (SRP): Principle states that a class or module should **have only one reason** to change
- it encourages developers to create modular and reusable code by dividing each component into a single responsibility. This helps in making the code more maintainable, testable, and easier to understand,
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
##### 2. Open/Closed Principle (OCP)
should be open for extension but closed for modification.