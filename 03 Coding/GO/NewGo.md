---
id: NewGo
aliases: []
tags:
  - coding
  - go
dg-publish: true
---
# Go Programming Language - Complete Guide

> [!info] Go (Golang) Overview
> Go is a statically typed, compiled programming language developed by Google. It's designed for simplicity, efficiency, and excellent concurrency support.

## Table of Contents

1. [Basics](#basics)
2. [Data Types](#data-types)
3. [Control Structures](#control-structures)
4. [Functions](#functions)
5. [Structs and Methods](#structs-and-methods)
6. [Interfaces](#interfaces)
7. [Concurrency](#concurrency)
8. [Memory Management](#memory-management)
9. [Error Handling](#error-handling)
10. [Advanced Features](#advanced-features)
11. [Best Practices](#best-practices)
12. [Performance Optimization](#performance-optimization)

## Basics

### Hello World

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

```

### Package System

```go
// Package declaration (must be first non-comment line)
package main

// Import statement
import (
    "fmt"          // Standard library
    "os"
    "math/rand"
    "github.com/user/repo" // External package
    . "fmt"        // Dot import (imports into current namespace)
    _ "image/png"  // Blank import (init only)
    alias "very/long/package/name" // Alias import
)

```

### Variables and Constants

```go
// Variable declarations
var name string                    // Zero value
var age int = 25                  // Explicit initialization
var city, country string          // Multiple variables
var (                             // Block declaration
    height float64
    weight float64
)

// Short variable declaration (inside functions only)
name := "John"
age, height := 25, 5.8

// Constants
const Pi = 3.14159
const (
    StatusOK = 200
    StatusNotFound = 404
)

// Typed constants
const TypedPi float64 = 3.14159

// iota for enumeration
const (
    Sunday = iota    // 0
    Monday           // 1
    Tuesday          // 2
    Wednesday        // 3
    Thursday         // 4
    Friday           // 5
    Saturday         // 6
)

// Complex iota usage
const (
    _  = iota             // Skip 0
    KB = 1 << (10 * iota) // 1024
    MB                    // 1048576
    GB                    // 1073741824
)

```

## Data Types

### Basic Types

```go
// Boolean
var isActive bool = true

// Numeric types
var (
    // Signed integers
    a int8   = -128 to 127
    b int16  = -32768 to 32767
    c int32  = -2147483648 to 2147483647
    d int64  = -9223372036854775808 to 9223372036854775807
    e int    = platform dependent (32 or 64 bit)
    
    // Unsigned integers
    f uint8  = 0 to 255
    g uint16 = 0 to 65535
    h uint32 = 0 to 4294967295
    i uint64 = 0 to 18446744073709551615
    j uint   = platform dependent
    k uintptr = holds pointer address
    
    // Floating point
    l float32 = IEEE-754 32-bit
    m float64 = IEEE-754 64-bit
    
    // Complex numbers
    n complex64  = complex(float32, float32)
    o complex128 = complex(float64, float64)
)

// String
var message string = "Hello"
var multiline string = `This is a
multiline string
using backticks`

// Byte (alias for uint8)
var b byte = 255

// Rune (alias for int32, represents Unicode code point)
var r rune = '♠'

```

### Composite Types

#### Arrays

```go
// Array declaration
var arr [5]int                    // Zero-valued array
var numbers = [5]int{1, 2, 3, 4, 5} // Initialized array
var auto = [...]int{1, 2, 3}     // Compiler determines length
var sparse = [10]int{1: 10, 9: 90} // Sparse initialization

// Multidimensional arrays
var matrix [3][4]int
var initialized = [2][3]int{{1, 2, 3}, {4, 5, 6}}

// Array operations
length := len(arr)
// Arrays are value types (copied on assignment)
arr2 := arr // Creates a copy

```

#### Slices

```go
// Slice creation
var slice []int                   // Nil slice
slice = make([]int, 5)           // Length 5, capacity 5
slice = make([]int, 3, 10)       // Length 3, capacity 10
slice = []int{1, 2, 3, 4, 5}     // Slice literal

// Slice from array
arr := [5]int{1, 2, 3, 4, 5}
slice = arr[1:4]                 // [2, 3, 4]
slice = arr[:3]                  // [1, 2, 3]
slice = arr[2:]                  // [3, 4, 5]
slice = arr[:]                   // [1, 2, 3, 4, 5]

// Slice operations
length := len(slice)
capacity := cap(slice)
slice = append(slice, 6, 7, 8)   // Append elements
slice = append(slice, []int{9, 10}...) // Append slice

// Copy slices
dest := make([]int, len(slice))
copy(dest, slice)

// Slice tricks
// Remove element at index i
slice = append(slice[:i], slice[i+1:]...)
// Insert element at index i
slice = append(slice[:i], append([]int{newElement}, slice[i:]...)...)

```

#### Maps

```go
// Map creation
var m map[string]int              // Nil map
m = make(map[string]int)          // Empty map
m = map[string]int{               // Map literal
    "apple":  5,
    "banana": 3,
}

// Map operations
m["orange"] = 8                   // Set value
value := m["apple"]               // Get value
value, ok := m["grape"]           // Check existence
delete(m, "banana")               // Delete key

// Iterate over map
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}

// Check if key exists
if value, exists := m["key"]; exists {
    fmt.Println("Key exists with value:", value)
}

```

#### Pointers

```go
// Pointer declaration and usage
var p *int                        // Pointer to int
x := 42
p = &x                           // Address of x
fmt.Println(*p)                  // Dereference pointer

// Pointer to struct
type Person struct {
    Name string
    Age  int
}

person := Person{"Alice", 30}
ptr := &person
ptr.Age = 31                     // Automatic dereferencing
(*ptr).Age = 31                  // Explicit dereferencing

// Function with pointer parameter
func increment(x *int) {
    *x++
}

// New function
p = new(int)                     // Allocates memory and returns pointer
*p = 42

```

## Control Structures

### Conditional Statements

```go
// if statement
if x > 0 {
    fmt.Println("Positive")
} else if x < 0 {
    fmt.Println("Negative")
} else {
    fmt.Println("Zero")
}

// if with initialization
if err := someFunction(); err != nil {
    return err
}

// switch statement
switch day := time.Now().Weekday(); day {
case time.Saturday, time.Sunday:
    fmt.Println("Weekend")
default:
    fmt.Println("Weekday")
}

// Type switch
switch v := interface{}(x).(type) {
case int:
    fmt.Printf("Integer: %d\n", v)
case string:
    fmt.Printf("String: %s\n", v)
case bool:
    fmt.Printf("Boolean: %t\n", v)
default:
    fmt.Printf("Unknown type: %T\n", v)
}

// Switch without expression (replaces if-else chain)
switch {
case x > 0:
    fmt.Println("Positive")
case x < 0:
    fmt.Println("Negative")
default:
    fmt.Println("Zero")
}

```

### Loops

```go
// for loop (traditional)
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// for loop (while-like)
i := 0
for i < 10 {
    fmt.Println(i)
    i++
}

// for loop (infinite)
for {
    if condition {
        break
    }
}

// for-range loop
slice := []int{1, 2, 3, 4, 5}
for index, value := range slice {
    fmt.Printf("Index: %d, Value: %d\n", index, value)
}

// Range over string (iterates over runes)
for index, rune := range "Hello, 世界" {
    fmt.Printf("Index: %d, Rune: %c\n", index, rune)
}

// Range over map
m := map[string]int{"a": 1, "b": 2}
for key, value := range m {
    fmt.Printf("Key: %s, Value: %d\n", key, value)
}

// Range over channel
ch := make(chan int)
go func() {
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)
}()
for value := range ch {
    fmt.Println(value)
}

```

### Flow Control

```go
// break and continue
for i := 0; i < 10; i++ {
    if i == 3 {
        continue // Skip iteration
    }
    if i == 7 {
        break // Exit loop
    }
    fmt.Println(i)
}

// Labeled break and continue
outer:
for i := 0; i < 3; i++ {
    for j := 0; j < 3; j++ {
        if i == 1 && j == 1 {
            break outer // Break out of outer loop
        }
        fmt.Printf("i=%d, j=%d\n", i, j)
    }
}

// goto statement (rarely used)
func example() {
    i := 0
start:
    if i < 3 {
        fmt.Println(i)
        i++
        goto start
    }
}

```

## Functions

### Basic Functions

```go
// Function declaration
func add(a, b int) int {
    return a + b
}

// Multiple parameters of same type
func multiply(a, b, c int) int {
    return a * b * c
}

// Multiple return values
func divmod(a, b int) (int, int) {
    return a / b, a % b
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return // Naked return
}

// Variadic functions
func sum(numbers ...int) int {
    total := 0
    for _, num := range numbers {
        total += num
    }
    return total
}

// Call: sum(1, 2, 3, 4)
// Call with slice: sum(slice...)

```

### Advanced Function Features

```go
// Function types
type MathFunc func(int, int) int

func operate(a, b int, op MathFunc) int {
    return op(a, b)
}

// Anonymous functions
add := func(a, b int) int {
    return a + b
}

// Closures
func makeCounter() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}

counter := makeCounter()
fmt.Println(counter()) // 1
fmt.Println(counter()) // 2

// Higher-order functions
func filter(slice []int, predicate func(int) bool) []int {
    var result []int
    for _, v := range slice {
        if predicate(v) {
            result = append(result, v)
        }
    }
    return result
}

// Usage
evens := filter([]int{1, 2, 3, 4, 5}, func(n int) bool {
    return n%2 == 0
})

// Defer statement
func example() {
    defer fmt.Println("This runs last")
    defer fmt.Println("This runs second to last")
    fmt.Println("This runs first")
}

// Defer with function calls
func copyFile(src, dst string) error {
    srcFile, err := os.Open(src)
    if err != nil {
        return err
    }
    defer srcFile.Close() // Ensure file is closed

    dstFile, err := os.Create(dst)
    if err != nil {
        return err
    }
    defer dstFile.Close() // Ensure file is closed

    _, err = io.Copy(dstFile, srcFile)
    return err
}

```

### Function Patterns

```go
// Method chaining
type Builder struct {
    data []string
}

func (b *Builder) Add(s string) *Builder {
    b.data = append(b.data, s)
    return b
}

func (b *Builder) Build() string {
    return strings.Join(b.data, " ")
}

// Usage: builder.Add("Hello").Add("World").Build()

// Functional options pattern
type Config struct {
    Host string
    Port int
    SSL  bool
}

type Option func(*Config)

func WithHost(host string) Option {
    return func(c *Config) {
        c.Host = host
    }
}

func WithPort(port int) Option {
    return func(c *Config) {
        c.Port = port
    }
}

func WithSSL() Option {
    return func(c *Config) {
        c.SSL = true
    }
}

func NewConfig(opts ...Option) *Config {
    config := &Config{
        Host: "localhost",
        Port: 8080,
        SSL:  false,
    }
    for _, opt := range opts {
        opt(config)
    }
    return config
}

// Usage: NewConfig(WithHost("example.com"), WithPort(443), WithSSL())

```

## Structs and Methods

### Struct Definition

```go
// Basic struct
type Person struct {
    Name    string
    Age     int
    Email   string
}

// Struct with tags (used by JSON, XML, etc.)
type User struct {
    ID       int    `json:"id" db:"user_id"`
    Username string `json:"username" db:"username"`
    Password string `json:"-" db:"password"` // Omit from JSON
}

// Anonymous struct
var config struct {
    Host string
    Port int
}{
    Host: "localhost",
    Port: 8080,
}

// Embedded structs (composition)
type Address struct {
    Street string
    City   string
    State  string
}

type Employee struct {
    Person  // Embedded struct
    Address // Embedded struct
    Salary  float64
}

// Anonymous fields
type Point struct {
    int // Anonymous field
    int // Multiple anonymous fields of same type not allowed
}

```

### Methods

```go
// Method with value receiver
func (p Person) GetFullInfo() string {
    return fmt.Sprintf("%s (%d years old)", p.Name, p.Age)
}

// Method with pointer receiver
func (p *Person) SetAge(age int) {
    p.Age = age
}

// Methods on custom types
type MyInt int

func (m MyInt) Double() MyInt {
    return m * 2
}

// Method sets
type Shape interface {
    Area() float64
    Perimeter() float64
}

type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}

type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.Radius
}

```

### Advanced Struct Features

```go
// Struct initialization
p1 := Person{}                           // Zero value
p2 := Person{"Alice", 30, "alice@example.com"} // Positional
p3 := Person{                           // Named fields
    Name:  "Bob",
    Age:   25,
    Email: "bob@example.com",
}

// Struct comparison
if p1 == p2 {
    fmt.Println("Same person")
}

// Struct copying
p4 := p3 // Creates a copy

// Pointer to struct
ptr := &Person{Name: "Charlie", Age: 35}
ptr.Age = 36 // Automatic dereferencing

// Anonymous struct fields
type Data struct {
    string // Anonymous field
    int    // Anonymous field
}

d := Data{"hello", 42}
fmt.Println(d.string, d.int)

// Method promotion with embedding
emp := Employee{
    Person: Person{Name: "John", Age: 30},
    Salary: 50000,
}
info := emp.GetFullInfo() // Method promoted from Person

```

## Interfaces

### Basic Interfaces

```go
// Interface definition
type Writer interface {
    Write([]byte) (int, error)
}

type Reader interface {
    Read([]byte) (int, error)
}

// Interface composition
type ReadWriter interface {
    Reader
    Writer
}

// Empty interface
var anything interface{}
anything = 42
anything = "hello"
anything = []int{1, 2, 3}

// Type assertion
var i interface{} = "hello"
s := i.(string)        // Type assertion
s, ok := i.(string)    // Safe type assertion

// Type switch
switch v := i.(type) {
case int:
    fmt.Printf("Integer: %d\n", v)
case string:
    fmt.Printf("String: %s\n", v)
default:
    fmt.Printf("Unknown type: %T\n", v)
}

```

### Interface Patterns

```go
// Strategy pattern
type PaymentProcessor interface {
    ProcessPayment(amount float64) error
}

type CreditCard struct{}
func (cc CreditCard) ProcessPayment(amount float64) error {
    fmt.Printf("Processing $%.2f via credit card\n", amount)
    return nil
}

type PayPal struct{}
func (pp PayPal) ProcessPayment(amount float64) error {
    fmt.Printf("Processing $%.2f via PayPal\n", amount)
    return nil
}

// Observer pattern
type Observer interface {
    Update(data interface{})
}

type Subject interface {
    Register(Observer)
    Unregister(Observer)
    Notify(data interface{})
}

// Dependency injection
type Database interface {
    Get(key string) (string, error)
    Set(key, value string) error
}

type UserService struct {
    db Database
}

func NewUserService(db Database) *UserService {
    return &UserService{db: db}
}

// Interface segregation
type FileReader interface {
    Read() ([]byte, error)
}

type FileWriter interface {
    Write([]byte) error
}

type FileReadWriter interface {
    FileReader
    FileWriter
}

```

### Advanced Interface Concepts

```go
// Interface with multiple methods
type Sorter interface {
    Len() int
    Less(i, j int) bool
    Swap(i, j int)
}

// Implementing sort.Interface
type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

// Generic interfaces (Go 1.18+)
type Comparable[T comparable] interface {
    Compare(T) int
}

type Constraint interface {
    ~int | ~string | ~float64
}

// Interface assertion patterns
func PrintIfStringer(v interface{}) {
    if s, ok := v.(fmt.Stringer); ok {
        fmt.Println(s.String())
    }
}

// Nil interface vs nil value
var w io.Writer
if w == nil {
    fmt.Println("w is nil")
}

w = (*os.File)(nil)
if w == nil {
    fmt.Println("w is nil") // This won't print
} else {
    fmt.Println("w is not nil but contains nil pointer")
}

```

## Concurrency

### Goroutines

```go
// Basic goroutine
go func() {
    fmt.Println("Hello from goroutine")
}()

// Goroutine with parameters
go func(name string) {
    fmt.Printf("Hello %s\n", name)
}("Alice")

// Anonymous function goroutine
go myFunction()

// Wait for goroutines (using WaitGroup)
var wg sync.WaitGroup

for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Printf("Worker %d\n", id)
    }(i)
}

wg.Wait()

```

### Channels

```go
// Channel creation
ch := make(chan int)           // Unbuffered channel
buffered := make(chan int, 10) // Buffered channel

// Send and receive
go func() {
    ch <- 42 // Send
}()
value := <-ch // Receive

// Channel directions
func send(ch chan<- int) {     // Send-only channel
    ch <- 42
}

func receive(ch <-chan int) {  // Receive-only channel
    value := <-ch
}

// Closing channels
close(ch)

// Check if channel is closed
value, ok := <-ch
if !ok {
    fmt.Println("Channel is closed")
}

// Range over channel
go func() {
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)
}()

for value := range ch {
    fmt.Println(value)
}

```

### Advanced Channel Patterns

```go
// Select statement
select {
case msg1 := <-ch1:
    fmt.Println("Received from ch1:", msg1)
case msg2 := <-ch2:
    fmt.Println("Received from ch2:", msg2)
case <-time.After(1 * time.Second):
    fmt.Println("Timeout")
default:
    fmt.Println("No channels ready")
}

// Fan-out pattern
func fanOut(input <-chan int, workers int) []<-chan int {
    outputs := make([]<-chan int, workers)
    for i := 0; i < workers; i++ {
        output := make(chan int)
        outputs[i] = output
        go func() {
            defer close(output)
            for data := range input {
                output <- process(data)
            }
        }()
    }
    return outputs
}

// Fan-in pattern
func fanIn(inputs ...<-chan int) <-chan int {
    output := make(chan int)
    var wg sync.WaitGroup
    
    for _, input := range inputs {
        wg.Add(1)
        go func(ch <-chan int) {
            defer wg.Done()
            for data := range ch {
                output <- data
            }
        }(input)
    }
    
    go func() {
        wg.Wait()
        close(output)
    }()
    
    return output
}

// Pipeline pattern
func pipeline() <-chan int {
    // Stage 1: Generate numbers
    numbers := make(chan int)
    go func() {
        defer close(numbers)
        for i := 1; i <= 10; i++ {
            numbers <- i
        }
    }()
    
    // Stage 2: Square numbers
    squares := make(chan int)
    go func() {
        defer close(squares)
        for num := range numbers {
            squares <- num * num
        }
    }()
    
    return squares
}

// Worker pool pattern
func workerPool(jobs <-chan int, results chan<- int, numWorkers int) {
    var wg sync.WaitGroup
    
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for job := range jobs {
                results <- process(job)
            }
        }()
    }
    
    go func() {
        wg.Wait()
        close(results)
    }()
}

```

### Synchronization Primitives

```go
// Mutex
var mu sync.Mutex
var counter int

func increment() {
    mu.Lock()
    defer mu.Unlock()
    counter++
}

// RWMutex
var rwmu sync.RWMutex
var data map[string]int

func read(key string) int {
    rwmu.RLock()
    defer rwmu.RUnlock()
    return data[key]
}

func write(key string, value int) {
    rwmu.Lock()
    defer rwmu.Unlock()
    data[key] = value
}

// Once
var once sync.Once
var instance *Singleton

func GetInstance() *Singleton {
    once.Do(func() {
        instance = &Singleton{}
    })
    return instance
}

// Cond
var cond = sync.NewCond(&sync.Mutex{})
var ready bool

func waitForReady() {
    cond.L.Lock()
    for !ready {
        cond.Wait()
    }
    cond.L.Unlock()
}

func setReady() {
    cond.L.Lock()
    ready = true
    cond.L.Unlock()
    cond.Broadcast()
}

// Atomic operations
var atomicCounter int64

func atomicIncrement() {
    atomic.AddInt64(&atomicCounter, 1)
}

func atomicRead() int64 {
    return atomic.LoadInt64(&atomicCounter)
}

```

## Memory Management

### Allocation and Deallocation

```go
// Stack vs Heap allocation
func stackAllocation() {
    var x int = 42 // Allocated on stack
    fmt.Println(x)
} // x is automatically deallocated

func heapAllocation() *int {
    var x int = 42 // Allocated on heap (escapes to heap)
    return &x      // Pointer returned
}

// new and make
ptr := new(int)        // Returns *int, zero-valued
slice := make([]int, 5) // Returns []int, initialized

// Memory pools
var pool = sync.Pool{
    New: func() interface{} {
        return make([]byte, 1024)
    },
}

func usePool() {
    buf := pool.Get().([]byte)
    defer pool.Put(buf)
    // Use buf
}

```

### Garbage Collection

```go
// Force garbage collection (rarely needed)
runtime.GC()

// Memory statistics
var m runtime.MemStats
runtime.ReadMemStats(&m)
fmt.Printf("Alloc = %d KB", m.Alloc/1024)
fmt.Printf("TotalAlloc = %d KB", m.TotalAlloc/1024)
fmt.Printf("Sys = %d KB", m.Sys/1024)
fmt.Printf("NumGC = %v\n", m.NumGC)

// Finalizers (rarely used)
type Resource struct {
    file *os.File
}

func NewResource(filename string) (*Resource, error) {
    file, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    r := &Resource{file: file}
    runtime.SetFinalizer(r, (*Resource).finalize)
    return r, nil
}

func (r *Resource) finalize() {
    if r.file != nil {
        r.file.Close()
    }
}

func (r *Resource) Close() {
    if r.file != nil {
        r.file.Close()
        r.file = nil
        runtime.SetFinalizer(r, nil)
    }
}

```

## Error Handling

### Basic Error Handling

```go
// Error interface
type error interface {
    Error() string
}

// Creating errors
err := errors.New("something went wrong")
err = fmt.Errorf("error in %s: %v", "function", originalErr)

// Custom error types
type MyError struct {
    Code    int
    Message string
}

func (e MyError) Error() string {
    return fmt.Sprintf("Error %d: %s", e.Code, e.Message)
}

// Function returning error
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Error handling
result, err := divide(10, 0)
if err != nil {
    log.Fatal(err)
}

```

### Advanced Error Handling

```go
// Error wrapping (Go 1.13+)
err := fmt.Errorf("failed to process: %w", originalErr)

// Error unwrapping
unwrapped := errors.Unwrap(err)

// Error checking
if errors.Is(err, ErrNotFound) {
    // Handle specific error
}

var myErr *MyError
if errors.As(err, &myErr) {
    // Handle specific error type
}

// Error sentinel values
var (
    ErrNotFound = errors.New("not found")
    ErrInvalid  = errors.New("invalid input")
)

// Panic and recover
func safeFunction() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Printf("Recovered from panic: %v\n", r)
        }
    }()
    
    panic("something went wrong")
}

