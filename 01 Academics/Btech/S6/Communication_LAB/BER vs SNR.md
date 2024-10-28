### Signal-to-Noise Ratio (SNR)

**Definition:**

- SNR is a measure of the strength of the desired signal compared to the background noise. It is usually expressed in decibels (dB).

**Formula:** 

$$
SNR (linear)=\frac{Psignal}{Pnoise} {SNR (linear)} = \frac{P_{\text{signal}}}{P_{\text{noise}}}SNR (linear)=Pnoise​Psignal​​ SNR (dB)=10log⁡10(PsignalPnoise)\text{SNR (dB)} = 10 \log_{10} \left( \frac{P_{\text{signal}}}{P_{\text{noise}}} \right)SNR (dB)=10log10​(Pnoise​Psignal​​)
$$
where:

- PsignalP_{\text{signal}}Psignal​ is the power of the signal.
- PnoiseP_{\text{noise}}Pnoise​ is the power of the noise.

**Interpretation:**

- A higher SNR indicates a clearer and stronger signal relative to the noise, leading to better communication quality.
- SNR is a key parameter that affects the performance of a communication system, including the BER.

### Bit Error Rate (BER)

**Definition:**

- BER is a measure of the number of bit errors in a transmitted message over a communication channel. It is the ratio of the number of erroneous bits to the total number of transmitted bits.

**Formula:** BER=NerrorsNtotal bits\text{BER} = \frac{N_{\text{errors}}}{N_{\text{total bits}}}BER=Ntotal bits​Nerrors​​

where:

- NerrorsN_{\text{errors}}Nerrors​ is the number of bit errors.
- Ntotal bitsN_{\text{total bits}}Ntotal bits​ is the total number of transmitted bits.

**Interpretation:**

- A lower BER indicates fewer errors in the received data, leading to better communication reliability and accuracy.
- BER is directly influenced by the SNR; as SNR increases, the BER typically decreases.