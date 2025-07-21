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

```bash
mkdir prog_name
cd prog_name
echo"CAT EOF
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
EOF" >> hello.go
go build ./hello.go
go run .

```

---

GOPATH -> `go/bin`

## Basics

- Every Go program is made up of packages.
- Programs start running in package main.
- the package name is the same as the last element of the import path.

- [ ] In Go, a name is exported if it begins with a capital letter.

  > [!NOTE] Exporting
  > `Pizza` is an exported name, as is `Pi`, which is exported from the math package.
  > pizza and pi do not start with a capital letter, so they are not exported.
  > So , which means that after exporting `Pi` , we should them using _smallLetters_

this is not correct

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.pi)
}
```

and this one is correct

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Pi)
}
```
