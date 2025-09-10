# Domain Driven Design 

- **Ubiquitous language**  
    Everyone (developers, business people, domain experts) speaks the same language. The terms you use in code (`StaffExperience`, `StaffID`, etc.) should match the terms business people actually use.
- **Entities & Value Objects**
    - **Entities**: Objects with identity (e.g., `Staff` with a unique `StaffID`).
    - **Value Objects**: Objects defined only by their values (e.g., `DateRange`, `Address`).
- **Aggregates & Aggregate Roots**
    - An **aggregate** is a cluster of domain objects that should be treated as one unit.
    - The **aggregate root** is the entry point. You only interact with the root directly, and it enforces the rules.
    Example: `Order` is the aggregate root, containing `OrderLine` items. You don’t save `OrderLine` directly, you save the `Order`.
- **Repositories**  
    Abstractions for persisting and retrieving aggregates.  
    They pretend the database doesn’t exist — you just “ask the repo” for a domain object.