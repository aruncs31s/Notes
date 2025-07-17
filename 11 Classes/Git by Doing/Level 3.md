---
tags:
  - git_by_doing
  - for_students
  - sub_module
github: https://github.com/aruncs31s/git_by_doing_level_3/
Status: Done
---
# Level 3

Task: Understanding `git log`, `git commit` and `git checkout`


>[!IMPORTANT] 
> This task if more difficult and involves , editing some files, but there are some rules 
>1. Do not create new `functions` just try copy pasting
> What you need is already in this repo , try to find it.
> 
> **To Complete this Level**
>The following program should not contain any errors 
>```bash
>Bash check. Sh
>```

>[!TIP]
> Hints: 
> 2. `app.py` is corrupted 
> 3. `simple_math.py` is missing some functions (all functions to be exact)
> 4. Hints will be in the `README.md` of each commit.





## `git commit`
The `git commit` command captures a **snapshot** of the project's currently staged changes.

1. So what is a SnapShot?

The typical defenition of *snapshot* is "a casual photograph made typically by an amateur with a small handheld camera" taken from [this](https://www.merriam-webster.com/dictionary/snapshot) site

2. What are the characteristics of a photograph
- Once taken its contents can not be changed.
- No matter when you look at it , it will stays the name (ignoring aging)

We can say that snapshot is a mechanism used to preserve some systems state.

  

3. What this *snapshots* have to do with the `git commit`

So you use `git commit` to take the snapshot of the `state` of the directory. Which means you are storing a check point in your folder , and you can comeback at any time in the future to this check point.

### Example

Imagine you are creating a music app and it has this following functions

File Name: `app.py`
```python
def album_cover():
def play():
def pause():
def stop():
```

and you decided to store this store this state , let name it state `x1`.
After some days some of your app's user requsted , they want to see the lyrics of currently playing songs. So the you created a new version of that app

```python
def play():
def pause():
def stop():
def show_lyrics():
```

Then he uploaded this app again. But after uploading he suddently realize that his music app no loger shows the `album_cover()`, but he realizes that he did store a check point `x1` which has that code, so he was saved.

### Procedure

In order to do a `git commit` yo have to do `git add` first

### Lets try
- I have a file named `app.py` in my git directory.

![alt text](imgs_for_3/image-1.png)

if i check the status of the directory you can see that there is a new `untracked` file

![alt text](imgs_for_3/image-2.png)

i have now staged the file using `git add`

![alt text](imgs/image-3.png)

- Let's `commit` it using `git commit`

![alt text](imgs_for_3/image-4.png)

- If we check status now , you can see that it says there is nothing to commit , so now **the staged files are commited**

![alt text](imgs_for_3/image-5.png)


##### How to check if all working fine?

Just type `git log` and you will se the following


![alt text](imgs_for_3/image-7.png)

![alt text](imgs_for_3/image-6.png)


![alt text](imgs_for_3/image-8.png)

>[!IMPORTANT]
> **New Command**
> ```bash
> Git log
> ```
> Usage: Used to view the commit history.

#### Now Lets make some changes

As i've said in above example i have removed one line and added one line

![alt text](imgs_for_3/image-9.png)

You can see that there is `def album_cover():` is missing.

Now lets `commit` this new change.

![alt text](imgs_for_3/image-10.png)

And If you check `log` now you can see that There are 2 `commits` , first one if the older one with the `album_cover` and second one is the newly created one.

![alt text](imgs_for_3/image-11.png)


##### This is cool and all but how to recover the lost function ?

![alt text](imgs_for_3/image-12.png)

You can see the contents of the `app.py` before i do `git checkout <checkpint id>` and after i do the `checkout` thing. You think long enough , you will realize that , this is just like doing `undo` operation , in a sense the `git commit` thing is a `undo` history.

>[!IMPORTANT]
> **New Command**
> ```bash
> Git checkout
> ```
> Usage: Used to view (go to) specific , commits.

#### Now that you got what you wanted , how to go back?


```bash
git checkout -
```
This command is used to go back to where you come from , just like `redo` thing.

![alt text](imgs_for_3/image-13.png)

![alt text](imgs_for_3/image-14.png)