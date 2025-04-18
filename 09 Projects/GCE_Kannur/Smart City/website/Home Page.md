---
aliases:
  - smart city home page
tech: flask
---

# Home Page
- [ ] The home page should display all the devices 
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
This device.csv if first created by the u