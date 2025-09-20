---
id: Creational_Patterns
aliases: []
tags:
  - coding
  - design_patterns
dg-publish: true
---
# Creational Patterns
- [[Factory Design Pattern]]
- [[Builder]]
- [[Singleton]]
**Purpose**: Deal with object creation mechanisms, trying to **abstract the instantiation process**

#### Examples:
- **Abstract Factory**: Provide an interface for creating families of related objects without specifying concrete classes
- **Builder**: Separate construction of complex objects from their representation
- **Factory Method**: Define an interface for creating objects, but let subclasses decide which class to instantiate
- **Prototype**: Create new objects by copying a prototypical instance
- **Singleton**: Ensure a class has only one instance with global access

#### Code Example - Factory Pattern

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()

# Usage
pet = animal_factory("dog")
print(pet.speak())  # Output: Woof!

```
