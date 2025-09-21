1 Determine the number of channels per cluster and the total channel capacity for a 
cellular telephone area composed of 10 clusters with seven cells in each cluster 
and 10 channels in each cell.
(3)
Answer: Channels per cluster = 7 cells × 10 channels = 70. Total physical channels deployed in the entire service area = 70 × 10 clusters = 700 channel positions (frequencies/time-slots). Only 70 are unique (reused 10 times). Capacity gain arises from spatial reuse.
2 What is cell splitting? How does it improve system performance? (3)
Answer: Cell splitting subdivides an overloaded large cell into smaller micro/mini cells using lower antenna heights and reduced transmit power, shrinking reuse distance so channels can be reassigned more frequently. Benefits: increases capacity (more Erlangs/km²), reduces call blocking, lowers handset transmit power, improves SINR through reduced path loss. Trade-offs: more handoffs, higher infrastructure and planning cost.
3 What is fading? List various types of small scale fading. (3)
Answer: Fading is rapid fluctuation of the amplitude/phase (or envelope/SNR) of a received signal due to multipath propagation and/or Doppler from motion. Small-scale fading classifications: (a) Frequency perspective: flat vs frequency-selective; (b) Time perspective: fast vs slow; (c) Statistical envelope models: Rayleigh, Rician, Nakagami-m, Weibull; (d) Mechanism descriptors: multipath (delay spread) vs Doppler (time selectivity) induced.
4 A transmitter radiates a sinusoidal carrier frequency of 3GHz. For a vehicle 
moving at a speed of 72Kmph, compute the received frequency if the mobile is 
moving 
i) Directly towards the transmitter 
ii) Directly away from the transmitter 
(3)
Answer: Speed v = 72 km/h = 20 m/s. Wavelength λ = c/f = 3×10^8 / 3×10^9 = 0.1 m. Maximum Doppler shift f_D = v/λ = 20 / 0.1 = 200 Hz. (i) Towards: f_r = 3 000 000 000 + 200 = 3 000 000 200 Hz. (ii) Away: f_r = 3 000 000 000 − 200 = 2 999 999 800 Hz.
5 Describe cyclic prefix. Why is cyclic prefix required in OFDM? (3)
Answer: The cyclic prefix (CP) copies the last L_CP samples of an OFDM symbol and prepends them as a guard interval. If L_CP ≥ channel delay spread (L_h−1), the linear convolution becomes circular, preserving subcarrier orthogonality after FFT. Functions: (1) Eliminates ISI between consecutive OFDM symbols; (2) Converts frequency-selective channel into per-subcarrier complex gain; (3) Provides tolerance to timing offset. Cost: reduces spectral/energy efficiency by overhead fraction L_CP/(N + L_CP).
6 Define average error probability and outage probability. (3)
Answer: Average error probability: P_e,avg = E[ P_e(γ) ] = ∫ P_e(γ) f_γ(γ) dγ over the fading SNR PDF—gives long-term BER/SER performance. Outage probability: P_out = Pr{γ < γ_th} (or capacity C < C_req) = F_γ(γ_th); it measures the fraction of time the link fails a minimum QoS (SNR/rate) requirement.
7 Describe the selection combining technique used in diversity receivers. (3)
Answer: Selection Combining (SC) monitors L diversity branches (antennas/frequencies) and selects the one with the highest instantaneous SNR (or envelope). Output SNR = max(γ_1,...,γ_L). For i.i.d. Rayleigh fading with mean γ̄: P_out(γ_th) = [1 − e^{−γ_th/γ̄}]^L. Pros: simplest RF chain after selection, low power. Cons: Lower performance than MRC (loses cumulative SNR), requires branch SNR measurement and fast switching.
8 Define equalization in the context of digital communication systems. Differentiate 
between linear and nonlinear equalization techniques.
(3)
Answer: Equalization mitigates intersymbol interference (ISI) introduced by a band-limited/multipath channel by approximating or adapting the inverse channel response. Linear equalizers (ZF, MMSE) apply a linear FIR/IIR filter: simple, fixed latency, but ZF amplifies noise in spectral nulls; MMSE trades residual ISI vs noise enhancement. Nonlinear equalizers (Decision Feedback Equalizer, MLSE/Viterbi) use previous symbol decisions or sequence estimation: better performance in severe ISI, reduced noise enhancement, but higher complexity and possible error propagation (DFE) or exponential state growth (MLSE).
9 What are the advantages and limitations of ground wave propagation for longdistance communication?
(3)
Answer: Advantages: follows earth’s curvature enabling beyond-line-of-sight at LF/MF (<2–3 MHz); relatively stable over time; useful for maritime & navigation; diffraction aids coverage behind obstacles. Limitations: high attenuation over poor-conductivity ground; efficiency drops sharply with frequency (not viable at VHF+); large antennas required (λ-scale); limited bandwidth/data rate; susceptible to man‑made noise at low frequencies.
10 Define critical frequency and maximum usable frequency and establish the 
relation between them. 
(3)
Answer: Critical frequency f_c of an ionospheric layer: highest frequency that will be reflected (returned to Earth) for vertical incidence; f_c (MHz) ≈ 9 √(N_max) where N_max is peak electron density (electrons/m³ ×10^{-12}). Maximum Usable Frequency (MUF) for an oblique path with incidence angle θ relative to the normal: MUF = f_c / cos θ = f_c sec θ. Thus MUF ≥ f_c; larger hop distances (shallower incidence) increase MUF.
## 1. Channel capacity per cluster & total system capacity (3 Marks)
**Answer:** Channels per cluster = 7 cells × 10 channels = 70. Total deployed channel instances = 70 × 10 clusters = 700 (only 70 unique reused 10×). Spatial reuse multiplies capacity without extra spectrum.

