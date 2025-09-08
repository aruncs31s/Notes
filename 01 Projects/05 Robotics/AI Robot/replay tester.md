---
aliases: 
Date: "16-06-2025"
---
# replay tester

>Improved version of [[Position tester v0.0.1]]
- [[Servos]]

1. I can get the `initial_angles` of the servos from the [[Position Scraper.py]] which is in the format 
>[!info]- how did i get this?
>```python
>from position_scraper import extract_positions
>url = "https://raw.githubusercontent.com/AI-Robot-GCEK/robo-initial-positions/main/src/initial-positions.h"
>print(extract_positions(url))
>```

```
{'LA1_INITIAL_POSITION': 25, 'LA2_INITIAL_POSITION': 30, 'LA3_INITIAL_POSITION': 160, 'RA1_INITIAL_POSITION': 160, 'RA2_INITIAL_POSITION': 160, 'RA3_INITIAL_POSITION': 30, 'LH_INITIAL_POSITION': 93, 'RH_INITIAL_POSITION': 107, 'LL1_INITIAL_POSITION': 130, 'LL2_INITIAL_POSITION': 25, 'LL3_INITIAL_POSITION': 160, 'RL1_INITIAL_POSITION': 60, 'RL2_INITIAL_POSITION': 150, 'RL3_INITIAL_POSITION': 30, 'LF_INITIAL_POSITION': 90, 'RF_INITIAL_POSITION': 99}
```
2. And a reading from the `data.json` is in the format
>[!info]- how did i get this?
>```python
>import json
>def get_readings(datafile):
>    with open(datafile, "r") as data:
>        all_readings = json.load(data)
>    list_readings = []
>    for number in range(len(all_readings)):
>        list_readings.append(all_readings[number]["servo_values"])
>    return list_readings
>def list_to_dict(data):
>    the_dict = {i: data[i] for i in range(len(data))}
>    return the_dict
>if __name__ == "__main__":
>    data_file = "/home/aruncs/Git/Organizations/AI-Robot-GCEK/ai_robo_position_replayer/data.json"
>    readings = get_readings(data_file)
>    # print(readings)
>    for i in readings:
>        print(i)
>```

```
{'0': 25, '1': 30, '2': 160, '3': 160, '4': 160, '5': 30, '6': 93, '7': 107, '8': 130, '9': 25, '10': 160, '11': 60, '12': 150, '13': 30, '14': 90, '15': 99}
{'0': 25, '1': 30, '2': 160, '3': 160, '4': 160, '5': 30, '6': 93, '7': 107, '8': 130, '9': 25, '10': 160, '11': 60, '12': 150, '13': 30, '14': 90, '15': 99}
{'0': 25, '1': 30, '2': 160, '3': 160, '4': 160, '5': 30, '6': 93, '7': 107, '8': 130, '9': 25, '10': 160, '11': 60, '12': 150, '13': 30, '14': 90, '15': 99}
{'0': 25, '1': 30, '2': 160, '3': 160, '4': 160, '5': 30, '6': 93, '7': 107, '8': 130, '9': 25, '10': 160, '11': 60, '12': 150, '13': 30, '14': 90, '15': 99}
```

So first thing is to make the two similar. 

```python
from position_scraper import extract_positions
url = "https://raw.githubusercontent.com/AI-Robot-GCEK/robo-initial-positions/main/src/initial-positions.h"

def convert_to_indexed_dict(the_dict):
    indexed_dict = {}
    for i, key in enumerate(the_dict):
        indexed_dict[i] = the_dict[key]
    return indexed_dict

print(convert_to_indexed_dict(extract_positions(url)))
```
Now i have to also convert the readings to the same format.

```python
def convert_keys_to_int(data):
    return {int(k): v for k, v in data.items()}
for i in readings:
        print(convert_keys_to_int(i))
```
