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
Part B (50 Marks)