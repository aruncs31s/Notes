---
id: platformio
aliases: []
tags:
  - coding
  - embedded_programming
Date: 
Created: 2024-12-17
cssClasses: wide-page
dg-publish: true
---
# Platform IO 
- [[Lib]]
## Install

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py

```

**Neovim Setup**

```bash
pio project init --ide vim --board uno_r4_minima
platformio run -t compiledb

```

- Nodemcu

```bash
pio project init --ide vim --board nodemcuv2

```

## Initial Configs 

	