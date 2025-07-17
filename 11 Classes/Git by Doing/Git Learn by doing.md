---
dg-publish: true
startTime: Sat Jul 12 09:51:16 PM IST 2025
---

# Git Learn By Doing
It is planed to teach git in 100 levels.
Starting from clone to fully mastering git.
- [[Level 0]]
- [[Level 1]]
- [[Level 2]]
- [[Level 3]] 
- [[Level 4]]



- [x] `git add` ✅ 2025-07-14
- [x] What is git ✅ 2025-07-13
- [ ] `git commit` 

**Objectives**
1. Introducing Git

How this is planned: The difficulty will increase from task to task by end of this you will learn about
1. Git 
2. `git add` 
3. `git commit`
4. `git branch`
5. `git checkout`
6. `git push`
7. `git pull`
8. `git log`
9. `git stash`


## Task 1: Installing Git 
1. Windows: click [here](https://git-scm.com/downloads/win) to download 
2. Linux assuming no one is using linux (now)
> [!abstract]- **Install git in linux**
> No need linux comes with `git` type the following to check if installed 
> ```bash 
> git -v 
> ```
>> [!note]- If not installed
>> ```bash
>> # Ubuntu 
>> sudo apt install git 
>> # Arch 
>> sudo pacman -S git 
>> paru -S git 
>> yay -S git
>> ```


## Task 2: Obstaining a repo 

  

```bash

1. initialize score to 0

2. initialize question_count to 0

3. ask a question

4. increment the qustion_count

5. check the answer

6. if the answer is correct increment the score

7. now ask a new question

8. increment the qustion_count

9. check the answer

10. if the answer is correct increment the score

  

this happens all over again

```

If you have read that , you can see steps 4, 5 , 6 and 8 , 9 , 10 are same

more specificly incrementing counts(score as well) and checking answers almost always same so you can just do this

  

```bash

create a function say fn which does the step 4, 5 and 6

  

1. initialize score to 0

2. initialize question_count to 0

3. ask a question

4. call fn()

5. now ask a new question

6. call fn

```

  

You can see we have , reduced the repetations , in theory , the repetatin will still remain the same , but the coder have to write less when they use functions.