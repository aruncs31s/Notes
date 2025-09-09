---
id: playground
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - test
dg-publish: true
---

```bash

echo " Hello World!"
read a
echo $a

```

```rust
use std::io::{self, Write};
fn main() {
    print!("Please enter something: ");
    io::stdout().flush().unwrap(); // Ensure the prompt is displayed
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    println!("You entered: {}", input.trim());

```

```rust
fn main(){
   let mut line = String::new();
   println!("Enter your name :");
   let b1 = std::io::stdin().read_line(&mut line).unwrap();
   println!("Hello , {}", line);
   println!("no of bytes read , {}", b1);
}

```

##### Programm to find the area of triangle

```python
length = int(input("Enter the Length"))
breadth = int(input("Enter the Breadth"))
area = (length * breadth)/2
print("Area Is = " ,area)

```

```c
#include <stdio.h>
int main(int argc, char *argv[]) {
  int l, b, area;
  printf("Enter Length and Breadth");
  scanf("%d%d", &l, &b);

  printf(" Area = %d", (l * b) / 2);
}

```

```

```

```javascript
let l = console.prompt("Enter the length") 
let b = console.prompt("Enter the breadth")
console.log((l*b)/2)

```

```javascript
const readline = require('readline');
const rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout
});
rl.question('Please enter your input: ', (input) => {
 console.log(`You entered: ${input}`);
 rl.close();

```

$$
x = \frac{-b \underset {-}{+}\sqrt{b^2 - 4ac}}{2a}
$$[[quadratic%20x|quadratic x]]
