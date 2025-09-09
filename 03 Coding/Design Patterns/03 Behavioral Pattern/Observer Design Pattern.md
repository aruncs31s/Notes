---
id: Observer_Design_Pattern
aliases: []
tags:
  - coding
  - design_patterns
  - behavioral_pattern
dg-publish: true
---
# Observer  Pattern 

>   lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing , but since it’s also going to notify other objects about the changes to its state, we’ll call it publisher.All other objects that want to track changes to the publisher’s state are called subscribers.

## Example

```python
class Publisher:
    def __init__(self):
        self._subscribers = []
    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)
    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} received message: {message}")
publisher = Publisher()
subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")
publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)
publisher.notify("Hello, Subscribers!")

```

Now, whenever an important event happens to the publisher, it goes over its subscribers and calls the specific notification method on their objects.

![](https://refactoring.guru/images/patterns/diagrams/observer/structure-indexed.png?id=2ca2c123503ede860740af2a22bc4b4d)
 

## Example in Go

```go
package main

type Subject interface {
    register(observer Observer)
    deregister(observer Observer)
    notifyAll()
}

```

## References 
1. https://refactoring.guru/design-patterns/observer