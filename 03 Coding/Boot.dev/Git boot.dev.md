---
id: Git boot.dev
aliases: []
tags:
  - coding
  - bootdev
cssclasses: 
dg-publish: true
---
# Git boot.dev

#### Initial Setup

```bash
go install github.com/bootdotdev/bootdev@latest

bootdev --version

```

To run

```bash
bootdev run

```

To submit

```bash
bootdev submit

```

To login

```bash
bootdev login

```

```bash
bootdev run 65e6780d-fdde-447a-9898-b30b73793a3a
bootdev submit 65e6780d-fdde-447a-9898-b30b73793a3a

```

Just to check everything is working as intended? i guess

##### Installing Git

1. Arch Based Systems

```bash
sudo pacman -Sy git

```

2. Ubuntu/Debian Based Systems

```bash
sudo apt install git

```

Check

```bash
bootdev run 0552b1c3-49d9-4d4b-b44d-e91188a79c92
bootdev submit 0552b1c3-49d9-4d4b-b44d-e91188a79c92

```

#### Git

High Level commands

```bash
git status
git add
git commit
git push
git pull
git log

```

Low Level commands

```bash
git apply
git commit-tree
git hash-object

```

`master` is `git`'s default branch
`main` is `github`'s default branch

##### Initial Configs

To check

```bash
git config --get user.name
git config --get user.email

```

To Set

```bash
git config --add --global user.name "github_username_here"
git config --add --global user.email "email@example.com"

```

To set default branch `master`

```bash
git config --global init.defaultBranch master

```

To check above go well

```bash
cat ~/.gitconfig

```

```bash
bootdev run 69fb8a76-9456-47e2-9804-05466614882e
bootdev submit 69fb8a76-9456-47e2-9804-05466614882e

```