---
## 2. Cell splitting & performance improvement (3 Marks)
**Answer:** Divides a large congested cell into smaller low-power cells reducing reuse distance so frequencies are reassigned more often. Benefits: higher capacity (more Erlangs/km²), lower blocking, improved SINR, reduced handset Tx power. Trade-offs: more handoffs, higher site/backhaul/optimization cost.

---
## 3. Fading definition & small-scale types (3 Marks)
**Answer:** Rapid amplitude/phase fluctuation from multipath + motion/Doppler. Types: Flat vs frequency-selective; Fast vs slow; Statistical (Rayleigh, Rician, Nakagami-m); Mechanistic (delay-spread / Doppler dominated). 

---
## 4. Doppler shift at 3 GHz for 72 km/h (3 Marks)
**Answer:** v = 72 km/h = 20 m/s; λ = 0.1 m; f_D = v/λ = 200 Hz. Received: Towards ≈ 3 000 000 200 Hz; Away ≈ 2 999 999 800 Hz.

---
## 5. Cyclic prefix role in OFDM (3 Marks)
**Answer:** CP copies last L_CP samples to front making linear channel convolution circular if CP ≥ max delay spread. Eliminates ISI, preserves subcarrier orthogonality enabling one-tap equalization; adds overhead L_CP/(N+L_CP).

---
## 6. Average error probability vs outage probability (3 Marks)
**Answer:** Average error probability: expectation of conditional error over SNR PDF (long-term BER/SER). Outage probability: P{γ < γ_th} (or capacity < target)—fraction of time QoS unmet.

---
## 7. Selection Combining diversity (3 Marks)
**Answer:** Picks branch with max instantaneous SNR: γ_out = max(γ_i). Rayleigh outage: P_out = [1 - e^{-γ_th/γ̄}]^L. Pros: simple/low power. Cons: lower gain than MRC; needs SNR measurement & switch.

