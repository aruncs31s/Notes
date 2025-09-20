---
id: Structural_Pattern
aliases: []
tags:
  - coding
  - design_patterns
dg-publish: true
---
# Structural Patterns

- [[Facade]]
- [[Adapter Pattern]]
- [[Repository Design Pattern]]
> How **objects relate to eachother** 

**Purpose**: **Organizing classes and objects into larger structures** to simplify relationships and ensure **flexible and efficient composition**

#### Code Example - Decorator Pattern

```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

# Usage
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())  # Output: 8

```
