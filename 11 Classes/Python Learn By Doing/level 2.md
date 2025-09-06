# Level 2


## `level_2.py` Workflow (Current)

### Overview
`level_2.py` acts as a setup wizard for a GitHub portfolio website. It collects user info, fetches repositories, lets users verify/correct their details, and prepares everything to run the web app.

### Workflow Diagram

```mermaid
flowchart TD
   Start[Script Start] --> Init[initialize_repos]
   Init --> StatusObj[Create Status Object]
   StatusObj --> QHelper[Create Question Helper]
   QHelper --> AskUser[Ask GitHub Username]
   AskUser --> ConfirmUser{Confirm Username?}
   ConfirmUser -- Yes --> Setup[Setup Git & Files Objects]
   ConfirmUser -- No --> Fallback[Use Default Username]
   Setup --> CheckRepos{repos.json exists?}
   CheckRepos -- No --> FetchSave[Fetch & Save Repositories]
   CheckRepos -- Yes --> SkipFetch[Skip Fetch]
   FetchSave --> SetStatus[Set Status Git Reference]
   SkipFetch --> SetStatus
   Fallback --> ReturnObjs[Create Fallback Objects]
   SetStatus --> ReturnObjs
   ReturnObjs --> Main[main]
   Main --> ShowStatus[Display Current Status]
   ShowStatus --> InfoCorrect{Is Info Correct?}
   InfoCorrect -- Yes --> RunInstr[Show Run Instructions]
   InfoCorrect -- No --> AskCorrect[Ask Which to Correct]
   AskCorrect --> Choice{Choice}
   Choice -- Name --> NewName[Ask New Name]
   Choice -- Username --> NewUser[Ask New Username]
   Choice -- Email --> NewEmail[Ask New Email]
   Choice -- Invalid --> Exit[Exit]
   NewName --> UpdateName[Update Git Name]
   NewUser --> UpdateUser[Update Git Username]
   NewEmail --> UpdateEmail[Update Git Email]
   UpdateName --> SaveRepos[Save Repositories]
   UpdateUser --> SaveRepos
   UpdateEmail --> SaveRepos
   SaveRepos --> FinalStatus[Display Final Status]
   FinalStatus --> RunInstr
   RunInstr --> End[End]
   Exit --> End
```

### Detailed Flow

