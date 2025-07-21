---
id: Go
aliases: []
tags: []
---

# GO

- [[Gin]]

## Creating New Project

- [ ] ?

```bash
mkdir project_name
go mod init example/project_name
```

```tree

```

This works

```
❯ mkdir math_
❯ cd math_
❯ nvim p1.go
❯ go run .
My favorite number is 2
```

---

GOPATH -> `go/bin`

## Basics

- Every Go program is made up of packages.
- Programs start running in package main.
- the package name is the same as the last element of the import path.

- [ ] In Go, a name is exported if it begins with a capital letter.
- Pizza is an exported name, as is Pi, which is exported from the math package.
