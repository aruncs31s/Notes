---
id: Binary_Phase_Shift_Keying
aliases: []
tags:
  - academics
  - btech
  - s6
  - communication_lab
  - part_a
  - experiment_2
dg-publish: true
---
# Binary Phase Shift Keying
Created : 2024-04-29 09:32

## Contents

#### Theory
In binary phase shift keying, the binary symbols 1 and 0 modulate the phase of the carrier. Let the carrier signal for transmitting the binary symbol ‘1’ be $s_1(t)=A \cos(2\pi f_ct)$. For the transmission of
symbol ‘0’, phase of the carrier is shifted by an amount of 180° (p radians). So $s_2 (t) = -A \cos(2\pi f_ct)$ = $A \cos(2\pi f_ct + \pi)$. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From the above equations, BPSK signal can be defined as $s(t) = b(t) A \cos(2\pi f_ct)$, where $b(t) = +1$ to transmit symbol ‘1’ and $b(t) = –1$ to transmit symbol ‘0’.

**Modulator** : This circuit mainly consists of a unity gain op-amp inverting amplifier and two switches.Inverting amplifier provides 180° phase-shift to carrier signal s(t). The binary symbols are applied to the control inputs of two switches. An op-amp inverting Zero Crossing Detector (ZCD) enables to apply symbol ‘1’ at the control input of one switch while ‘0’ at the control input of the other switch. BPSK signal has constant amplitude as in the case of BFSK signal. Therefore, the noise can be removed easily.

**Demodulator** : BPSK signal can be demodulated non-coherently by converting it to BASK signal and then by using an envelope detector. The original carrier is added with BPSK signal using a summing amplifier to obtain BASK signal. BASK[^1] signal is further demodulated using an envelope detector. The output of the envelope detector may not be square-shaped. Therefore, the demodulated signal is converted to a square-shaped signal with the help of a comparator

[^1]: BASK (Binary Amplitude Shift Keying) is a modulation scheme where the amplitude of the carrier signal is varied to represent binary data.
---

## References
1. 