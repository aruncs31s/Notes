# System Modeling: Poles, Zeros & Transfer Functions

## What is a System?

A **system** is any physical device or process that:
- Takes an **input** (stimulus)
- Processes it internally
- Produces an **output** (response)

### System Types
| Type | Property | Example |
|------|----------|---------|
| **Linear** | Output is proportional to input | Most circuits, springs |
| **Nonlinear** | Nonlinear relationship | Diodes, transistors in saturation |
| **Time-Invariant (LTI)** | Properties don't change with time | Resistors, capacitors |
| **Time-Variant** | Properties change with time | Aging, temperature-dependent |
| **Causal** | Output depends only on past/present input | All physical systems |
| **Stable** | Bounded input → bounded output | Most designs |

---

## System Modeling: The Process

### Step 1: Derive Physical Equations
Start with **fundamental laws** (Newton's, Kirchhoff's, etc.)

**Example: RC Circuit**
- Kirchhoff's voltage law: $V_{in}(t) = V_R(t) + V_C(t)$
- Ohm's law: $V_R(t) = R \cdot i(t)$
- Capacitor equation: $i(t) = C \frac{dV_C}{dt}$

Combining:
$$V_{in}(t) = RC\frac{dV_C}{dt} + V_C(t)$$

This is a **differential equation** (hard to solve).

### Step 2: Apply Laplace Transform
Convert to **frequency domain** (easier to work with)

Assuming zero initial conditions:
$$V_{in}(s) = RC \cdot s \cdot V_C(s) + V_C(s)$$
$$V_{in}(s) = V_C(s)[RCs + 1]$$

### Step 3: Find the Transfer Function
$$H(s) = \frac{V_C(s)}{V_{in}(s)} = \frac{1}{RCs + 1}$$

**This is our system model!**

### Step 4: Extract Poles & Zeros
From $H(s) = \frac{1}{RCs + 1}$:
- **Zero** (numerator = 0): None
- **Pole** (denominator = 0): $RCs + 1 = 0 \Rightarrow s = -\frac{1}{RC}$

---

## Poles and Zeros Explained

### What are Poles?

**Poles** are values of $s$ where the transfer function becomes infinite (denominator = 0).

$$H(s) = \frac{N(s)}{D(s)} \quad \Rightarrow \quad \text{Poles occur when } D(s) = 0$$

### What are Zeros?

**Zeros** are values of $s$ where the transfer function becomes zero (numerator = 0).

$$\text{Zeros occur when } N(s) = 0$$

### General Form

