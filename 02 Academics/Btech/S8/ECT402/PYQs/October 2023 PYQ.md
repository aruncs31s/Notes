# October 2023 PYQ Answers

## 1. Compare and contrast the analog and digital cellular systems

**Analog Cellular Systems (e.g., AMPS):**
- Use analog modulation techniques for voice transmission
- Lower spectral efficiency and capacity
- Prone to interference and eavesdropping
- Simpler technology and lower cost
- Limited to voice services

**Digital Cellular Systems (e.g., GSM, CDMA):**
- Use digital modulation and processing
- Higher spectral efficiency and capacity
- Better security and privacy
- Support data services and advanced features
- More complex but offer better performance

## 2. What are the methods adopted for hand-off procedures?

The main hand-off methods are:

1. **Hard Hand-off:** The connection to the current cell is broken before establishing connection with the new cell. Used in GSM.

2. **Soft Hand-off:** The mobile maintains connection with multiple cells simultaneously during transition. Used in CDMA.

3. **Softer Hand-off:** A type of soft hand-off where the mobile connects to multiple sectors of the same cell site.

## 3. How does fading occur? Derive the expression for doppler shift.

**Fading Occurrence:**
Fading occurs due to multipath propagation where signals arrive at the receiver via multiple paths with different delays, amplitudes, and phases. This causes constructive and destructive interference, leading to variations in signal strength.

**Doppler Shift Derivation:**
When a mobile moves with velocity v towards a transmitter, the frequency appears higher. The relative velocity component is v cosθ, where θ is the angle between velocity vector and line of sight.

The Doppler shift frequency is:
f_d = (v/c) f cosθ

Where:
- v = mobile velocity
- c = speed of light
- f = carrier frequency
- θ = angle between velocity and line of sight

## 4. Power and Voltage Calculation

Given:
- P_t = 50 W
- d = 10 km = 10000 m
- f = 900 MHz = 9 × 10^8 Hz
- G_t = 1
- G_r = 2

First, wavelength λ = c/f = 3 × 10^8 / 9 × 10^8 = 0.333 m

Using Friis transmission equation:
P_r = P_t G_t G_r (λ/(4πd))^2

P_r = 50 × 1 × 2 × (0.333/(4 × 3.1416 × 10000))^2
P_r = 100 × (0.333/125663.7)^2
P_r = 100 × (2.65 × 10^-6)^2
P_r = 100 × 7.02 × 10^-12
P_r = 7.02 × 10^-10 W = 0.702 nW

RMS voltage across 50 Ω resistor:
V_rms = √(P_r × R) = √(7.02 × 10^-10 × 50) = √(3.51 × 10^-8) = 1.87 × 10^-4 V

## 5. How is the outage probability computed for a wireless channel?

Outage probability is the probability that the received signal quality falls below an acceptable threshold.

For a Rayleigh fading channel, the outage probability is:
P_out = 1 - exp(-γ_th / γ_avg)

Where:
- γ_th = threshold SNR
- γ_avg = average SNR

This represents the probability that the instantaneous SNR γ < γ_th.

## 6. Explain the significance of using cyclic prefix in an OFDM system

The cyclic prefix (CP) is a guard interval added to each OFDM symbol to combat inter-symbol interference (ISI).

**Significance:**
- Converts linear convolution into circular convolution
- Eliminates ISI in multipath channels
- Allows simple frequency domain equalization
- Trades bandwidth efficiency for robustness against delay spread

## 7. Differentiate between microdiversity and macrodiversity

**Microdiversity:**
- Combines signals from multiple antennas at the same location
- Mitigates small-scale fading effects
- Implemented at base station or mobile unit
- Examples: MRC, selection diversity

**Macrodiversity:**
- Combines signals from different cell sites
- Mitigates shadowing and large-scale fading
- Requires coordination between base stations
- Used in soft hand-off procedures

## 8. Compare pros and cons of linear equalizer over non-linear equalizer

**Linear Equalizer:**
*Pros:*
- Simpler implementation
- Lower computational complexity
- No distortion amplification
- Stable convergence

*Cons:*
- Limited performance in nonlinear channels
- Cannot handle phase distortions
- May not compensate for severe ISI

**Non-linear Equalizer:**
*Pros:*
- Better performance in nonlinear channels
- Can handle phase and amplitude distortions
- More robust to severe channel conditions

*Cons:*
- Higher computational complexity
- Potential for error propagation
- May introduce additional distortion

