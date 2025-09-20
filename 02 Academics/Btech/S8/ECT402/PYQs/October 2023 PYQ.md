---

## Additional Questions

### 7. Compare and contrast the analog and digital cellular systems

> [!info]- Short Answer
> **Analog**: Uses continuous signals, FDMA access, limited capacity, poor security, voice only.
> **Digital**: Uses discrete signals, TDMA/CDMA access, higher capacity, better security, voice+data.

| **Aspect** | **Analog Cellular** | **Digital Cellular** |
|------------|--------------------|--------------------||
| **Signal Type** | Continuous analog signals | Discrete digital signals |
| **Multiple Access** | FDMA[^24] (Frequency Division) | TDMA[^25]/CDMA[^26] |
| **Capacity** | Limited (1 user per channel) | Higher (multiple users per channel) |
| **Voice Quality** | Degrades with distance/interference | Consistent until threshold |
| **Security** | Poor (easily intercepted) | Better (encryption possible) |
| **Services** | Voice only | Voice + Data + SMS |
| **Power Consumption** | Higher | Lower |
| **Handoff** | Analog measurement based | Digital measurement + algorithms |
| **Error Correction** | None | Built-in error correction codes |
| **Spectral Efficiency** | Low | High |
| **Examples** | AMPS[^27] (1G) | GSM[^28], CDMA (2G) |

**Key Differences:**
- **Modulation**: Analog uses FM, Digital uses PSK/QAM
- **Channel Coding**: Digital systems use error correction
- **Network Intelligence**: Digital systems have advanced network management
- **Evolution Path**: Digital enables 3G/4G/5G progression

---

### 8. Methods adopted for hand-off procedures

> [!info]- Short Answer
> **Handoff Types**: Hard handoff (break-before-make), Soft handoff (make-before-break), Softer handoff (same cell).
> **Methods**: Signal strength measurement, pilot signal comparison, hysteresis-based decisions.

**Handoff Types:**

**1. Hard Handoff (Break-before-Make):**
- Connection to old base station is terminated before connecting to new one
- Brief interruption in communication
- Used in FDMA/TDMA systems
- **Process**: Monitor → Decision → Execute → Complete

**2. Soft Handoff (Make-before-Break):**
- Mobile maintains connections with multiple base stations simultaneously
- No interruption in communication
- Used in CDMA systems
- **Advantage**: Seamless transition, diversity gain

**3. Softer Handoff:**
- Handoff between sectors of the same base station
- Faster processing due to same base station controller
- Common in sectorized cells

**Handoff Methods:**

**1. Signal Strength Based:**
- Monitor received signal strength (RSS)
- Handoff when RSS falls below threshold
- **Formula**: $RSS = P_t \cdot G_t \cdot G_r \cdot \left(\frac{\lambda}{4\pi d}\right)^2$

**2. Signal Quality Based:**
- Consider signal-to-interference ratio (SIR)
- Better than pure signal strength
- **Threshold**: SIR < SIR_min triggers handoff

**3. Hysteresis-Based:**
- Prevents ping-pong effect
- **Condition**: $RSS_{new} > RSS_{old} + H$ (where H = hysteresis margin)
- Adds stability to handoff decisions

**4. Pilot Signal Comparison:**
- Compare pilot signals from neighboring cells
- Used in CDMA systems
- **Active Set**: List of base stations in communication

---

### 9. How does fading occur? Derive the expression for doppler shift

> [!info]- Short Answer
> **Fading**: Signal amplitude variation due to multipath propagation and mobile movement.
> **Doppler Shift**: $f_d = \frac{v \cos \theta}{c} \cdot f_c$ where v=velocity, θ=angle, c=speed of light, fc=carrier frequency.

**Fading Mechanisms:**

**1. Multipath Fading:**
- Signal reaches receiver via multiple paths
- Different path lengths cause phase differences
- **Result**: Constructive/destructive interference

**2. Shadow Fading:**
- Large obstacles block direct path
- **Characteristics**: Log-normal distribution, slow variation

**3. Fast Fading:**
- Rapid signal fluctuations due to mobile movement
- **Rayleigh Fading**: No line-of-sight
- **Rician Fading**: Strong line-of-sight component

**Doppler Shift Derivation:**

**Setup:**
- Mobile moving with velocity $v$
- Angle $\theta$ between velocity vector and line to transmitter
- Carrier frequency $f_c$

**Derivation:**
1. **Relative velocity component**: $v_r = v \cos \theta$
2. **Wavelength**: $\lambda = \frac{c}{f_c}$
3. **Doppler frequency**: Rate of change of phase due to motion
4. **Phase change per unit time**: $\frac{d\phi}{dt} = \frac{2\pi v_r}{\lambda}$
5. **Doppler shift**: $f_d = \frac{1}{2\pi} \frac{d\phi}{dt} = \frac{v_r}{\lambda} = \frac{v \cos \theta}{\lambda}$

**Final Expression:**
$$f_d = \frac{v \cos \theta}{c} \cdot f_c$$

**Where:**
- $f_d$ = Doppler shift (Hz)
- $v$ = mobile velocity (m/s)
- $\theta$ = angle between velocity and transmitter direction
- $c$ = speed of light (3×10⁸ m/s)
- $f_c$ = carrier frequency (Hz)

**Special Cases:**
- $\theta = 0°$ (moving toward): $f_d = +\frac{vf_c}{c}$ (positive shift)
- $\theta = 90°$ (perpendicular): $f_d = 0$ (no shift)
- $\theta = 180°$ (moving away): $f_d = -\frac{vf_c}{c}$ (negative shift)