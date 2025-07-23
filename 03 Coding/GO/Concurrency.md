---
id: Concurrency
aliases: []
tags: []
---

# Concurrency

```go
go doSomething()
```
- it spawns new [[goroutine]]

## Channels

- Channels allow different goroutines to communicate with each other.
-  send and receive data safely without explicit locks

- `<-` channel operator.
- This operation will block until another goroutine is ready to receive the value

```go
package main

import "fmt"

func main() {
	ch := make(chan int)

	go func() {
		ch <- 42
	}()

	value := <-ch

	fmt.Println(value)
}
```
