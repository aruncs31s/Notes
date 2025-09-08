---
id: Position_replayer
aliases: []
tags: []
---

### data.py

@function

@logic -> It reads all the data from the datafile(data.json) and returns a list [data1,data2,data3]

```python
def get_readings(datafile):
    with open(datafile, "r") as data:
        all_readings = json.load(data)
    list_readings = []
    for number in range(len(all_readings)):
        list_readings.append(all_readings[number]["servo_values"])
    return list_readings
```

@function

```python
def list_to_dict(data):
    the_dict = {i: data[i] for i in range(len(data))}
    return the_dict
```