$$H(s) = \frac{K(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}$$

Where:
- $z_i$ = zeros
- $p_i$ = poles
- $K$ = gain constant
- $m$ = number of zeros
- $n$ = number of poles

---

## Pole-Zero Diagram

A **pole-zero diagram** (or pole map) plots poles and zeros in the complex $s$-plane.

- **✕** = Pole
- **⊙** = Zero

```
        jω (imaginary axis)
        ↑
        |
   ✕    |    ⊙
   ⊙    |  ✕
--------|-------- σ (real axis)
        |
   ✕    |    ⊙
        |
```

### Key Regions

| Region | Behavior | Stability |
|--------|----------|-----------|
| **Left Half-Plane (LHP)** | Exponential decay | ✓ Stable |
| **Imaginary Axis** | Oscillation (undamped) | ⚠️ Marginally stable |
| **Right Half-Plane (RHP)** | Exponential growth | ✗ Unstable |

---

## Impact of Poles on System Response

### Pole Location → System Behavior

#### **Real Pole at $s = -a$ (where $a > 0$)**

Transfer function: $H(s) = \frac{1}{s+a}$

Time response: $h(t) = e^{-at}u(t)$

- **Effect**: Exponential decay (low-pass behavior)
- **Characteristic**: Slower decay for smaller $|a|$ (longer time constant $\tau = \frac{1}{a}$)
- **Analogy**: RC circuit relaxation

```
Impulse Response:
|
|     ╱
|    ╱
|   ╱
|  ╱________
|___________→ t
Decaying exponential
```

---

#### **Pair of Complex Conjugate Poles at $s = -\sigma \pm j\omega_d$**

Transfer function: $H(s) = \frac{\omega_d}{(s+\sigma)^2 + \omega_d^2}$

Time response: $h(t) = e^{-\sigma t} \sin(\omega_d t)$

- **Effect**: Damped oscillation
- **$\sigma$**: Controls decay rate (damping)
- **$\omega_d$**: Controls oscillation frequency (natural frequency)
- **Analogy**: RLC circuit ringing

```
Impulse Response:
|    ╱╲
|   ╱  ╲╱╲
|  ╱      ╲
|_╱________╲___→ t
         
Damped oscillation
```

---

#### **Pole on Imaginary Axis at $s = \pm j\omega$**

Transfer function: $H(s) = \frac{\omega}{s^2 + \omega^2}$

Time response: $h(t) = \sin(\omega t)$

- **Effect**: Sustained oscillation (no decay/growth)
- **System**: Marginally stable
- **Problem**: Can oscillate forever with any disturbance
- **Analogy**: Ideal LC circuit (no resistance)

```
Impulse Response:
|    ╱╲      ╱╲
|   ╱  ╲    ╱  ╲
|  ╱    ╲  ╱    ╲___→ t
|_╱      ╲╱
        
Pure oscillation (forever)
```

---

#### **Pole in Right Half-Plane at $s = +a$ (where $a > 0$)**

Transfer function: $H(s) = \frac{1}{s-a}$

Time response: $h(t) = e^{at}u(t)$

- **Effect**: Exponential growth (unstable!)
- **Problem**: Output grows without bound
- **Example**: Positive feedback in amplifiers
- **Analogy**: Runaway thermal runaway in transistors

```
Impulse Response:
|                    ╱
|                  ╱
|                ╱
|              ╱
|            ╱___→ t
|          ╱
|        ╱
      ╱
UNSTABLE! System explodes
```

---

## Impact of Zeros on System Response

### Zeros: Where the System "Cancels Out"

**Zeros don't directly determine stability**, but they shape the frequency response.

#### **Zero at $s = -b$ (real zero)**

Contributes factor $(s+b)$ to numerator.

- **Effect**: Blocks (attenuates) signals near frequency $\omega = b$
- **High-pass behavior**: Blocks low frequencies
- **Analogy**: Capacitor in series blocks DC

#### **Pair of Complex Conjugate Zeros at $s = -\alpha \pm j\omega_z$**

- **Effect**: Notch filter at frequency $\omega_z$
- **Application**: Noise rejection in circuits

#### **Zero at Origin $s = 0$**

Contributes factor $s$ to numerator.

- **Effect**: Blocks DC completely
- **High-pass filter characteristic**
- **Analogy**: Capacitor coupling

---

## Practical Example 1: RC Low-Pass Filter

### Physical Circuit
```
Vin ─────R─────┬─────Vout
              ─┴─ C
               |
              GND
```

### Step 1: Derive Equation
$$V_{out}(t) = \frac{1}{RC} \int_0^t (V_{in}(\tau) - V_{out}(\tau)) d\tau$$

### Step 2: Laplace Transform
$$V_{out}(s) = \frac{V_{in}(s)}{RCs + 1}$$

### Step 3: Transfer Function
$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{RCs + 1} = \frac{1/RC}{s + 1/RC}$$

### Step 4: Poles & Zeros
- **Pole**: $s = -\frac{1}{RC}$ (LHP → Stable ✓)
- **Zero**: None
- **Cutoff frequency**: $f_c = \frac{1}{2\pi RC}$

### Step 5: Frequency Response
$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega RC)^2}}$$

- At $\omega = 0$ (DC): $|H| = 1$ (passes DC)
- At $\omega = \frac{1}{RC}$ (cutoff): $|H| = 0.707$ (-3dB point)
- At $\omega → \infty$ (high freq): $|H| → 0$ (blocks high frequencies)

**This is a LOW-PASS FILTER!**

---

## Practical Example 2: RL High-Pass Filter

### Physical Circuit
```
Vin ─────┬─────L─────┬─────Vout
         |           |
        GND         GND
        (not really - Vout measured across R)
        
Actually:
Vin ─────L─────┬─────Vout
              R│
               ├─────GND
```

Wait, let me redraw:

### Physical Circuit (Correct)
```
Vin ─────L─────┬─────┐
              R│     │ Vout
               └─────┤
                     └─ GND
```

### Transfer Function
$$H(s) = \frac{Ls}{Ls + R} = \frac{s}{s + R/L}$$

### Poles & Zeros
- **Pole**: $s = -\frac{R}{L}$ (LHP → Stable ✓)
- **Zero**: $s = 0$ (at origin)

### Frequency Response
$$|H(j\omega)| = \frac{\omega\sqrt{L^2}}{\sqrt{R^2 + (\omega L)^2}} = \frac{\omega L}{\sqrt{R^2 + (\omega L)^2}}$$