// Result type pattern
type Result[T any] struct {
    Value T
    Error error
}

func (r Result[T]) IsOk() bool {
    return r.Error == nil
}

func (r Result[T]) Unwrap() (T, error) {
    return r.Value, r.Error
}

```

## Advanced Features

### Generics (Go 1.18+)

```go
// Generic function
func Max[T comparable](a, b T) T {
    if a > b {
        return a
    }
    return b
}

// Generic types
type Stack[T any] struct {
    items []T
}

func (s *Stack[T]) Push(item T) {
    s.items = append(s.items, item)
}

func (s *Stack[T]) Pop() (T, bool) {
    if len(s.items) == 0 {
        var zero T
        return zero, false
    }
    item := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return item, true
}

// Type constraints
type Ordered interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
    ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
    ~float32 | ~float64 |
    ~string
}

func Sort[T Ordered](slice []T) {
    sort.Slice(slice, func(i, j int) bool {
        return slice[i] < slice[j]
    })
}

// Generic interfaces
type Getter[T any] interface {
    Get() T
}

type Setter[T any] interface {
    Set(T)
}

type GetSetter[T any] interface {
    Getter[T]
    Setter[T]
}

```

### Reflection

```go
// Basic reflection
func inspectType(x interface{}) {
    t := reflect.TypeOf(x)
    v := reflect.ValueOf(x)
    
    fmt.Printf("Type: %s\n", t)
    fmt.Printf("Kind: %s\n", t.Kind())
    fmt.Printf("Value: %v\n", v)
}

