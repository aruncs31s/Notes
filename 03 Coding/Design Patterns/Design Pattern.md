---
tags:
  - programming
---
# Design Patterns

- [[Decorator]]

- designing reusable object-oriented software
- Your design should be specific to the problem at hand but also general enough to address future problems and requirements.
- *, they reuse solutions that have worked for them in the past*
- These patternssolve specific design problems and make object-oriented designs moreflexible,elegant, and ultimately reusable[^2]
- object-oriented designers follow patterns like "represent states with objects"
- descriptions of communicating objects and classes that are customized to solve a general design problem in a particular context.
> [!Abstract] represent states with objects
> - each possible state of an object is implemented as a separate class or object
> - This allows an object to **change its behavior** depending on its **current state**

- decorate objects so you can easily add/remove features? 

>  **decoupling views from model** -> **separating the UI (view)** from the **data and business logic (model)**
>  - The **model** doesn’t care _how_ it’s displayed.
>- The **view** doesn’t care _how_ data is fetched or processed.
>- They can change **independently**.

## Design Pattern types
1. Creational Pattern: patterns deal with object creation mechanisms, trying to **abstract the instantiation proces**
2. Structural Pattern: **organizing classes and objects into larger structures**, especially to simplify relationships and ensure **flexible and efficient composition**.
3. Behavioral Pattern: concerned with **communication between objects**, focusing on **how responsibility is distributed** and **how algorithms are handled**

### Creational Pettern
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

pet = animal_factory("dog")
print(pet.speak()) 
```

### Structural Pattern 
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

print(coffee.cost())  

```
### Behavioral Pattern 

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class EmailNotifier:
    def update(self, message):
        print(f"Sending email: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"Sending SMS: {message}")

# Usage
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())

subject.notify("New order received.")

```
### Factory
***Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.*[^1]
- a typical solution to a common object creation problem
[^1]:https://refactoring.guru/design-patterns/factory-method 
[^2]: https://www.javier8a.com/itc/bd1/articulo.pdf