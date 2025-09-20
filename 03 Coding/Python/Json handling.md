---
id: Json_handling
aliases: []
tags:
  - coding
  - python
Date: 16-06-2025
dg-publish: true
---
# Json Processing

```python
data = [
    {
        "name": "dd",
        "servo_values": {
            "0": 25,
            "1": 30,
            "2": 160,
            "3": 160,
            "4": 160,
            "5": 30,
            "6": 93,
            "7": 107,
            "8": 130,
            "9": 25,
            "10": 160,
            "11": 60,
            "12": 150,
            "13": 30,
            "14": 90,
            "15": 99
        }
    },
    {
        "name": "dd1",
        "servo_values": {
            "0": 25,
            "1": 30,
            "2": 160,
            "3": 160,
            "4": 160,
            "5": 30,
            "6": 93,
            "7": 107,
            "8": 130,
            "9": 25,
            "10": 160,
            "11": 60,
            "12": 150,
            "13": 30,
            "14": 90,
            "15": 99
        }
    },
]

```

```python
num_data_entry = len(data)
print(f"Got: {num_data_entry} data entries")

```

```python
servo_values = data[0]["servo_values"]
print(servo_values)

```

```python
servo_values = data[0]["servo_values"]

# values = list(servo_values.values())
keys = list(servo_values.keys())

print("Keys:", keys)
print("Values:", values)

```