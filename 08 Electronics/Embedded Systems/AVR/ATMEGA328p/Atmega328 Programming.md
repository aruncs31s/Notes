---
id: Atmega328_Programming
aliases: []
tags:
  - electronics
  - embedded_systems
  - avr
  - atmega328p
Date: 
Created: 14-12-2024
cssClasses: wide-page
dg-publish: true
---
## Communication Protocol 

### SPI 

**Initializing SPI as Master**
[Source](http://www.rjhcoding.com/avrc-spi.php)

```c
#define SPI_DDR DDRB
#define CS      PINB2
#define MOSI    PINB3
#define MISO    PINB4
#define SCK     PINB5

void SPI_init()
{
    // set CS, MOSI and SCK to output
    SPI_DDR |= (1 << CS) | (1 << MOSI) | (1 << SCK);

    // enable SPI, set as master, and clock to fosc/128
    SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR1) | (1 << SPR0);
}

```

```c
SPI_DDR |= (1 << CS) | (1 << MOSI) | (1 << SCK);

```

Expanded Form 

```c
DDRB |= (1 << PINB2) | (1 << PINB3) | (1 << PINB5);

```

- **DDRB** is used to enable output 
- 