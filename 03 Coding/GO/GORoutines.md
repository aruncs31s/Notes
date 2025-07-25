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


## File Processing using Go Routines
Requirement is to read a `json` file and get a specific element from the file , since the file processing takes too much time it is best to use [[Concurrency]] for this , it may be as follows

- read the `json` file , start new job 
- tell the function which depents on job to wait for it to finish 
