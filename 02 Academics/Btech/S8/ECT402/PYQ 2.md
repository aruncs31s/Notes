---
id: PYQ_2
aliases: []
tags:
  - academics
  - btech
  - s8
  - ect402
dg-publish: true
---
# PYQ 2

## Questions
1. Define Grade Of Service (GOS) and Trunking.
2. What are the standards used for implementing Wireless Personnel Area Network (WPAN)?
3. Find the Fraunhofer distance for an antenna with maximum dimension of one meter and operating frequency of 900MHz. What is the significance of Fraunhofer distance?
4. What is meant by coherence bandwidth of the channel? Define coherence bandwidth in terms of rms delay spread of the channel.
5. What is the total bandwidth required for multi carrier modulation implementation with non-overlapping subchannels?
6. What is Peak-to-Average Power-Ratio (PAPR) in OFDM system? How can it be reduced?

---

## Ans 

### 1.  Grade Of Service (GOS)

> [!info]- Short Answer
> **GOS:** Probability of call blocking/delay due to insufficient resources. Lower GOS = better quality.
> **Trunking:** Dynamic channel sharing among multiple users from a common pool for efficient resource utilization.

- **Definition:** Measure of quality in telecommunications[^1].
- **Key Point:** Probability of a call being blocked or delayed due to insufficient resources.
- **Indicator:** Lower GOS = better quality (fewer blocked calls or delays).

**Grade of Service (GOS):**
Grade of Service (GOS) is a measure used in telecommunications to describe the quality of service provided to users. It is defined as the probability of a call being blocked or delayed due to insufficient resources (e.g., bandwidth[^2], channels) at the time of the call. A lower GOS indicates a better quality of service, as it means that users are less likely to experience blocked calls or delays.

---

#### Trunking
- **Definition:** Efficient channel utilization in telecommunications.
- **Key Point:** Multiple users share a pool of channels, dynamically allocated as needed.
- **Benefit:** Optimizes resource usage and improves system capacity, especially with bursty or unpredictable traffic.

**Trunking:**
Trunking is a method used in telecommunications to efficiently utilize communication channels by allowing multiple users to share a smaller number of channels. In a trunked system, a pool of channels is dynamically allocated to users as needed, rather than assigning a dedicated channel to each user. This approach helps to optimize resource usage and can improve overall system capacity, especially in environments with bursty or unpredictable traffic patterns.

---

### 2. WPAN Standards

> [!info]- Short Answer
> Main WPAN standards: **Bluetooth** (IEEE 802.15.1), **ZigBee** (IEEE 802.15.4), **Infrared** (IrDA), and **Ultra-Wideband** (UWB) for short-range wireless communication.

- **IEEE 802.15.1 (Bluetooth):**
  - Most widely used WPAN[^3] standard for short-range wireless communication.
  - Supports voice, data, and multimedia transmission between devices.
- **IEEE 802.15.4 (ZigBee):**
  - Designed for low-power, low-data-rate applications such as sensor networks and home automation.
  - Provides secure networking and supports mesh topology[^4].
- **Infrared (IrDA[^5]):**
  - Uses infrared light for short-range, point-to-point communication.
  - Common in remote controls and some legacy devices.
- **Ultra-Wideband (UWB[^6]):**
  - Offers high data rates over short distances.
  - Used for precise location tracking and multimedia streaming.

**Summary:**
WPAN standards include Bluetooth (IEEE 802.15.1), ZigBee (IEEE 802.15.4), Infrared (IrDA), and Ultra-Wideband (UWB). These standards enable short-range wireless communication between devices, each suited for specific applications such as data transfer, automation, and location tracking.

---
### 3. Fraunhofer Distance

> [!info]- Short Answer
> **Formula:** $d_f = \frac{2D^2}{\lambda}$ = $\frac{2(1)^2}{1/3}$ = **6 meters**
> **Significance:** Boundary between near-field and far-field regions; beyond this distance, antenna radiation pattern becomes stable.

- **Formula:**
  $$
  d_f = \frac{2D^2}{\lambda}
  $$
  where:
  - $d_f$ = Fraunhofer distance
  - $D$ = maximum dimension of the antenna
  - $\lambda$ = wavelength of the operating frequency

- **Calculation:**
  - Given:
    - $D = 1$ meter
    - Frequency $f = 900$ MHz $= 900 \times 10^6$ Hz
    - Speed of light $c = 3 \times 10^8$ m/s
    - Wavelength $\lambda = \frac{c}{f} = \frac{3 \times 10^8}{900 \times 10^6} = \frac{1}{3}$ meters
    - Fraunhofer distance:
      $$
      d_f = \frac{2 \times (1)^2}{\frac{1}{3}} = 2 \times 3 = 6 \, \text{meters}
      $$

