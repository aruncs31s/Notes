---
aliases:
  - lcd
  - i2c
---
# I2C LCD Interfacing
Created : 2024-07-23 17:59
[[PCF8574]]
- GND: Pin 6 (GND)
- VCC: Pin 4 (5V)
- SDA: Pin 3 (SDA)
- SCL: Pin 5 (SCL)
- 
## Contents
- [[#PI]]


###  PI
Supported Port expanders , `MCP23017`, `MCP23008` , `PCF8574`
```bash
pip install RPLCD 
```
```python
# Source: DS,https://rplcd.readthedocs.io/en/stable/getting_started.html
from RPLCD.i2c import CharLCD
import time
import os

# Initialize the LCD
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

try:
    while True:
        # Get CPU temperature
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=", "").replace("'C\n", "")

        # Display temperature on the LCD
        lcd.clear()
        lcd.write_string("CPU Temp:")
        lcd.crlf()
        lcd.write_string(f"{temp} C")

        # Wait for 2 seconds
        time.sleep(2)

except KeyboardInterrupt:
    lcd.clear()
    lcd.close()
```


#### Scrolling Text
Source: https://blog.dbrgn.ch/2014/4/20/scrolling-text-with-rplcd/
TODO: Check what it does 
```python
from RPLCD import CharLCD
lcd = CharLCD()
lcd.write_string(u'Raspberry Pi HD44780')
lcd.cursor_pos = (2, 0)
lcd.write_string(u'http://github.com/\n\rdbrgn/RPLCD') 
```
## References
1. [[Raspberry Pi]]
2. [[Raspberry Pi 2 B]]
3. [Maker Pro Online](https://maker.pro/raspberry-pi/tutorial/connecting-an-lcd-screen-to-raspberry-pi-with-a-logic-converter)
4. https://learn.adafruit.com/character-lcds/wiring-a-character-lcd
5. https://blog.dbrgn.ch/2014/4/20/scrolling-text-with-rplcd/
