---
id: Behavioral_Pattern
aliases: []
tags:
  - coding
  - design_patterns
dg-publish: true
---
### 🤝 Behavioral Patterns
- [[Strategy Pattern]]
- [[Observer Design Pattern]]
**Purpose**: Concerned with **communication between objects**, focusing on **how responsibility is distributed** and **how algorithms are handled**

#### Code Example - Observer Pattern

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class EmailNotifier:
    def update(self, message):
        print(f"Sending email: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"Sending SMS: {message}")

# Usage
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())

subject.notify("New order received.")
# Output: 
# Sending email: New order received.
# Sending SMS: New order received.

```
