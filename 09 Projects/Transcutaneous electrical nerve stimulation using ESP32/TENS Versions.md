---
id: TENS Versions
aliases: 
tags:
  - Regular_Note,
Date:
  Created: 08-12-2024
cssclasses:
  - wide-page
Status:
  Completed: false
GithubLink:
---

# TENS Versions

## Initial Design

![[TENS Design.excalidraw|900x100]]

### Components Required

| Name                          | Cost         |
| ----------------------------- | ------------ |
| ESP32/Arduino                 | 500/-        |
| Transformer                   | 250/-        |
| MOSFET                        | 15/-         |
| Dot PCB                       | 50/-         |
| 3.7 V Battery                 | 70/-         |
| DC up Converter               | 90/- or 70/- |
| Resistors                     | 5/-          |
| miscellaneous                 | 20/-         |
| Battery Management System<br> | 40/-<br>     |
| Total                         | 1040/-       |

## Version 0.1.0

In this version i am planing to use mosquito bat circuit

![[Tens Version 0.1.0.excalidraw|900x300]]

### Inverter Circuit

![[Inverter Circuit.excalidraw]]

### Duration Circuit

![[monostablemultivibrator.excalidraw]]

#### Design

Required Duration :

![[555#^aeeb05]]

Using this relation to obtain 1seconds to 30 seconds duration

$$
\begin {align}
30 \text{ sec} &= 1.1 R \times C \\
\text{let C = 0.01uF} \\
R &= \frac{30}{1.1 \times 0.01 \times 10^{-6} } = 2.727 \times 10^{7}K \ohm \\
\text{the resistance value is too high so } \\
\text{taking C = 680 uF} \\
R &= \frac{30}{1.1 \times 680 \times 10^{-6}} = 40.1K\ohm
\end{align}
$$

_we can use 100k pot to adjust an obtain duration 30sec and 1 sec_

### Astable Multivibrator

#### Design

Required Freq : $1 Hz \text{ to } 50 Hz$

| Components  | Value |
| ----------- | ----- |
| Rb          | 200k  |
| Transformer | x:x   |

## Version 0.2.0

The [[#Version 0.1.0]] has severe issues that , when the transformer is on it messes up the whole circuit.</br> So going to use the Arduino instead of the [[555]] timer

### Logic 
- The $\micro C$ will control the output , ie turn on and off the transformer 
	- **Required frequency** : *2 to 105Hz* 
```cpp
digitalWrite(pin,HIGH);
delay(duration)
digitalWrite(pin,LOW);
delay(duration)
```
Here `ON time == OFF time` gives 50% duty Cycle 
```python
required_delay = (2,105)
required_delay_in_ms = required_delay[0] * 1000 , required_delay[1] * 1000
print(required_delay_in_ms)
```
### Coding

```c
const uint8_t OUTPUT_PIN = 6;
#define DEBUG
#define ADC_MAX 0x3FF
// Need 1 to 60 second -> delay(1000) to delay(1000 * 60)
uint8_t DELAY_POT = A0;
const uint8_t MIN_DELAY_TIME = 0x3C ;
const uint8_t MAX_DELAY_TIME = 0b1 ;

void setup() {
  Serial.begin(9600);
  pinMode(DELAY_POT,INPUT);
}

uint8_t find_delay(uint8_t _pin,uint8_t _min,uint8_t _max){
  uint16_t _adc_value = analogRead(_pin);
#if defined(DEBUG)
Serial.println("ADC Value: " + String(_adc_value));
#endif
  return (_adc_value * _max) / ADC_MAX;
}
void loop() {
  Serial.println(find_delay(DELAY_POT,MIN_DELAY_TIME,MAX_DELAY_TIME));
  delay(500);
 }
```

```
0
ADC Value: 670
0
ADC Value: 670
```

```cpp
/* Try 2 */
# if defined(ESP8266)
const uint8_t ADC_PIN = A0;
#endif
const uint8_t required_delay[] = {1,60} ;// Min Max
uint8_t current_delay = 0; // To store the delay

void get_delay(uint8_t *_current_delay){
uint16_t _raw_adc_value = analogRead(ADC_PIN);
*_current_delay = _raw_adc_value/ 17;  // 60 / 1023(ADC_MAX)  = ~17
}

void setup() {
  Serial.begin(9600);
  pinMode(ADC_PIN, INPUT);
}
void loop(){
get_delay(&current_delay);
Serial.println("Current Delay : " + String(current_delay));
}
```

#### References

1. https://www.electrothinks.com/2019/09/mosquito-killer-bat-circuit-working-explanation.html
2.
