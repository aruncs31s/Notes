# Module 1

## Basic Antenna Parameters

Antennas are devices that convert electrical signals into electromagnetic waves and vice versa. Basic parameters characterize their performance.

### Gain
The gain of an antenna is the ratio of the power radiated in a particular direction to the power radiated by an isotropic antenna (which radiates equally in all directions). It accounts for both directivity and efficiency losses.

**Formula:** $ G = \frac{4\pi U(\theta, \phi)}{P_{rad}} $, where $ U $ is radiation intensity, $ P_{rad} $ is total radiated power.

### Directivity
Directivity is a measure of how concentrated the radiation is in a particular direction, without considering losses. It's the maximum value of gain if the antenna were 100% efficient.

**Formula:** $ D = \frac{4\pi U_{max}}{P_{rad}} $

### Beam Width
The beam width is the angular width of the main lobe of the radiation pattern, typically measured at the half-power points (-3 dB).

- Half-power beam width (HPBW)
- First null beam width (FNBW)

### Effective Aperture
The effective aperture $ A_e $ is the equivalent area that would intercept the same power as the antenna from an incident plane wave.

**Formula:** $ A_e = \frac{\lambda^2}{4\pi} G $, where $ \lambda $ is wavelength.

### Effective Height
For wire antennas, effective height $ h_e $ is the height that would produce the same open-circuit voltage as the actual antenna.

**Formula:** $ h_e = \frac{V_{oc}}{E_i} $, where $ E_i $ is incident field strength.

### Wave Polarization
Polarization describes the orientation of the electric field vector in the electromagnetic wave.

- Linear (horizontal/vertical)
- Circular (right-hand/left-hand)
- Elliptical

### Radiation Resistance
Radiation resistance $ R_r $ is the equivalent resistance that accounts for power radiated by the antenna.

**Formula:** $ R_r = \frac{2 P_{rad}}{I_0^2} $, where $ I_0 $ is current at feed point.

### Radiation Efficiency
Radiation efficiency $ \eta $ is the ratio of radiated power to total input power.

**Formula:** $ \eta = \frac{P_{rad}}{P_{in}} = \frac{R_r}{R_r + R_l} $, where $ R_l $ is loss resistance.

### Antenna Field Zones
- **Reactive near field** (Fresnel zone): $ r < 0.62 \sqrt{D^3 / \lambda} $, fields decay as 1/r^2 or faster.
- **Radiating near field** (Fresnel zone): $ 0.62 \sqrt{D^3 / \lambda} < r < 2D^2 / \lambda $, transition region.
- **Far field** (Fraunhofer zone): $ r > 2D^2 / \lambda $, fields decay as 1/r, plane waves.

## Duality and Principles of Reciprocity

### Principle of Reciprocity
The reciprocity theorem states that the transmission characteristics between two antennas are the same regardless of which is transmitting and which is receiving. If antenna A transmits to antenna B, the received power is the same as if B transmitted to A.

**Implication:** Antennas can be used interchangeably for transmit and receive.

### Duality Principle
The duality principle relates electric and magnetic fields. If you have a solution for electric sources, you can obtain the magnetic counterpart by swapping E and H fields, and electric and magnetic sources.

**Example:** A dipole antenna has a dual in the form of a loop antenna.

## Helmholtz Theorem

Helmholtz theorem states that any vector field that satisfies certain conditions can be decomposed into the sum of an irrotational (curl-free) vector field and a solenoidal (divergence-free) vector field.

For electromagnetic fields, it allows decomposition into Transverse Electric (TE) and Transverse Magnetic (TM) modes.

### Derivation
Consider a vector field $ \vec{A} $ that is twice differentiable and vanishes at infinity.

$ \vec{A} = \vec{A}_1 + \vec{A}_2 $, where $ \nabla \times \vec{A}_1 = 0 $ (irrotational) and $ \nabla \cdot \vec{A}_2 = 0 $ (solenoidal).

Using vector identities and Green's theorem, we can show that such a decomposition is possible.

In waveguides, this leads to TE and TM modes.

## Field, Directivity and Radiation Resistance of Short Dipole and Half-Wave Dipole

### Short Dipole (Far Field Derivation)
A short dipole has length $ l \ll \lambda $.

**Far field electric field:** $ E_\theta = \frac{60 I_0 l}{r} \sin\theta e^{j(kr - \omega t)} $ (in V/m, for free space)

**Directivity:** 1.5 (1.76 dB)

**Radiation resistance:** $ R_r = 80 \pi^2 (l/\lambda)^2 $ ohms

### Half-Wave Dipole (Far Field Derivation)
Length $ l = \lambda/2 $.

**Far field electric field:** $ E_\theta = \frac{60 I_0}{r} \frac{\cos((\pi/2)\cos\theta)}{\sin\theta} e^{j(kr - \omega t)} $

**Directivity:** 2.15 (3.4 dB)

**Radiation resistance:** 73 ohms
