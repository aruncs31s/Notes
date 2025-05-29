---
id: APIs
aliases: []
tags:
  - smartcity
  - website
cssclasses:
  - wide-page
dg-publish: true
---

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

```bash
$ curl localhost:8000/api/data

{
  "message": "Device ID is required",
  "status": "error"
}
```

## /api/data/old

#wholecode

```python
def get_old_data():
    if test:
        db.update_random_data()
    current_node, day = (request.args.get("device_id"), request.args.get("day"))
    if day is None:
        return jsonify({"status": "error", "message": "Day is required"}), 400
    if current_node is None:
        return jsonify({"status": "error", "message": "Device ID is required"}), 400
    if debug:
        print(f"current_node: {current_node}, day: {day}")
    current_node_ip = esp_devices.get_ip_of_the_node(current_node)
    if current_node_ip is None:
        return jsonify({"status": "error", "message": "Device not found"}), 404
    the_date = (datetime.now() - timedelta(days=int(day))).strftime("%Y-%m-%d")
    # raw_data = db.get_data(current_node_ip,date=the_date)
    raw_data = db.get_10_min_interval_data(device_id=current_node_ip, date=the_date)
    if debug:
        print("Raw Data length: ", len(raw_data))
    data = [
        {
            "timestamp": row[TIME_INDEX].strftime(highcharts_timestamp_format),
            "battery_voltage": row[BAT_INDEX],
        }
        for row in raw_data
    ]
    return jsonify(data), 200
```

#response

```
$ curl "localhost:8000/api/data/old?device_id=Chittariparamba&day=2"
[
  {
    "battery_voltage": 11.1,
    "timestamp": "2025-05-08 21:40:22"
  },
  {
    "battery_voltage": 9.68,
    "timestamp": "2025-05-08 21:40:22"
  }
]
```

```
args:
  device_id(str)
  day(int)
```

- Obtain the args

```python
current_node, day = (
        request.args.get("device_id"),
        request.args.get("day")S
)
```

- get the `current_node_ip`

```python
current_node_ip = esp_devices.get_ip_of_the_node(current_node)
# eg: '192.168.1.1'

```

- generate random readings (test)
  _this is only done in testing because , the data from the esp is not stored for a longer period of time_

```python
if test:
    db.update_random_data()
```

[flag:: `test`] _is set to 1_

- calculate the `date`

```python

the_date = (datetime.now() - timedelta(days=int(day))).strftime("%Y-%m-%d")
```

- get data corresponding to that

```python

raw_data = db.get_10_min_interval_data(device_id=current_node_ip, date=the_date)
```

- Return the data

```python
data = [
        {
            "timestamp": row[TIME_INDEX].strftime(highcharts_timestamp_format),
            "battery_voltage": row[BAT_INDEX],
        }
        for row in raw_data
    ]
    # print(data)
    return jsonify(data), 200
```
