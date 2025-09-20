---
id: BPSK_Implementation
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: "07-04-25"
dg-publish: true
---
# BPSK Implementation

## Transmitter
**BPSK** *Transmitter* Flow Graph Include mainly consist of the following
1. **File Source** : for File processing processing 
> it sends preamble first , then data, file name , `#EOF` 
>[!NOTE] File Processing
> File processing is in the sense that , it is a embedded python block, it reads data for example if you have a file 
> ```message.txt
> hi im arun 
> hi im arun
>```

>then , the the EPB(Embedded Python Block) will first read the say 10Bytes "hi im arun" , then transmits it , under the hood , it first sends a preamble like %UUUU] , then the data("hi im arun") then a post filter "#EOF" for marking it is the end of file . 

2. **Stream CRC32** : It computes the 32 bit checksum for the data 
3. **Protocol Formater** : adds a header with acccess code 
4. **Tagged Stream MUX** : multiplex it to gether (combines header and payload)
5. **Constellation Modulator** : modulate to the constellations $-S(t)\cos \omega t$ and $-S(t) \cos \omega t$
   > sps: 4 
   > dif_encoding: true 
   > excess_bw:  0.35
6. **FFT Filter** :  It is used to shape the signal spectrum
7. **Fractional Resambler** :  It is used to resample the signal to get the desired sampling rate , 48K to 768k
8. **Pluto Sink** :  It is used to transmit the signal 
![[Pasted Image 20250405210642_732.png]]

## Receiver
**BPSK** *Receiver* Flow Graph Include mainly consist of the following
1.  **Pluto Source** :  It is used to receive the signal 
2. **AGC** : used to automaticaly adjust the gain
3. **FLL Band Edge** : carrier frequency synchronization
4. **Symbol Sync** : symbol timing reecovery
5. **Costas Loop** : phase recovery
6. **BPSK Demodulator**
7. **Diff Decoder**
8. **Detect Access Code**
9. **Repack Bits** 1 ->  8 because the *demodulation* happens at bit level in **gnu radio**
>- **Before repacking**: [0x01, 0x00, 0x01, 0x01, 0x00, 0x00, 0x01, 0x00] (8 bytes representing 8 bits)
>- **After repacking**: [0x5A] (1 byte containing all 8 bits: 01011010 in binary)
1. **Stream CRC** : Check the CRC 
> expects byte-aligned data to properly verify the checksum
11.  **File Sink** :  It is used to save the data 

![[Pasted Image 20250405210826_055.png]]

