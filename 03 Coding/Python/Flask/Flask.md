---
id: Flask
aliases: []
tags:
  - coding
  - python
  - flask
dg-publish: true
---
# Flask

## APIs 

### GET 

```python
@app.route("/api/data", methods=["GET"])
def get_data():
    db.update_random_data(esp_ips)
    current_node = request.args.get("device_id")
    if current_node is None:
        return jsonify({"status": "error", "message": "Device ID is required"}), 400
    current_node_ip = esp_devices.get_ip_of_the_node(current_node)
    if current_node_ip is None:
        return jsonify({"status": "error", "message": "Device not found"}), 404t
    date_now = datetime.today().date()
    raw_data = db.get_data(current_node_ip,date=date_now)
    data = [
        {
            'timestamp': row[TIME_INDEX].strftime(highcharts_timestamp_format),
            'battery_voltage': row[BAT_INDEX]
        }
        for row in raw_data
    ]
    return jsonify(data), 200

```

#### Example POST

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(f"Name: {name}, Email: {email}, Password: {password}")
    return jsonify({"status": "success", "message": name})

if __name__ == "__main__":
    app.run(debug=True)

```

For this the following wont work 
![[curl POST examples#^00546a]]

Because my code uses 

```python
request.form.get("name")

```

This expects **form-encoded data** (like `application/x-www-form-urlencoded` or `multipart/form-data`, not JSON).

If i change it like this

```python
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    print(f"Name: {name}, Email: {email}, Password: {password}")
    return jsonify({"status": "success", "message": name})

```

^14bd6e

![[curl POST examples#^00546a]]

```json
{
  "message": "aruncs",
  "status": "success"
}

```

### POST Upload Image

```python
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # Limit: 2MB
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

```