- **Significance:**
  - The Fraunhofer distance marks the boundary between the near-field[^7] and far-field[^8] regions of an antenna.
  - Beyond this distance, the antenna's radiation pattern becomes stable and predictable.

---

### 4. Coherence Bandwidth

> [!info]- Short Answer
> **Definition:** Range of frequencies over which channel appears "flat" (non-selective fading).
> **Formula:** $B_c \approx \frac{1}{5\tau_{rms}}$ - inversely related to RMS delay spread.

- **Definition:**
  - Coherence bandwidth ($B_c$) is a statistical measure of the range of frequencies over which the channel can be considered "flat" or non-selective[^9], meaning all frequency components experience similar fading[^10].
  - It indicates the maximum frequency separation over which two signals will experience correlated or similar channel effects.

- **Relation to RMS Delay Spread:**
  - Coherence bandwidth is inversely related to the root mean square (rms) delay spread[^11] ($\tau_{rms}$) of the channel.
  - A smaller delay spread results in a larger coherence bandwidth, and vice versa.

- **Formula:**
  $$
  B_c \approx \frac{1}{5\tau_{rms}}
  $$
  where:
  - $B_c$ = coherence bandwidth
  - $\tau_{rms}$ = rms delay spread of the channel

- **Significance:**
  - If the signal bandwidth is less than the coherence bandwidth, the channel is considered flat fading[^12] (frequency non-selective).
  - If the signal bandwidth exceeds the coherence bandwidth, the channel exhibits frequency-selective fading[^13].

---

### 5. Total Bandwidth for Multi-Carrier Modulation (Non-Overlapping Subchannels)

> [!info]- Short Answer
> **Formula:** $B_{total} = N \times B_{sub}$
> Total bandwidth = Number of subchannels × Bandwidth per subchannel (plus guard bands)

- **Definition:**
  - Multi-carrier modulation divides the available spectrum into multiple non-overlapping subchannels, each carrying a portion of the data.
  - Each subchannel operates at a different frequency with its own bandwidth.

- **Total Bandwidth Calculation:**
  - For N non-overlapping subchannels, each with bandwidth $B_{sub}$:
  $$
  B_{total} = N \times B_{sub}
  $$
  where:
  - $B_{total}$ = total bandwidth required
  - $N$ = number of subchannels
  - $B_{sub}$ = bandwidth of each subchannel

- **Key Characteristics:**
  - **Guard Bands[^14]:** Additional bandwidth may be required between subchannels to prevent interference.
  - **Spectral Efficiency:** Lower than overlapping schemes (like OFDM[^15]) due to guard bands.
  - **Simplicity:** Easier implementation compared to overlapping subcarrier systems.

- **Example:**
  - If 4 subchannels each require 10 kHz bandwidth:
  - Total bandwidth = 4 × 10 kHz = 40 kHz (plus guard bands)

- **Applications:**
  - Frequency Division Multiple Access (FDMA[^16])
  - Traditional multi-carrier systems
  - Satellite communication systems

---

### 6. Peak-to-Average Power-Ratio (PAPR) in OFDM System

> [!info]- Short Answer
> **PAPR:** Ratio of peak instantaneous power to average power in OFDM signals. High PAPR causes amplifier saturation and distortion.
> **Reduction Methods:** Clipping, coding, tone reservation, active constellation extension, partial transmit sequences.

> [!note]- Deep Explanation
> **What is PAPR?**
> - **Average Power**: Like steady power consumption of a light bulb
> - **Peak Power**: Like sudden power surge when turning on a microwave
> - **PAPR**: Ratio between these - how much power "spikes" compared to normal
> 
> **The OFDM Problem:**
> - OFDM combines many subcarriers (sine waves) simultaneously
> - When sine waves align constructively → very high amplitude spikes
> - When they align destructively → low amplitudes
> - **Worst case**: N subcarriers can create PAPR of N:1 (e.g., 64 subcarriers = 18 dB PAPR)
> 
> **Why High PAPR is Bad:**
> - **Power Amplifier Limits**: Amplifiers have "linear region" - peaks exceed this → distortion
> - **Like pouring gallon through cup-sized funnel** - doesn't work properly
> - **Real consequences**: Signal corruption, interference, wasted power, expensive components
> 
> **Reduction Techniques Explained:**
> - **Clipping**: Cut off peaks (simple but introduces distortion)
> - **PTS**: Try different phase rotations, pick lowest PAPR version
> - **SLM**: Create multiple signal versions, select best one
> - **Tone Reservation**: Reserve subcarriers for "anti-peak" signals
> - **Active Constellation**: Allow constellation points to move outward to reduce peaks
> 
> **Real-World Impact:**
> - WiFi example: Without PAPR reduction need 100W amplifier for 10W average
> - With 6dB PAPR reduction: Only need 25W amplifier → 75% power savings
> - **Critical for**: Battery life, heat management, cost-effective infrastructure

