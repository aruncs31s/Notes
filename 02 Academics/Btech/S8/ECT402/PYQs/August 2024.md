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

**Answer:**
| Generation | Approx Era | Core Services | Access / Air Interface | Peak/User Data Rate (order) | Key Technology Enablers | Limitations Driving Next Gen |
|------------|------------|---------------|------------------------|-----------------------------|-------------------------|------------------------------|
| 2G (GSM/IS-95) | ~1991–2000 | Circuit voice + low-rate SMS/data (GPRS/EDGE) | TDMA/FDMA (GSM), CDMA (IS-95) | Tens–100 kbps (EDGE ~200 kbps) | Digital modulation, SIM-based auth, basic encryption, frequency reuse optimization | Limited data throughput; circuit-switched core |
| 3G (UMTS/CDMA2000) | ~2001–2010 | Voice + packet data + multimedia (video calls) | W-CDMA / CDMA2000 | Few Mbps (HSPA+ peak ~10–40 Mbps) | Wideband spreading, soft handoff, improved spectral efficiency, core packet integration | Still moderate latency; fragmented enhancements |
| 4G (LTE) | ~2009–2020 | All-IP broadband: high-rate data, VoIP, streaming HD | OFDMA (DL), SC-FDMA (UL), MIMO | 100+ Mbps (LTE-A: 1 Gbps peak) | Orthogonal subcarriers, scalable bandwidth, MIMO spatial multiplexing, carrier aggregation, flat IP core (EPC) | Capacity/latency constraints for massive devices & URLLC |
| 5G (NR) | 2019– | Enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency (URLLC), Massive mMTC | OFDM-based flexible numerology (sub-6 GHz + mmWave), massive MIMO, beamforming | Multi-Gbps (mmWave), <1 ms air latency target | Network slicing, SDN/NFV virtualization, edge computing (MEC), dynamic TTI, massive MIMO beam steering, DSS | Deployment complexity, backhaul demand, energy efficiency, security scaling |
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
## 14. (a) Impulse Response Model of a Multipath Channel (7 Marks)
**Answer:** A wide-sense stationary uncorrelated scattering (WSSUS) baseband channel with L discrete resolvable paths is modeled as
$$ h(t,\tau) = \sum_{l=1}^{L} \alpha_l(t) \, \delta(\tau - \tau_l) $$
where: \(\tau_l\) = excess delay of path l, \(\alpha_l(t)= a_l e^{j\phi_l(t)}\) complex gain (amplitude fading + phase), and \(\delta(\cdot)\) Dirac delta. For time-varying Doppler shifts \(f_{D,l}\):
$$ \alpha_l(t) = a_l e^{j(2\pi f_{D,l} t + \phi_{0,l})} $$
The received baseband signal (ignoring noise) for input \(s(t)\):
$$ r(t) = \int h(t,\tau) s(t-\tau) d\tau = \sum_{l=1}^{L} \alpha_l(t) s(t-\tau_l) $$
If paths form a continuum, impulse response becomes stochastic process:
$$ h(t,\tau) = \sum_k \alpha_k(t) \delta(\tau - \tau_k) \;\Rightarrow\; R_h(t; \Delta t, \Delta \tau) = E[h(t,\tau) h^*(t+\Delta t, \tau+\Delta \tau)] $$
WSSUS assumption: uncorrelated for distinct delays →
$$ R_h(\Delta t, \tau) = P_h(\tau) R_t(\Delta t) $$
with power delay profile (PDP) \(P_h(\tau) = E[|h(t,\tau)|^2]\). Transfer function (time-varying frequency response):
$$ H(t,f) = \int h(t,\tau) e^{-j2\pi f\tau} d\tau = \sum_{l=1}^{L} \alpha_l(t) e^{-j2\pi f \tau_l} $$
**Short Answer:** Discrete multipath channel: \(h(t,\tau)=\sum_l \alpha_l(t)\delta(\tau-\tau_l)\); output is sum of time-varying scaled, delayed replicas of input.

---
## 14. (b) Flat vs Frequency-Selective Fading (4 Marks)
**Answer:**
| Aspect | Flat Fading | Frequency-Selective Fading |
|--------|-------------|-----------------------------|
| Relation of signal BW (B_s) to coherence bandwidth (B_c) | \(B_s \ll B_c\) | \(B_s > B_c\) |
| Channel effect | Single complex gain multiplies entire signal | Different subbands experience different gains (amplitude/phase distortion) |
| ISI Presence | Negligible (symbol duration >> delay spread) | Significant ISI (delay spread comparable to / larger than symbol time) |
| Equalization Need | Simple (one-tap) or none | Requires multi-tap equalizer or multicarrier (OFDM) |
| Diversity Opportunity | Limited frequency diversity | Exploitable frequency diversity across subcarriers |
| BER Variation | All frequencies fade together | Some frequencies deep fade, others strong |
| Mitigation | Power control, time/frequency interleaving | OFDM + coding + adaptive bit loading, RAKE/DFE |
**Short Answer:** Flat fading = bandwidth narrower than channel coherence → uniform gain, no ISI; frequency-selective = signal spans multiple fading taps → distortion + ISI, requiring equalization/multicarrier.

