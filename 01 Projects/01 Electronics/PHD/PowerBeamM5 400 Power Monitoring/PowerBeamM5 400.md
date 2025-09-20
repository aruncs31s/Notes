---
id: PowerBeamM5 400
aliases: []
tags:
  - projects
  - electronics
  - phd
  - powerbeamm5_400_power_monitoring
dg-publish: true
---
# Power Beam M5 400

#### IP Configurations

| IP           | Device            |
| ------------ | ----------------- |
| 172.16.36.10 | Raspberry Pi      |
| 172.16.36.11 | ArchLinux         |
| 172.16.36.12 | Ubiquity AP       |
| 172.16.36.13 | Ubiquity Reciever |

#### Rain Sensor

The sensor is a self-emptying tipping bucket collector. This means that for each 0.011" (0.2794 mm) of rain that falls in the sensor, the bucket will tilt, dumping the water out and closing a momentary contact.

#### LIFEPo4 Battery

| State   | Voltage                                        |
| ------- | ---------------------------------------------- |
| Dead    | 3V and Kept Increasing after Disconnect        |
| Charing | 12.40 Volts charges at a rate of 1 A per Sec   |
| Charged | 13.14 Volts across the terminal after charging |

I kept 13.1 V to constant to charge the battery from 01:14 AM to ~4:00 AM

##### Batter Life

- Starting Voltage 13.1
- Measured From 2024-07-17 5:10 PM to 10:02 PM Still Left Most of the life
- Now the voltage is 12.78 V

### Measuring

| Measuring Points | Status |
| ---------------- | ------ |
| 10 AM            |        |
| 12 PM            |        |
| 2 PM             |        |
| 4 PM             |        |
| 8 PM             |        |
