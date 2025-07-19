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

## Linux Basics
- `mkdir` , `ls` , `cd` , `nano` , `mv` 

## Linux Commands
```bash
command <required> [optional]
```


Arguments in angle brackets <> are mandatory and must be provided when running the command.
Arguments in square brackets [] are optional and can be included if needed.
#### `mkdir`

```bash
mkdir folder_name 
```




git status
git add
git commit
git push
git pull
git log


git apply
git commit-tree
git hash-object


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