---
## 14. (c) Coherence Time Calculation (3 Marks)
**Answer:** Given velocity v = 50 m/s, carrier f_c = 1800 MHz. Wavelength: \(\lambda = c/f_c = 3\times10^8 / 1.8\times10^9 = 0.1667\,\text{m}\). Maximum Doppler shift: \(f_D = v/\lambda = 50 / 0.1667 \approx 300\,\text{Hz}\). Approximate coherence time (common empirical): \(T_c \approx \frac{1}{2 f_D} = \frac{1}{600} \approx 1.67\,\text{ms}\). (Alternate Jakes form \(0.423/f_D \approx 1.41\,\text{ms}\); either acceptable if stated.)
**Short Answer:** \(f_D \approx 300\,\text{Hz}\); \(T_c \approx 1.4\text{–}1.7\,\text{ms}\) depending on formula used.

---
## 15. (a) Average BER of BPSK in Rayleigh Flat Fading (8 Marks)
**Answer:** Conditional BER of coherent BPSK over AWGN at instantaneous SNR \(\gamma\): \(P_b(\gamma) = Q(\sqrt{2\gamma})\). For Rayleigh flat fading (slow or symbol-rate variation) with average SNR \(\bar{\gamma}\), the PDF: \(f_\gamma(\gamma) = \frac{1}{\bar{\gamma}} e^{-\gamma/\bar{\gamma}}\). Average BER:
$$ \bar{P_b} = \int_0^{\infty} Q(\sqrt{2\gamma}) \frac{1}{\bar{\gamma}} e^{-\gamma/\bar{\gamma}} d\gamma $$
Closed form identity: \( \int_0^{\infty} Q(\sqrt{a x}) e^{-b x} dx = \frac{1}{2b} \left(1 - \sqrt{\frac{b}{b+a/2}}\right) \) with \(a=2, b=1/\bar{\gamma}\). Thus:
$$ \bar{P_b} = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}}\right) = \frac{1}{2}\left(1 - \sqrt{\frac{\text{SNR}_{avg}}{1+\text{SNR}_{avg}}}\right) $$
Applies when symbol duration ≥ channel coherence time (independent fading per symbol) or slow enough that each symbol sees quasi-static gain but interleaving spans many fades.
**Short Answer:** \(\bar{P_b} = \tfrac{1}{2}\left(1 - \sqrt{\bar{\gamma}/(1+\bar{\gamma})}\right)\).

---
## 15. (b) Required Average SNR for BER < 10^{-4} with 95% Reliability (— Marks)
**Answer:** Target: BER threshold \(P_b^{th} = 10^{-4}\). From 15(a): \(\bar{P_b}(\bar{\gamma}) = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}}\right)\). Solve for \(\bar{\gamma}\) meeting \(\bar{P_b} = 10^{-4}\):
Set \(1 - \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}} = 2\times10^{-4} \Rightarrow \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}} = 1 - 2\times10^{-4} = 0.9998\).
Square: \(\frac{\bar{\gamma}}{1+\bar{\gamma}} = 0.9996 \Rightarrow \bar{\gamma} = 0.9996(1+\bar{\gamma}) \Rightarrow \bar{\gamma} - 0.9996 \bar{\gamma} = 0.9996 \Rightarrow 0.0004 \bar{\gamma} = 0.9996 \Rightarrow \bar{\gamma} = 2499 \approx 2.5\times10^{3}\).
In dB: \(10 \log_{10}(2499) \approx 34.0\,\text{dB}\).

However requirement adds 95% reliability: Probability that average BER < 10^{-4} should be ≥0.95. In quasi-static (slow) fading, instantaneous SNR \(\gamma\) is exponential with mean \(\bar{\gamma}\). Condition \(P_b(\gamma) = Q(\sqrt{2\gamma}) < 10^{-4}\) roughly needs instantaneous \(\gamma \gtrsim 8.4\) dB (since AWGN BPSK BER 10^{-4} ≈ Q(√(2γ)) ⇒ √(2γ) ≈ Q^{-1}(10^{-4}) ≈ 3.719 ⇒ γ ≈ (3.719^2)/2 ≈ 6.92 ≈ 8.4 dB when accounting for approximation). Using threshold \(\gamma_{th} \approx 7\) dB (≈5 in linear) to 8 dB for margin.

Reliability constraint: \(P\{\gamma > \gamma_{th}\} = e^{-\gamma_{th}/\bar{\gamma}} \ge 0.95 \Rightarrow e^{-\gamma_{th}/\bar{\gamma}} \ge 0.95 \Rightarrow \bar{\gamma} \ge \gamma_{th} / (-\ln 0.95) \).
Take \(\gamma_{th} = 6.9\) (linear) (≈ 8.4 dB):
\(-\ln 0.95 = 0.051293\) ⇒ \(\bar{\gamma} \ge 6.9 / 0.051293 ≈ 134.6\) (≈ 21.3 dB).

Conservative design uses higher of two computations: 34 dB (from average BER formula) vs 21 dB (from reliability of instantaneous threshold). Because average BER formula already integrates fading, the 34 dB solution ensures \(\bar{P_b}\le 10^{-4}\) unconditionally; 95% reliability of instantaneous criterion alone underestimates requirement.

**Result:** Required average SNR ≈ 34 dB (linear ≈ 2.5×10^3) to achieve average BER < 10^{-4}. Reliability note: If instead interpreting “95% of time BER < 10^{-4}” under instantaneous AWGN mapping, ~21 dB would suffice, but strict average target dictates ~34 dB.
**Short Answer:** \(\bar{\gamma} \approx 2.5\times10^{3}\) (≈34 dB) for \(\bar{P_b}<10^{-4}\); 95% instantaneous criterion alone would give ≈21 dB.

---