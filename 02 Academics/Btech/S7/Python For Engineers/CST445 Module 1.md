---
id: CST445_Module_1
aliases: []
tags:
  - academics
  - btech
  - s7
  - python_for_engineers
Date: "30-05-2025"
dg-publish: true
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
  - [x] Numeric data types and Character sets, ✅ 2025-05-30
  - [ ] Keywords,
  - [x] Variables and ✅ 2025-05-30
  - [x] Assignment statement, ✅ 2025-05-30
  - [x] Operators, ✅ 2025-05-30
  - [ ] Expressions,
  - [ ] Working with numeric data,
  - [x] Type conversions, ✅ 2025-05-30
  - [x] Comments in the program, ✅ 2025-05-30
  - [x] Input Processing, ✅ 2025-05-30
  - [x] and Output, ✅ 2025-05-30
  - [x] Formatting output. ✅ 2025-05-30
- [ ]
- [x] How Python works. ✅ 2025-05-30
- [ ] Detecting and correcting syntax errors.
- [ ] Using built in functions and modules in math module.
- [x] Control statements ✅ 2025-05-30
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

^38a289

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

- this program will not work as expected (run and find out) (happens because `int(5)` is not same as `str(5)`)

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

```python
a = 5 
type(a)
a = str(a)
type(a)
a = float(a)
type(a)

```

![[Pasted image 20250530165358.png]]

### Comments

```python
# this is the single line comment
'''
This is the multiline 
Comment 
'''
"""
This is also a multiline 
Comment
"""

```

![[Pasted image 20250530165727.png]]

### Formatting The output

```python
# Normal 
for i in range(10):
# Normal 
	print(i)
for i in range(10):
# right justify
	print("%6s" % i)
for i in range(10):
# left justify
	print("%-6s" % i)

```

```python
for i in range(10):
# right justify
	print(f"%{i}s" % i)

```

```python
for i in range(10):
# right justify
	print(f"%{i}s%{10-2*i}s" % (i , i))

```

```op
0         0
1       1
 2     2
  3   3
   4 4
    55
     66 
      77   
       88     
        99 

```

```python
for i in range(10):
	print(i , i**4 * 10)
	

```

```python
for i in range(10):
	print("%6s%12s" %( i , i**4 * 10))

```

### How Python Works
- Interpreter reads the source code and , if it encounters an gramatical(syntax) error it stops the exceution and throws and error.
- If there is no error the python code is converted into **byte code**(low level language)
- This byte code is then send to the **Python Virtual Machine(PVM**) 

#### Errors 

#####  Intendation
Most of the  errors(syntax errors) will occur due to **intendation** 
- intendation groups same block of codes to gether and it is the main part of the python syntax
- Each new line shuld match the previous line intendation 

```python
a = 10 
	b = 20 

```

This will cause a `unexpected indent` error  but the following will not

```python
if 5==int(5):
	print(5) # intend with 4 spaces
	

```

```python
if 5==int(5):
  print(5) # intend with 2 spaces
	

```

**Rules**
1. Same block → Same indentation
2. 4(Tab) , 2 space intendation for new code block
3. Intendation do not matter for code enclosed in `()` , `[]` or `{}`

## Functions 
**Important things to keep in mind**
- intend the defenition of a function from its decleration
- scope is limited within intendations 

#syntax 

![[02 Academics/Btech/S7/Python For Engineers/Class Notes#^8ae1a2|Class Notes]]

#example 

![[02 Academics/Btech/S7/Python For Engineers/Class Notes#^06cc71|Class Notes]]

## Control Statements
1. Selection Strucure `if else`
2. Iteration structure `for i in ..`

![[02 Academics/Btech/S7/Python For Engineers/Class Notes#IF ELSE|Class Notes]]

![[02 Academics/Btech/S7/Python For Engineers/Class Notes#Iterative Statements(Loops)|Class Notes]]
