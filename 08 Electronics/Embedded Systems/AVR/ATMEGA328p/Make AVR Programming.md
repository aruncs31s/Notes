---
id: Make AVR Programming
aliases: []
tags: []
Date:
  Started: "2024-12-12"
cssClasses: wide-page
---

Make: AVR Programming
**Requirement**:

1. BreadBoard

### Atmega168

**Specs**:

1. **1kb** Ram -> use external Ram
2. No **FPU**

![[8051 pinout.png]]

```
stty -F /dev/tty.iap ispeed 19200

```

### ADC

```c
#include <avr/io.h>
#include <util/delay.h>
#include "pinDefines.h"
uint16_t readADC(uint8_t channel) {
	ADMUX = (0xf0 & ADMUX) | channel;
	ADCSRA |= (1 << ADSC);
	loop_until_bit_is_clear(ADCSRA, ADSC);
	return (ADC);
}
int main(void) {
// -------- Inits --------- //
	uint16_t lightThreshold;
	uint16_t sensorValue;
// Set up ADC
	ADMUX |= (1 << REFS0);
/* reference voltage on AVCC */
	ADCSRA |= (1 << ADPS1) | (1 << ADPS0);
/* ADC clock prescaler /8*/
	ADCSRA |= (1 << ADEN);
/* enable ADC */
	LED_DDR = 0xff;
// ------ Event loop ------ //
	while (1) {
		lightThreshold = readADC(POT);
		sensorValue = readADC(LIGHT_SENSOR);
		if (sensorValue < lightThreshold) {
			LED_PORT = 0xff;
		}
		else {
			LED_PORT = 0x00;
		}
			}
		return (0);
/* End event loop */
/* This line is never reached */
}
```

````
// ---------------
//   Pin Defines
// ---------------

#define LED_PORT                PORTB
#define LED_PIN                 PINB
#define LED_DDR                 DDRB

#define LED0                    PB0
#define LED1                    PB1
#define LED2                    PB2
#define LED3                    PB3
#define LED4                    PB4
#define LED5                    PB5
#define LED6                    PB6
#define LED7                    PB7

#define BUTTON_PORT             PORTD
#define BUTTON_PIN              PIND
#define BUTTON_DDR              DDRD

#define BUTTON                  PD2
#define BUTTON2                 PD3
#define BUTTON3                 PD4

#define SPEAKER                 PD6                            /* OC0A */
#define SPEAKER_PORT            PORTD
#define SPEAKER_PIN             PIND
#define SPEAKER_DDR             DDRD

#define ANTENNA                 PD5                            /* OC0B */
#define ANTENNA_PORT            PORTD
#define ANTENNA_PIN             PIND
#define ANTENNA_DDR             DDRD

#define MODULATION              PD3                            /* OC2B */
#define MODULATION_PORT         PORTD
#define MODULATION_PIN          PIND
#define MODULATION_DDR          DDRD

#define LIGHT_SENSOR            PC0                            /* ADC0 */
#define LIGHT_SENSOR_PORT       PORTC
#define LIGHT_SENSOR_PIN        PINC
#define LIGHT_SENSOR_DDR        DDRC

#define CAP_SENSOR              PC1                            /* ADC1 */
#define CAP_SENSOR_PORT         PORTC
#define CAP_SENSOR_PIN          PINC
#define CAP_SENSOR_DDR          DDRC

#define PIEZO                   PC2                            /* ADC2 */
#define PIEZO_PORT              PORTC
#define PIEZO_PIN               PINC
#define PIEZO_DDR               DDRC

#define POT                     PC3                            /* ADC3 */
#define POT_PORT                PORTC
#define POT_PIN                 PINC
#define POT_DDR                 DDRC

//  SPI and I2C serial mode defines

#define SPI_SS                     PB2
#define SPI_SS_PORT                PORTB
#define SPI_SS_PIN                 PINB
#define SPI_SS_DDR                 DDRB

#define SPI_MOSI                     PB3
#define SPI_MOSI_PORT                PORTB
#define SPI_MOSI_PIN                 PINB
#define SPI_MOSI_DDR                 DDRB

#define SPI_MISO                     PB4
#define SPI_MISO_PORT                PORTB
#define SPI_MISO_PIN                 PINB
#define SPI_MISO_DDR                 DDRB

#define SPI_SCK                     PB5
#define SPI_SCK_PORT                PORTB
#define SPI_SCK_PIN                 PINB
#define SPI_SCK_DDR                 DDRB

#define I2C_SDA                     PC4
#define I2C_SDA_PORT                PORTC
#define I2C_SDA_PIN                 PINC
#define I2C_SDA_DDR                 DDRC

#define I2C_SCL                     PC5
#define I2C_SCL_PORT                PORTC
#define I2C_SCL_PIN                 PINC
#define I2C_SCL_DDR                 DDRC

## Analog Interfacing

- `ADSC` set one to start the conversion
```c
ADCSRA = 1 << ADSC;
````

### References

1.  “Make: AVR Programming by Elliot Williams (MAKE). Copyright 2014 Elliot Williams, 978-1-4493-5578-4.”
