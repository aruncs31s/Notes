---
id: 07-Modules
tags:
  - python
  - modules
  - datetime
  - requests
dg-publish: true
---

# Common Modules

Useful built-in and third-party Python modules.

## datetime

```python
from datetime import datetime
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")

# Common formats
datetime.now().strftime("%Y%m%d%H%M%S")  # 20260422123456
datetime.now().strftime("%Y-%m-%d")       # 2026-04-22
datetime.now().strftime("%H:%M:%S")      # 12:34:56
```

## requests

```python
import requests
response = requests.get("https://api.example.com")
data = response.json()
```

## unittest.mock

```python
from unittest.mock import Mock, patch
mock = Mock()
mock.return_value = "fake response"
```

## Flask (Web Framework)

```python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def get_data():
    device_id = request.args.get("device_id")
    if device_id is None:
        return jsonify({"error": "Device ID required"}), 400
    return jsonify({"data": "some data"}), 200

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    return jsonify({"status": "success", "message": name}), 201

app.run(debug=True)
```

---

**Next:** [[08-Exception-Handling]] - Handling errors

**See Also:** [[06-Classes]] - Classes