---
id: Digital Modulation
aliases: []
tags:
  - electronics
  - communication
  - wireless
Date: "03-11-2024"
dg-publish: true
---
# Digital Modulation
- [[OFDM]]
- [ ] ASK,
- [ ] PSK,
- [ ] QAM,
- [ ] FSK

## Basics

_"he main goal of modulation is to squeeze as much data into the least amount of spectrum possible"_[^1]

[^1]: https://pysdr.org/content/digital_modulation.html

- The main goal of modulation schemes is to maximize spectral efficiency[^2] with `limited` amount of `bandwidth` possible

> [!important] Higher Speeds
> The problem with increased speed is that when we increase the `speed` the `signal change` will be also `faster` and according to [[Fourier Series and Transform|Fourier Properties]] the sudden changes will require broader range of frequencyies

[^2]: Spectral efficiency : using least amount of frequency spectrum to transmit high amount of data , useful in multi-user network where limited frequency spectrum if usable by one user

#### Factors to consider when choosing Modulation Schemes

- Data Rate
- Bandwidth Usage: The range of frequencies the signal occupies.
- Power Efficiency: Higher-order modulation schemes may require stronger signals to prevent errors.
- Error Rate: More complex modulation schemes can be more prone to errors, especially in noisy environments.

**Q?** So what defines a good modulation Scheme ?

## Trade-offs

- sharp changes in time domain use a large amount of bandwidth/spectrum

![[Pasted image 20241103175246.png]]
## Modulation Schemes
- [[ASK]]
- [[PSK]]
