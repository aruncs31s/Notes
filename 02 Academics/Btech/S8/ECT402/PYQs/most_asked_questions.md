---
cssclasses:
  - wide-page
---


# ECT402 – Most Asked / High-Frequency Topics

This consolidated note extracts the most frequently recurring question themes across:
- `October 2023 PYQ.md`
- `May 2024.md`
- `PYQ 2.md`

It helps rapid revision by clustering overlapping conceptual areas that exams repeatedly target.

## Selection Criteria
Topics included if they appear (explicitly or implicitly) in ≥2 papers or form foundational building blocks referenced by multiple distinct questions (e.g., diversity, fading, capacity, multiple access, OFDM fundamentals).

## Top Recurring Themes


| Theme                                   | Core Idea / Focus                              |
| --------------------------------------- | ---------------------------------------------- |
| Frequency Reuse & Capacity              | Reuse patterns, cluster size, capacity scaling |
| Cell Splitting & Sectoring              | Capacity enhancement & interference control    |
| Trunking & Grade of Service             | Erlang B/C, blocking probability               |
| Interference Types                      | Co-channel vs adjacent channel                 |
| Fading (Small-Scale / Multipath)        | Mechanism; Rayleigh/Rician stats               |
| Doppler / Time Selectivity              | Doppler shift; coherence time                  |
| Outage Probability                      | SNR threshold distribution (Rayleigh)          |
| Link Budget / Friis Equation            | Received power & path loss                     |
| Diversity Techniques                    | Spatial / selection / macro vs micro           |
| Equalization (Linear vs Nonlinear / ZF) | ISI mitigation trade-offs                      |
| Cyclic Prefix / OFDM Fundamentals       | ISI removal; subcarrier orthogonality          |
| PAPR in OFDM                            | Peak vs average power mitigation               |
| Channel Capacity (Shannon / Ergodic)    | Limits; adaptation concepts                    |
| Multiple Access Comparison              | FDMA vs TDMA vs CDMA traits                    |
| Generational Evolution                  | 1G → 4G feature progression                    |
| Ionospheric Propagation                 | Critical frequency; refraction mechanism       |
| Two-Ray / Path Loss Models              | Free space vs two-ray regions                  |
| Trunking / Erlang Formulas              | Blocking probability & efficiency              |


## Quick Reference Formula Snippets
| Topic                      | Key Formula                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| Frequency Reuse Distance   | $D = R\sqrt{3N}$                                                  |
| Friis (Received Power)     | $P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi d}\right)^2$         |
| Rayleigh Outage            | $P_{out} = 1 - e^{-\gamma_{th}/\bar{\gamma}}$                     |
| Ergodic Capacity           | $C_{erg} = \mathbb{E}[B\log_2(1+\gamma)]$                         |
| Shannon (AWGN)             | $C = B\log_2(1+\text{SNR})$                                       |
| BPSK BER (AWGN)            | $P_b = Q(\sqrt{2E_b/N_0})$                                        |
| Coherence Bandwidth        | $B_c \approx 1/(5\tau_{rms})$                                     |
| Two-Ray Crossover Distance | $d_c \approx \frac{4\pi h_t h_r}{\lambda}$                        |
| Erlang B                   | $B(C,A)=\dfrac{A^C/C!}{\sum_{k=0}^C A^k/k!}$                      |
| PAPR                       | $$\text{PAPR}= \frac{\max_t \|x(t)\|^2}{\mathbb{E}[\|x(t)\|^2]}$$ |
| Doppler Shift              | $f_D = \frac{v}{c} f \cos \theta$                                 |

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
