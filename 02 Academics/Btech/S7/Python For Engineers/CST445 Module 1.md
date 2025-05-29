---
aliases: 
Date: "30-05-2025"
---
# CST445 Module 1
## Syllabus

- [x] Getting Started with Python Programming ✅ 
- [x] Running code in the interactive shell, ✅ 
  - [x] Editing, ✅ 
  - [x] Saving, ✅
  - [x] and Running a script. ✅ 
- [x] Using editors ✅ 
  - [x] IDLE, ✅ 
  - [x] Jupyter. ✅ 
- [x] Basic coding skills ✅ 
- [x] - [ ] Working with data types, ✅ 2025-05-30
  - [ ] Numeric data types and Character sets,
  - [ ] Keywords,
  - [ ] Variables and
  - [ ] Assignment statement,
  - [ ] Operators,
  - [ ] Expressions,
  - [ ] Working with numeric data,
  - [ ] Type conversions,
  - [ ] Comments in the program,
  - [ ] Input Processing,
  - [ ] and Output,
  - [ ] Formatting output.
- [ ]
- [ ] How Python works.
- [ ] Detecting and correcting syntax errors.
- [ ] Using built in functions and modules in math module.
- [ ] Control statements
- [ ] Selection structure
  - [ ] if-else,
  - [ ] if-elif-else.
- [ ] Iteration structure
  - [ ] for, while.
- [ ] Testing the control statements.
- [ ] Lazy evaluation.


## Getting Started With Python
- **Python** is high-level , general-purpose programming language ? nop it is a scripting language
**Downloading Windows**
- [Link](https://www.python.org/downloads/)
**Linux** (no need comes pre installed)
```bash
# debian
sudo apt install python

# arch
yay -S python 
sudo pacman -S python
```

**Running Code in interactive shell**
just type `python` then start typing , *variables and function definitions all those will be in memory and it will stay in memory as long as the interpreter session running*


#### Input , output , processing
```python
# input
a = input("Enter a number")

# output
print(a)
```

- One thing to note here that the default type will be a string from the `input()` and you may need to type cast it to work as expected for example 
```python
a = input("Enter a number")
if a==5:
	print("HI")
```
- this program will not work as expected (run and find out)
```python
a = int(input("Enter a number"))
if a==5:
	print("HI")
```

#### Editing
 - Used when the program is no loger one or two lines(complex) 
 - Easy to transport , save for later etc.
- You can use editor such as [[Neovim]] or vim etc , or you can use python ide [IDLE](https://docs.python.org/3/library/idle.html)
#### Data types

| Integer          | `int`, `long` | 1,2,3, -1 , 0       |
| ---------------- | ------------- | ------------------- |
| Real Numbers     | `float`       | 1.2 , -1.2          |
| Character strngs | str           | "HI" , "" , "Hello" |

### Operators
1. Arithmetic

#### Arithmetic Operators
```python
a , b  = 1 , 2 
a + b  # 3 "#" is the single line comment
a - b  # -1  
a * b  # 2 
a / b  # .5 
a % b  #  1 
b ** 2 # 4
a // b # 0
```

#### Comparison Operator

```python
a, b = 5, 10

# Equal to
a == b  # False

# Not equal to
a != b  # True

# Greater than
a > b   # False

# Less than
a < b   # True

# Greater than or equal to
a >= b  # False

# Less than or equal to
a <= b  # True
```
#### Logical Operators

```python
x, y = True, False

# AND - True if both operands are True
x and y  # False

# OR - True if at least one operand is True
x or y   # True

# NOT - Inverts the Boolean value 0 -> 1 , 1 -> 0
not x    # False
not y    # True
```

#### Membership Operators
```python
lst = [1, 2, 3, 4]
name = "Arun"

# IN - True if value is found in sequence
2 in lst       # True
"run" in name  # True
5 in lst       # False

# NOT IN - True if value is not found in sequence
5 not in lst   # True
"y" not in name # True
```

#### Identity Operators
```python
m = [1, 2]
n = [1, 2]
p = m

# IS - True if both variables point to same object
m is p    # True

m is n    # False (same values but different objects)

# IS NOT - True if variables point to different objects
m is not n  # True
```

```python
print(m is n) # False , different objects even if values are sae
print(m == n) # True same value even if different objects
``` 

#### Bitwise Operators

```python 
a , b = 1, 2  # 01 , 10

''' Bitwise AND 
  01
& 10 '''
a & b  # 0

#Bitwise OR
# 11 
a | b  # 3

# Bitwise XOR
 
a ^ b  # 3

# Bitwise NOT
# this might be confusing explain later.
~a     # -2

#  Left Shift (<<)

a << 1  # 2

#Right Shift (>>)
a >> 1  # 0
```

- [ ] explain biwise `not` 🏁 delete 

#### Assignment Operators
```python
x = 10

x += 3  # x = x + 3 → 13
x -= 2  # 11
x *= 2  #  22
x /= 4  # 5.5
x %= 3  #  2.5
x **= 2 #   6.25
x //= 2 #  3.0
```

### Type Casting
```python
int(3.1) # 3 
float(3) # 3.0
str(10) # '10'
```