// Struct reflection
type Person struct {
    Name string `json:"name" validate:"required"`
    Age  int    `json:"age" validate:"min:0,max:150"`
}

func inspectStruct(x interface{}) {
    t := reflect.TypeOf(x)
    v := reflect.ValueOf(x)
    
    if t.Kind() == reflect.Ptr {
        t = t.Elem()
        v = v.Elem()
    }
    
    for i := 0; i < t.NumField(); i++ {
        field := t.Field(i)
        value := v.Field(i)
        
        fmt.Printf("Field: %s, Type: %s, Value: %v\n",
            field.Name, field.Type, value.Interface())
        
        if tag := field.Tag.Get("json"); tag != "" {
            fmt.Printf("JSON tag: %s\n", tag)
        }
    }
}

// Method reflection
func inspectMethods(x interface{}) {
    t := reflect.TypeOf(x)
    
    for i := 0; i < t.NumMethod(); i++ {
        method := t.Method(i)
        fmt.Printf("Method: %s, Type: %s\n", method.Name, method.Type)
    }
}

// Dynamic method calls
func callMethod(obj interface{}, methodName string, args ...interface{}) {
    v := reflect.ValueOf(obj)
    method := v.MethodByName(methodName)
    
    if !method.IsValid() {
        fmt.Printf("Method %s not found\n", methodName)
        return
    }
    
    values := make([]reflect.Value, len(args))
    for i, arg := range args {
        values[i] = reflect.ValueOf(arg)
    }
    
    results := method.Call(values)
    for _, result := range results {
        fmt.Printf("Result: %v\n", result.Interface())
    }
}

