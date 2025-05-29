---
id: Analog Interfacing
aliases: []
tags: []
---

#### Analog Interfacing

> [!blank|right-small]
> ![[03 Electronics/Embedded Systems/Micro Controllers/Espressif/ESP32/programming/attachments/esp32 non linear.excalidraw]]

- Non Linear
- Can not measure 0-0.2 and 3.2-3.3

#syntax

```arduino
analogRead(pin_number);
```

### Usefull Functions

1. analogReadMilliVolts(pin)

```c
analogReadMilliVolts()
```

> [!float|right-small] ADC2
> **ADC2** can't be used while using wifi
> [25,26,14,12,13,04,02,15]

> [!blank|left-small] > ![](https://lastminuteengineers.com/wp-content/uploads/iot/ESP32-ADC-Pins.png)

- Has 2 12-bit SAR ADCs {ADC1 , ADC2}
- ADC will have a defined resolution and a reference voltage which is usually the supply voltage
- Maximum Possible Value

$$
Max = 2^N -1
$$

_Where N = resolution_

- If resolution is `8 bit`

$$
Max = 255
$$

 <details>
<summary>Example</summary>
Thus, if the reference voltage is 5V and an 8−bit ADC is used, then 5V corresponds to a reading of 255, 1V corresponds to a reading of (255/5*1) = 51, 2V corresponds to a reading (255/5*2) = 102 and so on. If we had a 12 bit ADC, then 5V would correspond to a reading of 4095, 1V would correspond to a reading of (4095/5*1) = 819, and so on.
</details>

Calculate Resolution

```python
N=int(input("Enter the ADC Value"))
print("Max Value = " ,2**N -1)
```

#### Connecting ADC Sensors With ESP32

- [Conecting LDR Sensor ]()

##### Connecting LDR Sensor

`Credit` [Intercaing Code](https://github.com/yash-sanghvi/ESP32/blob/master/AnalogReadWithLDR/AnalogReadWithLDR.ino)

```c
const int LDR_PIN = 36;

void setup() {
   Serial.begin(9600);
   analogReadResolution(10); //default is 12. Can be set between 9-12.
}
void loop() {
   float LDR_Voltage = ((float)LDR_Reading*3.3/1023);
   Serial.print("Reading: ");Serial.print(LDR_Reading); Serial.print("\t");Serial.print("Voltage: ");Serial.println(LDR_Voltage);
}
```

#### Measure Voltage using ADC Pins

```bash
float analog_voltage = 0;
float get_voltage(int adc_value) {
   return VMIN + (adc_value / ADC_MAX_12);

}

void setup(){
   Serial.begin(9600);
}
void loop(){
analog_value = analogRead(adc_pin);
analog_voltage = get_voltage(analog_value);
}
```

## Sources

- [Source1](<https://www.tutorialspoint.com/esp32_for_iot/interfacing_esp32_with_analog_sensors.htm#:~:text=In%20the%20image%20shown%20below,36%20(VN)%20of%20ESP32.>)
