---
id: Strategy_Pattern
aliases: []
tags:
  - coding
  - design_patterns
  - behavioral_pattern
dg-publish: true
---
# Strategy Pattern
- [[Strategy Pattern Using Golang]]

> It lets me define *a family of algorithms, encapsulate each one, and make them interchangeable*.

> *Strategy lets the algorithm vary independently from clients that use it*.

>[!Note]- Analogy
>Imagine if i have a specific goal like  computing something or doing some task , but there might be different way to go about it , this is what the [[Strategy Pattern]] all about

>[!Note]- **Example**
> Imagine a navigation app like Google Maps:
>
> It can show directions by driving, walking, bicycling, or public transit.
>
> Each is a strategy for finding directions.
>
> You can switch between them at runtime.

## ✅ When to Use Strategy Pattern
- You want to use different variants of an algorithm (e.g., different sorting techniques).

- You want to avoid using many **conditional statements** (`if-else` or `switch`) to choose behavior.

- You want to make algorithms interchangeable and independently testable.

## 🏗️ Structure of Strategy Pattern

```go
type Strategy interface {
    Execute(data string) string
}
type ConcreteStrategyA struct{}
func (s *ConcreteStrategyA) Execute(data string) string {
    return "ConcreteStrategyA: " + data
}
type ConcreteStrategyB struct{}
func (s *ConcreteStrategyB) Execute(data string) string {
    return "ConcreteStrategyB: " + data
}
type Context struct {
    strategy Strategy
}
func (c *Context) SetStrategy(strategy Strategy) {
    c.strategy = strategy
}
func (c *Context) ExecuteStrategy(data string) string {
    return c.strategy.Execute(data)
}

``` 