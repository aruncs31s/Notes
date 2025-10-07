# Module 1

## Task List

- [ ] Basic Antenna Parameters
  - [ ] Gain
  - [ ] Directivity
  - [ ] Beam Width
  - [ ] Effective Aperture
  - [ ] Effective Height
  - [ ] Wave Polarization
  - [ ] Radiation Resistance
  - [ ] Radiation Efficiency
  - [ ] Antenna Field Zones
- [ ] Duality and Principles of Reciprocity
  - [ ] Principle of Reciprocity
  - [ ] Duality Principle
- [ ] Helmholtz Theorem
  - [ ] Statement and Importance
  - [ ] Derivation
- [ ] Field, Directivity and Radiation Resistance of Short Dipole and Half-Wave Dipole
  - [ ] Short Dipole (Far Field Derivation)
  - [ ] Half-Wave Dipole (Far Field Derivation)

## Basic Antenna Parameters

Antennas are devices that convert electrical signals into electromagnetic waves and vice versa. Basic parameters characterize their performance, helping engineers design and evaluate antenna systems for various applications like wireless communication, radar, and satellite systems.

### Gain
The gain of an antenna is the ratio of the power radiated in a particular direction to the power radiated by an isotropic antenna (which radiates equally in all directions). It accounts for both directivity and efficiency losses.

**Formula:** $ G = \frac{4\pi U(\theta, \phi)}{P_{rad}} $, where $ U $ is radiation intensity, $ P_{rad} $ is total radiated power.

**Detailed Explanation:**
- **Isotropic Antenna:** A hypothetical antenna that radiates power equally in all directions. It has a gain of 1 (0 dB) and directivity of 1.
- **Radiation Intensity $ U(\theta, \phi) $:** Power per unit solid angle in a specific direction. Measured in watts per steradian.
- **Total Radiated Power $ P_{rad} $:** Total power radiated by the antenna, excluding losses.
- **Units:** Dimensionless, often expressed in dB (decibels): $ G_{dB} = 10 \log_{10} G $.
- **Example:** A dipole antenna has a gain of about 2.15 (3.3 dB) in its maximum direction.
- **Measurement:** Using anechoic chambers or field measurements with reference antennas.
- **Importance:** Higher gain means better signal strength in desired directions, crucial for long-range communication.

### Directivity
Directivity is a measure of how concentrated the radiation is in a particular direction, without considering losses. It's the maximum value of gain if the antenna were 100% efficient.

**Formula:** $ D = \frac{4\pi U_{max}}{P_{rad}} $

**Detailed Explanation:**
- **Difference from Gain:** Gain includes efficiency, directivity does not. $ G = \eta D $, where $ \eta $ is efficiency.
- **Maximum Radiation Intensity $ U_{max} $:** The peak value of radiation intensity.
- **Calculation:** For directional antennas, directivity can be calculated from radiation patterns.
- **Units:** Same as gain, dimensionless or dB.
- **Example:** Parabolic dish antennas have high directivity (20-40 dB).
- **Applications:** Used in radar systems for focused beams.

### Beam Width
The beam width is the angular width of the main lobe of the radiation pattern, typically measured at the half-power points (-3 dB).

- Half-power beam width (HPBW)
- First null beam width (FNBW)

**Detailed Explanation:**
- **HPBW:** Angle between points where power is half the maximum (3 dB down).
- **FNBW:** Angle between first nulls on either side of main lobe.
- **Measurement:** From radiation pattern plots in E-plane and H-plane.
- **Importance:** Narrower beam width means higher directivity but requires precise pointing.
- **Example:** For a dipole, HPBW is about 78 degrees in E-plane.

### Effective Aperture
The effective aperture $ A_e $ is the equivalent area that would intercept the same power as the antenna from an incident plane wave.

**Formula:** $ A_e = \frac{\lambda^2}{4\pi} G $, where $ \lambda $ is wavelength.

**Detailed Explanation:**
- **Physical Aperture:** Actual area for aperture antennas like horns or dishes.
- **Relationship:** For aperture antennas, $ A_e \approx \eta A_{phys} $, where $ \eta $ is aperture efficiency.
- **Units:** Square meters.
- **Example:** A 1m diameter parabolic dish at 10 GHz has effective aperture around 0.5 m².
- **Applications:** Used in link budget calculations for communication systems.

### Effective Height
For wire antennas, effective height $ h_e $ is the height that would produce the same open-circuit voltage as the actual antenna.

**Formula:** $ h_e = \frac{V_{oc}}{E_i} $, where $ E_i $ is incident field strength.

**Detailed Explanation:**
- **Open-Circuit Voltage $ V_{oc} $:** Voltage across antenna terminals when open-circuited.
- **Incident Field $ E_i $:** Strength of incoming electromagnetic wave.
- **Units:** Meters.
- **Example:** For a quarter-wave monopole, effective height is λ/4.
- **Importance:** Used in antenna matching and impedance calculations.

