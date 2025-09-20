---
id: xrandr
aliases: []
tags:
  - os
  - tools
dg-publish: true
---
# xrandr

> [!float|right-small] Contents
> [[#Adding a new resolution]]

#### Adding a new resolution

_Example adding a 1366x768 resolution_

1. calculate VESA GTF mode lines

```bash
gtf 1366 768 60

```

```bash
  # 1368x768 @ 60.00 Hz (GTF) hsync: 47.70 kHz; pclk: 85.86 MHz
  Modeline "1368x768_60.00"  85.86  1368 1440 1584 1800  768 769 772 795  -HSync +Vsync

```

2. use `xrandr` to add new mode

```bash
xrandr --newmode "1368x768_60.00"  85.86  1368 1440 1584 1800  768 769 772 795  -HSync +Vsync

```

3. Add the new mode

```bash
xrandr --addmode nxoutput0 "1368x768_60.00"

```

4. Finally apply the new mode

```bash
xrandr --output nxoutput0 --mode "1368x768_60.00"

```
