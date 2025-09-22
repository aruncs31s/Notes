---
id: Module_2
aliases: []
tags:
  - academics
  - btech
  - s8
  - ect402
dg-publish: true
---
# Module 2

## Module 2 Syllabus

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

**With loss factor:**
$$
P_{r} = \frac{P_{t} G_{t} G_{r} \lambda^2}{(4 \pi d)^2 L}
$$

---

## Free Space Propagation Model

Electromagnetic signals traveling through wireless channels experience fading due to various effects. However, in some cases, transmission occurs with a direct line of sight, such as in satellite communication.

**Key Points:**
- Used to predict received signal strength when the transmitter and receiver have a clear, unobstructed line-of-sight path between them.
- Satellite communication systems and microwave line-of-sight radio links typically undergo free space propagation.

---

## Basic Methods of Propagation
- **Reflection:** Occurs when a signal bounces off a surface.
- **Diffraction:** Occurs when a signal bends around obstacles.
- **Scattering:** Occurs when a signal is dispersed due to small objects or rough surfaces.
- These phenomena, along with line-of-sight (LoS) communication, are fundamental to mobile communication systems.

---

### Reflection
- If the medium on which the electromagnetic wave is incident is a dielectric, some energy is reflected back and some is transmitted.
- If the medium is a perfect conductor, all energy is reflected back to the first medium.
- The amount of energy reflected depends on the polarization of the electromagnetic wave.