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
Channels allow different goroutines to communicate with each other.

- `<-` channel operator.
- This operation will block until another goroutine is ready to receive the value
