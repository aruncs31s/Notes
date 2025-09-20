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

