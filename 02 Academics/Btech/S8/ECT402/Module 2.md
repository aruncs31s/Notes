# Module 2

## Syllabus

### 2.1 Path Loss and Shadowing
- [ ] Free space path loss
- [ ] Two-Ray model
- [ ] Shadowing

### 2.2 Statistical Multipath Channel Models
- [ ] Time-varying channel impulse response
- [ ] Narrowband fading
- [ ] Wideband fading models
- [ ] Delay spread and coherence bandwidth
- [ ] Doppler spread and coherence time
- [ ] Flat fading vs frequency selective fading
- [ ] Slow fading vs fast fading
- [ ] Discrete-time model

### 2.3 Capacity of Wireless Channels
- [ ] Review of capacity in AWGN
- [ ] Capacity of flat fading channel – Ergodic capacity
- [ ] Capacity with outage
- [ ] Capacity with CSI-R
> Derivations of capacity formulae are not required; only expressions, computations, and significance required.

---

## Path Loss

**Formula:**

$$
PL(dB) = 20\log_{10}\left( \frac{4\pi d}{\lambda} \right)
$$

### Friis Transmission Formula

$$
P_{r} = P_{t} G_{t} G_{r} \left( \frac{\lambda}{4 \pi d} \right)^2
$$

---

## Free Space Propagation Model

Electromagnetic signals traveling through wireless channels experience fading due to various effects. However, in some cases, transmission occurs with a direct line of sight, such as in satellite communication.

**Key Points:**
- Used to predict received signal strength when the transmitter and receiver have a clear, unobstructed line-of-sight path between them.
- Satellite communication systems and microwave line-of-sight radio links typically undergo free space propagation.