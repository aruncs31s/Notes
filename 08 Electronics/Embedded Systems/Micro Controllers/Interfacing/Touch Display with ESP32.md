# Touch Display With ESP 32 

## Esp 32 s 3 touch lcd
![[Touch Display with ESP32.png]]

- LVGL
- Onboard voltage regulator, supports 7~36V
![[Touch Display with ESP32-1.png]]

![[Touch Display with ESP32-2.png]]



![[Touch Display with ESP32-3.png]]

1. **ESP32-S3-WROOM-1-N16R8**  
    The SoC with WiFi and Bluetooth, up to 240MHz operating frequency, integrated 8MB PSRAM and 16MB Flash
2. **TF card slot**
3. **USB Type-C port**
4. **BOOT button**  
    Press and hold while powering on for program burning
5. **RESET button**
6. **Optocoupler isolation**
7. **Touch panel connector**
8. **5inch display panel connector**
9. **RS485 and CAN terminal resistors selection**  
    close by default
10. **Battery power supply ON/OFF**
11. **3.7V single lithium battery GH1.25 header**
12. **Status Indicators**  
    DONE: Lithium battery charging completed indicator  
    CHG: Lithium battery charging indicator  
    PWR: Power supply indicator  
    (the CHG will blink and DONE will light on when connecting with DC power supply and without lithium battery connected or battery switch is OFF)
13. **7-36V DC power supply terminal**
14. **I2C interface terminal**  
    VOUT pin output 5V/3.3V (switching by onboard resistor)
15. **CAN interface terminal**
16. **RS485 interface terminal**
17. **Digital output**  
    5~36V, open-drain output, output load: 450mA per channel (MAX)
18. **Input signal common terminal**  
    NC: dry contact passive input  
    Connect to power supply positive: digital input low active, for NPN wet contact active input, 5V-36V DC  
    Connect to power supply negative: digital input high active, for PNP dry contact active input, 5V-36V DC
19. **Digital input**  
    5~36V, supports passive / active input (NPN or PNP)
20. **I2C VOUT output selection**  
    for switching output valtage and I/O level of I2C VOUT, 3.3V by default
21. **RTC battery holder**  
    Compatible with CR927 battery



---

23. https://www.waveshare.com/esp32-s3-touch-lcd-5.htm