## 9. Deduce the expression for critical frequency of an ionised region

The critical frequency f_c is the maximum frequency that can be reflected by an ionized layer.

For a parabolic electron density profile, the critical frequency is:
f_c = 9 √N_max kHz

Where N_max is the maximum electron density in electrons/m³.

**Derivation:**
The refractive index μ = √(1 - (f_p/f)^2), where f_p = plasma frequency.

For reflection, μ = 0 when f = f_p.

f_p = (1/(2π)) √(N e²/(ε₀ m))

Critical frequency f_c = f_p_max = (1/(2π)) √(N_max e²/(ε₀ m))

Substituting constants: f_c ≈ 9 √N_max kHz (for N_max in 10^6 electrons/m³)

## 10. Explain the mechanism of wave bending (refraction) in the ionosphere

When a high-frequency (HF) radio wave enters the ionosphere, it encounters a medium whose refractive index varies with altitude due to changing electron density. Instead of reflecting abruptly like from a metallic surface, the wave is gradually refracted (bent) back toward the Earth. When the bending is sufficient that the ray returns to the ground, we term it (loosely) as having been "reflected" by the ionosphere.

### 10.1 Basic Mechanism (Gradual Refraction)
1. Electron density N(h) increases with height (up to a peak) in an ionospheric layer (e.g., E, F1, F2).
2. The plasma (Appleton) refractive index (neglecting Earth's magnetic field and collisions for simplicity) is:
	n = √(1 - (f_p^2 / f^2)) ,  where  f_p = 9√N   (f_p in Hz if N in electrons/m³ / 10^6)
3. As the wave penetrates to regions of higher N, f_p increases, so (f_p/f) increases and n decreases.
4. By Snell's law for a stratified medium:  n(h) sin θ(h) = constant = n_0 sin θ_0 . As n decreases with altitude, sin θ must increase, causing θ (the angle from the normal) to increase; hence the ray bends away from the normal (toward the Earth surface direction).
5. At some altitude h_c, θ → 90° (wave becomes horizontal). Beyond that point propagation upward would require sin θ > 1 (impossible), so the energy is returned downward.

### 10.2 Critical Frequency and Vertical Incidence
For vertical incidence (θ_0 = 0 ⇒ sin θ_0 = 0), Snell's law does not invoke angular bending; the wave penetrates until n → 0. The condition n = 0 gives f = f_p(max) = f_c (critical frequency) for that layer. Thus vertically incident waves with f > f_c pass through the layer into higher regions of the ionosphere / space; those with f < f_c are returned.

### 10.3 Oblique Incidence and Maximum Usable Frequency (MUF)
For an oblique path of range D with reflection from a layer of maximum electron density N_max (critical frequency f_c):
MUF ≈ f_c / cos θ_i  (secant law)
where θ_i is the angle of incidence at the equivalent flat layer (from the normal). Higher MUF allows longer skip distances for the same layer.

### 10.4 Skip Distance
The skip distance is the minimum ground range from the transmitter at which a sky wave of a given frequency returns to Earth on its first hop. For frequencies just below MUF, the virtual reflection height is high and the ray returns far away, creating a "skip zone" (no coverage) between the end of ground wave and the first sky wave return point.

### 10.5 Simplified ASCII Ray Diagram

Transmitter (Tx) at left, ionospheric layer with increasing N upward, ray bending progressively:

```
	 Ionosphere (electron density ↑ with height)
		  N ↑
		  |                 . (turning point where θ=90°)
		  |              .'
		  |           .'
		  |        .'
		  |     .'
		  |  .'
---------'----------------------------------  (Approx lower boundary of layer)
	Tx  / )  Upward ray enters layer
		/  )  θ increases as n decreases
	  /  )
	 /  )  Ray becomes horizontal then returns
```

### 10.6 Key Relations Summary
1. Refractive index (simplified): n ≈ √(1 - (f_p/f)^2)
2. Plasma (critical) frequency: f_p = (1/2π) √(N e^2 / (ε_0 m_e)) ≈ 9√N   (Hz, N in electrons/m³ / 10^6)
3. Snell's law in stratified ionosphere: n(h) sin θ(h) = constant
4. Critical frequency (vertical incidence): f_c = f_p(max)
5. MUF (single hop, flat layer approximation): MUF ≈ f_c / cos θ_i

### 10.7 Factors Affecting Bending
- Time of day (solar ionization increases daytime electron density)
- Solar activity (sunspots enhance N_max → higher f_c and MUF)
- Season and latitude (affect recombination rates)
- Magnetic field and collisions (refine the index via full Appleton-Hartree equation)

### 10.8 Practical Significance
- Enables long-distance HF communication beyond the horizon
- Determines optimal operating frequency window: between Lowest Usable Frequency (LUF) and MUF
- Knowledge of bending guides frequency selection to avoid skip zones and maximize coverage

### 10.9 Distinction: Refraction vs True Reflection
Physically the process is continuous refraction due to gradient in electron density, but for engineering design it is often treated as a specular reflection at a "virtual height" to simplify path calculations.

## 11. (a) Features of GSM System Architecture (with block diagram)

GSM (Global System for Mobile Communications) architecture is divided into subsystems that separate radio access, switching, subscriber data, and operations. Core features include digital TDMA structure, SIM-based authentication, hierarchical cell planning, roaming, and standardized interfaces.

### Major Subsystems
1. MS (Mobile Station): Mobile Equipment (ME) + SIM (Subscriber Identity Module) storing IMSI, Ki, and user data.
2. BSS (Base Station Subsystem): Provides radio interface.
	 - BTS (Base Transceiver Station): RF transceivers, handles channel coding, modulation.
	 - BSC (Base Station Controller): Manages radio resources, handovers within BSS, power control, frequency hopping.
3. NSS / Core Network (Network Switching Subsystem): Switching and subscriber management.
	 - MSC (Mobile Switching Centre): Call control, mobility management, interworking to PSTN/ISDN.
	 - HLR (Home Location Register): Permanent subscriber profiles, service data.
	 - VLR (Visitor Location Register): Temporary location and service data for roaming subscribers.
	 - AuC (Authentication Center): Generates triplets (RAND, SRES, Kc).
	 - EIR (Equipment Identity Register): Lists valid/invalid IMEI equipment.
4. OSS (Operations Support System): Network management, performance, configuration, alarms.

### Supporting Interfaces
- Um: Air interface (MS ↔ BTS)
- Abis: BTS ↔ BSC (often over E1/T1 with LAPD signaling)
- A: BSC ↔ MSC
- MAP over SS7: Signaling for HLR/VLR/AuC database transactions

### Key Features Summary
- Digital TDMA (8 time slots per 200 kHz carrier)
- Frequency reuse with planned cluster sizes
- Support for voice, SMS, low-rate data (CSD, GPRS extension later)
- SIM-based portability & security (A3/A8 algorithms)
- Mobility management: location updating, handover (intra-BTS, inter-BTS, inter-MSC)
- Power control & discontinuous transmission (DTX) for battery and interference management
- Encryption on air interface (A5 family)

### Simplified ASCII Block Diagram
```
	[ MS ]
		|
	 Um
		|
	[ BTS ] -- Abis -- [ BSC ] -- A -- [ MSC ] -- PSTN/ISDN
																	|
																MAP (SS7)
						------------------------------
						|      |       |       |     |
					[HLR]  [VLR]   [AuC]   [EIR]  [OSS]
```

### Functional Flow (Call Origination Example)
1. MS sends channel request on RACH (random access). 
2. BTS relays request; BSC assigns SDCCH.
3. Authentication & ciphering via HLR/AuC (SRES, Kc).
4. MSC performs call setup (ISUP if PSTN destination).
5. Traffic channel (TCH) allocated; handovers managed by BSC/MSC as user moves.

### Security & Mobility Highlights
- TMSI used instead of IMSI over air to preserve anonymity.
- Location areas reduce signaling load via periodic updates.
- Handover criteria: Rx level/quality, timing advance, BTS load.

## 11. (b) Cell Splitting and Sectoring for Capacity & Coverage Improvement

Both techniques are interference management strategies that increase capacity without new spectrum by improving frequency reuse efficiency.

### Cell Splitting
Divides a congested large cell into several smaller cells with reduced radius (R → R/2 etc.). Each smaller cell uses lower transmit power to maintain cluster interference constraints.

#### Effects
1. Increased capacity: More cells → more channels reused within same geographic area.
2. Higher handover rate: Users traverse more cell boundaries.
3. Power and antenna height reduction required to limit coverage footprint.
4. Smaller cells better match traffic hotspots (microcells, picocells).

#### Capacity Scaling (Idealized)
Channel reuse count ∝ Number of cells. If radius reduced by factor a (a>1), area per cell scales as 1/a², so theoretical capacity gain ≈ a² (ignoring edge effects and guard channels).

### Sectoring
Replaces an omnidirectional cell antenna with multiple directional antennas (e.g., 3 sectors of 120°, or 6 sectors of 60°). Each sector acts like a smaller cell in azimuth, reducing co-channel interference by narrowing beam patterns.

#### Benefits
1. Improves carrier-to-interference ratio (C/I) enabling smaller cluster size N.
2. Increases capacity: If cluster size drops from N_old to N_new, capacity gain ≈ N_old / N_new.
3. Lower interference improves quality and data rates.

#### Trade-offs
- Additional hardware: Multiple antennas, feeders, combiners.
- More complex planning: Sector ID, neighbor lists.
- Potential for increased handovers at sector boundaries.

### Combined Approach
Often applied together: split overloaded cells and sector each daughter cell for finer interference control and incremental capacity gains.

### Illustrative ASCII Diagrams
Cell Splitting (one macrocell → 4 microcells):
```
	 _______
	/       \          After splitting:
 /         \        __________   __________
 \         /       /          \ /          \
	\_______/       /            X            \
									\__________/ \__________/
```

Sectoring (120° sectors):
```
		/\
	 /  \   (Each wedge = separate sector)
	/____\
	\    /
	 \  /
		\/
```

### Quantitative Example
Suppose original cluster size N=7 with omni cells. After 3-sectoring, improved C/I permits N=4. Capacity gain ≈ 7/4 ≈ 1.75× (75% increase) for same spectrum. Further splitting reducing radius by 1.5 adds ≈ 1.5² = 2.25×; combined ≈ 1.75 × 2.25 ≈ 3.94× theoretical (practical lower due to overhead).

### Key Distinctions
| Aspect | Cell Splitting | Sectoring |
|--------|----------------|-----------|
| Goal | Increase channel count by more cells | Improve C/I enabling lower reuse factor |
| Method | Physically add new BTS sites (smaller radius) | Replace omni antenna with directional panels |
| Impact on Handovers | Increases inter-cell handovers | Adds intra-site (inter-sector) handovers |
| CapEx | High (sites, backhaul) | Moderate (antennas, RF) |
| Primary Limitation | Site acquisition, interference planning | Diminishing returns beyond 6 sectors |


## 12. (a) Channel Assignment Strategies in Cellular Systems

Efficient allocation of limited radio channels among cells is critical to maximize capacity while minimizing interference and blocking probability. Three principal strategies are used:

### 1. Fixed Channel Assignment (FCA)
- Each cell is allocated a predetermined, disjoint set of voice/data channels based on frequency reuse plan.
- If all channels in a cell are occupied, additional call attempts are blocked (unless borrowing allowed).
- Simplicity: low real-time computational load.
- Drawback: Traffic imbalance (hotspot cells block while neighboring cells have idle channels).

### 2. Channel Borrowing Variants (FCA with Borrowing)
- A congested cell temporarily borrows channels from adjacent cells’ unused pools while maintaining interference constraints (co-channel / adjacent channel spacing rules).
- Policies: Selective borrowing, directed retry, guard channel concept.
- Requires real-time coordination and interference checking to avoid degradation.

### 3. Dynamic Channel Assignment (DCA)
- Channels are not permanently allocated; they are assigned on demand from a central or distributed pool.
- Selection criteria consider: co-channel distance, interference measurements, traffic statistics, reuse constraints.
- Benefits: Adapts to spatial/temporal traffic variation → lower blocking probability for same spectrum.
- Costs: Higher signaling overhead, complexity, need for rapid measurements of channel quality.

### 4. Hybrid or Hierarchical Schemes
- Combine FCA for a core subset (stability) with DCA for overflow/hotspot traffic.
- Hierarchical cell structures (macro / micro / pico tiers): allocate frequency layers; higher mobility users prefer macro layer to reduce handovers.

### 5. Trunking & Guard Channel Concepts
- Guard channels reserved for high-priority (e.g., handoff) calls reduce forced termination probability.
- Trunking efficiency: Larger aggregated pools lower blocking per Erlang-B.

### 6. Interference & Reuse Considerations
- Reuse factor determined by cluster size N (e.g., N = 7, 4, 3) subject to required carrier-to-interference ratio (C/I).
- DCA can opportunistically use channels that would be idle under FCA if instantaneous interference is below threshold.

### Comparison Snapshot
| Strategy | Complexity | Adapts to Traffic | Blocking (Hotspots) | Interference Control |
|----------|------------|-------------------|---------------------|----------------------|
| FCA | Low | Poor | High | Deterministic (planned) |
| FCA + Borrowing | Moderate | Moderate | Reduced | Needs coordination |
| DCA | High | Excellent | Lowest | Measurement-driven |
| Hybrid | Moderate-High | Good | Low | Mixed (plan + adapt) |

## 12. (b) Features of 4G Wireless Networks

Fourth Generation (4G) systems (e.g., LTE / LTE-Advanced, WiMAX evolution) introduced an all-IP, high-throughput, low-latency architecture supporting seamless mobility and broadband multimedia.

### Key Architectural & Design Features
- All-IP Packet Switched Core: Elimination of circuit-switched domain; IMS for voice (VoIP/VoLTE).
- Flat Architecture: Fewer network elements (eNB directly to EPC) → lower latency & cost.
- OFDMA (Downlink) & SC-FDMA (Uplink in LTE): High spectral efficiency, flexible bandwidth allocation (1.4–20 MHz, carrier aggregation up to 100 MHz+ in LTE-A).
- MIMO & Advanced Antenna Techniques: Spatial multiplexing, beamforming, MU-MIMO.
- Carrier Aggregation: Combines fragmented spectrum blocks for higher peak rates.
- Adaptive Modulation & Coding (QPSK, 16QAM, 64QAM, 256QAM in later releases).
- Flexible Frame Structure: Subframes (1 ms) enabling low latency scheduling & HARQ.

### Performance Targets (Approximate ITU-R IMT-Advanced / LTE-A)
- Peak Downlink > 1 Gbps (stationary / low mobility); early LTE ~100 Mbps.
- Peak Uplink hundreds of Mbps (e.g., 500 Mbps in advanced configs).
- User-plane latency ~ <10 ms; control-plane setup latency reduction.
- Spectral efficiency improvements vs 3G (3–5× per Hz typical in loaded conditions).

### QoS & Mobility Enhancements
- QoS bearers with dedicated Guaranteed Bit Rate (GBR) and non-GBR flows.
- Seamless handovers: Intra-LTE (X2) and inter-RAT (to 3G/2G Wi-Fi) with minimal interruption.
- Fast Idle to Active transitions (DRX for power saving).

### Security & Management
- Mutual authentication (USIM/Aka), integrity protection, ciphering (e.g., AES-based algorithms in later releases).
- Simplified key hierarchy (KASME, KeNB, etc.).
- Self-Organizing Networks (SON): Automatic configuration, optimization, healing.

### IP Multimedia & Services
- VoLTE for voice with QoS guarantee.
- Rich Communication Services (RCS), video streaming, gaming, telemedicine.
- Multicast/Broadcast: eMBMS for efficient content distribution.

### Energy & Spectrum Efficiency
- Sleep modes (micro-sleep at subframe level), eICIC/ICIC for interference coordination in heterogeneous networks (macro + small cells).
- Heterogeneous Networks (HetNets): Pico, femto, relay nodes extend coverage/capacity.

### Evolutionary Extensions
- LTE-Advanced Pro features: LAA (Licensed Assisted Access), Massive MIMO precoding, higher-order carrier aggregation, enhanced CoMP.
- Smooth migration path to 5G NR leveraging existing EPC.

### Comparative Advantages Over 3G
| Aspect | 3G (WCDMA/HSPA) | 4G (LTE / LTE-A) |
|--------|------------------|------------------|
| Core | Mixed circuit & packet | All-IP (EPC + IMS) |
| Access | Wideband CDMA | OFDMA/SC-FDMA + MIMO |
| Peak DL Rate | ~14–42 Mbps (HSPA+) | 100 Mbps – 1 Gbps+ |
| Latency | 50–100 ms | <10 ms user-plane |
| Spectral Efficiency | Lower | Higher (flexible scheduling) |
| Voice | Circuit / CSFB / early VoIP | VoLTE native |
| Interference Mgmt | Soft handoff, power control | ICIC, eICIC, CoMP |

### Practical Impact
- Enabled smartphone broadband ecosystem, streaming media, cloud services.
- Provided scalable platform for IoT (narrowband adaptations later like LTE-M, NB-IoT).


