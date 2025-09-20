---
id: HC-SR04
aliases: []
tags:
  - electronics
  - embedded_systems
  - modules
  - sensors
Date: 12-10-2024
dg-publish: true
---
# HC-SR04
>[!blank|right-small]
>![[HC-SR04.excalidraw|200x200]]
## Specs 

| Spec                | Value     |
| ------------------- | --------- |
| Max Vcc             | 3.3v - 5v |
| Max Distance        | 3m        |
| Operating Frequency | $40kHz$   |
| Current draw        | $15mA$    |

| Pins | Function                             |
| ---- | ------------------------------------ |
| Vcc  | 3.3v ~ 5v for power                  |
| Trig | Input pin to ,$10\micro s$ TTL Pulse |
| Echo | TTL Out pin (w.r.t Sensor)           |
| GND  | GND                                  |

## Working

$$
\text{range} = \text{High level time} * \text{velocity of sound  / }  2 \tag{1.0}
$$
- here velocity of sound is $340ms^{-1}$ 

How to find the distance?
> - Sound will travel at $343ms^{-1}$
> - it will travel twice the distance because source to target + target to source 

$$
\begin{align}
\text{Distance traveled} & = \frac{\text{speed of light} \times t}{2}
\end{align}
$$
*We can measure $t$* ,and substituting the values 
$$
\begin{align}
\text{Distance} &= \frac{(343ms^{-1}) * t }{2} \\
&= 171.5  \times t  

\end{align}
$$

*Convert it to centimeter/micro seconds*
$$
\begin{align} 
\text{Distance} &= \frac{171.5  \times t }{10^6} \times 100\\
&= 0.01715 \times t \tag{2.0}\\

or \\
\text{Distance} &= \frac{t}{58}\tag{t in us}
\end{align}
$$
*Here duration is in micro seconds*

#example 
**Q**: find the duration of the pulse if the target distance is $30cm$ 
$$
\begin{align} 
\text{We know}\\
\text{Distance} &= {t\over 58}\\
30 &= {t \over 58}\\
\therefore t &= 30 \times 58 = 1740 \micro s\\
&= 1.74 ms
\end{align}

$$

Source[^1]

```c
unit8_t trig=9;
uint8_t echo=8;
int duration;
float distance, meter;
void setup()
{
	Serial.begin(9600);
	pinMode(trig, OUTPUT);
	digitalWrite(trig, LOW);
	delayMicroseconds(100);
	pinMode(echo, INPUT);
	delay(6000);
}
void loop()
{
	digitalWrite(trig, HIGH); // Make trigger pin High for 10 us
	delayMicroseconds(10);
	digitalWrite(trig, LOW); // Then Make it low creating a pulse of 10us
	duration = pulseIn(echo, HIGH);
	if(duration>=38000){
		Serial.print("Out range");
	 }
	else{
		distance = duration/58;
		Serial.print(distance);
		Serial.print("cm");
		meter=distance/100;
		Serial.print("\t");
		Serial.print(meter);
		Serial.println("m");
	}
	delay(1000);
}

```

[^1]: [Datasheet](https://www.handsontec.com/dataspecs/HC-SR04-Ultrasonic.pdf) It is not the origional datasheet i think but it has some pretty usefull information and sample code 