```

### Code Generation

```go
//go:generate stringer -type=Day
type Day int

const (
    Monday Day = iota
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
)

// Build tags
//go:build linux
// +build linux

func linuxSpecific() {
    // Linux-specific code
}

//go:build windows
// +build windows

func windowsSpecific() {
    // Windows-specific code
}

// Embedding files (Go 1.16+)
//go:embed templates/*
var templates embed.FS

//go:embed config.json
var configData []byte

//go:embed static
var staticFiles embed.FS

```

### Unsafe Operations

```go
import "unsafe"

// Unsafe pointer conversion
func unsafeExample() {
    var x int64 = 12345
    ptr := unsafe.Pointer(&x)
    
    // Convert to different type (dangerous!)
    y := (*int32)(ptr)
    fmt.Printf("x: %d, y: %d\n", x, *y)
}

// String to byte slice without copy
func stringToBytes(s string) []byte {
    return *(*[]byte)(unsafe.Pointer(
        &struct {
            string
            Cap int
        }{s, len(s)},
    ))
}

// Byte slice to string without copy
func bytesToString(b []byte) string {
    return *(*string)(unsafe.Pointer(&b))
}

// Struct field offset
type Example struct {
    A int32
    B int64
    C string
}

func structOffsets() {
    fmt.Printf("Size of Example: %d\n", unsafe.Sizeof(Example{}))
    fmt.Printf("Offset of A: %d\n", unsafe.Offsetof(Example{}.A))
    fmt.Printf("Offset of B: %d\n", unsafe.Offsetof(Example{}.B))
    fmt.Printf("Offset of C: %d\n", unsafe.Offsetof(Example{}.C))
}

