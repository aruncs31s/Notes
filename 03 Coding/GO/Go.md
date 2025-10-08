---
id: Go
aliases: []
tags:
  - coding
  - go
dg-publish: true
---
# GO

- [[Gin]]
- [[GORM]]
- [[JSON]]
- [[HTTP Servers]]
- [[SOLID principle]]
- [[Programming Practices]]
- [[MultiThreading]]
## Creating New Project

## Need

```tasks
not done
path includes 03 Coding/Go

```

## Creating New Project

```bash
mkdir project_name
go mod init project_name

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

### IO 

```go
fmt.Print("Enter product code: ")
code, _ := reader.ReadString('\n')
code = strings.TrimSpace(code)

```

### Var
- use camelCase for variables also 

#### Types
>[!NOTE] **Concrete Types**
>A concrete type is a data type that is not an **interface**

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

`issue@var_def_init obsidian`

```go 
type Students struct {
	gorm.Model
	Name       string `json:"name"`
	Username   string `json:"username"`
	LevelOne   bool   `json:"level_0"`
	LevelTwo   bool   `json:"level_1"`
	LevelThree bool   `json:"level_2"`
	LevelFour  bool   `json:"level_3"`
	LevelFive  bool   `json:"level_4"`
	LevelSix   bool   `json:"level_5"`
	LevelSeven bool   `json:"level_6"`
}
u := models.Students

```

- [ ] Check why this is working and the first one dont 

```go
u := models.Students{}

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

###### Converting from `string`

```go
func Atoi(str string) (int, error)

```

>[!NOTE]- **Example**
>```go
>func main() {
>  x := "245"
>  y, e := strconv.Atoi(x)
>  if e == nil {
> 	 fmt.Printf("%T \n %v", y, y)
> 	 }
>}
>```

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

## Iterative Statements

```go
for i := 0; i < 10; i++ {
        fmt.Println(i)
     }

```

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ { // no parentheses surrounding and { always required
		sum += i
	}
	fmt.Println(sum)
}

```

```go

package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; { // no init and post
		sum += sum
	}
	fmt.Println(sum)
}

```

> [!NOTE]
> For is Go's "while" , so there is no seperate `while`
>
> ```go
> for sum < 1000 {
> 	sum += sum
> }
> fmt.Println(sum)
>}
> ```

```go
// infinite loop
for {
	}

```

### Switches

```go

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("macOS.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}

```

## Conditional

```go
if x < 0 { // no () but must -> {}
		return sqrt(-x) + "i"
	}

```

### Short if

```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim { // scope of v limited to this if.
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}

```

```go
func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return v // this will result in an error {undifined}
}

```

```go
if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim) // v is also in scope
	}
v + 10 // error not in scope

```

## Interfaces
^0cc7de

_“Any type that has this method is allowed.”_ ^d2e304

```go
type Bird interface {
    Fly() string
}

```

Any type that has a method `Fly() string` is considered a `Bird`.

### Map Interface

![[Go MAP.png|200]]

## Pointers 

```go 
func BrokenSwap(a int, b int) {
  a, b = b, a
}

func RealSwap(a *int, b *int) {
  *a, *b = *b, *a
}

```



```go
package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Name string `json:"user_name" validate:"required,min=3"`
	Age  int    `json:"user_age"`
	City string `json:"-"` // "-" indicates the field should be ignored for this tag
}

func main() {
	user := User{Name: "Alice", Age: 30, City: "New York"}

	// Get the reflect.Type of the struct
	// If 'user' is a pointer, use .Elem() to get the underlying struct type
	typ := reflect.TypeOf(user)

	fmt.Println("Struct Field Names and 'json' Tag Values:")
	// Iterate over each field in the struct
	for i := 0; i < typ.NumField(); i++ {
		field := typ.Field(i) // Get the StructField at index i

		// Get the field name
		fieldName := field.Name

		// Get the value of the "json" tag
		jsonTag := field.Tag.Get("json")

		fmt.Printf("Field Name: %s, JSON Tag: %s\n", fieldName, jsonTag)
	}

	fmt.Println("\nAccessing a specific tag key (e.g., 'validate'):")
	// Accessing a specific field by name and its tag
	if field, ok := typ.FieldByName("Name"); ok {
		validateTag := field.Tag.Get("validate")
		fmt.Printf("Field 'Name', Validate Tag: %s\n", validateTag)
	}
}
```
## References
1. _Learning Go: An Idiomatic Approach to Real-World Go Programming_