---
## 8. Linear vs nonlinear equalization (3 Marks)
**Answer:** Equalization combats ISI by approximating inverse channel. Linear (ZF, MMSE): simpler, fixed latency; ZF noise enhancement, MMSE residual ISI tradeoff. Nonlinear (DFE, MLSE): better performance in severe ISI; costs complexity & potential error propagation (DFE) or exponential states (MLSE).

---
## 9. Ground wave propagation pros & limits (3 Marks)
**Answer:** Pros: beyond LOS via earth-following diffraction, reliable LF/MF coverage, maritime/navigation utility. Limits: strong attenuation over poor ground, inefficiency at higher f, large λ-scale antennas, narrow bandwidth, high noise susceptibility.

---
## 10. Critical frequency & MUF relation (3 Marks)
**Answer:** Critical frequency f_c ≈ 9√(N_max) (MHz). MUF for incidence angle θ: MUF = f_c / cos θ = f_c sec θ ≥ f_c. Shallower incidence (longer path) increases MUF.

---
## Part B (50 Marks)

## 11. (a) Evolution of Wireless Generations: 2G → 3G → 4G → 5G (8 Marks)
\n+## 11. (a) Evolution of Wireless Generations: 2G → 3G → 4G → 5G (8 Marks)
**Answer:**
| Generation | Approx Era | Core Services | Access / Air Interface | Peak/User Data Rate (order) | Key Technology Enablers | Limitations Driving Next Gen |
|------------|------------|---------------|------------------------|-----------------------------|-------------------------|------------------------------|
| 2G (GSM/IS-95) | ~1991–2000 | Circuit voice + low-rate SMS/data (GPRS/EDGE) | TDMA/FDMA (GSM), CDMA (IS-95) | Tens–100 kbps (EDGE ~200 kbps) | Digital modulation, SIM-based auth, basic encryption, frequency reuse optimization | Limited data throughput; circuit-switched core |
| 3G (UMTS/CDMA2000) | ~2001–2010 | Voice + packet data + multimedia (video calls) | W-CDMA / CDMA2000 | Few Mbps (HSPA+ peak ~10–40 Mbps) | Wideband spreading, soft handoff, improved spectral efficiency, core packet integration | Still moderate latency; fragmented enhancements |
| 4G (LTE) | ~2009–2020 | All-IP broadband: high-rate data, VoIP, streaming HD | OFDMA (DL), SC-FDMA (UL), MIMO | 100+ Mbps (LTE-A: 1 Gbps peak) | Orthogonal subcarriers, scalable bandwidth, MIMO spatial multiplexing, carrier aggregation, flat IP core (EPC) | Capacity/latency constraints for massive devices & URLLC |
| 5G (NR) | 2019– | Enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency (URLLC), Massive mMTC | OFDM-based flexible numerology (sub-6 GHz + mmWave), massive MIMO, beamforming | Multi-Gbps (mmWave), <1 ms air latency target | Network slicing, SDN/NFV virtualization, edge computing (MEC), dynamic TTI, massive MIMO beam steering, DSS | Deployment complexity, backhaul demand, energy efficiency, security scaling |

**Capabilities Progression:**
1. Shift from circuit-switched voice (2G) → packet-integrated (3G) → pure IP flat core (4G) → cloud-native, sliceable, service-based architecture (5G).
2. Spectral efficiency improvements via modulation + coding + MIMO + carrier aggregation.
3. Latency reduction: multi-100 ms (2G) → ~100 ms (3G) → ~<30 ms (4G user plane) → sub-10 ms (5G eMBB) → sub-1 ms (URLLC scenarios).
4. Device density scaling to support IoT (mMTC) in 5G.

**Short Answer:** 2G: digital voice/SMS; 3G: packet data & multimedia; 4G: all-IP broadband with OFDMA+MIMO; 5G: unified platform for eMBB, URLLC, mMTC using flexible numerology, massive MIMO, network slicing.

