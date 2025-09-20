---
id: csv
aliases: []
tags:
  - coding
  - programming
  - javascript
dg-publish: true
---
# CSV

**Modules**: `fs`

#### Reading

```javascript
const fs = require("fs");

fs.createReadStream("./2024-09-09_log.csv", { encoding: "utf8" })
  .on("data", (chuck) => console.log(chuck))
  .on("end", () => {
    console.log("End");
  })
  .on("error", (error) => {
    console.log(error);
  });

```
