---
id: Concurrency
aliases: []
tags: []
cssclasses:
  - wide-page
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
Before Passing 3 
After passing 1 
Before start 1 
Send 4 
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

---
> [!multi-column]
> 
>> [!blank|medium-left]
>> Prog_1
>> ![[#^prog1]]
> 
>> [!blank| medium-right]
>>```mermaid
>> graph TB 
>> channel_creation --> goroutine_launch --> race --> 
>>```


- [ ] fix this latter 

#### Execution Flow Step-by-Step

  Here is exactly what happens when you run the program:

1. Start and Channel Creation
 * The main goroutine starts.
 * ch := make(chan int): It creates an empty channel that can hold integers.

2. Goroutine Launch
 * go func() { ... }(): The main goroutine launches the new, anonymous goroutine.
 * Crucially, `main` does NOT wait. It immediately continues to its next line of code while the new goroutine starts running
   concurrently.

3. The Race Begins (First ~10 milliseconds)
 * `main` goroutine executes fmt.Println("Before Passing").
     * OUTPUT: Before Passing
 * At the same time, the new goroutine executes fmt.Println("Before start").
     * OUTPUT: Before start
 * The new goroutine then immediately executes time.Sleep(10 * time.Second). It now pauses for 10 seconds.

4. The Block (The next 10 seconds)
 * The main goroutine moves to its next line: value := <-ch.
 * This is a blocking receive. The main goroutine tries to take a value from the channel ch.
 * But the channel is empty! The other goroutine is sleeping and hasn't sent anything yet.
 * So, the `main` goroutine stops and waits right here. It is blocked. Nothing else in main will happen until a value is put into the
   channel.
 * For the next 10 seconds, your program appears to do nothing.

5. The Unblock (After 10 seconds)
 * The time.Sleep(10 * time.Second) inside the new goroutine finally finishes.
 * The new goroutine wakes up and executes its next line: ch <- 42. It sends the value 42 into the channel.
 * This is the magic moment! The main goroutine, which was patiently waiting to receive a value, is instantly unblocked. It receives
   the 42 and assigns it to the value variable.

6. The Finish
 * The `main` goroutine is now free to continue. It executes:
     * fmt.Println("After passing")
         * OUTPUT: After passing
     * fmt.Println(value)
         * OUTPUT: 42
 * Meanwhile, the new goroutine also continues. It executes:
     * fmt.Println("Send")
         * OUTPUT: Send
 * Both goroutines have now finished their work, and the program exits.


