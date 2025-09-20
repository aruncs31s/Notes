---
id: Design Pattern
aliases: []
tags:
  - coding
  - design_patterns
cssclasses: 
dg-publish: true
---
# Design Patterns
- [ ] Checkout MVVM 
- [ ] Checkout **Atomic Design methodology**
- [[Dependency Injunction]]

**Used In**
- [[SOLID principle]]
- [[Decorator]]

## 📚 Design Pattern Categories
- [[Creational Patterns|🪛Creational Patterns]]
- [[Structural Pattern|🏠Structural Pattern]]
- [[Behavioral Pattern|🤝 Behavioral Patterns]]
---
## 📖 Definition

Design patterns are **descriptions of communicating objects and classes** that are customized to solve a general design problem in a particular context. They help create **reusable object-oriented software** that is flexible, elegant, and maintainable.

> *"They reuse solutions that have worked for them in the past"*

### Key Benefits
- 🎯 **Specific to the problem** at hand but **general enough** for future requirements
- 🔄 **Reusable solutions** that have been proven effective
- 🏗️ Make object-oriented designs more **flexible**, **elegant**, and **reusable**

---

## 🎨 Core Principles

### State Pattern
> [!Abstract] Represent states with objects
> - Each possible state of an object is implemented as a separate class or object
> - This allows an object to **change its behavior** depending on its **current state**

### Decorator Pattern
- **Decorate objects** so you can easily add/remove features

### Model-View Separation

> **Decoupling views from model** → **separating the UI (view)** from the **data and business logic (model)**
> - The **model** doesn't care _how_ it's displayed
> - The **view** doesn't care _how_ data is fetched or processed  
> - They can change **independently**

---

---

## 🔧 Popular Patterns 
- [[Factory Design Pattern]]
- [[Builder]]
- [[Singleton]]
- [[Observer Design Pattern]]
### Popular Other Things
- [ ] Organize them into catagories 

#### Guard Clauses Technique 
> Used to write , **Cleaner** and more **readable code**

```c++
void someFunction(){
  if (wifi){
    if(login){
      if(admin){
        someFunction();
      } else {
        // Handle non-admin user
        return;
    }
  }else {
    // Handle no login
    return;
    }
  }else {
    // Handle no wifi
    return;
  }
}

```

This change to 

```c++
void someFunction(){
  if (!wifi) {
    // Handle no wifi
    return;
  }
  if (!login) {
    // Handle no login
    return;
  }
  if (!admin) {
    // Handle non-admin user
    return;
  }
  someFunction();
}

```

---

## 📚 References

[^1]: [Factory Method Pattern - Refactoring Guru](https://refactoring.guru/design-patterns/factory-method)
[^2]: [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.javier8a.com/itc/bd1/articulo.pdf)