#### 1. Initialization & Imports
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from modules.question import Question
from modules.status import Status
from modules.git import *
from modules.files import *
```
- **Purpose**: Set up Python path to access modules in `src/` directory
- **Imports**: Question helper, Status tracker, Git operations, File operations

#### 2. `initialize_repos()` Function

**Purpose**: Collect GitHub username and initialize core objects

**Steps**:
1. **Create Status Object**
   ```python
   status = Status(current_question=0)
   ```
   - Initializes status tracking with question counter at 0

2. **Create Question Helper**
   ```python
   question_helper = Question(status)
   ```
   - Links question system with status tracking

3. **Ask for GitHub Username**
   ```python
   github_username = question_helper.ask_question("What is your github username")
   ```
   - Prompts user for GitHub username
   - Updates status counter

4. **Confirm Username**
   ```python
   is_sure = input(f"Are you sure that your username is {github_username} ? ")
   ```
   - Asks user to confirm the entered username

5. **Setup Objects (If Confirmed)**
   ```python
   if is_sure.lower() in ["yes","y"]:
       git: Git = Git(username=github_username)
       files: Files = Files(git=git)
   ```
   - Creates Git object with username
   - Creates Files object linked to Git

6. **Check Repository File**
   ```python
   if not files.is_repos_available():
       files.save_repositories_to_file("repos.json")
   ```
   - Checks if `repos.json` exists and has data
   - Fetches and saves repositories if file is missing/empty

7. **Set Status Git Reference**
   ```python
   status.set_git(git)
   ```
   - Links Git object to status for display purposes

8. **Return Objects**
   ```python
   return git, files, status, question_helper
   ```

9. **Fallback (If Not Confirmed)**
   ```python
   else:
       return Git(username="aruncs31s"), Files(git=Git(username="aruncs31s")), Status(current_question=0), Question(Status(current_question=0))
   ```
   - Uses default username "aruncs31s" if user declines

#### 3. `main()` Function

**Purpose**: Main orchestration function that handles user interaction flow

**Steps**:
1. **Initialize Components**
   ```python
   git, files, status, question_helper = initialize_repos()
   ```

2. **Display Current Status**
   ```python
   status.status()
   ```
   - Shows current name, username, and email

3. **Ask for Confirmation**
   ```python
   is_correct: str = input("Is this all correct ? (yes/no) ")
   ```

4. **Success Path (Information Correct)**
   ```python
   if is_correct.lower() in ["yes","y"]:
       print("Now Run the website using python src/app.py")
       return
   ```
   - Provides instructions to run the web app
   - Exits successfully

5. **Correction Path (Information Incorrect)**
   ```python
   else:
       print("Which one is incorrect ?")
       which_one = input("1. Name\n2. Username\n3. Email\n")
   ```

6. **Handle Corrections**
   - **Option 1 (Name)**:
     ```python
     new_name = question_helper.ask_question("What is your name")
     git.name = new_name
     ```
   - **Option 2 (Username)**:
     ```python
     new_username: str = question_helper.ask_question("What is your github username")
     git.username = new_username
     ```
   - **Option 3 (Email)**:
     ```python
     new_email: str = question_helper.ask_question("What is your email")
     git.github_email = new_email
     ```

7. **Save Updated Data**
   ```python
   files.save_repositories_to_file("repos.json")
   ```
   - Fetches fresh repository data with updated username

8. **Display Final Status**
   ```python
   status.status()
   ```
   - Shows updated information

9. **Final Instructions**
   ```python
   print("Now Run the website using python src/app.py")
   ```

### Key Classes Used

#### `Status` Class
- Tracks current question number
- Stores reference to Git object
- Provides status display functionality

#### `Question` Class
- Handles user input prompts
- Updates status counter
- Formats questions with numbering

#### `Git` Class
- Manages GitHub username
- Fetches user information from GitHub API
- Handles local git configuration

#### `Files` Class
- Manages repository data file (`repos.json`)
- Fetches repositories from GitHub
- Saves data to JSON format

### Error Handling

#### Repository Fetching
- Checks if `repos.json` exists
- Falls back to API call if file is missing
- Handles API failures gracefully

#### User Input Validation
- Accepts multiple confirmation formats ("yes", "y", "no", "n")
- Provides clear options for corrections
- Handles invalid menu selections

#### Fallback Scenarios
- Uses default username if user declines input
- Creates fresh objects for fallback cases
- Maintains consistent object structure

### Data Flow

```mermaid
flowchart LR
    A[User Input] --> B[Question System]
    B --> C[Status Updates]
    C --> D[Git Object]
    D --> E[Files Object]
    E --> F[repos.json]
    F --> G[Web App]
    G --> H[Portfolio Display]
    
    I[GitHub API] --> D
    J[Local Git Config] --> D
```

### Exit Points

1. **Successful Confirmation**: User confirms info is correct
2. **Invalid Menu Choice**: User enters invalid option
3. **Script Completion**: After corrections are made and saved

### Integration Points

- **GitHub API**: Fetches user repositories and profile data
- **Local Git Config**: Reads/writes git user settings
- **File System**: Reads/writes `repos.json`
- **Web App**: Provides instructions to run `python src/app.py`

This script serves as a setup wizard that ensures all user information is correct before launching the portfolio website.

### Detailed Flow

#### 1. Initialization & Imports
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from modules.question import Question
from modules.status import Status
from modules.git import *
from modules.files import *
```
- **Purpose**: Set up Python path to access modules in `src/` directory
- **Imports**: Question helper, Status tracker, Git operations, File operations

#### 2. `initialize_repos()` Function

**Purpose**: Collect GitHub username and initialize core objects

**Steps**:
1. **Create Status Object**
   ```python
   status = Status(current_question=0)
   ```
   - Initializes status tracking with question counter at 0

2. **Create Question Helper**
   ```python
   question_helper = Question(status)
   ```
   - Links question system with status tracking

3. **Ask for GitHub Username**
   ```python
   github_username = question_helper.ask_question("What is your github username")
   ```
   - Prompts user for GitHub username
   - Updates status counter