```

## Best Practices

### Code Organization

```go
// Package naming
package user // lowercase, short, descriptive

// File naming
// user.go - main functionality
// user_test.go - tests
// user_internal.go - internal helpers

// Import organization
import (
    // Standard library
    "fmt"
    "os"
    
    // Third-party packages
    "github.com/gin-gonic/gin"
    "github.com/stretchr/testify/assert"
    
    // Internal packages
    "myproject/internal/user"
    "myproject/pkg/database"
)

// Exported vs unexported
type User struct {
    ID       int    // Exported
    username string // Unexported
}

func (u *User) GetUsername() string { // Exported method
    return u.username
}

func (u *User) setPassword(pwd string) { // Unexported method
    // Implementation
}

```

### Error Handling Best Practices

```go
// Early return
func processUser(id int) error {
    user, err := getUser(id)
    if err != nil {
        return fmt.Errorf("failed to get user: %w", err)
    }
    
    if err := validateUser(user); err != nil {
        return fmt.Errorf("user validation failed: %w", err)
    }
    
    if err := saveUser(user); err != nil {
        return fmt.Errorf("failed to save user: %w", err)
    }
    
    return nil
}

// Error context
func processFile(filename string) error {
    file, err := os.Open(filename)
    if err != nil {
        return fmt.Errorf("opening file %s: %w", filename, err)
    }
    defer file.Close()
    
    // Process file
    return nil
}

