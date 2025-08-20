# Dependency Injunction

```tasks 
not done 
path includes Design Patterns/Dependency Injunction
```


```dataview
LIST 
From #design_pattern and #dependency_injunction
```


- [ ] Check out DI in containers 


use a container for managing objects ?
Constructor Injection and Setter Injection ? 

- [ ] Checkout microservices architecture 

#### ✅ Benefits:

Helps you to **decouple** the external logic of your implementation 

---

*An important point of injecting dependencies is to avoid injecting implementations (structs), you should inject abstractions (interfaces).* ? 

- [ ] Checkout Dependency Inversion Principle ? 

>  An important point of injecting dependencies is to avoid injecting implementations (structs), you should inject abstractions (interfaces). It’s the letter D of S.O.L.I.D: Dependency Inversion Principle. It allows you to switch easily the implementation of some dependency and, you could change the real implementation for a mock implementation. It's fundamental for unit testing. - [Source](https://medium.com/avenue-tech/dependency-injection-in-go-35293ef7b6)

```go 
type SomeRepo interface{}
type SomeLogger interface{}
type SomeMessageBroker interface{}

type SomeService struct {
	repo SomeRepo
	logger SomeLogger 
	broker SomeMessageBroker 
}

func NewSomeService ( repo SomeRepo , logger SomeLogger , broker SomeMessageBroker)SomeService{
	return &SomeService{
		repo: SomeRepo
		logger: SomeLogger 
		broker: SomeMessageBroker 
	}
} 
```