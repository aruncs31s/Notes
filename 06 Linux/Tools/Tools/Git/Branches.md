---
id: 1722694456-PFUM
aliases:
  - Branchers
tags: []
---

# Branches

#### Adding a branch locally and submitting it to remote

1. Goto that repo

```bash
cd /path/of/repo
```

2. Create new Branch

```bash
git checkout -b new-branch-name
```

3. Stage and commit the changes

```bash
git add .
git commit -m "message"
```

4. push that change to the new branch

```bash
git branch -u origin new_branch
```

#### Remove A branch

[source](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/)

```bash
// delete branch locally
git branch -d localBranchName

// delete branch remotely
git push origin --delete remoteBranchName
```
