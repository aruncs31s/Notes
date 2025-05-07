---
tags:
  - smartcity
  - website
cssclasses:
  - wide-page
dg-publish: true
---
# APIs

## Fetching Data
Used functions -> 
```python 
@app.route("/api/data", methods=["GET"])
def get_data():
    db.update_random_data(esp_ips)
    current_node = request.args.get("device_id")
    if current_node is None:
        return jsonify({"status": "error", "message": "Device ID is required"}), 400
    current_node_ip = esp_devices.get_ip_of_the_node(current_node)
    if current_node_ip is None:
        return jsonify({"status": "error", "message": "Device not found"}), 404
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