// Custom error types for different handling
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation error on field %s: %s", e.Field, e.Message)
}

type NetworkError struct {
    URL string
    Err error
}

func (e NetworkError) Error() string {
    return fmt.Sprintf("network error for URL %s: %v", e.URL, e.Err)
}

func (e NetworkError) Unwrap() error {
    return e.Err
}

```

### Testing

```go
// Basic test
func TestAdd(t *testing.T) {
    result := add(2, 3)
    expected := 5
    if result != expected {
        t.Errorf("add(2, 3) = %d; want %d", result, expected)
    }
}

// Table-driven tests
func TestAddTable(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive numbers", 2, 3, 5},
        {"negative numbers", -2, -3, -5},
        {"mixed", -2, 3, 1},
        {"zero", 0, 5, 5},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("add(%d, %d) = %d; want %d", 
                    tt.a, tt.b, result, tt.expected)
            }
        })
    }
}

// Benchmarks
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        add(2, 3)
    }
}

// Examples
func ExampleAdd() {
    result := add(2, 3)
    fmt.Println(result)
    // Output: 5
}

// Test helpers
func assertEqual(t *testing.T, actual, expected interface{}) {
    t.Helper()
    if actual != expected {
        t.Errorf("got %v; want %v", actual, expected)
    }
}

