---
dg-publish: true
id: project_template
aliases: 
tags:
  - esp32
  - project
  - weather_station
Created: 14-09-2024
Starting Date: 14-09-2024
Target Date: ""
---

# GCEK Weather Station
>[!float|right-small] Contents
>- [[#Methodology]]
>- [[#Modules]]
>- [[#Sensors Used]]
>- [[#Pins Used]]
## Modules
- [[Weather Data Scraper]]
- [[Solar Battery Monitor]]

**Initial Plans**:
1. [x] Measure the Environmental conditions ✅ 2024-09-14
	1. [x] Rain Fall(Volume) ✅ 2024-09-14
	2. [x] Humidity ✅ 2024-09-14
	3. [x] Temperature ✅ 2024-09-14
	4. [x] Wind Direction ✅ 2024-09-14
	5. [x] Wind Speed ✅ 2024-09-14
	6. [x] Light Intensity ✅ 2024-09-14
**Tasks**:
1. Rain Fall Measurement
2. Humidity Measurement 
3. Temperature Measurement 
4. Wind Speed Measurement 
5. Wind Direction Measurement 
6. Light Intensity Measurement

**Sensors**:

> 1. Light Intensity Sensor `VEML7700`
> 2. Wind Meter

---
#### Rain Volume  Measurement 

^c08e06

>[!blank|right-small] Rain Gauge 
>![[tipping bucket.png]]

 **Sensors Used**:
1.  **rain gauge**: Used to measure the  rainfall , uses tipping bucket mechanism
	- For each **0.011" (0.2794 mm) of rain** the bucket tipps
	- The value is measured by using the [[Interrupts|Interrupt method]] , this can be done using [[03 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/programming/Interrupt Programming]]
	- When switch close it closes the circuit and causes the current to flow from the **VCC** to **GND** through the **R1** + **Internal PULLUP**(if used) resistors 
	 


>[!blank|left-small] 
>![[tipping bucket circuit diagram.png]]

#code 

```c
const uint8_t rain_meter_pin = 13;
long int tipping_count = 0;

void IRAM_ATTR rain_meter_isr(){
tipping_count +=1;
}
void setup(){
pinMode(rain_meter_pin,INPUT_PULLUP);
attachInterrupt(rain_meter_pin,rain_meter_isr,FALLING);
}
void loop(){
  Serial.println(rain_count);
}
```

 ----
#### Wind Speed Measurement 

>[!blank|right-small] 
>![[Anemometer.png.png]]

**Sensors Used**:
1. **Anemometer**:
	- **$1.492 mph = 1 \text{switch closure}/\text{second}$**
	- It also uses [[Interrupts]] like in the [[#Rain Volume Measurement]]

#### Wind Direction Measurement 

>[!blank|right-smal] Wind Direction 
>![[Wind Vane.png.png]]

**Sensors Used**:
1. **Wind vane**:
	- Uses different resistors to produce different values 
>[!blank|right-small]
>![[wind vane circuit.png]]
##### Light Intensity Measurement 

- It Uses `I2C`
- Sample Programming [[03 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32 1/programming/Interfacing#Light Intensity Sensor|Light Intensity Sensor]]
- Supply voltage range VDD: **2.5 V to 3.6 V**

##### Wind Direction

[Source](file:///home/aruncs/Documents/ESP%20Mesh/Weather_Meter_Kit_Datasheet.pdf)

- A voltage must be supplied to each instrument to produce an output.

- we can use interrupt programming for this
- ==Green== Wind Direction and black
  ![[wind_station.excalidraw]]
  Expected Values

```c
#define SFE_WMK_ADC_ANGLE_0_0 3118
#define SFE_WMK_ADC_ANGLE_22_5 1526
#define SFE_WMK_ADC_ANGLE_45_0 1761
#define SFE_WMK_ADC_ANGLE_67_5 199
#define SFE_WMK_ADC_ANGLE_90_0 237
#define SFE_WMK_ADC_ANGLE_112_5 123
#define SFE_WMK_ADC_ANGLE_135_0 613
#define SFE_WMK_ADC_ANGLE_157_5 371
#define SFE_WMK_ADC_ANGLE_180_0 1040
#define SFE_WMK_ADC_ANGLE_202_5 859
#define SFE_WMK_ADC_ANGLE_225_0 2451
#define SFE_WMK_ADC_ANGLE_247_5 2329
#define SFE_WMK_ADC_ANGLE_270_0 3984
#define SFE_WMK_ADC_ANGLE_292_5 3290
#define SFE_WMK_ADC_ANGLE_315_0 3616
#define SFE_WMK_ADC_ANGLE_337_5 2755
```

Obtained Values

```c
3938
3950
3941
3951
3943
3939
4095
4095
4095
4095
4095
4095
4095
3945
3948
```

##### Temp and Humidity Sensor

Name: 7semi SHT40 Humidity and Temperature Sensor Probe I2C

| Operating Voltage:<br> | 3.3V<br>     |
| ---------------------- | ------------ |
| Interface:             | I2C          |
| Temperature Range:     | -40 to 125 C |
| Humidity Range:        | 0~100%rh     |
| VCC                    | Red          |
| Black                  | GND          |
| Yellow                 | SDA          |
| Green                  | SCL          |


#### Pins Used

| Sensor           | Pin            | ESP32 GPIO |
| ---------------- | -------------- | ---------- |
| VEML7700         | SDA            | 21         |
|                  | SCL            | 22         |
| Wind Speed Meter | Intterrupt PIN | 34         |
| Wind Direction   | GPIO/ADC       | 32         |
| Rain Fall        | Interrupt      | 35         |
| Batter Monitor   | ADC 1          | 36         |
| SHT40            | {VEML7700}     | SDA        |

##### 
- Light Sensor 
SDA -> D2 
SCL -> D1 

- We