---
## 11. (b) Bluetooth in Personal Area Networks (PANs) (8 Marks)
**Answer:**
Bluetooth is a short-range wireless technology (typically 10 m for Class 2) designed for low-power personal area networking among devices (headsets, wearables, peripherals, IoT sensors). It complements higher-power WLAN (Wi‑Fi) and cellular by focusing on low energy consumption, simple pairing, and modest throughput.

**Main Roles in PAN Evolution:** Cable replacement (HID, audio), formation of ad hoc piconets, enabling body-area sensor networks, and supporting audio streaming (A2DP, LE Audio) and beaconing (BLE advertisements) for proximity services.

**Distinguishing Features:**
1. Frequency Band: 2.4 GHz ISM using frequency hopping spread spectrum (FHSS); LE uses adaptive channel selection among 40 channels (2 MHz spacing).
2. Topology: Piconet (1 master + up to 7 active slaves); scatternet by interconnecting piconets; BLE supports star & broadcast modes.
3. Power Classes: Multiple Tx power levels (Class 1 up to ~100 mW; Class 2 ~2.5 mW typical) enabling energy-efficient operation.
4. Low Energy (BLE): Optimized for very low duty cycle devices (years of battery life) via short connection events and advertising channels.
5. Profiles & Interoperability: Standardized profiles (HFP, A2DP, GATT) simplify multi-vendor ecosystem integration.
6. Security: Pairing modes (Just Works, Passkey, Numeric Comparison), AES-CCM link layer encryption.
7. Latency & Throughput: Classic BR/EDR up to ~3 Mbps raw; BLE 5 long-range (coded PHY) trades rate for robustness; direction finding (AoA/AoD) for positioning.
8. Coexistence: Adaptive hopping mitigates interference vs static channels used by Wi-Fi.

**Comparison vs Other Wireless:**
- Wi‑Fi: Higher throughput, higher power, infrastructure oriented; Bluetooth: lower power, simpler, PAN-focused.
- Zigbee: Mesh + ultra-low data rates; Bluetooth: broader device ecosystem and audio support.
- NFC: Very short range (cm) for secure tap; Bluetooth: meters-range sustained links.

**Short Answer:** Bluetooth enables low-power short-range device interconnection using frequency hopping and standardized profiles; BLE adds ultra-low energy modes and proximity services—differentiated from Wi‑Fi (throughput) and Zigbee (mesh, lower rate) by ecosystem breadth and audio/data versatility.

---
## 12. (a) Handoff Techniques & Seamless Mobility (8 Marks)
**Answer:**
Handoff (handover) transfers an ongoing call/data session from one cell/base station (BS) or channel to another to maintain link quality and continuity as a user moves or radio conditions change.

**Key Types:**
1. Hard Handoff (Break-Before-Make): Used in traditional GSM / early cellular. Connection to old BS is released before new one established. Simpler resource control but brief interruption; more noticeable at cell edges with rapid fading.
2. Soft Handoff (Make-Before-Break): In CDMA / some 3G systems; mobile simultaneously connected to multiple BSs (active set) combining signals (RAKE). Provides macro-diversity, smoother transitions, improves Eb/N0.
3. Softer Handoff: Between sectors of the same physical BS (different sector antennas). Combines at baseband internally; reduces backhaul signaling overhead vs inter-BS soft handoff.
4. Horizontal vs Vertical Handoff: Horizontal within same RAT (e.g., LTE cell to LTE cell); Vertical across different RATs (e.g., LTE → Wi‑Fi) for load balancing or coverage extension.
5. Intra-frequency vs Inter-frequency (or Inter-band) Handoff: Same carrier frequency vs different carriers—latter requires retuning and measurement gaps (e.g., LTE inter-frequency measurement events). 
6. Forced / Emergency Handoff: Triggered by rapid deterioration (e.g., power below threshold, interference spike) to prevent call drop.

