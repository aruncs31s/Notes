---
complete: false
cssclasses:
  - wide-page
---

# ESP32 Expansion Board
```dataview
TABLE 
	file.mtime as "Last Modified",
	file.outlinks as "Outgoing Links"
WHERE file = this.file


```




## Pin Configuration
The `ADC2_CH0:7` will not work when using WiFi. In this board the wifi will be utilized most of the time so going to ignore the ADC2_CH0:7 pins  
- [ ] Check if they can be used for something else 🔽 📅 2025-04-29

```c
#define ADC_1 33  
#define ADC_2 32
#define ADC_3 35
#define ADC_4 34
#define ADC_5 39 
#define ADC_6 36
```

These are the exposed **ADC_1** to **ADC_6**  , but the the **ADC_4:6** is connected to the [[GY-61]]
> This pins are arranged in **LTR** manner .

```cpp
#define ENA 
#define ENB
#deinf 
```

## Integrations

I have integrated l298n sensor to the expansion board but the following problems exist
-  i have used the 7805 IC which only supports max 1.5 A
- [ ] also  need to find out which voltage regulator ic is used in the original l298n 
- [ ] Also look for a way to increase the current in the new design 📅 2025-04-16

### l298n
The [[l298n]] is a motor driver 

>- Operating supply voltage up to 46 V. (50 abs max) 
>-  Total dc current up to 4 A. 
>- Low saturation voltage. 
>- Overtemperature protection. 
>- Logical "0" input voltage up to 1.5 V (high noise immunity).
>- Total Power Dissipation (25W)

>[!multi-column]
>
>>[!blank]
>>```bash
>>1 -> CURRENT SENSING A
>>2 -> OUTPUT 1
>>3 -> OUTPUT 2
>>4 -> SUPPLY VOLTAGE V
>>5 -> INPUT 1
>>6 -> ENABLE A
>>7 -> INPUT 2
>>8 -> GND
>>9 -> LOGIC SUPPLY VOLTAGE VSS
>>10 -> INPUT 3
>>11 -> ENABLE B
>>12 -> INPUT 4
>>13 -> OUTPUT 3
>>14 -> OUTPUT 4
>>15 -> CURRENT SENSING B
>>```

- [ ] there are 4 diodes left to solder

> the diodes that are left to solder should solder in a way that cathod should be connected to the +ve power rail and anode should connect to the output
`cathod +ve power rail (5v)` and `anode output(1:4)`


### Buzzer
The buzzer is connected to `BUZZER_PIN(x)` pin of the esp32
Test code from [How to Set up a Buzzer With an Arduino | Arduino | Maker Pro](https://maker.pro/arduino/projects/buzzer)
```cpp
 int buzzer = 12;//the pin of the active buzzer 
 void setup() { 
	 pinMode(buzzer,OUTPUT);//initialize the buzzer pin as an output 
} 
void loop() {
	unsigned char i;
	while(1) {//output an frequency 
		for(i=0;i<80;i++) { 
			digitalWrite(buzzer,HIGH);
			 delay(1);//wait for 1ms 
			 digitalWrite(buzzer,LOW); 
			 delay(1);//wait for 1ms 
			 } //output another frequency 
			 for(i=0;i<100;i++) { 
				 digitalWrite(buzzer,HIGH); 
				 delay(2);//wait for 2ms 
				 digitalWrite(buzzer,LOW); 
				 delay(2);//wait for 2ms 
				 }
			  }
	   }
```