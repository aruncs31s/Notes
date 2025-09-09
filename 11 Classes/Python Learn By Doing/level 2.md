---
id: level_2
aliases: []
tags:
  - classes
  - python_learn_by_doing
dg-publish: true
---
# Level 2

## Coding 
- Using Behavioural Design Pattern

### Classes 
- **Status** must be shared between all the other objects.
- **Git** must be shared between **Files** and **Status**.
- **Question** must be shared between **Status** and **Files**.
- **Files** must be shared between **Status** and **Git**.
- **Status** must be initialized after **Git**.
- **Files** must be initialized after **Git**.
- **Question** must be initialized after **Status**.
- **Git** must be initialized first.

### Class Responsibility Collaborator (CRC) Cards
| Class Name | Responsibility | Collaborators |
|------------|----------------|---------------|
| Git        | To interact with GitHub API and fetch user data | Status, Files |
| Status     | To manage and track the current state of the application | Git, Question |
| Files      | To manage and track the files in the application | Git, Status |
| Question   | To manage and track the questions in the application | Status, Files |  

### Flow of Control

1. First create a `Git` object. The username can be passed as as an argument or can be set later. 

```python
def initialize_git() -> Git:
    username = input("Enter your GitHub username: ")
    return Git(username=username)

```

There is an another level of verification of username in the `Git` class itself.

```python
class Git:
    def __init__(self,username: str = ""):
        # Initialize with empty username
        self.username = username
        
        if self.username == "":
            self.ask_username()
            if self.username == "":
                raise ValueError("Username cannot be empty")

```