// Mocking with interfaces
type UserRepository interface {
    GetUser(id int) (*User, error)
}

type MockUserRepository struct {
    users map[int]*User
}

func (m *MockUserRepository) GetUser(id int) (*User, error) {
    user, exists := m.users[id]
    if !exists {
        return nil, errors.New("user not found")
    }
    return user, nil
}

```

## Performance Optimization

### Profiling

```go
// CPU profiling
import _ "net/http/pprof"

func main() {
    go func() {
        log.Println(http.ListenAndServe("localhost:6060", nil))
    }()
    
    // Your application code
}

// Memory profiling
func profileMemory() {
    f, err := os.Create("memory.prof")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()
    
    runtime.GC()
    if err := pprof.WriteHeapProfile(f); err != nil {
        log.Fatal(err)
    }
}

// CPU profiling in code
func profileCPU() {
    f, err := os.Create("cpu.prof")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()
    
    if err := pprof.StartCPUProfile(f); err != nil {
        log.Fatal(err)
    }
    defer pprof.StopCPUProfile()
    
    // Your code to profile
}

```

### Optimization Techniques

```go
// String building
func inefficientStringBuilding(words []string) string {
    result := ""
    for _, word := range words {
        result += word + " " // Creates new string each time
    }
    return result
}

func efficientStringBuilding(words []string) string {
    var builder strings.Builder
    for _, word := range words {
        builder.WriteString(word)
        builder.WriteString(" ")
    }
    return builder.String()
}

