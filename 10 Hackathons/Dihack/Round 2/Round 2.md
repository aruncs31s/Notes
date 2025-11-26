---
id: Round 2
aliases: []
tags:
  - hackethons
  - dihack
  - round_2
dg-publish: true
---
# Round 2

- [x] Requirement Analysis ✅ 2024-12-14
- [x] Hardware Block Diagram ✅ 2024-12-14
- [x] Software Block Diagram ✅ 2024-12-14

![[functional diagram.canvas|functional diagram]]

![[Drawing 2024-12-14 17.00.57.excalidraw]]
![[Drawing 2024-12-14 17.10.03.excalidraw]]
![[Drawing 2024-12-14 17.13.24.excalidraw]]

#### Platform IO
PlatformIO Core has been successfully installed into an isolated environment `/home/aruncs/.platformio/penv`!

The full path to `platformio.exe` is `/home/aruncs/.platformio/penv/bin/platformio`

If you need an access to `platformio.exe` from other applications, please install Shell Commands
(add PlatformIO Core binary directory `/home/aruncs/.platformio/penv/bin` to the system environment PATH variable):

See https://docs.platformio.org/page/installation.html#install-shell-commands

```bash
platformio run -t upload -t nobuild

```