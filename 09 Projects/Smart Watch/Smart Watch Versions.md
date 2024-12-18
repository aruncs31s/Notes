---
Created: 29-10-2024
tags:
  - smart-watch
---
# Smart Watch Versions 

## Version 1 
- [[Speech Processing]]

**Requirements**:
- SOS 
- Trigger SOS When the button is not available using Heart Rate 

### Modules 
1. SOS Module 



#### SOS Module 
It consist of single button in which when it is pressed it will send signal to **Police** and **Parents**
- In worst case it should detect when the lady says **HELP!** and send corresponding signal?(location? ) to **Police** and **Parents**

###### **Requirements**:
- Send Message : -> `GSM` Module 

#### Heart Rate Monitoring 
- [[SEN-11574]]
- Used PN **VP** -> 36

######  **Requirements**
- Sense if the heart beat is too high 
	- if yes send the same SOS Message to -> **Police** and **Parents** 
#### Components 