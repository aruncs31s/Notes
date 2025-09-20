---
id: Objects
aliases: []
tags:
  - coding
  - js
dg-publish: true
---
# Objects

```js
let fruit = 'apple', number = 19;
let obj = {fruit, foo: 'bar', number};
console.log(obj);
// {fruit: 'apple', foo: 'bar', number: 19}

```

- [ ] check this 📅 🏁 delete 

```js
let obj = {
number: 2,
multiply: function (n) { // old way
return this.number * n;
},
times(n) { // new way
return this.number * n;
},
// This doesn't work because the
// arrow function "this" value is not obj.
product: n => this.number * n
};
console.log(obj.multiply(2)); // 4
console.log(obj.times(3)); // 6
console.log(obj.product(4)); // NaN

```