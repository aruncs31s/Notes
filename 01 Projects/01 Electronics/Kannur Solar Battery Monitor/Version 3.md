---
id: Version_3
aliases: []
tags:
  - projects
  - electronics
  - kannur_solar_battery_monitor
Date: "06-02-25"
dg-publish: true
---
# Version 3
The version 3 started in **06-02-25**  which entirely changes the philosophy in a way that which result(may be) in higher efficiency 
#### Changes
-  Moved the server from the ESP8266 to more powerfull computer 
- Only send data when there are any change ? and less frequent.

# Codes

## ESP8266 Code

```cpp

```

#### Scraping

```python
esp_url = "http://192.168.58.43/data"

```

```python
@app.route('/api/data', methods=['POST'])
@app.route('/api/data', methods=['GET'])

```

##### device.css

```css
@import './base.css';
header {
background-color: var(--nord1);
color: var(--nord6);
padding: 20px 0;
text-align: center;
font-size: 24px;
}
/**/

/* ul { */

/* list-style-type: none; */

/* padding: 0; */

/* display: flex; */

/* flex-direction: column; */

/* align-items: center; */

/* } */

/**/

/* li { */

/* background-color: var(--nord2); */

/* margin: 10px 0; */

/* padding: 10px; */

/* border-radius: 5px; */

/* max-width: 600px; */

/* width: 100%; */

/* box-sizing: border-box; */

/* } */

  

/* main .current-values { */

/* text-align: center; */

/* background-color: var(--nord1); */

/**/

/* } */

/**/

.dashboard {

text-align: center;

}

  

.current-values {

margin: 20px;

padding: 20px;

background-color: var(--nord1);

border-radius: 5px;

}

  

.control-button {

padding: 15px 30px;

font-size: 18px;

background-color: #4CAF50;

color: white;

border: none;

border-radius: 5px;

cursor: pointer;

margin: 10px;

margin-bottom: 10px;

}

  

.control-button:hover {

background-color: #45a049;

}

  

.control-button.active {

background-color: #e74c3c;

}

  

.button-status {

margin-top: 10px;

font-style: italic;

}

  

/* .control-panel {

display: flex;

flex-direction: column ;

align-items: center;

justify-content: center;

/* height: 100vh; Full viewport height */

/* } */

  

main .device-status {

margin: 20px;

padding: 20px;

background-color: var(--nord1);

border-radius: 5px;

}

  

main .row {

display: flex;

flex-direction: row;

margin-left: 2rem;

align-items: stretch;

  

}

  

main .column-right {

margin: auto;

display: flex;

flex-direction: column;

}

  

/* For All devices which are nearby and under the main node */

  

.related-devices{

background-color: var(--nord1);

display: flex;

flex-direction: row;

justify-content: space-around;

padding-bottom: 100px;

margin: 20px;

border-radius: 10px;

margin-bottom: 100px;

}

/* For Nearby devices */

  

/* .nearby-devices .device-list{

display: flex;

flex-direction: column;

  

} */

.device-list li{

width: 120%;

margin: 10px 0;

padding: 10px;

border-radius: 10px;

max-width: 600px;

display: flex;

justify-content: space-between;

align-items: center;

}

  

.device-list span a:hover{

background-color: var(--nord3);

color: var(--nord6);

}

.device-under-main-node{

background-color: var(--nord1);

display: flex;

flex-direction: row;

justify-content: space-around;

}

```