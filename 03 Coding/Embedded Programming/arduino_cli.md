---
id: arduino_cli
aliases: []
tags:
  - coding
  - embedded_programming
dg-publish: true
---
## ESP32

- [[#ESP32 Setup]]

#### Esp32 Setup

1. Install arduino_cli

```bash
sudo pacman -S arduino-cli

```

2. Add ESP32 Board link

```bash
arduino-cli  --additional-urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

arduino-cli config add board_manager.additional_urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

```

3. Install ESP32 Board

```bash
arduino-cli core update-index
arduino-cli core install esp32:esp32

```

4. **Compiling and uploading the code**

```bash
arduino_cli compile --fqbn esp32:esp32:esp32 /path/to/sketch/folder --log
arduino_cli upload -p port --fqbn esp32:esp32:esp32 /path/to/sketch/folder --log

```

#### Esp8266 Setup

1.

```bash
arduino-cli  core update-index --additional-urls https://arduino.esp8266.com/stable/package_esp8266com_index.json

arduino-cli core install esp8266:esp8266 --config-file ./.cli-config.yml
arduino-cli compile --fqbn esp8266:esp8266:nodemcuv2
arduino-cli board listall |findstr esp8266
arduino-cli upload --fqbn esp8266:esp8266:generic -p /dev/ttyUSB0 --log

```

2. Create file `.cli-config.yml` 

```txt
board_manager:
  additional_urls:
    - http://arduino.esp8266.com/stable/package_esp8266com_index.json

```

```bash
arduino-cli core install esp8266:esp8266 --config-file ./.cli-config.yml

```