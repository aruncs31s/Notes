---
id: 06-Classes
tags:
  - python
  - classes
  - oop
  - object-oriented
dg-publish: true
---

# Classes & OOP

Learn Object-Oriented Programming in Python.

## What is OOP?

OOP treats real-world entities as objects, grouping related data and functionality together. In traditional languages like C, data and functions are separate, but in OOP they're grouped together as objects.

## Class vs Object

- **Class**: Blueprint for creating objects
- **Object**: Instance of a class

Everything in Python is an object:

```python
print(type(1))        # <class 'int'>
print(type("Hello"))  # <class 'str'>
print(type(1.5))      # <class 'float'>
```

## Creating a Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_age(self):
        print(f"Age is {self.age}")
```

## Creating Objects

```python
P1 = Person("Arun", 23)
P2 = Person("Arun Again", 24)

P1.print_age()  # Age is 23
```

- **`self`**: Reference to the current instance of the class

## The `__init__` Method

The initializer is called when an object is created:

```python
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth
    
    def print_area(self):
        print(f"Area is {self.area}")

R1 = Rectangle(2, 5)
R1.print_area()  # Area is 10
```

Can you create a class without `__init__`? Yes:

```python
class Empty:
    def print_something(self):
        print("Something")

E = Empty()
E.print_something()
```

## The `__str__` Method

Defines a string representation of an object:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person Name: {self.name}"

Arun = Person("Arun", 23)
print(Arun)  # Person Name: Arun
```

---

## Encapsulation

Bundling data and methods, restricting direct access to some components.

### Public vs Private

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # Public
        self.__age = age    # Private (name mangling)

Arun = Person("Arun", 23)
print(Arun.name)     # Works
print(Arun.__age)    # AttributeError!
```

### Accessing Private Attributes

```python
# The "Pythonic" way - use getter methods
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

Arun = Person("Arun", 23)
print(Arun.get_age())  # 23
```

### Private Methods

Add `__` prefix to make methods private:

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
    
    def __private_method(self):
        print("Private!")

p = Person("Arun", 23)
p.__private_method()  # AttributeError
```

---

## Inheritance

A class inherits attributes and methods from a parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print(f"{self.name} Barks!")

class GermanShepherd(Dog):
    def search(self):
        print(f"{self.name} is Searching!")

Buddy = GermanShepherd("Buddy")
Buddy.bark()     # Buddy Barks!
Buddy.search()   # Buddy is Searching!
```

### Types of Inheritance

| Type | Description |
|------|-------------|
| Single | One parent class |
| Multiple | Multiple parent classes |
| Multilevel | A → B → C chain |
| Hierarchical | One parent, multiple children |
| Hybrid | Combination of types |

### Multiple Inheritance

```python
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

c = C()
c.method_a()  # Method A
c.method_b()  # Method B
c.method_c()  # Method C
```

---

## The `super()` Method

Calls methods from the parent class:

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        return f"{self.firstname}, {self.lastname}"

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Call parent __init__
        self.graduationyear = year
    
    def print_details(self):
        print(f"{super().printname()}, Graduation: {self.graduationyear}")

student1 = Student("Arun", "PP", 2025)
student1.print_details()  # Arun, PP, Graduation: 2025
```

---

## Polymorphism

Objects of different classes responding to the same method call differently:

```python
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

R1 = Rectangle(3, 4)
C1 = Circle(3)

print(R1.area())  # 12
print(C1.area())  # 28.26
```

Same method `.area()` works differently based on the class.

---

## Abstraction

Hiding complex implementation details, showing only essential features:

```python
from math import sqrt
print(sqrt(25))  # 5
```

You only need to know `sqrt()` returns square root - implementation is hidden.

---

**Next:** [[07-Modules]] - Common Python modules

**See Also:** [[05-Comprehensions]] - Comprehensions
