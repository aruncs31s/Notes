---
aliases:
  - squaring circuit
Date: 18-05-2025
tags:
  - opamp
  - electronics
---
# Schmitt Triger
## Components Required
 1. Dual Power Supply 
 2. Function Generator 
 3. Ossciloscope
 4. Bread Board
 5. [[IC741]]
 6. Resistor 
 7. Probes and Connecting Wires

## Design

$$
V_{ut } = \frac{R_{1}}{R_{1}+R_{2}} (+V_{sat})
$$

$$
V_{lt} = \frac{R_{1} }{R_{1} + R_{2}} (-V_{sat})
$$
$$
V_{hy} = V_{ut} - V_{lt}
$$
To minimize the offset issues a resistor $R_{om}$ can be connected between *inverting terminal* and *ground*
$$
R_{om} = R_{1} || R_{2}
$$
## Circuit

 ![[img_schmitt_trigger.png]]
## Output Waveform 
 ![[img_st_out.png]]

### Hysteresis
![[hysteresis_st.excalidraw]]

## Characteristics
- Speed of operation 
- Accuracy 
- Compatibility of output -> TTL 
