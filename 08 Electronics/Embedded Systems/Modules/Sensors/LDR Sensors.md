<h2 align="center">LDR Sensor</h2>

- [Introduction]()
- [Working]()
- [Interfacing]()

#### Introduction
An LDR (Light Dependent Resistor) sensor is a type of photoresistor that varies its resistance based on the amount of light it is exposed to -- tgpt 

![[Projects/Iot_based_smart_energy_management_system/Files/Images/Pasted image 20240328225646.png|300x250]]

`Credit` [Interfcaing Code](https://github.com/yash-sanghvi/ESP32/blob/master/AnalogReadWithLDR/AnalogReadWithLDR.ino)

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

#### Sources
1. https://www.tutorialspoint.com/esp32_for_iot/interfacing_esp32_with_analog_sensors.htm#:~:text=In%20the%20image%20shown%20below,36%20(VN)%20of%20ESP32.
2. 