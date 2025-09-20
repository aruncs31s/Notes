---
id: Pyaudio
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# Pyaudio
Created : 2024-05-02 03:31

## Contents

#### Get Audio device

```python
import pyaudio
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get("deviceCount")

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get("maxInputChannels")) > 0:
        print(
            "Input Device id ",
            i,
            " - ",
            p.get_device_info_by_host_api_device_index(0, i).get("name"),
        )

```

## References
1. 