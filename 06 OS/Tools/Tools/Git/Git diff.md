---
id: Git_diff
aliases: []
tags:
  - os
  - tools
  - git
dg-publish: true
---
- Show files changed in the last commit
git diff --name-only HEAD^0

- Show files changed in the commit before the last one
git diff --name-only HEAD^1

- Show files changed in the commit before that
git diff --name-only HEAD^2
