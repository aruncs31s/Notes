---
tags:
  - programming
  - design_pattern
  - behavioural_pattern
  - go
  - "#work"
---
# Strategy Patter Using Golang 


```go 
func main() {
	// Create executor with synchronous strategy
	executor := NewCommandExecutor(&SynchronousStrategy{})

	fmt.Println("=== Using Synchronous Strategy ===")
	output, err := executor.ExecuteCommand("echo", "Hello World!")
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Output:", output)
	}

	// Switch to timeout strategy
	executor.SetStrategy(&TimeoutStrategy{Timeout: 5 * time.Second})
	fmt.Println("\n=== Using Timeout Strategy ===")
	output, err = executor.ExecuteCommand("echo", "Hello with timeout!")
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Output:", output)
	}

	// Switch to verbose strategy
	executor.SetStrategy(&VerboseStrategy{})
	fmt.Println("\n=== Using Verbose Strategy ===")
	output, err = executor.ExecuteCommand("echo", "Hello with verbose logging!")
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Output:", output)
	}
}

```

## Interface
```go
// Strategy interface defines the execution contract
type ExecutionStrategy interface {
	Execute(command string, args ...string) (string, error)
}
```
What does this mean 

First recall what is an interface ![[Go#Interfaces]]
So in this case  any type that has` Execute()`  method is considered as an `ExecutionStrategy`. Its like saying anything that has leaves is called a tree. It is not the same but , it requires more condition to be met. 

## Strategies 

1. `SynchronousStrategy`
```go
// SynchronousStrategy executes commands synchronously
type SynchronousStrategy struct{}

func (s *SynchronousStrategy) Execute(command string, args ...string) (string, error) {
	cmd := exec.Command(command, args...)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}
```
2. `TimeoutStrategy`
```go
// TimeoutStrategy executes commands with a timeout
type TimeoutStrategy struct {
	Timeout time.Duration
}

func (s *TimeoutStrategy) Execute(command string, args ...string) (string, error) {
	ctx, cancel := context.WithTimeout(context.Background(), s.Timeout)
	defer cancel()

	cmd := exec.CommandContext(ctx, command, args...)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

```