![[Recording 20250920212700.m4a]]

![PAPR](https://youtu.be/F4LAZTdm_b8?si=f5KhHxuIQfKPerK7)

- **Definition:**
  - PAPR[^17] is the ratio of the peak instantaneous power to the average power of an OFDM signal.
  - It represents how much the signal power varies from its average value.

- **Mathematical Expression:**
  $$
  PAPR = \frac{P_{peak}}{P_{average}} = \frac{\max|x(t)|^2}{E[|x(t)|^2]}
  $$

  where:
  - $P_{peak}$ = peak instantaneous power
  - $P_{average}$ = average power
  - $x(t)$ = OFDM signal in time domain
  - $E[\cdot]$ = expectation operator

- **Problems Caused by High PAPR:**
  - **Amplifier Saturation:** Power amplifiers[^18] operate in non-linear region
  - **Signal Distortion:** Clipping and intermodulation distortion
  - **Spectral Regrowth:** Out-of-band emissions
  - **Reduced Efficiency:** Lower power amplifier efficiency
  - **Increased Cost:** Need for high-dynamic-range components

- **PAPR Reduction Techniques:**

  **1. Signal Distortion Techniques:**
  - **Clipping[^19]:** Limit signal amplitude to threshold value
  - **Peak Windowing:** Apply window function to reduce peaks
  - **Companding:** Compress large signals, expand small signals

  **2. Coding Techniques:**
  - **Block Coding:** Use error-correcting codes to avoid high-PAPR sequences
  - **Complementary Sequences:** Use sequences with low autocorrelation

  **3. Multiple Signal Representation:**
  - **Partial Transmit Sequences (PTS[^20]):** Partition data into sub-blocks with different phase rotations
  - **Selected Mapping (SLM[^21]):** Generate multiple candidate signals and select lowest PAPR
  - **Interleaving:** Rearrange data to reduce peak correlation

  **4. Probabilistic Techniques:**
  - **Tone Reservation[^22]:** Reserve some subcarriers for PAPR reduction
  - **Active Constellation Extension[^23]:** Extend constellation points to reduce peaks
  - **Tone Injection:** Add specific tones to cancel peaks

- **Trade-offs:**
  - **Complexity vs Performance:** More sophisticated methods offer better PAPR reduction but higher complexity
  - **Data Rate vs PAPR:** Some methods reduce data rate (overhead) for PAPR reduction
  - **BER vs PAPR:** Signal distortion methods may increase bit error rate

---

## Footnotes

[^1]: **Telecommunications**: Communication over a distance by cable, telegraph, telephone, or broadcasting
[^2]: **Bandwidth**: The range of frequencies within a given band that can carry a signal
[^3]: **WPAN**: Wireless Personal Area Network - network for interconnecting devices centered on an individual person's workspace
[^4]: **Mesh Topology**: Network topology where each node connects to several others, creating multiple paths for data
[^5]: **IrDA**: Infrared Data Association - set of protocols for infrared communications
[^6]: **UWB**: Ultra-Wideband - radio technology for short-range, high-bandwidth communications
[^7]: **Near-field**: Region close to antenna where electromagnetic field behavior is complex and distance-dependent
[^8]: **Far-field**: Region far from antenna where electromagnetic waves behave as plane waves
[^9]: **Non-selective**: Channel that affects all frequency components equally (flat frequency response)
[^10]: **Fading**: Variation in signal amplitude/phase due to multipath propagation
[^11]: **RMS Delay Spread**: Statistical measure of multipath delay spread in wireless channels
[^12]: **Flat Fading**: Fading that affects all frequency components of signal equally
[^13]: **Frequency-selective Fading**: Fading that affects different frequency components differently
[^14]: **Guard Bands**: Unused frequency bands that separate communication channels to prevent interference
[^15]: **OFDM**: Orthogonal Frequency Division Multiplexing - method of encoding digital data on multiple carrier frequencies
[^16]: **FDMA**: Frequency Division Multiple Access - channel access method where users are assigned different frequency bands
[^17]: **PAPR**: Peak-to-Average Power Ratio - measure of power variation in communication signals
[^18]: **Power Amplifiers**: Electronic devices that increase the power of a signal while preserving its waveform
[^19]: **Clipping**: Signal processing technique that limits signal amplitude to prevent saturation
[^20]: **PTS**: Partial Transmit Sequences - PAPR reduction technique using phase rotation of data sub-blocks
[^21]: **SLM**: Selected Mapping - technique that generates multiple signal representations and selects the best one
[^22]: **Tone Reservation**: Method reserving specific subcarriers exclusively for PAPR reduction
[^23]: **Active Constellation Extension**: Technique that extends constellation points outward to reduce signal peaks