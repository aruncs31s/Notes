# PYQ 2

## Questions
1. Define Grade Of Service (GOS) and Trunking.
2. What are the standards used for implementing Wireless Personnel Area Network (WPAN)?
3. Find the Fraunhofer distance for an antenna with maximum dimension of one meter and operating frequency of 900MHz. What is the significance of Fraunhofer distance?
4. What is meant by coherence bandwidth of the channel? Define coherence bandwidth in terms of rms delay spread of the channel.
---

## Ans 

### Grade Of Service (GOS)
- **Definition:** Measure of quality in telecommunications.
- **Key Point:** Probability of a call being blocked or delayed due to insufficient resources.
- **Indicator:** Lower GOS = better quality (fewer blocked calls or delays).

**Grade of Service (GOS):**
Grade of Service (GOS) is a measure used in telecommunications to describe the quality of service provided to users. It is defined as the probability of a call being blocked or delayed due to insufficient resources (e.g., bandwidth, channels) at the time of the call. A lower GOS indicates a better quality of service, as it means that users are less likely to experience blocked calls or delays.

---

### Trunking
- **Definition:** Efficient channel utilization in telecommunications.
- **Key Point:** Multiple users share a pool of channels, dynamically allocated as needed.
- **Benefit:** Optimizes resource usage and improves system capacity, especially with bursty or unpredictable traffic.

**Trunking:**
Trunking is a method used in telecommunications to efficiently utilize communication channels by allowing multiple users to share a smaller number of channels. In a trunked system, a pool of channels is dynamically allocated to users as needed, rather than assigning a dedicated channel to each user. This approach helps to optimize resource usage and can improve overall system capacity, especially in environments with bursty or unpredictable traffic patterns.

---

### WPAN Standards
- **IEEE 802.15.1 (Bluetooth):**
  - Most widely used WPAN standard for short-range wireless communication.
  - Supports voice, data, and multimedia transmission between devices.
- **IEEE 802.15.4 (ZigBee):**
  - Designed for low-power, low-data-rate applications such as sensor networks and home automation.
  - Provides secure networking and supports mesh topology.
- **Infrared (IrDA):**
  - Uses infrared light for short-range, point-to-point communication.
  - Common in remote controls and some legacy devices.
- **Ultra-Wideband (UWB):**
  - Offers high data rates over short distances.
  - Used for precise location tracking and multimedia streaming.

**Summary:**
WPAN standards include Bluetooth (IEEE 802.15.1), ZigBee (IEEE 802.15.4), Infrared (IrDA), and Ultra-Wideband (UWB). These standards enable short-range wireless communication between devices, each suited for specific applications such as data transfer, automation, and location tracking.

---
### Fraunhofer Distance
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
  - The Fraunhofer distance marks the boundary between the near-field and far-field regions of an antenna.
  - Beyond this distance, the antenna's radiation pattern becomes stable and predictable.

---

### Coherence Bandwidth
- **Definition:**
  - Coherence bandwidth ($B_c$) is a statistical measure of the range of frequencies over which the channel can be considered "flat" or non-selective, meaning all frequency components experience similar fading.
  - It indicates the maximum frequency separation over which two signals will experience correlated or similar channel effects.

- **Relation to RMS Delay Spread:**
  - Coherence bandwidth is inversely related to the root mean square (rms) delay spread ($\tau_{rms}$) of the channel.
  - A smaller delay spread results in a larger coherence bandwidth, and vice versa.

- **Formula:**
  $$
  B_c \approx \frac{1}{5\tau_{rms}}
  $$
  where:
  - $B_c$ = coherence bandwidth
  - $\tau_{rms}$ = rms delay spread of the channel

- **Significance:**
  - If the signal bandwidth is less than the coherence bandwidth, the channel is considered flat fading (frequency non-selective).
  - If the signal bandwidth exceeds the coherence bandwidth, the channel exhibits frequency-selective fading.

