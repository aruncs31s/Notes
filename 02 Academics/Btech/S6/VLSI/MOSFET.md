---
id: MOSFET
aliases: []
tags:
  - academics
  - btech
  - s6
  - vlsi
dg-publish: true
---
# MOSFET
![](https://cdn1.byjus.com/wp-content/uploads/2021/01/mosfet-circuit.png)

##### Types
![](https://cdn1.byjus.com/wp-content/uploads/2022/03/MOSFET.png)

##### Depletion Type
- When there is ==no voltage across the gate terminal, the channel shows maximum conductance==.
- When the voltage across the gate terminal is either positive or negative, then the channel conductivity decreases.
##### Enhancement Type
- When there is ==no voltage across the gate terminal, then the device does not conduct==. 
- When there is the maximum voltage across the gate terminal, then the device shows enhanced conductivity.

#symbols
![](https://cdn1.byjus.com/wp-content/uploads/2021/01/symbol-of-p-channel-mosfet.png)

#### Region of Operation
##### Cut-Off Region

The cut-off region is a region in which there will be no conduction and as a result, the MOSFET will be OFF. In this condition, MOSFET behaves like an open switch.

##### Ohmic Region

The ohmic region is a region where the current (_IDS_)increases with an increase in the value of _VDS._ When MOSFETs are made to operate in this region, they are used as amplifiers.

##### Saturation Region

In the saturation region, the MOSFETs have their _IDS_ constant in spite of an increase in _VDS_ and occurs once _VDS_ exceeds the value of pinch-off voltage _VP_. Under this condition, the device will act like a closed switch through which a saturated value of _IDS_ flows. As a result, this operating region is chosen whenever MOSFETs are required to perform switching operations.

#### MOSFET OPERATION
##### Modes
| $V_{gs}$               | Accumulation Mode |
| ---------------------- | ----------------- |
| $V_t \gt V_{gs} \gt 0$ | Depletion Mode    |
| $V_{gs} \gt V_t$       | Inversion Mode    |
##### Operating Regions
| $V_{gs} \lt V_t$                                          | Cut-Off Region    |
| --------------------------------------------------------- | ----------------- |
| $V_{gs} \gt V_t \& V_{ds} \lt \left(V_{gs} - V_t \right)$ | Linear Region     |
| $V_{gs} \gt V_t \& V_{ds} \gt \left(V_{gs} - V_t \right)$ | Saturation Region |

> [!NOTE] $V_{gs}$
> $V_{gs}$​ is crucial because it determines the ==operational state of the MOS transistor==, specifically whether it is in cutoff, triode, or saturation mode.

###### Cut-Off Region
It happens when 
$$
V_{gs} \lt V_t
$$
- In this region, the MOS transistor is essentially off, and there is negligible current flowing from the Drain (D) to the Source (S).

###### Linear/Triode Region
It happens when 
$$
V_{gs} \gt V_t \& V_{ds} \lt \left(V_{gs} - V_t \right)
$$
- ie, $V_{gs} \gt V_{th}$ and  $V_{DS}$​ (the voltage difference between the Drain and the Source) is small enough $V_{ds} \lt \left(V_{gs} - V_t \right)$

- [ ] finish $I_d$ MOS TRANSISTOR CURRENT EQUATIONS