- At $\omega = 0$ (DC): $|H| = 0$ (blocks DC)
- At $\omega → \infty$ (high freq): $|H| → 1$ (passes high frequencies)

**This is a HIGH-PASS FILTER!**

**Key insight**: The **zero at origin** blocks DC, creating high-pass behavior!

---

## Practical Example 3: RLC Resonant Circuit

### Physical Circuit (Series RLC)
```
Vin ─┬─→ I ─→ R ─→ L ─────┬─ Vout
     |                      |
     └──────┬── C ──┬───────┘
            └─ GND ─┘
```

### Transfer Function (Voltage across C)
$$H(s) = \frac{V_C(s)}{V_{in}(s)} = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

Where:
- $\omega_n = \frac{1}{\sqrt{LC}}$ = natural frequency
- $\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$ = damping ratio

### Poles
$$s = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$$

### Three Cases

#### **Case 1: $\zeta > 1$ (Overdamped)**
- Poles: Two real, distinct values in LHP
- Response: Slow, no overshoot
- Time response: Two exponential decays

```
Step Response:
|     ╱──────────
|    ╱
|___╱____________→ t
Slow, smooth approach
```

#### **Case 2: $\zeta = 1$ (Critically Damped)**
- Poles: Repeated real pole in LHP
- Response: Fastest without overshoot (optimal for many applications)
- Time response: $(1 + At)e^{-\omega_n t}$

```
Step Response:
|     ╱──────────
|    ╱
|___╱____________→ t
Fastest no-overshoot response
```

#### **Case 3: $\zeta < 1$ (Underdamped)**
- Poles: Complex conjugate pair in LHP
- Response: Oscillation with decay
- Time response: Damped sinusoid
- Peak overshoot: $M_p = e^{-\frac{\zeta\pi}{\sqrt{1-\zeta^2}}}$

```
Step Response:
|       ╱╲
|      ╱  ╲╱╲
|     ╱    ╱  ╲___
|____╱____╱_______→ t
    
Oscillates then settles
(ringing - common in electronics)
```

### Pole-Zero Diagram Examples

**Underdamped ($\zeta = 0.3$):**
```
       jω
        |
    ⊙   |   ⊙
        |  
--------|-------- σ
        |
    ⊙   |   ⊙
```
Poles close to imaginary axis → More oscillation

---

## Practical Example 4: Op-Amp Integrator

### Physical Circuit
```
     ╔════════════════════╗
     ║                    ║
Vin ─┤─R─┤\ 
       │   ├─O─┬──── Vout
     ─┤+ ╱      │ 
     GND │      ├─ C (feedback cap)
        │       │
        └───────┴────── GND
       Vin
```

### Transfer Function
$$H(s) = \frac{-1}{RCs}$$

### Poles & Zeros
- **Pole**: $s = 0$ (at origin) ← **Marginally stable!**
- **Zero**: None

### Problem!
A pole at the origin means:
- System is **marginally stable**
- Any small disturbance can cause oscillation
- DC offset in input causes output to drift to infinity

### Real Implementation: Add Parallel Resistor

```
     ╔═══╦══════════════╗
     ║   ║              ║
Vin ─┤─R─┤\ 
       │   ├─O─┬──── Vout
     ─┤+ ╱      │ 
     GND │      ├─C (feedback cap)
        │       │ ├─Rf (parallel resistor)
        │       │ │
        └───────┴─┴─ GND
```

New transfer function:
$$H(s) = \frac{-1/(RC)}{s + 1/(R_f C)}$$

Now we have:
- **Pole**: $s = -\frac{1}{R_f C}$ (in LHP → Stable ✓)
- Integrator behavior at low frequencies, but stable!

---

## Practical Example 5: Lead-Lag Compensator

Used in control systems to shape response.

### Transfer Function
$$H(s) = K \frac{(s + z)}{(s + p)}$$

Where typically $z > p$ (zero to the right of pole).

### Poles & Zeros
- **Zero**: $s = -z$
- **Pole**: $s = -p$
- Both in LHP → **Stable**

### Effect on Bode Plot
- **Lead** (phase lead): Adds phase in certain frequency range
- **Lag** (phase lag): Reduces phase in certain frequency range

### Application: PID Control
- Lead compensators → Faster response
- Lag compensators → Better steady-state accuracy

---

## Pole-Zero Summary Table

