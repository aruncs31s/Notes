---
id: Position_Scraperpy
aliases: []
tags:
  - coding
  - python
  - my_modules
Date: 15-06-2025
dg-publish: true
---
# Position Scraper.py

```python
def extract_positions(url):
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    pattern_define = re.compile(r'#define\s+(\w+_INITIAL_POSITION)\s+(\d+)', re.MULTILINE)
    define_positions = {}
    for match in pattern_define.finditer(content):
        name = match.group(1)
        value = int(match.group(2))
        define_positions[name] = value

    return define_positions 

```

```python
import requests

```

##### To display the content

```python 
import requests
url = "https://raw.githubusercontent.com/AI-Robot-GCEK/robo-initial-positions/main/src/initial-positions.h"
response = requests.get(url)
response.raise_for_status()
content = response.text
print(content)

```

#### Update current IP

```python
 global ip_entry
    ip = ip_entry.get()
    if not ip.strip():
        print("IP cannot be empty!")
        return
    data = {"ip": ip}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"IP saved to data.json: {ip}")

```
