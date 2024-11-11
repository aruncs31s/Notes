---
aliases: 
Date: 03-11-2024
---
# pySDR

## Modulations 

### BPSK 

^c938fb

```python
"""
- Simulate BPSK modulation and demodulation using python
- Eb/Nb Vs BER  over AWGN Channel
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

debug = False
# Specify the number of symbels to transmit
numSymbols = 1000
# Specify the Eb/No in dB for simulation
EbN0dBs = np.arange(-2, 10, 2)

print(f"EbN0dBs {EbN0dBs}")

# Number of points in BPSK
M = 2

# Simulated BER Values
BER_sim = np.zeros(len(EbN0dBs))

m = np.arange(0, M)  # all possible input symbols

# print(f"Value of m {m}")
A = 1
# amplitude
constellation = A * np.cos(m / M * 2 * np.pi)  # reference constellation for BPSK

print(f"Constelation {constellation}")

#### Transmitter Side
inputSyms = np.random.randint(0, M, numSymbols)  # generate random 1's and 0's

s = constellation[inputSyms]  # modulate the input symbols
# print(s)

fig, ax = plt.subplots(1, 1)
ax.plot(
    np.real(constellation),
    np.imag(constellation),
    "bo",
    label="Reference Constellation",
)
# plt.show()


#### Channel
# Add AWGN noise
for j, EbN0dB in enumerate(EbN0dBs):
    # print(j)
    # print(EbN0dB)
    gammma = 10 ** (EbN0dB / 10)  # Convert SNR to linear scale ?
    P = sum(abs(s) ** 2) / len(s)  # Calculate the average power
    # print(P)
    N0 = P / gammma  # noise spectral density ?
    n = np.sqrt(N0 / 2) * np.random.standard_normal(s.shape)  # Computed Noise vector
    r = s + n  # received signal
    if debug == True:
        print(r)

    # if debug == True:
    #     plt.plot(np.real(r), np.imag(r), "ro", label="Received Signal")
    #     plt.show()

    #### Receiver Side
    detectedSyms = r <= 0  # Convert symbols to true or false
    detectedSyms = detectedSyms.astype(int)  # map True or False to 1 and 0
    BER_sim[j] = np.sum(detectedSyms != inputSyms) / numSymbols  # Calculate BER


BER_theory = 0.5 * erfc(np.sqrt(10 ** (EbN0dBs / 10)))
print(BER_theory)
fig, ax = plt.subplots(1, 1)
ax.semilogy(EbN0dBs, BER_sim, color="r", marker="o", linestyle="", label="BPSK Sim")
ax.semilogy(EbN0dBs, BER_theory, marker="", linestyle="-", label="BPSK Theory")
ax.set_xlabel("$E_b/N_0(dB)$")
ax.set_ylabel("BER ($P_b$)")
ax.set_title("Probability of Bit Error for BPSK over AWGN channel")
ax.set_xlim(-5, 13)
ax.grid(True)
ax.legend()
plt.show()
```