### Wave Polarization
Polarization describes the orientation of the electric field vector in the electromagnetic wave.

- Linear (horizontal/vertical)
- Circular (right-hand/left-hand)
- Elliptical

**Detailed Explanation:**
- **Linear Polarization:** E-field oscillates in a single plane.
- **Circular Polarization:** E-field rotates in a circle, useful for satellite communication to avoid Faraday rotation.
- **Elliptical:** Combination of linear and circular.
- **Polarization Mismatch:** Can cause signal loss; cross-polarization discrimination (XPD) measures this.
- **Example:** TV antennas are linearly polarized; GPS uses circular.

### Radiation Resistance
Radiation resistance $ R_r $ is the equivalent resistance that accounts for power radiated by the antenna.

**Formula:** $ R_r = \frac{2 P_{rad}}{I_0^2} $, where $ I_0 $ is current at feed point.

**Detailed Explanation:**
- **Equivalent Circuit:** Antenna can be modeled as R_r in series with loss resistance.
- **Units:** Ohms.
- **Example:** Half-wave dipole has R_r = 73 Ω.
- **Calculation:** From radiation pattern integration.
- **Importance:** Affects impedance matching and efficiency.

### Radiation Efficiency
Radiation efficiency $ \eta $ is the ratio of radiated power to total input power.

**Formula:** $ \eta = \frac{P_{rad}}{P_{in}} = \frac{R_r}{R_r + R_l} $, where $ R_l $ is loss resistance.

**Detailed Explanation:**
- **Loss Resistance $ R_l $:** Due to conductor losses, dielectric losses.
- **Units:** Percentage or dimensionless.
- **Example:** High-efficiency antennas have η > 90%.
- **Improvement:** Use low-loss materials, optimize design.
- **Applications:** Critical for battery-powered devices.

### Antenna Field Zones
- **Reactive near field** (Fresnel zone): $ r < 0.62 \sqrt{D^3 / \lambda} $, fields decay as 1/r^2 or faster.
- **Radiating near field** (Fresnel zone): $ 0.62 \sqrt{D^3 / \lambda} < r < 2D^2 / \lambda $, transition region.
- **Far field** (Fraunhofer zone): $ r > 2D^2 / \lambda $, fields decay as 1/r, plane waves.

**Detailed Explanation:**
- **Near Field:** Complex field patterns, used for RFID, medical applications.
- **Far Field:** Simple plane waves, used for most communication.
- **D:** Maximum dimension of antenna.
- **λ:** Wavelength.
- **Measurement:** Far-field measurements require large distances or compact ranges.

## Duality and Principles of Reciprocity

### Principle of Reciprocity
The reciprocity theorem states that the transmission characteristics between two antennas are the same regardless of which is transmitting and which is receiving. If antenna A transmits to antenna B, the received power is the same as if B transmitted to A.

**Implication:** Antennas can be used interchangeably for transmit and receive.

**Detailed Explanation:**
- **Proof:** Based on Lorentz reciprocity theorem in electromagnetics.
- **Applications:** Simplifies antenna design; same antenna for TX/RX in radios.
- **Limitations:** Does not apply to nonlinear or time-varying systems.
- **Example:** In a two-antenna system, S21 = S12.

### Duality Principle
The duality principle relates electric and magnetic fields. If you have a solution for electric sources, you can obtain the magnetic counterpart by swapping E and H fields, and electric and magnetic sources.

**Example:** A dipole antenna has a dual in the form of a loop antenna.

**Detailed Explanation:**
- **Mathematical Basis:** Maxwell's equations are symmetric under E ↔ H, J ↔ M.
- **Applications:** Design complementary antennas.
- **Example:** Electric dipole (current source) ↔ Magnetic dipole (magnetic current).

**Detailed Explanation:**
- **Mathematical Basis:** Maxwell's equations are symmetric under E ↔ H, J ↔ M.
- **Applications:** Design complementary antennas.
- **Example:** Electric dipole (current source) ↔ Magnetic dipole (magnetic current).

## Helmholtz Theorem

Helmholtz theorem states that any vector field that satisfies certain conditions can be decomposed into the sum of an irrotational (curl-free) vector field and a solenoidal (divergence-free) vector field.

For electromagnetic fields, it allows decomposition into Transverse Electric (TE) and Transverse Magnetic (TM) modes.

### Derivation
Consider a vector field $ \vec{A} $ that is twice differentiable and vanishes at infinity.

$ \vec{A} = \vec{A}_1 + \vec{A}_2 $, where $ \nabla \times \vec{A}_1 = 0 $ (irrotational) and $ \nabla \cdot \vec{A}_2 = 0 $ (solenoidal).

Using vector identities and Green's theorem, we can show that such a decomposition is possible.

In waveguides, this leads to TE and TM modes.

