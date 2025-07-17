---
id: Git Learn by doing
aliases: []
tags: []
dg-publish: true
startTime: Sat Jul 12 09:51:16 PM IST 2025
---

# Git Learn By Doing

It is planed to teach git in 100 Levels. Starting from clone to fully mastering git.

```dataview
Table  file.ctime as "Created" , file.mtime as "Modified" , type as "Type",status as "Status"
from #git_by_doing
sort file.name asc
```

---

How this is planned: The difficulty will increase from task to task by end of this you will learn about

## Installing Git

1. Windows: click [here](https://git-scm.com/downloads/win) to download
2. Linux assuming no one is using linux (now)
   > [!abstract]- **Install git in linux**
   > No need linux comes with `git` type the following to check if installed
   >
   > ```bash
   > git -v
   > ```
   >
   > > [!note]- If not installed
   > >
   > > ```bash
   > > # Ubuntu
   > > sudo apt install git
   > > # Arch
   > > sudo pacman -S git
   > > paru -S git
   > > yay -S git
   > > ```

## Introduction

What is Git?

> [!NOTE]- Non Technical
> Git was created by ["Linus Torvalds"](https://github.com/torvalds), for maintaining his projects. He is also the creater of linux.
> Maintaining ? Firt thing do not take the word "maintaining" in literal sense, maintaining means updating and patching[^1] etc.
>
> So `git` is used to do the **version control** thing.
>
> Version Control ? : Imagine you created a game using `python` programming language , and you send it to a friend , or publish it on playstore or Appstore or something , after sometime you have a new idea that you want to add little more features to this game , there is a fact that you have already published a this game. So what you will do is publish this _changes_(new features) as a new version. You might have this doubt ? Why cant i just the old publish and republish the game with new changes , then i wont have to worry about the versioning thing. You are right but imagin these senarios
>
> 1.  You made the initial game when you are using a old crappy computer and you bought a new computer and it is much faster that the old one , and you cramming too much features into the game and this made the game bulky. The old crappy computer may not handle this much things so the game will start to lag or in extreme case the old computer wont support new the bulky game.
> 2.  You can see the above trend with `windows` older computer will only support upto `windows 7` , and only new processor will support `windows 11` things like that.
>     More Technical Resons:
>     The versioning scheme is useful for
> 3.  Tracking your changes over time
> 4.  Colabrating with others
> 5.  Maintining support for older devices
>     There are many other reasons

> [!abstract]+ Technical
> There are mainly 2 types version control systems[^1]


> [!summary]+ Git
> Git is a distribute version control system created by "Linus Torvalds"

[^1] Version Control System: It is a tool that helps track changes in source code over time.
## References

- [Git Pro book](https://git-scm.com/book/en/v2)
- [Git branch](https://git-scm.com/docs/git-branch)
- [[Git]]
