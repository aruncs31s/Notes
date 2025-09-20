---
id: main_Exam
aliases: []
tags:
  - academics
  - btech
  - s7
  - python_for_engineers
Date: 28-11-2024
dg-publish: true
---
# main Exam

### Functional Oriented

```python
def square(num):
    return num * num
def which_is_large(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2
number = 2
result = square(number)
print(f"Square of Number: {result}")
print(f"10 sqare is {square(10)}")

print(f"Which is large 10 , 20 , large is = {which_is_large(10,20 )}")

```

### OOP

```python
class someClass:
    def __init__(self, numbers):
        self.numbers = numbers

    def which_is_large(self,num1,num2):
		if num1>num2:
			return num1
		else:
			return num2
	def square(self,num):
        return num * num

newNumber = someClass(10,20)

print(f"Sqare =  {newNumber.square(10)}")

```

#### Class

```python
class oldClass:
	methods
class nameOfClass(oldClass):
	def __inti__(self,arguments)
	. . .
	. . .
	methods 
A = nameOfClass(01,22,33)

```

 ### Try except
  - The try and except block in Python is used for **exception handling**. 
  - It allows you to write code that can **gracefully handle errors** **instead of crashing the program** when an error occurs

```python
result = 1
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

```