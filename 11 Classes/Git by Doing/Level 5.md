---
github: https://github.com/aruncs31s/git_by_doing_level_5
tags:
  - for_students
  - git_by_doing
  - sub_module
Status: working
dg-publish: true
---
# Level 5 
```dataview
Table without ID  file.name as "Name" , github as Link , status as Status, file.inlinks as Mentioned
where file = this.file
```
---
This is a recap , of what you have learn up until now and , reinforcing what you have learned up until now. 
Also we are going to switch completely to cli, meaning that we are going to use tools like , `vim` or `nano`. And almost ....
- [ ] complete this 

## Lets recap 
Up until you have seen the following commands 
- `git status`
- `git log`
- `git add`
- `git commit`
- `git log`


### Configuring Git
Let's start by properly configuring git 
![[Screenshot 2025-07-19 at 2.06.26 PM.png]]



Git comes with a [configuration](https://git-scm.com/docs/git-config) both at the global and the repo (project) level. Most of the time, you'll just use the global config.

## Assignment

Let's set your identity. Check if your `user.name` and `user.email` are already set:

```bash
git config --get user.name
```

```bash
git config --get user.email
```

If they aren't, set them. I recommend using your GitHub username and email.

```bash
git config --add --global user.name "github_username_here"
git config --add --global user.email "email@example.com"
```

Finally, let's set a default branch (we'll talk more about configs and branches later) so that we're all on the same page. Run:

To ensure you get proper credit (or more likely, blame) for all the code you write, you need to set your name and email.

We're using `master` for now because it is Git's default, but later we'll change it to `main`, which is GitHub's default. Just bear with us for a second.

Your `~/.gitconfig` file is the file that stores your global Git configuration. View it:

```bash
cat ~/.gitconfig
```

If you screw up a commit message, you can change it with the `--amend` flag. For example:

```bash
# Change the last commit message
git commit --amend -m "A: add contents.md"
```


# Git Log

A Git repo is a (potentially very long) list of commits, where each commit represents the _full state of the repository_ at a given point in time.

For convenience, you can refer to any commit or change within Git by using the first `7` characters of its hash. For mine, that's `5ba786f`.
Next, run `git log` again, but this time use the `-n` and `--no-pager` options to limit the maximum number of commits shown, and more importantly, to run it without the interactive pager. E.g.:

Next, run `git log` again, but this time use the `-n` and `--no-pager` options to limit the maximum number of commits shown, and more importantly, to run it without the interactive pager. E.g.:

```bash
git --no-pager log -n 10
```




# Cat File

Luckily, Git has a built-in plumbing command, [cat-file](https://git-scm.com/docs/git-cat-file), that allows us to see the contents of a commit without needing to futz around with the object files directly.

```bash
git cat-file -p <hash>
```

## Assignment

1. [ ] Use the `cat-file` command to view the contents of your last commit. (Use `-p` for pretty-print.)
2. [ ] For the CLI to be able to check your output, do it again, but redirect the output to a temporary file:

```bash
catfile-command-here > /tmp/catfileout.txt
```

**Run and submit** the CLI tests.

## Tip

Use `git log -1` to get the hash of your last commit.


# Trees and Blobs

Now that we understand some of our plumbing equipment, let's get into the pipes. Here are some terms to know:

- `tree`: git's way of storing a directory
- `blob`: git's way of storing a file

Here's what I got when I inspected my last commit:

```bash
> git cat-file -p 5ba786fcc93e8092831c01e71444b9baa2228a4f

tree 4e507fdc6d9044ccd8a4a3061324c9f711c4667d
author ThePrimeagen <the.primeagen@aol.com> 1705891256 -0700
committer ThePrimeagen <the.primeagen@aol.com> 1705891256 -0700

A: add contents.md
```

Notice that we can see:

- The `tree` object
- The `author`
- The `committer`
- The commit message

However, we _cannot_ see the contents of the `contents.md` file itself! That's because the `blob` object stores it.

## Assignment

1. [ ] Use `git cat-file -p` again, but this time with the hash of the `tree`object instead of the commit hash. You should see a `blob` object with _its_ own hash.
2. [ ] Use `cat-file` _again_ to view the contents of the `blob` object.
3. Run that same command, but this time [redirect the output](https://tldp.org/LDP/intro-linux/html/sect_05_01.html) to a temporary file: `/tmp/blobfile.txt`.

**Run and submit** the CLI tests.

