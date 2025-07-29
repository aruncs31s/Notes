---
tags:
  - programming
  - software_design
cssclasses:
  - wide-page
dg-publish: true
---

# Design Patterns
>[!NOTE]- **Hierarchy** 
>```mermaid
>---
>config:
>  theme: redux
>---
>flowchart LR
>    A["Design Pattern"] --> B["Creational Pattern"] & n1@{ label: "<strong data-start=\"844\" data-end=\"867\" style=\"color:\" data-darkreader-inline-color=\"\">Structural Patterns</strong>" } & n2["Behavioral Patterns"]
>    B --> C["setOptions"] & D["Factory Method"] & n9["Abstract Factory"] & n10["Builder"] & n11["Prototype"]
>    n1 --> n3["Adapter"] & n5["Bridge"] & n12["Composite"] & n13["Decorator"] & n14["Facade"] & n15["Flyweight"] & n16["Proxy"]
>    n2 --> n7["Chain of Responsibility"] & n8["Command"] & n17["Interpreter"] & n18["Iterator"] & n19["Mediator"] & n20["Memento"] & n21["Observer"] & n22["State"] & n23["Strategy"] & n24["Template Method"] & n25["Visitor"]
>    A@{ shape: rounded}
>    B@{ shape: rounded}
>    n1@{ shape: rounded}
>    n2@{ shape: rounded}
>    n3@{ shape: rect}
>    n5@{ shape: rect}
>    n7@{ shape: rect}
>    n8@{ shape: rect}
>    style A fill:#D50000
>    style B fill:#2962FF
>    style n1 fill:#FF6D00
>    style n2 fill:#AA00FF
>
> ```

- [ ] Checkout **Atomic Design methodology**


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