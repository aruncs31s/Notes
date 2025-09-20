---
id: Smart City WebSite
aliases: []
tags:
  - projects
  - web_based
  - kannur_solar_battery_monitor_website
cssclasses: 
dg-publish: true
---
# Smart City Website
>[!blank|right-small]+ Pages 
>There are mainly 4 pages , `Home` , `devices`,`info`, and `about`
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/Home Page]]
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/Device Page]]
>- [[01 Projects/02 Web_Based/Kannur Solar Battery Monitor Website/website/main_page]]
>Others
>- [[database]]
- [[Codes]]
## Tasks 

```tasks
not done 
path includes website

```

1. [x] Can it plot graphs ✅ 2025-05-04
2. [x] Can my website scraper can be integrated with this? ✅ 2025-05-04
3. [x] How re' going to store the data? ✅ 2025-05-04

>[!float|right-medium]+ Todoist Tasks 
>```todoist 
>filter: "#Monitoring Website"
>```

## Def
The smart city website is intented to give an interface to monitor the voltage leves of all microcontrollers from a single location , or a single site. The problem with earlier method[^1] is that the user have to check each's(microcontroller ) voltage by going into each microcontroller. The user have to dial each's ip on the *address bar* eg: `http://192.168.1.2`. This method is applicable for 1 or 2 micro-contorllers  but this becomes combersome when the number of microcontrollers increases. Also there is one more or one of meny problem is that , the storage is temporary in that version. , because the [[08 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/ESP32]] has a very limited storage (about `4MB`(bytes)  i guess) , by default the data is stored on the web , about ~1000 points. Now what does the new site offers
- introduction of database 
- entirely new framework called [[Flask]] 
## Versions

[^1]: In earlier method the site(server) was running inside the microcontroller and the client has to access one by one.  