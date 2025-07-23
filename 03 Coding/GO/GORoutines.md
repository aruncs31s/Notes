---
id: GORoutines
aliases: 
tags:
  - go
---
# GO Routines
```go
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(1000 * time.Millisecond)
		fmt.Println(s, i)
	}
}

func main() {
	go say("first")
	say("second")
}
```

```
first 0
second 0 // here
second 1
first 1
first 2
second 2
second 3
first 3
first 4
second 4

```