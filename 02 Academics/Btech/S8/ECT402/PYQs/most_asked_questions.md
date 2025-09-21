# ECT402 – Most Asked / High-Frequency Topics

This consolidated note extracts the most frequently recurring question themes across:
- `October 2023 PYQ.md`
- `May 2024.md`
- `PYQ 2.md`

It helps rapid revision by clustering overlapping conceptual areas that exams repeatedly target.

## Selection Criteria
Topics included if they appear (explicitly or implicitly) in ≥2 papers or form foundational building blocks referenced by multiple distinct questions (e.g., diversity, fading, capacity, multiple access, OFDM fundamentals).

## Top Recurring Themes & Linked Source Questions

| Theme | Core Idea / Focus | Source Question Links |
|-------|-------------------|------------------------|
| Frequency Reuse & Capacity | Reuse patterns, cluster size, capacity scaling | [[October 2023 PYQ#11. (b) Cell Splitting and Sectoring for Capacity & Coverage Improvement]] · [[May 2024.md#1. Frequency reuse (3 Marks)|May 2024 Q1]] · [[May 2024.md#11. (a) Capacity with 4-cell reuse (60 MHz total) (3 Marks)|May 2024 Q11a]] |
| Cell Splitting & Sectoring | Capacity enhancement & interference control | [[October 2023 PYQ#11. (b) Cell Splitting and Sectoring for Capacity & Coverage Improvement]] · [[May 2024.md#11. (a) Capacity with 4-cell reuse (60 MHz total) (3 Marks)]] |
| Trunking & Grade of Service | Erlang B/C, blocking probability | [[October 2023 PYQ#11. (b) Cell Splitting and Sectoring for Capacity & Coverage Improvement|Related to capacity]] · [[May 2024.md#11. (b) Trunking & Grade of Service (3 Marks)]] · [[PYQ 2.md#1.  Grade Of Service (GOS)|PYQ2 Q1]] |
| Interference Types | Co-channel vs adjacent channel | [[May 2024.md#2. Types of interference in cellular systems (3 Marks)|May 2024 Q2]] · (Implicit in reuse / sectoring questions) |
| Fading (Small-Scale / Multipath) | Mechanism, distributions | [[October 2023 PYQ#3. How does fading occur? Derive the expression for doppler shift.]] · [[May 2024.md#3. Multipath causing small-scale fading (3 Marks)]] |
| Doppler / Time Selectivity | Doppler shift, coherence time | [[October 2023 PYQ#3. How does fading occur? Derive the expression for doppler shift.]] · [[October 2023 PYQ#14. (c) Time selective fading]] |
| Outage Probability | SNR threshold stats (Rayleigh) | [[October 2023 PYQ#5. How is the outage probability computed for a wireless channel?]] · [[May 2024.md#16. (a) Outage probability of BPSK in flat (Rayleigh) fading & relation to fade margin (8 Marks)]] |
| Link Budget / Friis Equation | Received power computations | [[October 2023 PYQ#4. Power and Voltage Calculation]] · [[October 2023 PYQ#14. (a) Free space received power and path loss]] · [[May 2024.md#13. (b) Received power with half-wave antennas at 150 MHz (6 Marks)]] |
| Diversity Techniques | Spatial, selection, macro/micro | [[October 2023 PYQ#7. Differentiate between microdiversity and macrodiversity]] · [[May 2024.md#7. Types of diversity (3 Marks)]] · [[May 2024.md#18. (a) Selection Combining (SC) Diversity Features (9 Marks)]] |
| Equalization (Linear vs Nonlinear / ZF) | ISI mitigation trade-offs | [[October 2023 PYQ#8. Compare pros and cons of linear equalizer over non-linear equalizer]] · [[May 2024.md#8. Linear vs nonlinear equalizers (3 Marks)]] · [[May 2024.md#17. (a) Zero-Forcing (ZF) Equaliser Operation (7 Marks)]] |
| Cyclic Prefix / OFDM Fundamentals | ISI removal via CP; orthogonality | [[October 2023 PYQ#6. Explain the significance of using cyclic prefix in an OFDM system]] · [[May 2024.md#5. Multicarrier scheme eliminating ISI (3 Marks)]] · [[May 2024.md#15. (a) Orthogonal Frequency Division Multiplexing (OFDM) – Principle & System (10 Marks)]] |
| PAPR in OFDM | Peak vs average power mitigation | [[PYQ 2.md#6. Peak-to-Average Power-Ratio (PAPR) in OFDM System]] · [[May 2024.md#16. (b) PAPR in OFDM & reduction techniques (8 Marks)]] |
| Channel Capacity (Shannon / Ergodic) | Capacity limits & adaptation | [[May 2024.md#4. Ergodic capacity: definition & significance (3 Marks)]] · [[October 2023 PYQ#14. (b) Inference of AWGN channel capacity]] |
| Multiple Access Comparison | FDMA / TDMA / CDMA traits | [[May 2024.md#17. (b) Comparison: TDMA vs FDMA vs CDMA (7 Marks)]] · (Implied in GSM architecture / evolution sections) |
| Generational Evolution | 1G→4G feature progression | [[May 2024.md#12. (a) Compare the important features of 1G, 2G, 3G and 4G systems]] · [[October 2023 PYQ#12. (b) Features of 4G Wireless Networks]] |
| Ionospheric Propagation | Critical frequency, refraction | [[October 2023 PYQ#9. Deduce the expression for critical frequency of an ionised region]] · [[October 2023 PYQ#10. Explain the mechanism of wave bending (refraction) in the ionosphere]] |
| Two-Ray / Path Loss Models | Beyond free-space (d^-4 region) | [[May 2024.md#14. (a) Two-ray ground model path loss derivation (8 Marks)]] · (Related to link budget problems) |
| Trunking / Erlang Formulas | Blocking, efficiency | [[May 2024.md#11. (b) Trunking & Grade of Service (3 Marks)]] · [[PYQ 2.md#1.  Grade Of Service (GOS)]] |

## Quick Reference Formula Snippets
| Topic | Key Formula |
|-------|-------------|
| Frequency Reuse Distance | \(D = R\sqrt{3N}\) |
| Friis (Received Power) | \(P_r = P_t G_t G_r (\frac{\lambda}{4\pi d})^2\) |
| Rayleigh Outage | \(P_{out} = 1 - e^{-\gamma_{th}/\bar{\gamma}}\) |
| Ergodic Capacity | \(C_{erg} = \mathbb{E}[B\log_2(1+\gamma)]\) |
| Shannon (AWGN) | \(C = B\log_2(1+\text{SNR})\) |
| BPSK BER AWGN | \(P_b = Q(\sqrt{2E_b/N_0})\) |
| Coherence Bandwidth | \(B_c \approx 1/(5\tau_{rms})\) |
| Two-Ray Crossover | \(d_c \approx 4\pi h_t h_r / \lambda\) |
| Erlang B | \(B(C,A)=\frac{A^C/C!}{\sum_{k=0}^C A^k/k!}\) |
| PAPR | \(\max |x|^2 / \mathbb{E}[|x|^2]\) |
| Doppler Shift | \(f_D = (v/c) f \cos \theta\) |

## High-Yield Study Sequence
1. Link Fundamentals: Friis, path loss extensions (two-ray).
2. Fading & Diversity: Rayleigh/Rician, outage, diversity combining (SC, MRC conceptually).
3. Capacity & Performance: Shannon / ergodic vs outage, BER expressions.
4. Multiple Access & Evolution: FDMA/TDMA/CDMA → OFDM/OFDMA; 1G → 4G features.
5. Resource Efficiency: Trunking, frequency reuse, sectoring, splitting.
6. OFDM Deep Dive: CP, PAPR, equalization (ZF/MMSE), adaptive modulation.
7. Propagation Extras: Ionospheric refraction, critical frequency, skip distance (if included elsewhere).

## Suggested Practice Pairings
- Compute received power (Friis) then evaluate outage probability at that SNR.
- Contrast ZF vs MMSE equalization on an OFDM subcarrier with deep fade.
- Determine required fade margin for 1% outage then assess capacity tradeoff.
- Compare PAPR reduction methods for a given OFDM numerology (e.g., 64 subcarriers).

## Missing / To Curate Later
- Add MUF & skip distance explicit derivations to this sheet (link existing sections).
- Add MRC performance expression (average SNR and BER) for comparison with Selection Combining.

---
*End of consolidated most asked topics.*
