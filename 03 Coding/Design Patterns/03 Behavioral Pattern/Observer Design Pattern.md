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