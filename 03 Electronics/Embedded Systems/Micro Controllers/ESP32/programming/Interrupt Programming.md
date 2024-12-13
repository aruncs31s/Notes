---
id: Interrupt Programming
aliases:
  - esp32 interrupt
tags:
  -  #programming
  - esp32
Created: "24-08-2024"
Status: true
cssclasses:
  - wide-page
---

# Interrupt Programming

How It Works

> 1. Define the pin which is going to use i used `pin 13`(GPIO 13)
> 2. set the interrupt using `attachInterrupt`

```c
attachInterrupt(GPIOPin,ISR,Mode);
```

**ISR** : It is the function that we want to execute when interrupt occurs on that pin

#syntax

```c
void IRAM_ATTR ISR() {
    Statements;
}
```

rules:

- Should not have any `parameters`
- Should not `return` anything
- isr function should be small
- They should have the `IRAM_ATTR` attribute
  > [!info] `IRAM_ATTR`
  > When we flag a piece of code with the IRAM_ATTR attribute, the compiled code is placed in the ESP32’s Internal RAM (IRAM). Otherwise the code is kept in Flash. And Flash on ESP32 is much slower than internal RAM[^1]

[^1]: https://lastminuteengineers.com/handling-esp32-gpio-interrupts-tutorial/

#sample_program
**MODE**:
| Mode | Works |
|--------------- | --------------- |
| `LOW` | When Pin Is `Low`|
| `HIGH` | Pin Is `High` |
| `CHANGE` | Change form `Low to High` or `High to Low` |
| `FALLING` | When Pin goes from `High to Low` |
| `RISING` | When Pin goes from `Low to High`|

```c
const uint8_t wind_meter_pin = 13;
long int wind_count = 0;

void IRAM_ATTR wind_meter_isr(){
wind_count +=1;
}
void setup(){
Serial.begin(9600);
pinMode(wind_meter_pin,INPUT_PULLUP);
attachInterrupt(13,wind_meter_isr,FALLING);
}
void loop(){
  Serial.println(wind_count);
  delay(100);
}
```