**Trigger Metrics:** RSSI / RSRP, quality (C/I, SINR, RSRQ), timing advance, bit/block error rates, load conditions, predicted trajectory.

**Challenges Addressed & Mitigation:**
| Challenge | Impact | Technique Response |
|-----------|--------|--------------------|
| Rapid signal fluctuation (fading) | Premature or late handoff → drops/ping-pong | Hysteresis margins, time-to-trigger, filtering of measurements |
| Interference / edge SINR drop | Degraded QoS | Soft/softer handoff diversity gain; interference coordination (ICIC, eICIC) |
| High-speed mobility (Doppler) | Reduced channel coherence time | Adaptive measurement intervals, predictive mobility, fast HO signaling |
| Load imbalance | Congestion in popular cells | Load-aware / cell range expansion; vertical HO to Wi‑Fi/5G small cells |
| Heterogeneous layers (macro/pico/femto) | Coverage holes or ping-pong | Layer-specific thresholds and bias (cell selection offset) |
| Multi-RAT coexistence | Suboptimal user experience | Policy-based vertical handoff decision engines |

**Short Answer:** Hard HO breaks then makes; soft/softer HO maintain parallel links for diversity; vertical HO changes RAT; intelligent triggering (hysteresis, time-to-trigger, load-aware metrics) preserves seamless connectivity and reduces drops and ping-pong events.

---
## 12. (b) Optimal Cluster Size N and Reuse Factor Q (8 Marks)
**Question Restatement:** Digital TDMA system, required worst-case SIR ≥ 23 dB. Path loss exponent n = 4. Number of first-tier co-channel interferers i_0 = 6 (omnidirectional cells). Determine smallest cluster size N meeting SIR, then compute reuse factor Q.

**SIR Model (Co-Channel Interference, Equal Powers):**
For large distance ratio (D/R), approximate
$$ \text{SIR} \approx \frac{(D/R)^n}{i_0} $$
with \(n=4\), \(i_0=6\).

Let required linear SIR = \(\Gamma = 10^{23/10} = 10^{2.3} \approx 199.53\) (≈ 200).

Thus:
$$ \frac{(D/R)^4}{6} \ge 199.53 \;\Rightarrow\; (D/R)^4 \ge 1197.2 $$
$$ D/R \ge (1197.2)^{1/4} $$
Fourth root: \( (1197.2)^{1/2} \approx 34.60^{1/2} \approx 5.885\) (since \(34.60\) square root of 1197.2; refine: \(\sqrt{34.60}=5.885\)).

Reuse geometry for hexagonal cells: \( D/R = \sqrt{3N} \).
So:
$$ \sqrt{3N} \ge 5.885 \;\Rightarrow\; 3N \ge 34.64 \;\Rightarrow\; N \ge 11.55 $$

Cluster size N must be an integer of the form \(N = i^2 + ij + j^2\), where \(i,j\) integers. Candidate values near ≥ 11.55: 12, 13. Valid hex cluster numbers: 1,3,4,7,9,12,13,16,... Smallest ≥ 11.55 is 12.

Therefore choose \( N = 12 \).

Compute actual SIR check:
$$ D/R = \sqrt{3\times 12} = \sqrt{36} = 6 $$
$$ \text{SIR}_{linear} = \frac{6^4}{6} = \frac{1296}{6} = 216 $$
$$ \text{SIR}_{dB} = 10\log_{10}(216) \approx 23.35\,\text{dB} \ge 23\,\text{dB (meets)} $$

Reuse Factor / Reuse Ratio:
Often expressed as \(Q = D/R = 6\) for the selected cluster size.

**Results:** Minimum feasible cluster size \(N = 12\); reuse factor (distance ratio) \(Q = 6\); achieved SIR ≈ 23.35 dB (> 23 dB requirement).

**Short Answer:** \(N=12\), \(Q=6\), SIR ≈ 23.35 dB (meets 23 dB target).

---