**Detailed Derivation:**
1. Define $ \vec{A}_1 = \nabla \phi $, where $ \nabla^2 \phi = \nabla \cdot \vec{A} $.
2. Then $ \vec{A}_2 = \vec{A} - \vec{A}_1 $, and show $ \nabla \cdot \vec{A}_2 = 0 $.
3. For uniqueness, boundary conditions are needed.

**Importance:** Fundamental in solving wave equations in bounded regions.

## Field, Directivity and Radiation Resistance of Short Dipole and Half-Wave Dipole

### Short Dipole (Far Field Derivation)
A short dipole has length $ l \ll \lambda $.

**Far field electric field:** $ E_\theta = \frac{60 I_0 l}{r} \sin\theta e^{j(kr - \omega t)} $ (in V/m, for free space)

**Directivity:** 1.5 (1.76 dB)

**Radiation resistance:** $ R_r = 80 \pi^2 (l/\lambda)^2 $ ohms

**Detailed Derivation:**
1. Current distribution: $ I(z) = I_0 $ (constant for short dipole).
2. Vector potential: $ \vec{A} = \frac{\mu_0}{4\pi} \int \frac{I(z') e^{-jkr'}}{r'} dz' $.
3. Far field: $ E_\theta = -j \frac{\omega \mu_0}{4\pi r} e^{-jkr} \sin\theta \int_{-l/2}^{l/2} I(z) e^{j k z \cos\theta} dz $.
4. For short dipole, integral ≈ I_0 l.
5. Thus, $ E_\theta = j \frac{60 I_0 l}{r} \sin\theta e^{j(kr - \omega t)} $ (time convention).

**Directivity Calculation:** From pattern, D = 4π / Ω_A, where Ω_A is beam solid angle.

**Radiation Resistance:** From P_rad = (1/2) Re ∫ E × H* dS, leads to R_r = 80 π² (l/λ)².

### Half-Wave Dipole (Far Field Derivation)
Length $ l = \lambda/2 $.

**Far field electric field:** $ E_\theta = \frac{60 I_0}{r} \frac{\cos((\pi/2)\cos\theta)}{\sin\theta} e^{j(kr - \omega t)} $

**Directivity:** 2.15 (3.4 dB)

**Radiation resistance:** 73 ohms

**Detailed Derivation:**
1. Current distribution: $ I(z) = I_0 \cos(kz) $ for z from -λ/4 to λ/4.
2. Vector potential similar.
3. Integral: ∫ I(z) e^{j k z \cos\theta} dz = I_0 ∫_{-λ/4}^{λ/4} \cos(kz) e^{j k z \cos\theta} dz.
4. Evaluate using trigonometric identities.
5. Result: $ E_\theta = j \frac{60 I_0}{r} \frac{\cos((\pi/2)\cos\theta)}{\sin\theta} e^{j(kr - \omega t)} $.

**Directivity:** Calculated from pattern factor.

**Radiation Resistance:** 73 Ω, standard value for half-wave dipole.

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

**Detailed Derivation:**
1. Current distribution: $ I(z) = I_0 $ (constant for short dipole).
2. Vector potential: $ \vec{A} = \frac{\mu_0}{4\pi} \int \frac{I(z') e^{-jkr'}}{r'} dz' $.
3. Far field: $ E_\theta = -j \frac{\omega \mu_0}{4\pi r} e^{-jkr} \sin\theta \int_{-l/2}^{l/2} I(z) e^{j k z \cos\theta} dz $.
4. For short dipole, integral ≈ I_0 l.
5. Thus, $ E_\theta = j \frac{60 I_0 l}{r} \sin\theta e^{j(kr - \omega t)} $ (time convention).

**Directivity Calculation:** From pattern, D = 4π / Ω_A, where Ω_A is beam solid angle.

**Radiation Resistance:** From P_rad = (1/2) Re ∫ E × H* dS, leads to R_r = 80 π² (l/λ)².

### Half-Wave Dipole (Far Field Derivation)
Length $ l = \lambda/2 $.

**Far field electric field:** $ E_\theta = \frac{60 I_0}{r} \frac{\cos((\pi/2)\cos\theta)}{\sin\theta} e^{j(kr - \omega t)} $

**Directivity:** 2.15 (3.4 dB)

**Radiation resistance:** 73 ohms

**Detailed Derivation:**
1. Current distribution: $ I(z) = I_0 \cos(kz) $ for z from -λ/4 to λ/4.
2. Vector potential similar.
3. Integral: ∫ I(z) e^{j k z \cos\theta} dz = I_0 ∫_{-λ/4}^{λ/4} \cos(kz) e^{j k z \cos\theta} dz.
4. Evaluate using trigonometric identities.
5. Result: $ E_\theta = j \frac{60 I_0}{r} \frac{\cos((\pi/2)\cos\theta)}{\sin\theta} e^{j(kr - \omega t)} $.

**Directivity:** Calculated from pattern factor.

**Radiation Resistance:** 73 Ω, standard value for half-wave dipole.
