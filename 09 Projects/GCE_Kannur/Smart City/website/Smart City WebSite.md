---
id: Smart City WebSite
aliases: []
tags: []
---
# Smart City Website

Selecting `Flask` for web development

1. [ ] Can it plot graphs ✅ 2024-10-04
2. [ ] Can my website scraper can be integrated with this?
3. [ ] How re' going to store the data?

# Home Page
- [ ] The home page should display all the devices 
- [ ] If possible the battery voltage of each device should be visible in the home page.
> I think i can achive that by creating a script that updates the battery voltage by simply updating a field in the `device.csv` ,
> - [ ] Will that be efficient? check it 

![[Screenshot 2025-04-19 at 2.39.32 AM.png]]
## V0.0.1 Beta
Current status
```csv
import csv

devices = []

with open("../devices.csv", newline="") as csvfile:

reader = csv.DictReader(csvfile)

for row in reader:

devices.append(

{

"assigned_place": row["Assigned_Place"],

"status": row["Status"],

"ip": row["IP"],

}

)

# Sort devices by status

active_devices = [

device for device in devices if device["status"].lower() == "active"

]

inactive_devices = [

device for device in devices if device["status"].lower() == "inactive"

]

for i in active_devices:

print(i["assigned_place"])

# print(active_devices[0]["assigned_place"])

# print(inactive_devices)
```