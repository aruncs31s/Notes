---
id: Solar Battery Monitor
aliases: []
tags:
  - projects
  - electronics
  - solar_battery_monitor
Created: ""
Status: working
dg-publish: true
---
# Solar Battery Monitor

- [[Solar Battery Monitor Programming]]
  > [!blank|right-medium]
  > ![[solar battery monitor.excalidraw]]

Here

- **VMAX** : 14.4
- **VMIN** : 10.8
  When using $R_a$ as $3.5 R$ and $R_b$ as $R$ we get
  $$
  V_{R_b} = \frac{1}{4.5} Vin
  $$

```python
def calculte_V_Rb(Vin):
	return Vin * (1/4.5)
Vin = 10.8
print(calculte_V_Rb(Vin))

```

Also note that

- $10.8V$ = $0\%$ = $2.4 V$ at $V_{R_b}$
- $14.4V$ = $100\%$ = $3.2V$ at $V_{R_b}$

## Components

| Componets                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Model   | Quantity     | Price  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------ | ------ |
| [DC-DC Converter Duck](https://amzn.in/d/72f7SH8)                                                                                                                                                                                                                                                                                                                                                                                                                                     |         | 1(Pack of 2) | 132    |
| [Current Sensor](https://robu.in/product/acs712-30a-range-current-sensor-module-hall-sensor/)                                                                                                                                                                                                                                                                                                                                                                                         | ACS712  | 1            | 206    |
| [ESP-12F Module](https://robu.in/product/latest-esp-12f-esp8266-wifi-module-ap-station-remote-serial-wireless-iot-board/)                                                                                                                                                                                                                                                                                                                                                             | ESP-12F | 2            | 200    |
| [ESP8266 Burner](https://www.amazon.in/Walnut-Innovations-ESP8266-Fixture-Development/dp/B08WX14BK8/ref=sr_1_7?dib=eyJ2IjoiMSJ9.dvkHYKiniCIN9-lNKQiT4Yhk7p9WuRCoVPpO2An27h3W7O_VpSuw7DLcDDKfWXJvmqZLF0I3IVr2rgkHn6LDEC-wv0KNgB4YNwgx8VDlNiB-_SrfUx_uwf42hyNZmCBFC3esyLvN3erGpuHgNtbwlEF1My8cOgK5qkmofs5JaR_b-4HfTiWiKiK_nXhEjLB8N4bMGtQWpoJp7EqWOsoN_Qps72YxjmU7gKd9N75JFJo.HMcG8e1TfUXdVDPzWywNp2Ew6s5KpXdHN8jUUxCDLLw&dib_tag=se&keywords=esp8266+programmer&qid=1727445021&sr=8-7) |         | 1            | 800    |
| [Analog Mux](https://amzn.in/d/4Ng8vKp)                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |              | 1338/- |

**Reason for the above components:**

1. DC-DC Converter Duck: To convert the 12V to 3.3V , and 12V to 5V for the ESP8266.
2. Current Sensor : To measure the current.
3. ESP-12F Module: To test the low cost esp-12 f module.
4. esp8266 Burner: To burn the code into the esp8266.
5. Analog Mux: To measure the voltage and current.

#### Relay Interfacing

This relay will be used to control the LED

-
