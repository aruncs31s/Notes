# Position Testing

```python
import json
import requests
url = "http://192.168.95.6/setServo"
def get_pulse(val):
    return val * (512 - 102) / 180 + 102
def set_position(id, val):
    req_params = {"id": id, "angle": val}
    response = requests.get(url, params=req_params)
    print(f"Response: {response.text}")
while True:
    id = int(input("Enter servo ID (0-15): "))
    val = int(input("Enter angle (0-180): "))
    set_position(id, val)
```


# Get initial position from the web
```python
from position_scraper import extract_positions
print(
    extract_positions(
        "https://github.com/AI-Robot-GCEK/robo-initial-positions/blob/main/src/initial-positions.h"
    )
)
```