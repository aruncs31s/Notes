# Voltage Standing Wave Ratio
It is a measure of how efficiently radio-frequency power is transmitted ==from a power source, through a transmission line, into a load== . For example from an power amplifier to antenna through a transmission line.
>[!blank|right-small]
>![](https://upload.wikimedia.org/wikipedia/commons/7/7d/Standing_wave_2.gif)
Incident wave (blue) is fully reflected (red wave) out of phase at short-circuited end of transmission line, creating a net voltage (black) standing wave. $\Gamma = −1, SWR = \infty$.

- The max transfer of power requires exact match between source impedance and load impedance.

$$
VSWR = \frac{1 + |\Gamma |}{1-|\Gamma|}
$$
- It indicates the degree of mismatch between the transmission line and the load
- A higher VSWR indicates more power is being reflected back towards the source, which can lead to inefficiencies and potential damage to the transmitter
>[!info] summary
>In just the measure of forward waveform amplitude and the reflected waveform amplitude.
## References
1. [Source 1](https://www.analog.com/en/resources/glossary/vswr.html#:~:text=VSWR%20(Voltage%20Standing%20Wave%20Ratio,line%2C%20to%20an%20antenna).)
2. [Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)
3. 