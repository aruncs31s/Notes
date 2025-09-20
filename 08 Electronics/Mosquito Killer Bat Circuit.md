---
id: Mosquito Killer Bat Circuit
aliases: []
tags:
  - electronics
Date: "28-11-2024"
dg-publish: true
---
# Mosquito Killer Bat Circuit

The Mosquito killer bat uses a single 4V battery to achieve really high output voltage , it is an inverter which uses a high frequency(~44Khz) transformer to conver 4 V to ? 600V ?
![[mosquitobat.excalidraw|900x200]]

## Circuit

| Spec            | Value        |
| --------------- | ------------ |
| Operating Freq. | 100 - 200Khz |
| Input Voltage   | $4V$         |
| Output Voltage  | $~600$       |

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidZEAC0OsRH64Ld8EJKDaUJGzZlyA8rGwsxqPQdZstKnDHSAyqbxYon84mq2D6Ac-Ty1f070vXSBWeMxOHnamzSygAVVamEHRVhglB9yFNMv664whEQA6QZqy3HJ5fXz9yhwc2gKxk9Fcq/s1600/mosquito+killer+bat+internal+circuit.jpg)

### Schematics

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzUIvLs6LjSOoyPPKakqTQmv9mA9HZHS4oj3NL97pf9BlI6bJ4ejV7RONG5mSyzj8Zb7qhdZ593jSin1r7j49_kirVr0cNErqYJoB-qLV7RaKRZaWhtrlSnnYWuYApGbZOtOtJGUanQMIw/s1600/mosquito+killer+bat+circuit.jpg)

## Working

1. **Oscillators** : Oscillator converts the DC to a pulsating AC
2. **Transformer** : Transformer Step ups the voltage
3. **Ladder Network** : It is used to boost the output voltage from the transformer

## References

1. Circuit Diagram , Schematics -> [Source](https://www.etechnog.com/2018/12/mosquito-killer-bat-circuit-diagram-and.html)
