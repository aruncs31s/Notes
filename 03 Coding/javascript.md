---
id: javascript
aliases: []
tags: []
---

# javascript

Created : 2024-05-14 23:28

- [[]]

## Contents

###### Finding Dot Product

```js
const a = [1, 3, 4];
const b = [3, 4, 5];
dotProduct = (a, b) => {
  let result = 0;
  for (let i = 0; i < a.length; i++) {
    result = a[i] * b[i];
  }
  return result;
};
console.log(
  "Input vector 1 = " +
    a +
    "\nInput Vector 2 = " +
    b +
    "\nDot Product = " +
    dotProduct(a, b),
);
```

## References

1.
