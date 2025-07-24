---
id: Battery
aliases: []
tags: []
---
#### Battery Percentages

###### mAh to Watt Hours

$$
\frac{mAh \times V}{1000} = Wh
$$

### Charging

[Source](https://www.power-sonic.com/blog/how-to-charge-lithium-iron-phosphate-lifepo4-batteries/)

#### Sealed Lead Acid(SLA) Battery

It is a 3 stage process
![[SEALED-LEAD-ACID-BATTERY-CHARGING-PROFILE.excalidraw]]

###### Stage 1

- The current is limited to avoid damage to the battey
- The rate of of charge = $10\%$ to $30\%$ of the **curret of the capacity rating of the battery or less**

###### Stage 2 (Constant Voltage)

- Begins when the battery output voltage reaches **14.4** or **14.7**(for fast charging SLA batteries)
- Current gradually decreases
- This stage ends when the charging current falls bellow $5\%$

###### Stage 3 Floating Charge

- To keep the battery from **self discharging** and to ensure **Full Capacity**
- Keeps the batteries at $100\%$ **State of charge(SOC)** which avoids sulfation of the battery => prevents damage to the plates of the battery
- [ ] check out sulfation of the battery

#### LIFEPo4 Battery

![](https://www.renogy.com/product_images/uploaded_images/image-3-charging-parameters-chart.jpg)

##### LIFEPo4 Battery Charging
![[LiFEPO4-BATTERY-CHARGING-PROFILE.excalidraw]]


There are four stages instead of 3 stages in [[#Sealed Lead Acid(SLA) Battery|SLA]]

###### Stage 1 : Constant Current

- $30\%$ to $100\%$ current of the capacity rating of the battery
- [ ] Compared to SLA Batteries the LIFEPo4 battery takes only 1 hour to complete the first stage where as the SLA battery takes almost 4 ho ur to complete the first stage

- The lithium Ion Battery can charge fast even with only .5C($50%$ of the charging capacity )

###### Stage 2 : Constant Voltage

- Current gradually Decreaes to below .1C
