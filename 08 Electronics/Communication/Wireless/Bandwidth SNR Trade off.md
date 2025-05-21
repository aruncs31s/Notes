---
aliases: 
Date: 31-10-2024
---
# Bandwidth SNR Trade off
**Prerequisites ** :
- [[Bamdwidth]]
- [[SNR]]
**Things to take**
- [[Channel Capacity]] is Fixed ? or is it?
- Increasing the Bandwidth will decrease the **SNR**

#relation
- Suppose  
$$
\left[\frac{S_{1}}{N_{1}} \right] = 7
$$
- and Bandwidth $BW = 4 Khz$
- Then [[Channel Capacity]]  $C$ 
$$
C_{1} = B_{1 } \log \left( 1 + \frac{S_{1}}{N_{1}} \right) 
$$ ^53755f ^4070f4 ^3bb781
- After plugin the values 
$$
C_{1} = 12 Khz
$$

- now if the [[SNR]] is increased to a high value say 15 but channel capacity will not increase
$$
C_{1} = B_{1 } + (1 + 15) 
$$
- Which gives to get $C_{1} = 12 Khz$ we must reduce the value of $B_{1}$
- Now $B_{1}$ will be $3Khz$ -> $25\%$ reduction when the the [[SNR]] is increased to $60\%$ 

>[!Important] BW vs SNR
>When the **SNR** is increased while keeping the Channel 
- [ ] From where i get the $60\%$ 
