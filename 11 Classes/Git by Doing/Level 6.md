---
tags:
  - git_by_doing
  - for_students
  - sub_note
github: https://github.com/aruncs31s/git_by_doing_level_6
---
# Level 6
- [[Git API]]
```dataview
Table without ID  file.name as "Name" , github as Link , status as Status, file.inlinks as Mentioned
where file = this.file
```

## Lets recap 
Up until you have seen the following commands 
```bash
git status # to check the status of the repo 
git log # to see the commit history
git add # to add files to the staging area
git commit # to commit the staged files
git restore # to restore file that has been added but accidently deleted.
git log # to see the commit history
git branch # to see the branches
git checkout # to switch branches
git config # to mess with configuration
```
And you will need to use most of them inorder to complete this level. 

## New Commands
in this level you are going to learn the following commands. 
```bash
git pull 
git push 
```

> [!abstract]- Dev Notes
> I have to implement a task where they will use `git pull` and `git push` , but these 2 commands include remote? 



## Coding
- [[Parsing JSON]]
Since i have been busy , i tried to implement it using go , most of the techniques used here is done only to study their implementation like [[GORoutines]] 
