
# Module 2

**Syllabus**

2.1 Path loss and shadowing (1): 
- [ ] Free space path loss,
- [ ] Two-Ray model, Shadowing,

2.2 Statistical Multipath Channel Models (4): 
- [ ] Time-varying channel impulse response,
- [ ]  Narrowband fading,
- [ ] Wideband fading models, 
- [ ] Delay spread and Coherence bandwidth, 
- [ ] Doppler spread and Coherence time, 
- [ ] Flat fading versus frequency selective fading, 
- [ ] Slow fading versus fast fading, Discrete-time model.

2.3 Capacity of Wireless Channels (2):
- [ ] Review of Capacity in AWGN, 
- [ ] Capacity of flat fading channel – Ergodic capacity,
- [ ] Capacity with Outage,
- [ ] Capacity with CSI-R. (Derivations of capacity formulae are not required; Only expressions, computations and significance required.)


## Path Loss 

$$
PL(dB) = 20\log_{10}\left( \frac{4\pi d}{\lambda} \right)
$$

### Friis Transmission Formula 
$$
P_{r} = P_{t} G_{t} G_{r} \left( \frac{\lambda}{4 \pi d} \right)^2
$$

^648482




### Free Space Propagation Model

Although EM signals when traveling through wireless
channels experience fading effects due to various
effects, but in some cases the transmission is with a
direct line of sight such as in satellite
communication
• It is used to predict received signal strength when
the transmitter and receiver have a clear
unobstructed line-of-sight path between them.

• Satellite communication systems and microwave
line-of sight radio links typically undergo free space
propagation