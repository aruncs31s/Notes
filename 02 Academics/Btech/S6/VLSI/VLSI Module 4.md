---
id: VLSI Module 4
aliases: []
tags:
  - academics
  - btech
  - s6
  - vlsi
dg-publish: true
---
# Module 4 Arithmetic circuits
- Adders:
  - Static adder,
  - Carry-Bypass adder,
  - Linear Carry-Select adder
  - Square-root carry-select adder.
- Multipliers: Array multiplier

### Adders

![[Adders.canvas|Adders]]

Adders can be optimized in either the `logic level` or `hardware` level

> [!INFO] Key Terms
>
> - Carry propagation Delay : - Carry propagation delay of a full adder is the time taken by it to produce the output carry bit.
> - Sum propagation delay of a full adder is the time taken by it to produce the output sum bit.

#### Ripple Carry Adder

![[Ripple Carry Adder Drawing|400x200]]

- In this adder the inputs are $A0,A1,A2,A3$ and $B0,B1,B2,B3$
- $S0,S1,S2,S3$ is the outputs

  $$
  S0 = A(+)B(+)Cin
  $$

- $Cin$ is the Carr_in from an external circuit or similar adder

#disadvantages

- Too much delay
  > [!INFO] Worst Case Delay
  > Worst case delay of a ripple carry adder is the time after which the output sum bit and carry bit becomes available from the last full adder
  > When the input is $1110 + 1110$ then it the last adder have to wait the all other adder to finish computing and the carry have to pass through all the adders

1. Propagate : Carry is calculated at the current stage and ==$C_{in}$ is propagated to next stage==
   $$
   Propagate = A \oplus B
   $$
2. Generate : If Generate = 1 we have to find the Carry

$$
Generate = AB
$$

3. Delete :
   $$
   Delete =  {\bar A \bar B}
   $$

### Carry Bypass adder

![](Pasted%20image%2020240417192854.png)
if $P_0P_1P_2P_3 = BP =1$ carry is directly passed to ==next block== .ie , $C_{o,3}= C_{i}= 0$ when $BP = 1$

- When BP-1, the incoming carry is forwarded immediately to the next block through a bypass transistor _Mb_. Hence the name carry bypass adder or carry skip adder.
- If BP 1, Carry is obtained by normal route.
- To compute the delay of N-bit adder, assume that the total adder is divided into N/M equal length bypass stages, each of which contains M bits.
- N=16,M=4

$$
T{p}= T{setup} + MT{carry} + (N/M-1) T{bypass}+(M-1)TCarry+ T{sum}

$$

> - $T{setp}$ = time to create generate & propagate signal
> - $T{carry}$ = Propagation delay through single bit
> - $T{bypass}$ =propagation delay through bypass multiplexer of a single stage.
> - $T{sum}$=time to generate the sum of final stage
> - $T_p$ = Total propagation time :

#### Linear Carry Select adder

![](https://upload.wikimedia.org/wikipedia/en/1/10/Carry-select-adder-detailed-block.png)

![](https://sp-uploads.s3.amazonaws.com/uploads/services/2882348/20220108013047_61d8e9473ad07_vlsi_square_root_carry_select_adder__6page1.png)

- In ==ripple carry adder==, ==every full adder has to wait for incoming carry before an outgoing carry== can be generated.
- One way to reduce this delay by ==calculating both possible values of carry input & evaluate the result for both possibilities in advance==.
- Once the real values of incoming carry is known, correct result is selected with a single multiplexer stage.

![[Linear Carry adder.canvas|Linear Carry adder]]

> Consider the block of adder, which is adding bits K to K+3.
>
> - Instead of waiting an arrival of the output carry of bit K-1, ==both 0 & 1 possibilities are analyzed==.
> - When CO,K-1 finally settles, either the result of the 0 or 1 path is selected by the multiplexer.
> - Worst case propagation delay  
>   $${Tadd}=T{setup} + Mt{carry} +(N/M)T{mux} + T{sum}$$

![[Linear Carry adder 4 Block.canvas|Linear Carry adder 4 Block]]

- For the first stage there fewer no of bits are provided for faster calculation
- For 2,3,4 stages the no bits is increased wrt to their order to take advantage of the carry generation

#### Square-root Carry Select adder
![[Pasted image 20240526021026.png]]
- Here we can see that the 1st stage only has 2 bits as input (A0,B0) and the input bits increasing as the block stage increases 3 Bits for 2 Block , 4 bits for 3rd Block so on,
- This is done to take advantage of the calculation as debriefed below

##### Working
> We can see that the first block is generating the sum in 3_Unit time and the carry is generated at the 4_th Unit Time
> The second stage has 3 input bits and it takes 4Unit time to calculate the result and it generates carry at 5th Unit time 
> In this way this square-root carry select adder can reduce the computing time.
﻿  
-  Delay can be reduced by progressively adding more bits to the subsequent stages in the adder, requiring more time for the generation of carry signal.  
- Eg: 1st stage add 2 bits, 2nd contains 3 bits etc.  
- N bit adder contains P stages & 1st stage adds M-bits. An additional bits added into each subsequent stage.  
$$
 N=M+(M+1)+(M+2). (M+P-1)
$$
$$
T_{add} = T_{setup} + Mt_{carry} + (\sqrt{2N})T_{mux} + T_{sum}
$$

![[sqrt,ripple,linear select performance graph]]

