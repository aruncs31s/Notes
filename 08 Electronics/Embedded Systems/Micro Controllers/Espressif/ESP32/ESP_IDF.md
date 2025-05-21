---
id: ESP_IDF
aliases: []
tags: []
---

# ESP_IDF

## DefCon23 ESP-IDF Getting Started

[Source](https://youtu.be/J8zc8mMNKtc?si=Gh7jlwXQuXzNRFle)

### Why use ESP-IDF

- Lang : `C` , `Cpp` , `Python`
- Features:
  - Lots of components
  - Integrated Network Stacks{`bluetooth`,`wifi`}
  - components Manager
- Config:
  - component level Config
  - Supports Kconfig
- Debugging:
  - Supports `GDB Support`
  - `Unity` and `CMock`

### Project Workflow

Installation:

```bash
sudo pacman -S git wget flex bison gperf python3 python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0

mkdir ~/esp
cd ~/esp
git clone -b v5.x --recursive https://github.com/espressif/esp-idf.git
cd ./esp-idf
./install.sh esp32
. export.sh
idf.py -help
```

#### Create Project

```bash
idf.py create-project project_name
cd ./project_name
```

#### Project Structure

1. `main` directory -> main component

```bash
.
├── CMakeLists.txt
└── main
    ├── CMakeLists.txt
    └── smart_blink.c

2 directories, 3 files
```

2. `CMakeLists.txt` declare the entire project

```js
# CMakeLists.txt outside main directory
cmake_minimum_required(VERSION 3.16)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(smart_blink)
```

3. `main/CMakeLists.txt` to register the main component

```js
idf_component_register(SRCS "smart_blink.c"
                    INCLUDE_DIRS ".")
```

4. Source file for the main component

```c
#include <stdio.h>
void app_main(void){
  printf("Hello World\n")
}
```

- Here `app_main()` is the entry point of the project

### Programming Workflow

1. [[#Configure]]

- Setup configuration for each component
- Generate sdkconfig file

2. Build

- Compile source file from all components
- Link and generate project binary

3. Flash

- Reset the ESP-32 into firmware download mode
- Write the binary into flash memory

4. Monitor

- Reset the `ESP-32` into execution mode
- MOnitor the log output using `idf.py monitor`

#### Configure

```bash
idf.py set-target esp32
```

After configuration `build` directory will be created which stores all the temporary files needed for the project

```
 ./
├──  build/
├──  CMakeLists.txt
├──  main/
└──  sdkconfig
```

#### Building the project

1.

```bash
idf.py all
```

### Installation: Linux

[Source](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/linux-macos-setup.html#get-started-linux-macos-first-steps)

### Installation: Arch Linux

1. Install Prerequisites

```bash
sudo pacman -S --needed gcc git make flex bison gperf python cmake ninja ccache dfu-util libusb
```

2. Get ESP IDF

```bash
git clone --recursive  https:/github.com/espressif/esp-idf
cd esp-idf
./install.sh esp32
# Install all ./install.sh all
source export.sh

```

3. Create alias for `esp-idf`

```bash
alias get_idf='/path/to/esp-idf/export.sh'
```

```bash
git clone --recursive  https:/github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
```

Set `IDF_PATH` in your environment to the path of the esp-idf directory.

```bash
export IFD_PATH=~/path_to/esp-idf
```

#install_all

```bash
git clone --recursive  https:/github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
```

### Basics

Most ESP-IDF APIs return error codes defined with the [`esp_err_t`](https://docs.espressif.com/projects/esp-idf/en/v5.3.1/esp32/api-reference/system/esp_err.html#_CPPv49esp_err_t "esp_err_t") type