| Pole Type | Location | Effect | Stability | Example |
|-----------|----------|--------|-----------|---------|
| Real, negative | $s = -a$ (LHP) | Exponential decay | ✓ Stable | RC filter |
| Real, positive | $s = +a$ (RHP) | Exponential growth | ✗ Unstable | Runaway |
| Complex conjugate | $-\sigma \pm j\omega$ (LHP) | Damped oscillation | ✓ Stable | RLC circuit |
| Complex conjugate | $\pm j\omega$ (imaginary) | Sustained oscillation | ⚠️ Marginal | LC circuit |
| At origin | $s = 0$ | Integration (drift) | ⚠️ Marginal | Integrator |
| Repeated | Multiple at $-a$ (LHP) | Multiple exponentials | ✓ Stable | High-order filters |

---

## How to Model a System: Step-by-Step

### 1. **Understand Physics**
   - Identify governing equations (Newton's laws, Kirchhoff's laws, etc.)
   - Define input and output clearly

### 2. **Write Differential Equation**
   - Example: $L\frac{di}{dt} + Ri = V_{in}$

### 3. **Apply Laplace Transform**
   - Example: $LsI(s) + RI(s) = V_{in}(s)$

### 4. **Solve for Transfer Function**
   - $H(s) = \frac{Y(s)}{X(s)}$

### 5. **Factor Numerator & Denominator**
   - Identify zeros and poles
   - Express in canonical form

### 6. **Analyze Poles**
   - Check stability (all poles in LHP?)
   - Determine response type (oscillatory, exponential, mixed)

### 7. **Analyze Zeros**
   - Understand frequency response
   - Predict filtering characteristics

### 8. **Verify with Simulation/Experiment**
   - Test step response, impulse response
   - Measure frequency response
   - Compare with prediction

---

## Common Mistakes in System Modeling

### ❌ Mistake 1: Forgetting Initial Conditions
- **Wrong**: Assuming all initial conditions are zero
- **Right**: Include $f(0)$, $f'(0)$, etc. in Laplace transform
- **Impact**: Completely wrong transient response

### ❌ Mistake 2: Ignoring Parasitics
- **Wrong**: Ideal resistors, capacitors, inductors
- **Right**: Real components have parasitic resistance, inductance, capacitance
- **Impact**: May miss instabilities and nonlinear behavior

### ❌ Mistake 3: Wrong Pole Count
- **Rule**: For stable system, **number of poles ≥ number of zeros**
- **Wrong**: More zeros than poles
- **Impact**: System physically unrealizable

### ❌ Mistake 4: Pole-Zero Cancellation
- **Theory**: $(s+a)$ in numerator and denominator cancel
- **Practice**: Never perfect due to component tolerances
- **Hidden pole**: System still affected by "cancelled" pole
- **Impact**: Hidden instability at high frequencies

### ❌ Mistake 5: Confusing Stable ≠ Good Performance
- **Right**: Stable poles in LHP guarantee bounded response
- **Wrong**: Thinking all stable systems work well
- **Reality**: Poles close to imaginary axis = oscillatory, ringing, slow settling
- **Impact**: May design mediocre control systems

---

## Tools for Pole-Zero Analysis

| Tool | Purpose | Output |
|------|---------|--------|
| **MATLAB/Simulink** | `zpk()`, `pole()`, `pzmap()` | Pole-zero diagram, response plots |
| **Python** | `scipy.signal` | Transfer functions, root locus |
| **Frequency Analyzer** | Hardware measurement | Real Bode plots |
| **LTspice** | Circuit simulation | Transient/AC response |
| **Wolfram Alpha** | Quick calculations | Factorization, roots |

---

## Key Takeaways

1. **Poles determine stability** → All poles must be in LHP for stable system
2. **Pole location determines response type** → Real → exponential; Complex → oscillation
3. **Zeros shape frequency response** → Block/enhance certain frequencies
4. **Complex conjugate poles → Damped oscillation** → Very common in real systems
5. **Marginal stability (poles on axis) → Sustained oscillation** → Not acceptable
6. **System model comes from physics** → Differential equations → Laplace → H(s)
7. **Always verify with measurements** → Theory ≠ Reality (components vary)

---

## Tags
#control-systems #poles-zeros #transfer-functions #system-modeling #laplace-transform #stability #circuits #filter-design

## Related Notes
- [[Laplace Transform]]
- [[Transfer Functions]]
- [[Bode Plots]]
- [[Root Locus]]
- [[Feedback Control]]
- [[Filter Design]]
- [[Stability Analysis]]
