---
id: Basics
aliases: []
tags:
  - coding
  - js
dg-publish: true
---
- `let` is (roughly) a block-scoped version of var.
- `const` is a block-scoped, read-only constant.

```js
var x = 3;
function func(randomize) {
if (randomize) {
var x = Math.random(); // (A) scope: whole function
return x;
}
return x; // accesses the x from line A
}
func(false); // undefined

```

## Functions
- [[Arrow Functions]]
- [[Objects]]
- [[03 Coding/JS/Classes]]

```js
function fun1() {
  console.log("Function 1");
}
function fun2(a, b) {
  return a + b;
}
fun1();
console.log(fun2(1, 2));

```

## Scope

```js
function outerFun() {
  console.log("outerFun");
}
{
  function innerFun() {
    console.log("innerFun");
  }
}
outerFun();
innerFun();

```

_This works but accoring to the reference it should throw a `ReferenceError`_

## Default Params

## Rest Params

```js
function report(firstName, lastName, ...colors) {
  let phrase =
    colors.length === 0
      ? "no colors"
      : colors.length === 1
        ? "the color " + colors[0]
        : "the colors " + colors.join(" and ");
  console.log(firstName, lastName, "likes", phrase + ".");
}

```

```js
report("arun", "appu", "red", "green");

```

## Spread Operator

```js
let arr = [1, 2, 3, 4, 5];
let arr_2 = [6, 7, 8, 9, 10];
let arr_3 = [...arr, ...arr_2];
console.log(arr_3);
let arr_4 = [];
arr_4.push(...arr);
console.log(arr_4);
arr_4.push(...arr_2);
console.log(arr_4);

```

## Deconstructing

```js
let [a, b] = [2, 3];
console.log(a);
// 2
console.log(b);
// 3
// Default values can also be used like the following
let [b = 10, c = 20] = someVar;

[a, b] = [b, a]; // simple swap

// skip var , d-> 3 , e-> 4
[, , d, e] = [1, 2, 3, 4];

```

is the `someVar` is empty then the default value can be used.

## Math
Math.fround(number) - returns nearest single precision floating point number to number
Math.sign(number) - returns sign of number; -1, 0 or 1
Math.trunc(number) - returns integer part of number
Math.cbrt(number) - returns cube root of number
Math.expm1(number) - returns exp(number) - 1;
Math.exp returns e (Euler’s constant) raised to number power
Math.hypot(x, y, ...) - returns square root of sum of squares of arguments
Math.imul(n1, n2) - multiplies two 32-bit integers; for performance
logarithmic functions - Math.log1p(number), Math.log10(number), Math.log2(number)
Math.log1p returns Math.log(1 + number)
hyperbolic trig functions - Math.asinh(number), Math.acosh(number), Math.atanh(number)

Number.isFinite(n) - returns boolean indicating whether n is a Number
and is not NaN, Infinity or -Infinity
Number.isInteger(n) - returns boolean indicating whether n is an integer
and not a float, NaN, Infinity or -Infinity
Number.isNaN(n) - returns boolean indicating whether n is the special NaN value
Number.isSafeInteger(n) - returns boolean indicating whether n
can be represented exactly in a double (within 53 bits)
also new constants Number.MIN_SAFE_INTEGER and Number.MAX_SAFE_INTEGER
Number.toInteger(n) - converts a number to an integer
Number.parseInt(string) - parses a string into an integer; same as the global function
Number.parseFloat(string) - parses a string into a double; same as the global function

