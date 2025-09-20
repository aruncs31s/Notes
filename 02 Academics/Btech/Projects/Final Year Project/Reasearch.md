---
id: Reasearch
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: "27-03-25"
dg-publish: true
---
# Reasearch

![[Pasted image 20250327192939.png]]

- `rational_resampler_xxx_0` uses integer decimation but doesn't specify taps, which could lead to aliasing

```python
firdes.root_raised_cosine(
    nfilts,               # 1. Filter gain
    nfilts,               # 2. Sampling rate
    1.0/float(sps),       # 3. Symbol rate
    0.35,                 # 4. Excess bandwidth (roll-off factor)
    11*sps*nfilts         # 5. Number of taps
)

```

![[rrc_impulse response.png]]

```mermaid
graph LR
AGC --> FLL_band_Edge --> Symbol_Sync --> Costas_Loop

```