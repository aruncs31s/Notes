---
aliases: 
Date: "07-04-25"
---
# BPSK Implementation

## Transmitter
**BPSK** *Transmitter* Flow Graph Include mainly consist of the following
1. **File Source** : for packet processing 
> it sends preamble first , then data, file name , `#EOF` 
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
9. **Repack Bits** 1 ->  8
10. **Stream CRC** : Check the CRC 
11.  **File Sink** :  It is used to save the data 

![[Pasted Image 20250405210826_055.png]]