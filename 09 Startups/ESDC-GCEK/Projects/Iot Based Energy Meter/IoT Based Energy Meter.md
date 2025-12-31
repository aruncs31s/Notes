---
dg-publish: true
---
# IoT Based Energy Meter

Objective: Create a simple current measuring project using **esp8266 and current sensor**.

## Prerequisites.

1. Basic C. 
2. ADC Working
	1. ADC Resolution 
	2. Converting ADC Value to Voltage
	3. ESP8266 Operating Voltage
3. Potential Divider (Voltage Divider)

### Phase 1

| Name                   | Task                            | Date           | Status |
| ---------------------- | ------------------------------- | -------------- | ------ |
| [[Fathimath Safah KT]] | Create a sudo code              | 2025-12-11 + 5 | 🕐     |
| [[Anamika VV]]         | Create a simple circuit diagram | 2025-12-11 + 6 | 🕐     |

#### Create a Sude Code

1. Initialize the Micro Controller
2. Initialize the Current Sensor
3. Read data from the Current Sensor
4. Calculate the required Parameter 
5. Show the result 
6. Go to step 3 (Looping)

```mermaid
sequenceDiagram
    participant MCU as Microcontroller
    participant CS as Current Sensor
    participant UI as Display/Output

    MCU->>MCU: Initialize Microcontroller
    MCU->>CS: Initialize Current Sensor
    loop Continuous Reading
        MCU->>CS: Read Sensor Data
        CS-->>MCU: Current Value
        MCU->>MCU: Calculate Required Parameter
        MCU->>UI: Show Result
    end
```
>[!Note]- How did i drow
>I copy pasted this
>```
>1. Initialize the Micro Controller
>2. Initialize the Current Sensor
>3. Read data from the Current Sensor
>4. Calculate the required Parameter 
>5. Show the result 
>6. Go to step 3 (Looping)
>```
>give a mermaid sequence diagram for this 
>to `chatgpt` so nothing too time taking, just ask it.

This is a simple illustration , but create the complete sudo code.

#### Create a circuit diagram.

