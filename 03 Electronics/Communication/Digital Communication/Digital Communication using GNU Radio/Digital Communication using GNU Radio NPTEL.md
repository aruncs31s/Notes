---
aliases: 
Date: 26-12-2024
---
# Digital Communication using GNU Radio NPTEL

## Analog Vs Digital 
- Analog signals holds infinite posibilitty and it is hard to differentiate 
- the Digital signal has only 1 and 0 easy to differentiate 
- Identifying analog signals is more difficult than identifying digital signals , even with the noise 
![[Drawing 2024-12-26 13.31.25.excalidraw]]
```mermaid
graph LR
A[Bits] --modulation-->B[Waveform]
B --Demodulation --> A
```


- [ ] Channel and noise models 
- [ ] Correcting for channels (Equalization)
- [ ] Redundancy for robustness (Error control codes )


## GNU Radio Introduction 
- Blocks , source , sink,interactive features
- Signal modeling , sampling, processing
- Hardware vs software source , sinik 
- Filtering 

```mermaid
graph LR
A[Options] --> B[ID] --> python_file_name
```

**Throtle Block**: Used only when simulationg to limit the CPU Usage 
*should not use when interface with hardware *

#### Complex 
Gnu Radio always interprets comples signal as $e^{jw_{0}t}$ which causes a generation of $\cos(\omega_{0}t)$ as well as $j \sin (\omega_{0}t)$
![[realimg1.excalidraw]]


### Sampling 
- [[Nyquist Sampling Theorem#Nyquist Sampling Theorem]]

</br>

- [ ] $\cos(\omega t)$ -> FT -> is 2 sided ,ie there will be -ve and +ve freqency 

- [ ] watch https://www.youtube.com/watch?v=caNypt2dApU&list=PLOzRYVm0a65fPsbm_Uzs2fL_V7To6I6HL&index=4 10 mints lot of info 

