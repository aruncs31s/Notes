---
id: Classes
aliases: []
tags:
  - coding
  - js
dg-publish: true
---

```js
class Shoe {
	constructor(brand, model, size) {
	this.brand = brand;
	this.model = model;
	this.size = size;
	Shoe.count++;
}
static createdAny() { return Shoe.count > 0; }
	equals(obj) {
		return obj instanceof Shoe && 
		this.brand === obj.brand && 
		this.model === obj.model &&
		this.size === obj.size;
}
toString() {
	return this.brand + ' ' + this.model +
		' in size ' + this.size;
}
}
Shoe.count = 0; 
let s1 = new Shoe('Mizuno', 'Precision 10', 13);
let s2 = new Shoe('Nike', 'Free 5', 12);
let s3 = new Shoe('Mizuno', 'Precision 10', 13);
console.log('created any?', Shoe.createdAny()); // true
console.log('count =', Shoe.count); // 3
console.log('s2 = ' + s2); // Nike Free 5 in size 12
console.log('s1.equals(s2) =', s1.equals(s2)); // false
console.log('s1.equals(s3) =', s1.equals(s3)); // true

```

```js
class Shoe {
...
	get size() {
		return this._size;
	}
	set size(size) {
		this._size = size;
	}
...
}
let s = new Shoe();
s.size = 13; // invokes setter
console.log(s.size); // invokes getter

```

```js
class Shoe {
...
get size() {
return this._size;
}
set size(size) {
this._size = size;
}
...
}
let s = new Shoe();
s.size = 13; // invokes setter
console.log(s.size); // invokes getter

```

>*using size instead of _size for the “backing field” would cause a `ModuleEvaluationError` with message “Maximum call stack size exceeded”*

