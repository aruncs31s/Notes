---
id: Lib
aliases: []
tags:
  - coding
  - embedded_programming
dg-publish: true
---
## Publish

```

lib_dir/
	- src/
	- include/
	- examples
	- library.json
	- README.md

```

**liberary.json**

```json
{
  "name": "",
  "version": "1.0.0",
  "description": "",
  "keywords": "",
  "repository": {
    "type": "git",
    "url": "https://github.com/aruncs31s/lib.git"
  },
  "authors": [
    {
      "name": "",
      "email": "",
      "url": ""
    }
  ],
  "license": "MIT",
  "frameworks": ["arduino"],
  "platforms": ["espressif32", "espressif8266"]
}

```

### Publishing through terminal

```bash
pio account login
pio pkg publish .

```

^74ebd8

## How to Update 

```bash
git add .
git commit -m "Release version 1.0.1"
git tag -a 1.0.1 -m "Version 1.0.1"
git push origin --tags

```

^fd9329

**Update the version**

```json
"version": "1.0.1",

```

**Then update the Registery**

```bash
pio pkg publish .

```

^d80f33
