---
id: Channel_Coding
aliases: []
tags:
  - electronics
  - communication
  - wireless
Date: 31-10-2024
dg-publish: true
---
# Channel Coding

- [x] What is channel Coding ✅ 2024-11-02
- [ ] How changing channel coding schemes increases efficiency
- [ ] How can we implement a new channel coding method

#### Soft vs Hard Decoding

Soft Decision Decoding: it uses soft values , which should not be perfect `int` or something like that
Hard Decision Decoding: value will be perfect like , in [[BPSK]] `1` and `0`

### Why We need Channel Coding

- "The purpose of channel coding is to detect and correct errors at the receiver."[^1]
- Cyclic Redundancy Check(CRC) checks errors at the receiver
- if CRC fail result in re-transmission
- The purpose of channel coding is to transmit redundant information , using that redundant information the receiver can recover the original message even if there are slight errors

## Types of Error Correction Codes

1. Repetition Codes
2. [[Hamming Codes]]

#### Repetition Codes

[^1]: https://pysdr.org/content/channel_coding.html#why-we-need-channel-coding

[^2]: **Constellation**:A signal constellation is the physical diagram used to describe all the possible symbols

## Channel Coding Theorem

- Lets consider a **Discrete Memoryless Channel(DMC)**
