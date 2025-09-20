---
id: Channels
aliases: []
tags:
  - electronics
  - communication
  - wireless
Date: "05-04-25"
dg-publish: true
---
# Channels
- [ ] All the equations are designed for farfield communication . Then what about near field ?? 

## Path Loss and Shadowing 
Path oss (PL) refers to the loss or **attenuation** a propagating electromagnetic signal encounters along its path from (ransmitter to the receiver) 

$$
PL(dB) = 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right)  \tag{1}
$$
> where 
> d -> distance between the tx and the rx
> $\lambda$ is the wavelength of the signal

### Power at the receiver
$$
P_{r}  = P_{t} G_{t} G_{I}\left( \frac{\lambda}{4 \pi d} \right)^2
$$