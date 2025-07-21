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
```

```go
// hello.go
package main

import "fmt"

func main() {
    fmt.println("hello, world!")
}

```

```bash
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

### Var

#### Types

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128

const Pi = 3.14 // why Pi not in caps

```

- The `int`, `uint`, and `uintptr` types are usually `32` bits wide on 32-bit systems and `64` bits wide on 64-bit systems

```go
// multi var decleration
var c, python, java bool
// with initialization
var i, j int = 1, 2
// short var decleration
k := 3 // not available outside the function
// it can detect type.
c, python, java := true, false, "no!"
```

```go
package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s) // 0 0 false ""
}
```

##### Type Conversion

```go
var i int = 42 // 42 int
var f float64 = float64(i) // 42 float
var u uint = uint(f) // 42 int again
// or
i := 42 // 42 int
f := float64(i) // 42.00 ??
u := uint(f) // 42 int
```

##### Type inference

```go
var i int
j := i // j is an int
i := 42           // int
f := 3.142        // float64
g := 0.867 + 0.5i // complex128
```

##### Numeric Constants

- [ ] Check this program

```go

package main

import "fmt"
// NOTE: Constants defined in a block are computed once at compile-time.
const (
	// Create a huge number by shifting a 1 bit left 100 places.
	// In other words, the binary number that is 1 followed by 100 zeroes.
	Big = 1 << 100
	// Shift it right again 99 places, so we end up with 1<<1, or 2.
	Small = Big >> 99
)

func needInt(x int) int { return x*10 + 1 }
func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}
```

---

```go

var a, b string
a, b = swap("hello", "world")
// is equavalent to

a,b := swap("hello","world")
```

## Functions

```go
func <function_name>(<type args>) <return_type> {
	return <expression>
}
```

```go
package main
import "fmt"
func add( x int,  y int) int {
	return x + y
}
// is same as
func add_1(x, y int) int {
	return x + y
}

func main(){
fmt.Println(add(1,2))
fmt.Println(add_1(1,2))
}
```

```go
return x + y // possible
return x,y // possible
```

```go
func sum(x,y int) int {
return x + y
}
```

```go
func swap(x, y string) (string, string)  { // multiple return values  or tuple return
	return y, x
}
```

calling

```go
func main() {
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}
```

### Return Values

- A return statement without arguments returns the named return values. This is known as a "naked" return.

> [!Important]
> Naked return statements should be used only in short functions, as with the example shown here. They can harm readability in longer functions.

```go
package main
import "fmt"
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main(){
  fmt.Println(split(10))
}
```

Same as

```go
package main
import "fmt"
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main(){
  fmt.Println(split(10))
}
```