4. **Confirm Username**
   ```python
   is_sure = input(f"Are you sure that your username is {github_username} ? ")
   ```
   - Asks user to confirm the entered username

5. **Setup Objects (If Confirmed)**
   ```python
   if is_sure.lower() in ["yes","y"]:
       git: Git = Git(username=github_username)
       files: Files = Files(git=git)
   ```
   - Creates Git object with username
   - Creates Files object linked to Git

6. **Check Repository File**
   ```python
   if not files.is_repos_available():
       files.save_repositories_to_file("repos.json")
   ```
   - Checks if `repos.json` exists and has data
   - Fetches and saves repositories if file is missing/empty

7. **Set Status Git Reference**
   ```python
   status.set_git(git)
   ```
   - Links Git object to status for display purposes

8. **Return Objects**
   ```python
   return git, files, status, question_helper
   ```

9. **Fallback (If Not Confirmed)**
   ```python
   else:
       return Git(username="aruncs31s"), Files(git=Git(username="aruncs31s")), Status(current_question=0), Question(Status(current_question=0))
   ```
   - Uses default username "aruncs31s" if user declines

#### 3. `main()` Function

**Purpose**: Main orchestration function that handles user interaction flow

**Steps**:
1. **Initialize Components**
   ```python
   git, files, status, question_helper = initialize_repos()
   ```

2. **Display Current Status**
   ```python
   status.status()
   ```
   - Shows current name, username, and email

3. **Ask for Confirmation**
   ```python
   is_correct: str = input("Is this all correct ? (yes/no) ")
   ```

4. **Success Path (Information Correct)**
   ```python
   if is_correct.lower() in ["yes","y"]:
       print("Now Run the website using python src/app.py")
       return
   ```
   - Provides instructions to run the web app
   - Exits successfully

5. **Correction Path (Information Incorrect)**
   ```python
   else:
       print("Which one is incorrect ?")
       which_one = input("1. Name
2. Username
3. Email
")
   ```

6. **Handle Corrections**
   - **Option 1 (Name)**:
     ```python
     new_name = question_helper.ask_question("What is your name")
     git.name = new_name
     ```
   - **Option 2 (Username)**:
     ```python
     new_username: str = question_helper.ask_question("What is your github username")
     git.username = new_username
     ```
   - **Option 3 (Email)**:
     ```python
     new_email: str = question_helper.ask_question("What is your email")
     git.github_email = new_email
     ```

7. **Save Updated Data**
   ```python
   files.save_repositories_to_file("repos.json")
   ```
   - Fetches fresh repository data with updated username

8. **Display Final Status**
   ```python
   status.status()
   ```
   - Shows updated information

9. **Final Instructions**
   ```python
   print("Now Run the website using python src/app.py")
   ```

### Key Classes Used

#### `Status` Class
- Tracks current question number
- Stores reference to Git object
- Provides status display functionality

#### `Question` Class
- Handles user input prompts
- Updates status counter
- Formats questions with numbering

#### `Git` Class
- Manages GitHub username
- Fetches user information from GitHub API
- Handles local git configuration

#### `Files` Class
- Manages repository data file (`repos.json`)
- Fetches repositories from GitHub
- Saves data to JSON format

### Error Handling

#### Repository Fetching
- Checks if `repos.json` exists
- Falls back to API call if file is missing
- Handles API failures gracefully

#### User Input Validation
- Accepts multiple confirmation formats ("yes", "y", "no", "n")
- Provides clear options for corrections
- Handles invalid menu selections

#### Fallback Scenarios
- Uses default username if user declines input
- Creates fresh objects for fallback cases
- Maintains consistent object structure

### Data Flow

```
User Input → Question → Status Update → Git Object → Files Object → repos.json
     ↑                                                            ↓
     └──────────────────── Confirmation ──────────────────────────┘
```

### Exit Points

1. **Successful Confirmation**: User confirms info is correct
2. **Invalid Menu Choice**: User enters invalid option
3. **Script Completion**: After corrections are made and saved

### Integration Points

- **GitHub API**: Fetches user repositories and profile data
- **Local Git Config**: Reads/writes git user settings
- **File System**: Reads/writes `repos.json`
- **Web App**: Provides instructions to run `python src/app.py`

This script serves as a setup wizard that ensures all user information is correct before launching the portfolio website. 
