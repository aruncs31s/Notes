---
id: Home_Page
aliases: []
tags:
  - projects
  - web_based
  - kannur_solar_battery_monitor_website
  - website
tech: flask
cssclasses: 
dg-publish: true
---
# Home Page
>[!blank|right-small]+ Pages 
>There are mainly 4 pages , `Home` , `devices`,`info`, and `about`
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/Home Page]]
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/Device Page]]
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/main_page]]
>Others
>- [[database]]

- [x] The home page should display all the devices ✅ 2025-05-01
- [ ] If possible the battery voltage of each device should be visible in the home page.
> I think i can achive that by creating a script that updates the battery voltage by simply updating a field in the `device.csv` ,
> - [ ] Will that be efficient? check it 

![[Screenshot 2025-04-19 at 2.39.32 AM.png]]
## V0.0.1 Beta
Current status

```

# device.csv
IP,Assigned_Place,Status,Date of Creation,Main_Node,Nearby_Nodes

```

This device.csv if first created by the user in which the IP of the device , etc. are typed. 

```python
csv_file = "/Users/aruncs/Desktop/Projects/Kannur-Solar-Battery-Monitoring-System-Website/devices.csv"
import csv
devices = [] 
with open(csv_file,newline="") as csvFile:
	reader = csv.DictReader(csvFile)
	for row in reader:
		devices.append(
	            {
	                "assigned_place": row["Assigned_Place"],
	                "status": row["Status"],
	                "ip": row["IP"],
	            }
	        )

```

```python
print(devices)

```

But the `status` attribute here only indicates that if the device is placed on the field or not 

```python
active_devices = [
    device for device in devices if device["status"].lower() == "active"
]
inactive_devices = [
    device for device in devices if device["status"].lower() == "inactive"
]
for i in active_devices:
    print(i["assigned_place"])

```

```python
sorted_device = active_devices + inactive_devices

```

## Routing

```python
@app.route("/")
def home():

return render_template("home.html",devices=sorted_device)

```

    .querySelector("button button:nth-child(2)")

```js
let sortAscending = true;
document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("search-input")
    .addEventListener("input", searchDevices);
  document
    .querySelector(".sbutton")  // Changed from .sort-button to .sbutton to match HTML
    .addEventListener("click", sortDevices);
});

```
