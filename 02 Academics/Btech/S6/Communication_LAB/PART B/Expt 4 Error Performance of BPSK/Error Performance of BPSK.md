---
id: Error_Performance_of_BPSK
aliases: []
tags:
  - academics
  - btech
  - s6
  - communication_lab
  - part_b
  - expt_4_error_performance_of_bpsk
dg-publish: true
---
# Error Performance of BPSK
- [[pySDR#^c938fb|Using Python]]
## Contents
- [[#Aim]]
- [[#Theory]]
- [[#Algorithm]]
- [[#Code]]
---

#### **Aim:** 
1. Generate a string of message bits.
2. Encode using `BPSK`[^1] with energy per bit `Eb` and represent it using points in a signal-space.
3. Simulate transmission of the `BPSK` modulated signal via an [[AWGN]] channel with variance `N0/2`.
4. Detect using an ML decoder and plot the probability of error as a function of [[SNR|SNR]] per bit `Eb/N0`.

[^1]:  ***BPSK*** stands for Binary Phase Shift Keying. It's a type of digital modulation technique in which a carrier signal is modulated to convey information. The carrier signal's phase is changed between two discrete states to represent the binary data being transmitted. This technique is used in various communication systems, such as wireless and satellite communication*

---

#### Theory 

In a coherent binary PSK system, the pair of signals $S1(t)$ and $S2 (t)$ used to represent binary symbols
1 & 0 are defined by
$$ S1 (t) = √2Eb/τb Cos 2πfct $$
$$S2 (t) =√2Eb/Tb (2πfct+π)$$
$$ = - √ 2Eb/Tb Cos 2πfct$$
- where 0 ≤ t< Tb and
- Eb = Transmitted signed energy for bit

*In BPSK, there is only one basis function of unit energy.*
$$Øb (t) = {\sqrt{2/Tb}}\  cos (2\pi f_ct)\ \ \ \ \ for\ \ \  0 \ ≤  \ t \ < Tb$$
$$S_1 (t) = √Eb Ø1 (t) \ \  0≤ t ≤Tb$$
$$S_2 (t) = √Eb Ø1 (t) \ \ 0≤ t< Tb$$
> Where $S_1$ and $S_2$ represents transmitted signals corresponding to bit 1 and bit 0, respectively.
> The signal space is 1 dimensional ($N=1$) having two message points ($M = 2$)*

![[BPSK Block diagram]]

##### BPSK Reciever
- The recieved *BPSK* signal is applied to a *correlator*[^2] which is also supplied with a locally generated reference signal $\phi_1 (t)$. 
- The correlated output is then compared with *threshold* voltage

```c
recieved_Signal = (x>0)? 1 : 0

```

[^2]: A *correlator* is a signal processing device that measures the similarity between two signals

---

---
#### Algorithm
1. **Generate a sequence** : Generate a sequence of random bits of ones and zeros of certain length ($N_{sym}$ typically set in the order of 10000)

2. **Map The Bits** Using the **constellation** points, map the bits to modulated symbols (For example, bit ‘0’ is mapped to amplitude value A, and bit ‘1’ is mapped to amplitude value -A) using the following equation
3. **Compute the total power** : Compute the total power in the sequence of modulated symbols and add noise for the given $E_bN_0$ (SNR) value. The noise added symbols are the received symbols at the receiver.
4.** Detect The Bits** Use thresholding technique, to detect the bits in the receiver. Based on the constellation
diagram above, the detector at the receiver has to decide whether the receiver bit is above or
below the threshold 0.
5. **Compute the BER** Compare the detected bits against the transmitted bits and compute the bit error rate (BER).
6. **Plot The wave** Plot the simulated BER against the SNR values and compare it with the theoretical BER curve
for BPSK over AWGN

- Modulation : bpskMod()
- Demodulation : bpskDemod()

---
#### Code 
#wholeCode

```python
N=10000000;
EbN0dB = -6:2:10;
%---------------------------------------------
data=randn(1,N)>=0; bpskModulated = 2*data-1;
M=2; % message points 
Rm=log2(M);
Rc=1;
BER = zeros(1,length(EbN0dB));
index=1;
for k=EbN0dB,
EbN0 = 10.^(k/10);
noiseSigma = sqrt(1./(2*Rm*Rc*EbN0));
noise = noiseSigma*randn(1,length(bpskModulated));
received = bpskModulated + noise;
 
estimatedBits=(received>=0);
 
BER(index) = sum(xor(data,estimatedBits))/length(data);
index=index+1;
end
 
plotHandle=plot(EbN0dB,log10(BER),'r--');
set(plotHandle,'LineWidth',1.5);
title('SNR per bit (Eb/N0) Vs BER Curve for BPSK Modulation Scheme');
xlabel('SNR per bit (Eb/N0) in dB');
ylabel('Bit Error Rate (BER) in dB');
grid on;
hold on;
theoreticalBER = 0.5*erfc(sqrt(10.^(EbN0dB/10)));
plotHandle=plot(EbN0dB,log10(theoreticalBER),'k*');
set(plotHandle,'LineWidth',1.5);
legend('Simulated','Theoretical');
grid on;

```

[[Using Python#^56f9ed|Above Code Using Python]]

#### Explenation / Setps

1. 
> ```matlab
>N=1000000
>```

>Is used to Specify the number signals which are going to be generated

2.
> ```matlab
> EbN0dB = -6:2:10;
>```

>This value reperesents the *signal-to-noise* ratio in *dB*[^3] and the value is from -6 to 10 with a step size of 2 
3. 
>```matlab
>data=randn(1,N)>=0;
> bpskModulated = 2*data-1;
>```

>-> [[Using Python#^7126c5]]
>First line generates random bit which has vlues 0 and 1
>Then the second line maps `1` to `1` and `0` to `-1`
>ie `value = (bit > 0) ? 1 : 0`
>

4. 
>```

  > M = 2;
  > Rm=log2(M);
  > Rc=1; 
>```

>Here `M` represents the number of symbols in this modulation scheme(BPSK) 
>`Rm` Represents the code rate and in this case $2^1 = 2$  -> $\log_2(2) = 1$ -> $R_m = 1$ 
>

5.
> ```matlab
> BER = zeros(1,length(EbN0dB));
>index=1
>```

> `BER`([[Bit error rate]]) is used to store the value of *Bit error rates*
> Index is set to 1 to start he computation from index 1 due to matlab uses 1 as starting index

6.
> ```matlab
> for k=EbN0dB,
> ```

> This `for` iterates through each value in the `EbN0dB`

7. 
 >```matlab
 > EbN0 = 10.^(k/10);
 > ```

 > This converts `dB` to linear value 
 
 8.
>```

> noiseSigma = sqrt(1./(2*Rm*Rc*EbN0)); 
> noise = noiseSigma*randn(1,length(bpskModulated));
>```

>Here the standard deviation of the noise is calculated based on the current `EbN0` value which is now in linear.Then Gaussian noise with this standard deviation is then generated

9. **Calculating the received signal**
>```matlab
>received = bpskModulated + noise;
>```

>Calculates the received signal by taking the sum of both `bpskModulated` and `noise`

10. **Demodulation**
>```matlab
>estimatedBits=(received>=0);
>```

>in this $estimatedBit = (received>=0)?\  1\  :\  0$ 

11. **Calculate the Bit Error Rate**
> ```matlab
> BER(index) = sum(xor(data,estimatedBits))/length(data);
>```

>This calculates the Bit Error Rate (BER) by comparing the original data sequence (`data`) with the estimated data sequence (`estimatedBits`) and counting the number of bit errors
>And the result is normalized by dividing by the length of the data sequence.
>By expanding this line 
>-  `xor(data,estimatedBits)`: This function calculates the bitwise exclusive OR (XOR[^4]) operation between the `data` array and the `estimatedBits` array. 
>-  `sum(xor(data,estimatedBits))`: This part sums up all the elements of the result obtained from the XOR operation. This gives the total number of bit errors between the original data and the estimated data.
>- `length(data)`: This function returns the total number of elements in the `data` array, which represents the length of the data sequence
>- `(sum(xor(data,estimatedBits))/length(data))`: This calculates the ratio of the total number of bit errors to the length of the data sequence. It represents the Bit Error Rate (BER), which is the number of bit errors divided by the total number of bits transmitted.
>- `BER(index) = ...`: Finally, this assigns the calculated BER value to the `index`-th element of the `BER` array. This is done to store the BER value for each corresponding value of `EbN0dB` during the simulation.

12. **Increment The Index**
>```matlab
>index=index+1;
> end
>```

>This line increments the index and that causes the the index to point the next element in the *BER* 

13. **Plotting The Graph**
> ```matlab
> plotHandle=plot(EbN0dB,log10(BER),'r--');
> set(plotHandle,'LineWidth',1.5);
> title('SNR per bit (Eb/N0) Vs BER Curve for BPSK Modulation Scheme');
> xlabel('SNR per bit (Eb/N0) in dB');
> ylabel('Bit Error Rate (BER) in dB');
> grid on; hold on;
> theoreticalBER = 0.5*erfc(sqrt(10.^(EbN0dB/10)));
> plotHandle=plot(EbN0dB,log10(theoreticalBER),'k*');
> set(plotHandle,'LineWidth',1.5);
> legend('Simulated','Theoretical');
> grid on;
> ```

```

theoreticalBER = 0.5 * erfc(sqrt(10.^(EbN0dB / 10)));

```

*This calculates the theoretical BER for BPSK using the complementary error function*

[^3]: 
[^4]: XOR returns `1` if the corresponding bits are different and `0` if they are the same.

#output

![[expt1_graph.png]]

#### Class Notes

#steps

- Req { msg_signal};

1. Generate Random Number
*Note* : Transmission  in done in bipolar => convert to bipolar
*Messge Snl* = [0,1]

```Matlab

data = randn(1,N)>=0 ;

```

#### Explanation
`data = randn(1,N)>=0` Sets the data variable if the generated randn()'s output > mdcmd
 0 and resets(value will be equal to 0) if its output < 0

2. Make data => 1,-1

```Matlab
bpskModulated = 2*data-1;

```

2. Define channel add noise to it
*Req* : Length of message signal and noise should be equal

```matlab
noiseSigma = sqrt(1./(2*Rm*Rc*EbN0))
noise = noiseSigma * randn(2,length(bpskModulated)) % length... = 10

```

 
3. Identify The massege
*Note* :  Threshold Detection is used to identify the recieved signal

```matlab
recieved  = bpskModulated + noise

```

- Threshold detector

```matlab
estimatedBits = (received>=0)

```

- Detect No of Error Bits
XOR Tx and Rx , take sum = Bit error

## Resources 
2. [CodeFile Github](https://github.com/aruncs31s/BtechEC/blob/S6/Communication%20Lab/Expt_1_Generation_and_Detection_of_BPSK/generation_and_Detection_of_BPSK.md)
		   
