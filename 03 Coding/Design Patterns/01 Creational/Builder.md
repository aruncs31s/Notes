---
id: Builder
aliases: []
tags:
  - coding
  - design_patterns
  - creational
dg-publish: true
---
# Builder Pattern 
> **Builder** is a creational design pattern that *allows you to construct complex objects step by step*. It separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

```ts
class HTTPRequest{
    constructor(url, method, options) {
        this.url = url;
        this.method = method;
        this.options = options;
    }
}

// Without Builder - Single constructor doing all the work
const request = new HTTPRequest('https://api.example.com/data', 'GET', {
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ key: 'value' })
});

// With Builder Pattern
class RequestBuilder {
    constructor() {
        this.url = '';
        this.method = 'GET';
        this.options = {};
    }

    setUrl(url) {
        this.url = url;
        return this;
    }

    setMethod(method) {
        this.method = method;
        return this;
    }

    setOptions(options) {
        this.options = options;
        return this;
    }

    build() {
        return new HTTPRequest(this.url, this.method, this.options);
    }
}

// Usage
const request = new RequestBuilder()
    .setUrl('https://api.example.com/data')
    .setMethod('GET')
    .setOptions({
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ key: 'value' })
    })
    .build();

```

#### ✅ **Benefits**
> *Feels like cooking a dish step by step*
> *But someone who uses this code can clearly understand what every parameter does.* 

- ✅ **Separation of concerns**: Construction logic is separated from the object representation
- ✅ **Fluent interface**: Allows chaining methods for a more readable and expressive API
- ✅ **Flexibility**: Can create different representations of the same object without changing the construction process

