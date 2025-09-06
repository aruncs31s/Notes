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



