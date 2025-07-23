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


```go
package main
import (
	"fmt"
	"time"
)
func main() {
	ch := make(chan int) // creates a channel ch

	go func() {
		fmt.Println("Before start")
		time.Sleep(10 * time.Second)
		ch <- 42
		fmt.Println("Send")
	}()

	fmt.Println("Before Passing")
	value := <-ch

	fmt.Println("After passing")

	fmt.Println(value)
}
```
^prog1

```
Before Passing
After passing
Before start
Send
42
```


```go

package main
import (
	"fmt"
	"time"
)
func main() {
	ch := make(chan int) // creates a channel ch

	go func() {
		ch <- 42
		fmt.Println("Before start")
		fmt.Println("Send")
	}()

	fmt.Println("Before Passing")
	time.Sleep(10 * time.Second)
	value := <-ch

	fmt.Println("After passing")

	fmt.Println(value)
}
```
^prog2


```
Before Passing
Before start
After passing
42
```


> [!multi-column]
> 
>> [!blank|medium-left]
>> Prog_1
>> ![[#^prog1]]
> 
>> [!blank|medium-right]
>> Prog_2
>> ![[#^prog2]]

>[!multi-column]
> 
> > [!blank|float-left]
>> p_1
>> ```
>>Before Passing
>>After passing
>>Before start
>>Send
>>42
>>```
> 
>> [!blank|float-right]
>> p_2
>> ```
>> Before Passing
>> Before start
>> Send
>> After passing
>> 42
>> ```
