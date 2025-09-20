---
id: Eye_Diagram
aliases: []
tags:
  - academics
  - btech
  - s6
  - communication_lab
  - part_b
  - experiment_5
dg-publish: true
---
# Eye Diagram
Created : 2024-04-29 10:48

## Contents
- 

#WholeCode 

```c
close all; 
clear ;
rolloff = 0.4 ;
span = 10 ;
sps = 7 ;

M = 16 ;

k = log2(M); % 4

% Generation of sqrt Rased cosine filter
rcFilter=rcosdesign(rolloff,span,sps,'normal') ; % normal=> sqrt for sqrt filter

fvtool(rcFilter,'Analysis,'impulse');

Bipolar_Data = 2* randi([0 1], 50 , 1) - 1;

Upsampled_and_filtered = upfirdn(Bipolar_Data, rcFilter,sps,1)

EbN0 = 100;
snr =  EbN0+ 10*log10(k) - 10*log10(sps);

filterlength=10; % in symbols

rxSignal = awgn(Upsampled_and_filtered,snr,'measured');

rxFilteredSignal = upfirdn(rxSignal,rcFilter,1,sps);
rxFilteredSignal = rxFilteredSignal(filterlength + 1 :end -filterlength);

% Adding Noise
rxSignal = rxSignal + randn(size(rxSignal))*.01 ;

% plotting
figure
stem(Bipolar_Data,'filled')
hold on
plot(rxF)

```

## References
1. 