// Slice pre-allocation
func inefficientSliceGrowth() []int {
    var result []int
    for i := 0; i < 1000; i++ {
        result = append(result, i) // Multiple reallocations
    }
    return result
}

func efficientSliceGrowth() []int {
    result := make([]int, 0, 1000) // Pre-allocate capacity
    for i := 0; i < 1000; i++ {
        result = append(result, i)
    }
    return result
}

// Map pre-allocation
func efficientMapCreation() map[string]int {
    m := make(map[string]int, 1000) // Pre-allocate capacity
    // Populate map
    return m
}

// Avoiding interface{} when possible
func processInts(items []int) {
    // Type-specific processing
}

func processItems(items []interface{}) {
    // Generic processing (slower due to type assertions)
}

// Pool reuse
var bufferPool = sync.Pool{
    New: func() interface{} {
        return make([]byte, 0, 1024)
    },
}

func processData(data []byte) []byte {
    buf := bufferPool.Get().([]byte)
    defer bufferPool.Put(buf[:0])
    
    // Process data using buf
    return result
}

```

### Concurrency Optimization

```go
// Worker pool for CPU-intensive tasks
func optimizedProcessing(items []Item) []Result {
    numWorkers := runtime.NumCPU()
    itemCh := make(chan Item, len(items))
    resultCh := make(chan Result, len(items))
    
    // Start workers
    var wg sync.WaitGroup
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for item := range itemCh {
                result := processItem(item)
                resultCh <- result
            }
        }()
    }
    
    // Send items
    go func() {
        defer close(itemCh)
        for _, item := range items {
            itemCh <- item
        }
    }()
    
    // Close result channel when all workers are done
    go func() {
        wg.Wait()
        close(resultCh)
    }()
    
    // Collect results
    var results []Result
    for result := range resultCh {
        results = append(results, result)
    }
    
    return results
}

// Batching for better throughput
func batchProcess(items []Item, batchSize int) {
    for i := 0; i < len(items); i += batchSize {
        end := i + batchSize
        if end > len(items) {
            end = len(items)
        }
        
        batch := items[i:end]
        processBatch(batch)
    }
}

```

This comprehensive guide covers Go from basics to advanced features. Each section includes practical examples and best practices for real-world development.