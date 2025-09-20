---
id: Series_Exam_2
aliases: []
tags:
  - academics
  - btech
  - s7
  - python_for_engineers
Date: 18-10-2024
dg-publish: true
---
# Series Exam 2
### **Practice Questions:**
#### *Part A*
1. Explain constructor in python class with example. [[#^0ffaea|Answer]]
2. Write a Python class named ‘Rectangle’ constructed by a length and width and a method which will compute the area of a rectangle. [[#^5862c1|Answer]]
3. List the different object-oriented concepts. 
4. Explain how operator overloading is done in python with example.
5. Write a Python program to validate an integer input with exception handling.
6. Write the specific purpose of functions used in plotting: i) plot( ) ii) legend( ) iii. Title( )
7. Illustrate how mathematical expressions are written using matplotlib.
8. Give the reason for using Error bars in plotting with appropriate syntax.
9. Write the steps to be followed to draw a straight line using matplotlib module.
#### Answers
1. A **Constructor** in python class is a special method which is used to initialize the object of a newly created class. It will be called automatically when a function is creating  ^0ffaea

#example 

```python
class Student_class:
	def __init__(self, name, age):
		self.name = name
		self.age = age
new_student = Student_class("Arun" , 100)
print(f"Name {new_student.name} , Age: {new_student.age}" )

```

```

Name Arun , Age: 100

```

2. Python class named Rectangle and method to compute its area ? ^5862c1

```python
class Rectangle:
	def __init__(self,length,width):
		self.length = length
		self.width = width
		self.area = .5 * length * width
	def get_area(self):
		return self.area
new_rectangle = Rectangle(10,5)
print(f"Area: {new_rectangle.get_area()}" )

```

3. List the different [[oop]] concepts in python
- Class 
- Objects
- Polymorphism 
- Encapsulation
- Inheritance 
- Data Abstraction

#### Part B

1. Create a class Student with attributes name and roll no. and a method dataprint() for displaying the same. Create two instances of the class and call the method for each instance.
2. Explain inheritance and different forms of inheritance. How they are implemented in Python?
3. What is polymorphism? Why do we need polymorphism? Give an example in the context of OOP in Python.
4. How to handle an exception using try except block? Explain with the help of a program.
5. What is abstraction? Write a program to create an abstract class named quadrilateral to find the perimeter of a rectangle.
6. Create a class Person with attributes name, age salary. Define a method getdetails() to assign values to the attributes and a method display() for showing the details. Create an instance of the class and call the methods.
7. Write a Python class named bank account with details like Name of the depositor, account number, type of account and balance amount in the account. Write methods to assign the following:
- a) Initial values to deposit,
-  b) Withdraw an amount after checking the balance and
- c) Display name, account number and balance.

```python

class bank_account:
    def __init__(self, name, acc_number, type, balance):
        self.holder_name = name
        self.acc_number = acc_number
        self.type = type
        self.balance = balance

    def get_initial_values(self, value):
        self.inital_deposite = value

    def withdraw(self, money):
        if self.balance - money > 0:
            self.balance - money
        print(f"Balance is {self.balance}")

    def set_balance(self, amount):
        self.balance -= amount

arun = bank_account("Arun", 1221212, "savings", 1000)

while True:
    print(
        f" Account Name: {arun.holder_name}\n Acc No: {arun.acc_number}\n Type: {arun.type}\n Balance: {arun.balance}"
    )
    the_input = input("Want to withdraw money? (y/n)")
    if the_input == "y":
        amount = int(input("Enter the amount to withdraw: "))
        arun.withdraw(amount)
        arun.set_balance(amount)

```

8. Write a program that validates name and age as entered by the user to determine whether the person can cast vote or not.

```python
class Vote:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def validate(self):
        if self.age >= 18:
            print(f"{self.name} can cast a vote")
        else:
            print(f"{self.name} cannot cast a vote")

x = Vote("someGuy", 20)
x.validate()

```

9. Create an array in the range 1 to 20 with values 1.25 apart. Another array contains the log values of the elements in the first array. Create a plot of first vs second array. Specify the x- axis(containing first array’s values) title as ‘Random Values’ and y-axis title as ‘Logarithm Values’.
10.  Plot the functions tan x and cot x vs x on the same plot with x going from −2π to 2π. Makesure the limits of the x-axis do not extend beyond the limits of the data. Plot tan x in redcolor and cot x in blue color and include a legend to label the two curves. Place the legend within the plot at the lower right corner. Draw thin gray lines behind the curves, one horizontal at y = 0 and the other vertical at x = 0.
11. Plot the function sin(x)/x vs. x with x[0 to 10].Make sure the limits of the x-axis do not extend beyond the limits of the data. Plot sin x with multiple plots laid out in the same window.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 10, 0.01)

sin_x = np.sin(x)
sin_x_over_x = sin_x / x

plt.plot(x, sin_x_over_x, label="sin(x)/x")
plt.plot(x, sin_x, label="sin(x)")
plt.xlim([0, 10])
plt.legend()
plt.show()

```

13. Explain how matplotlib can be used to create dimensional vector field plots.
14. Write a Python code to plot lines with multiple axes in a figure.
15. Explain in detail about the structure of matplotlib.
16. Illustrate contour plot and vector plot.