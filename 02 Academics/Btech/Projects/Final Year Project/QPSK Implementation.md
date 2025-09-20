---
id: QPSK_Implementation
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: "13-03-25"
dg-publish: true
source: https://wiki.gnuradio.org/index.php?title=QPSK_Mod_and_Demod
---
# QPSK Implementation
**Requirement**
- [[QPSK]]
- [[BER Calculation]]

## Transmitter Side 
**steps**
1. Generate random bits ^4bd8f0
2. Modulate into complex contellation 
3. 

#### Genrate Random Bits

```mermaid
graph LR

Random_source --> B(0s and 1s)

```

![[input.png]]

- The random source generates random data

---
While we only expect 0's and 1's from the random source but we can actually have a complex signal comming from the random source (idk why)

maybe the representation goes like this

```

0 -> Real = 0 , Img = 0
1 -> Real = 1 , Img = 1
or
0 -> Real = 0 , Img = 1 
1 -> Real = 1 , Img = 0 

```

![[Pasted image 20250313230838.png]]
![[Pasted image 20250313230806.png]]

#### Modulate into complex constellation

To modulate the [[#^4bd8f0|Generated bits]] to complex contellation here [[Constellation Moulator]] Block is used 
- The constellation modulator expects packed bytes,
- constellation modulator uses a root raised cosine (RRC) , which is uses pulse shaping filter to control the **bandwidth**(reduce) that param is called excess bandwidth. 

```yaml
Constellation Modulator
	Constellaton: bpsk,qpsk,etc here qpsk
	Differential Encoding: true,false
	Samples/Symbol: 4 
	excess BW: 350m

```

```yaml
samp_rate: 32k
excess_bw: 350m
rrc_taps: firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
nfilts: 32
constellation object: 
  id: qpsk 
  symbol map: 0,1,2,3
  constellation point: [0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]
  rotational_sym: 4
  

```

![[Pasted image 20250313233625.png]]

![[Pasted image 20250313233113.png]]
The signal looks like it has ISI but it can be reduced using timing recovery , and **another RRC filter can be used at the receiver to minimize ISI.**

> [!INFO] RRC Filter
> But when we convolve two RRC filters together, we get a [raised cosine filter](http://en.wikipedia.org/wiki/Raised-cosine_filter) (which is a form of a [Nyquist filter](http://en.wikipedia.org/wiki/Nyquist_ISI_criterion)). This can be used to reduce **ISI**

![[transmitter.pdf]]

## Receiver Side 

```mermaid
graph LR 
Received_signal --> polyphaase_clock_sync --> Linear_Equalizer --> Constellation_Decoder

```

![[receiver.pdf]]

