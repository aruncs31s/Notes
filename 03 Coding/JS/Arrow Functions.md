---
id: Arrow_Functions
aliases: []
tags:
  - coding
  - js
dg-publish: true
---
# Arrow Functions
- [[Immediately invoked functions]]

```js
(params) => {expressions}

```

```js
let arr = [1,2,3,4]
let mul = arr.map(x => x * 2);
console.log(mul)
let sum = (a,b) => a+b ;
console.log(sum(4,5))
let average = numbers => {
let sum = numbers.reduce((a, b) => a + b);
return sum / numbers.length;
};
console.log(average(arr));

```
