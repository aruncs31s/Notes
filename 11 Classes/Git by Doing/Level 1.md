---
github: https://github.com/aruncs31s/level_1
tags:
  - git_by_doing
  - sub_module
  - for_students
Status: Done
dg-publish: true
type: Quiz
---
# Level 1
> Next 
> - [[Level 2]]
```dataview
Table without ID  file.name as "Name" , github as Link , status as Status, file.outlinks as Mentioned
where file = this.file
```
Task: Understanding what is git?

> [!IMPORTANT]
> After reading this complete page you need to install python in you system and run the following
>
>```bash
>Python quiz.py
>```
## Little About Git

Git was created by ["Linus Torvalds"](https://github.com/torvalds), for maintaining his projects. He is also the creater of linux.
Maintaining ? Firt thing do not take the word "maintaining" in literal sense, maintaining means updating and patching[^1] etc.

So `git` is used to do the **version control** thing.

Version Control ? : Imagine you created a game using `python` programming language , and you send it to a friend , or publish it on playstore or Appstore or something , after sometime you have a new idea that you want to add little more features to this game , there is a fact that you have already published a this game. So what you will do is publish this _changes_(new features) as a new version. You might have this doubt ? Why cant i just the old publish and republish the game with new changes , then i wont have to worry about the versioning thing. You are right but imagin these senarios

1. You made the initial game when you are using a old crappy computer and you bought a new computer and it is much faster that the old one , and you cramming too much features into the game and this made the game bulky. The old crappy computer may not handle this much things so the game will start to lag or in extreme case the old computer wont support new the bulky game.

2. You can see the above trend with `windows` older computer will only support upto `windows 7` , and only new processor will support `windows 11` things like that.
   More Technical Resons:
   The versioning scheme is useful for

3. Tracking your changes over time
4. Colabrating with others
5. Maintining support for older devices
   There are many other reasons

## Versioning

Software versioning usually follows the **Semantic versioning** it looks somethig like this `v0.0.1` `v0.0.1` etc in which is in the format `MAJOR.MINOR.PATCH` so if you have a major update from `v1.0.0` your new version will be `v2.0.0`
[^1]: patching means appling changes to something like a software to fix the bugs and things.
